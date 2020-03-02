def 1_letter(hash)
    FNV_offset_basis = 2166136261
    FNV_prime = 16777619
    pb = FNV_offset_basis * FNV_prime

    hash = "0x" + hash
    hash = int(hash, 16)
    hash = bin(hash)
    hash = hash[-8:]
    pb = str(bin(pb))
    pb = pb[-8:]
    hash = "0b" + hash
    pb = "0b" + pb
    hash = int(hash,2)
    pb = int(pb,2)
    letter = pb ^ hash
    letter = chr(letter)
    print(letter)
def FNV(byte_of_data):
    FNV_offset_basis = 2166136261
    FNV_prime = 16777619
    hash = FNV_offset_basis

    for letter in byte_of_data:
        letter = int(ord(letter))
        hash = hash * FNV_prime
        hash = hash ^ letter
        hash = hex(hash)
        hash = hash[-8:]
        print(hash)
        hash = "0x" + hash
        hash = int(hash, 16)