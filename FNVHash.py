FNV_offset_basis = 2166136261
FNV_prime = 16777619
byte_of_data = "Manu is cool"
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

