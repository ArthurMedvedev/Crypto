def text_caesar(plain_text: str, shift: int) -> str:
        
    alfabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_upper = alfabet_lower.upper()

    # p = '/.<,'

    ord_first_letter_lower = ord('a')
    ord_first_letter_upper = ord('A')

    cipher_text = ''
        
    for symbol in plain_text:
            
        if symbol in alfabet_lower:
            cipher_text += chr(((ord(symbol) - ord_first_letter_lower + shift) % 26) + ord_first_letter_lower)
            
        elif symbol in alfabet_upper:
            cipher_text += chr(((ord(symbol) - ord_first_letter_upper + shift) % 26) + ord_first_letter_upper)
            
        else:
            cipher_text += symbol

    
    return cipher_text


def decrypt_text_caesar(plain_text: str, shift: int) ->str:
    return text_caesar(plain_text, -shift)

'''t = int(input('key: '))

if t in range(61, 70):
     print(text_caesar('A', t))
     print(decrypt_text_caesar('N', t))
else:
    print(False)'''

    


