from utils import model
from argparse import ArgumentParser
from models.db import db
from utils.file import get_files_from_dir, get_data_about_path
from utils.hash import calculate_hashsum
from models.File import File
import os
import time
from multiprocessing import Pool


parser = ArgumentParser()
parser.add_argument('-d', '--dir', type=str, required=True)
args = parser.parse_args()


def recursive_search(_path: str):
    if os.path.isfile(_path):
        stats = get_data_about_path(_path)

        try:
            File.get(File.absolute_path == stats['abspath'])
        except:
            hashsum = calculate_hashsum(_path)
            return [File(name=stats["name"], size=stats['size'],
                         atime=stats['atime'], ctime=stats['ctime'],
                         mtime=stats['mtime'], absolute_path=stats['abspath'],
                         hashsum=hashsum,
                         ), ]
        return [None,]

    else:
        file_path_list = get_files_from_dir(_path)
        files = []
        for file_path in file_path_list:
            files += recursive_search(file_path)
        return files


def pool_search(_path: str):
    file_path_list = get_files_from_dir(_path)
    if file_path_list:
        with Pool(2) as pool:
            file_data_list = pool.map(recursive_search, file_path_list)
            return file_data_list
    return []


if __name__ == "__main__":
    model.create_tables()
    start = time.time()
    file_data_list = pool_search(args.dir)
    print(f"REMAIN TIME: {round(time.time() - start , 2)} sec.")

    for file_data in file_data_list:
        if file_data:
            filtered_data = [file for file in file_data if file]
            if len(filtered_data):
                with db.atomic():
                    File.bulk_create(file_data, batch_size=1000)
