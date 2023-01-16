import xxhash

BLOCK_SIZE = 2**20


def calculate_hashsum(_path: str) -> str:
    xxh128 = xxhash.xxh128()

    with open(_path, 'rb') as rb:
        while True:
            data = rb.read(BLOCK_SIZE)
            if data:
                xxh128.update(data)
            else:
                break
    return xxh128.hexdigest()
