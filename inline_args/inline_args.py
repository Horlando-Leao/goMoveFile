import sys
from typing import Dict
from text_colorized.text_colorized import console


def get_params_sys_args(keys: list) -> Dict[str, str]:
    """
    :param keys:  ["--paramkey=", "-p="] add "--name_params=" or "-name_params="
    :return:
    """
    args_dict = {}
    for i in range(1, len(sys.argv)):
        for key in keys:
            if sys.argv[i].find(key) == 0:
                console.bold(m=f"The {key} value is: {sys.argv[i][len(key):]}")
                args_dict[key] = sys.argv[i][len(key):]
                break
    return args_dict
