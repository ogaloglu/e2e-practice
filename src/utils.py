import os
import sys

import dill

from src.exception import CustromException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustromException(e, sys)
