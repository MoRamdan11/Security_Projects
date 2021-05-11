class cesar():
    def __init__(self):
        pass
    def encrypt(self, plainText, key):
        self.plainText = plainText
        self.key = key
        cipherText = ""
        for i in plainText:
            if i == ' ':
                cipherText += i
                continue
            if i.isupper():
                cipherText += chr((ord(i) + key - 65) % 26 + 65)  # upper case starts at 65 Ascii Code
            else:  # lowerCase letter
                cipherText += chr((ord(i) + key - 97) % 26 + 97)  # lower case starts at 97 Ascii Code
        return cipherText

# key = int(input("key\n"))
# cipher = cesar()
# open('caesar_output.txt', 'w').close()
# with open('caesar_plain.txt') as f:
#     messages = f.read()
# for m in messages.splitlines():
#     cipherMessage = cipher.encrypt(m, key)
#     with open('caesar_output.txt', 'a') as s:
#         s.write(cipherMessage)
#         s.write('\n')

