def encrypt(sequenses: bytes, shift: int) -> bytes:
    
    #print([x for x in sequenses])
    new_seq = [(x + shift) % 256 for x in sequenses]

    return bytes(new_seq)

def decrypt (sequenses: bytes, shift: int) -> bytes:
    
    return encrypt(sequenses, -shift)

def encrypt_files(file_name, shift):
    
    with open (file_name, 'rb') as f:
        seq = f.read()
    
    seq = encrypt(seq, shift)
    
    with open(file_name, 'wb') as f:
        f.write(seq)
    
def decrypt_files(file_name, shift):
    
    encrypt_files(file_name, -shift)

#print(encrypt(b'\xa0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b', 2))
encrypt_files('1.txt', 13)

