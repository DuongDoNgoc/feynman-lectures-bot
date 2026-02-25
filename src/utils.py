"""Shared utilities: config loading, env var resolution, logging setup."""
import logging
import os
import re
import yaml


def load_config(path: str = "config.yaml") -> dict:
    """Load YAML config and resolve ${ENV_VAR} placeholders."""
    with open(path) as f:
        raw = f.read()

    # Resolve ${VAR} references from environment
    def resolve(m):
        var = m.group(1)
        val = os.environ.get(var)
        if val is None:
            return m.group(0)  # keep placeholder; validated later
        return val

    resolved = re.sub(r"\$\{(\w+)\}", resolve, raw)
    return yaml.safe_load(resolved)


def validate_config(config: dict):
    """Assert required fields exist and env vars are resolved."""
    required = [
        ("telegram.bot_token", str),
        ("telegram.chat_id", str),
        ("schedule.times", list),
        ("schedule.timezone", str),
        ("database.path", str),
    ]
    for dotpath, expected_type in required:
        val = _get_nested(config, dotpath)
        assert val is not None, f"Missing config: {dotpath}"
        assert isinstance(val, expected_type), f"Bad type for {dotpath}: expected {expected_type}"
        # Unresolved env var placeholder means the env var was not set
        if isinstance(val, str) and val.startswith("${"):
            env_name = val.strip("${}")
            raise AssertionError(f"Environment variable {env_name} is not set")


def setup_logging(config: dict):
    log_cfg = config.get("logging", {})
    level = getattr(logging, log_cfg.get("level", "INFO"))
    log_file = log_cfg.get("file", "data/feynman-bot.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )


def _get_nested(d: dict, dotpath: str):
    """Access nested dict via dot notation: 'a.b.c' → d['a']['b']['c']."""
    keys = dotpath.split(".")
    val = d
    for k in keys:
        if not isinstance(val, dict):
            return None
        val = val.get(k)
    return val
