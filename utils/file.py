import os
import glob


def get_data_about_path(_path: str):

    if os.path.exists(_path):
        stat = os.stat(_path)
        return {
            "atime": stat.st_atime,
            "mtime": stat.st_mtime,
            "ctime": stat.st_ctime,
            "size": stat.st_size,
            "isdir": os.path.isdir(_path)
        }
    else:
        return None


def get_files_from_dir(_path: str):
    if os.path.isdir(_path):
        return glob.glob(os.path.join(_path, '*'))
    else:
        return None
