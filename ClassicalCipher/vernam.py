class vernam:
    def __init__(self):
        pass
    def encrypt(self, plainText, key):
        self.plainText = plainText
        self.plainText = self.plainText.upper()
        originalMessage = plainText
        cipherText = ''
        #-----------------------------------------------plainText and cipherText prepare
        self.key = key
        self.key = self.key.replace(' ', '')
        self.key = self.key.upper()
        #-----------------------------------------------key prepare
        for i in range(len(self.plainText)):
            if plainText[i] == ' ':
                cipherText += ' '
                continue
            keyVal = ord(self.key[i]) - 65  # upperLetter starts at 65
            cipheredLetter = (ord(self.plainText[i]) - 65) + keyVal
            cipheredLetter = chr((cipheredLetter % 26) + 65)
            if ord(originalMessage[i]) >= 97:
                cipherText += cipheredLetter.lower()
            else:
                cipherText += cipheredLetter.upper()
        return cipherText

# key = "SPARTANS" #key Generator
# cipher = vernam()
# open('vernam_output.txt', 'w').close()
# with open('vernam_plain.txt') as f:
#     messages = f.read()
# for m in messages.splitlines():
#     cipherMessage = cipher.encrypt(m, key)
#     with open('vernam_output.txt', 'a') as s:
#         s.write(cipherMessage)
#         s.write('\n')
