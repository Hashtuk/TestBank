import os
from pathlib import Path
from typing import Any


class Config:
    _isinstance = None
    _dictionary = {}

    def __new__(cls):
        if cls._isinstance is None:
            cls._isinstance = super().__new__(cls)

            config_path = Path(__file__).parents[4] / 'resources' / 'urls.properties'

            if not config_path.exists():
                raise FileNotFoundError(f'Config path not found {config_path}')

            with open(config_path, 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.split('=', 1)
                        cls._dictionary[key] = value.strip()

        return cls._isinstance

    @staticmethod
    def _convert_to_env(key: str):
        res = []
        for c in key:
            if c.isupper():
                res.append('_')
            res.append(c.upper())
        return ''.join(res)

    @staticmethod
    def fetch(key: str, default_value: Any = None) -> Any:
        env_key = Config._convert_to_env(key)
        env = os.getenv(env_key)
        if env:
            return env
        return Config()._dictionary.get(key, default_value)