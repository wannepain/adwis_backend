import os
import json


def read_secret_from_txt(secret_name):
    """Reads a text-based secret from Docker secrets."""
    path = f"/run/secrets/{secret_name}"
    try:
        with open(path, "r") as secret_file:
            return secret_file.read().strip()
    except FileNotFoundError:
        return None  # Handle missing secrets gracefully


def read_secret_json(secret_name):
    """Reads a JSON-based secret from Docker secrets and returns a dictionary."""
    path = f"/run/secrets/{secret_name}"
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError(f"Missing secret file: {path}")
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON format in secret file: {path}")
