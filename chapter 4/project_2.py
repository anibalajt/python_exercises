'''
1.	Write a script that inputs a line of encrypted text and a distance
    value and outputs plaintext using a Caesar cipher. The script should work
    for any printable characters

'''


def cesar_decrypt(text, key):
    code = ""
    # if key is equal to 0 return text
    if key == 0:
        return text
    for ch in text:
        # get code ascii
        ordValue = ord(ch)
        # validate that the code ascii is within the range
        if (ordValue > 32 and ordValue < 127):
            cipher = chr((ord(ch) - 33 - key) % 93 + 33)
        else:
            cipher = ch

        code += cipher
    return code


def main():
    text = input("Enter a encrypted message: ")
    key = int(input("Enter the distance value: "))

    print("Decrypted text:", cesar_decrypt(text, key))


main()
