import json
import logging

from pathlib import Path
from typing import Any, Type, TypeVar

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

# Generic, its like typename T in C++.
T = TypeVar("T", bound=BaseModel)


class BuildConfigLoader:
    _config_path: Path = Path('game_config.json')
    _configData: dict[str, Any]= None
    _is_loaded:bool = False

    def __init__(self):
        raise TypeError("Do not instantiate. This is meant to be used like a singleton.")

    @classmethod
    def load(cls) -> None:
        if cls._is_loaded:
            return

        if not cls._config_path.exists():
            raise FileNotFoundError(f'Build config file not found at path={cls._config_path}')

        try:
            with cls._config_path.open("r") as config_file:
                cls._configData: dict[str, Any] = json.load(config_file)

        except ValidationError as e:
            raise ValueError(f'Build config validation failed: {e.message}')

        cls._is_loaded = True


    @classmethod
    def fill_data(cls, package_name: str, dataclass_type: Type[T]) -> T:

        if not cls._is_loaded:
            raise RuntimeError('Attempted to fill build config data before calling ConfigLoader.load()')

        section_data = cls._configData.get(package_name, {})
        return dataclass_type(**section_data)
