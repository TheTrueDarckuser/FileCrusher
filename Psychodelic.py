import random

directory = input('Please write filename.extension ')
contEdits = 10000

with open(directory, 'rb') as file:
    ishodnik = file.read()
    ishodnik = bytearray(ishodnik)
    for edit in range(contEdits):
        ishodnik[random.randint(1, len(ishodnik))] = int(random.getrandbits(8))
    ishodnik = bytes(ishodnik)

    with open(directory, 'wb') as fileWite:
        fileWite.write(ishodnik)