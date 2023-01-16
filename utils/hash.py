import xxhash


def calculate_hashsum(_path: str) -> str:
    xxh128 = xxhash.xxh128()

    with open(_path, 'rb') as rb:
        while True:
            data = rb.read(65536)
            if data:
                xxh128.update(data)
            else:
                break
    return xxh128.hexdigest()
