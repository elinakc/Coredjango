import os
from .misc import yaml_coerce

"CORESETTINGS_IN_DOCKER =1"
{"IN_DOCKER": 1}


def get_settings_from_environment(prefix):
    prefix_len = len(prefix)

    return {
        key[prefix_len:]: yaml_coerce()
        for key, value in os.environ.items()
        if key.startswith(prefix)
    }
