from pathlib import Path

from oven.oven.utils import EOvenScriptExecTime
from oven.oven.config import Config

SCRIPT_NAME = 'versioning'
SCRIPT_EXEC_TIME = EOvenScriptExecTime.START_BUILD
SCRIPT_ORDER = -101

DEFAULT_VERSION_FILE_NAME = '.version'


def execute_script(config: Config, **kwargs):
    version_file_path: Path = config.root_path / kwargs.get('version_file_name', DEFAULT_VERSION_FILE_NAME)
    override_on_fail = kwargs.get('override_on_fail', True)

    if not version_file_path.exists():
        version_file_path.touch()

    with open(version_file_path, mode='r+') as f:
        try:
            major, minor, build  = map(int, f.readline().strip().split('.'))
        except Exception as e:
            if override_on_fail:
                major = 1
                minor = 1
                build = 0
            else:
                raise e
    with open(version_file_path, mode='w+') as f:
        f.write(f'{major}.{minor}.{build + 1}')
