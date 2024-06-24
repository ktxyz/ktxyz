from typing import Optional
from dataclasses import dataclass

from oven.oven.config import Config


FILTER_NAME = 'getversion'
DEFAULT_VERSION_FILE_NAME = '.version'

@dataclass
class Version:
    major: int
    minor: int
    build: int

def custom_filter(*args) -> Version:
    with open(Config().root_path / DEFAULT_VERSION_FILE_NAME, 'r+') as f:
        major, minor, build = map(int, f.read().strip().split('.'))
        return Version(major, minor, build)
