class Vigenere():
    def __init__(self):
        pass
    def repeatKey(self):
        count = 0
        self.key = self.key.upper()
        finalKey = self.key
        self.key = self.key.replace(' ', '')
        lenDifference = len(self.plainText) - len(self.key)
        if lenDifference > 0:  # plainText > key
            for i in range(lenDifference):  # repeat key
                finalKey += self.key[count]
                count += 1
                if count == len(self.key):
                    count = 0
        self.key = finalKey
    def autoKey(self):
        count = 0
        self.key = self.key.upper()
        finalKey = self.key
        self.key = self.key.replace(' ', '')
        lenDifference = len(self.plainText) - len(self.key)
        if lenDifference > 0:  # plainText > key
            for i in range(lenDifference):  # repeat key
                finalKey += self.plainText[count]
                count += 1
        self.key = finalKey

    def encrypt(self, plainText, key, mode):
        originalMessage = plainText
        self.plainText = plainText
        self.key = key
        cipherText = ''
        self.plainText = self.plainText.upper()
        if mode:
            self.autoKey()
        else:
            self.repeatKey()
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

# mode = bool(input())
# if mode == True:#repeat mode
#     key = 'aether'
# else:
#     key = 'pie'
# cipher = Vigenere()
# open('vigenere_op.txt', 'w').close()
# with open('vigenere_plain.txt') as f:
#     messages = f.read()
# for m in messages.splitlines():
#     cipherMessage = cipher.encrypt(m, key, mode)
#     with open('vigenere_op.txt', 'a') as s:
#         s.write(cipherMessage)
#         s.write('\n')