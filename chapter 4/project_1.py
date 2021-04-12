'''
1.	Write a script that inputs a line of plaintext and a distance value
    and outputs an encrypted text using a Caesar cipher. The script should
    work for any printable characters.

'''


def cesar_encrypt(text, key):
    code = ""
    # if key is equal to 0 return text
    if key == 0:
        return text
    for ch in text:
        # get code ascii
        ordValue = ord(ch)
        # validate that the code ascii is within the range
        if (ordValue > 32 and ordValue < 127):
            cipher = chr((ord(ch) - 33 + key) % 93 + 33)
        else:
            cipher = ch
        code += cipher
    return code


def main():
    text = input("Enter a message: ")
    key = int(input("Enter the distance value: "))

    print("Encrypted text:", cesar_encrypt(text, key))


main()
