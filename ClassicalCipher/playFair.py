from numpy import array

class playFair():
    def __init__(self):
        pass

    def updateplainText(self):
        self.plainText = self.plainText.upper()
        self.plainText = self.plainText.replace(' ', '')
        self.plainText = self.plainText.replace('J', 'I')
        if len(self.plainText) % 2 != 0:
            self.plainText += 'X'
        for i in range(len(self.plainText)):
            if i == 0:
                continue
            if self.plainText[i] == self.plainText[i - 1]:
                self.plainText = self.plainText[:i] + 'X' + self.plainText[i + 1:]

    def updateKey(self):
        self.key = self.key.upper()
        self.key = self.key.replace('J', 'I')
        self.key = self.key.replace(' ', '')

    def delRepeat(self):
        finalKey = ''  # key without repeatation
        for i in range(len(self.key)):
            repeat = False
            for j in range(i):
                if self.key[j] == self.key[i]:
                    repeat = True
                    break
            if repeat:
                continue
            finalKey += self.key[i]
        return finalKey

    def findChar(self, plainChar, playFair):  # m --> matrix
        for i in range(5):
            for j in range(5):
                if plainChar == playFair[i][j]:
                    return i, j
        return 0, 0

    def encrypt2Letters(self, twoLetters, playFair):
        [i1, j1] = self.findChar(twoLetters[0], playFair)
        [i2, j2] = self.findChar(twoLetters[1], playFair)
        if j1 == j2:
            rowIndex1 = (i1 + 1) % 5
            rowIndex2 = (i2 + 1) % 5
            return playFair[rowIndex1][j2], playFair[rowIndex2][j1]
        elif i1 == i2:
            columnIndex1 = (j1 + 1) % 5
            columnIndex2 = (j2 + 1) % 5
            return playFair[i1][columnIndex1], playFair[i2][columnIndex2]
        return playFair[i1][j2], playFair[i2][j1]

    def encrypt(self, plainText, key):
        self.plainText = plainText
        self.key = key
        self.updateKey()
        self.updateplainText()
        cipherText = ''
        letters = []
        alpha = 'A'
        for i in range(0, 26):
            letters.append(alpha)
            alpha = chr(ord(alpha) + 1)
        # ------------------------------------------------------------------Letter Part
        self.key = self.delRepeat()
        playFair = array([['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']])
        # -----------------------------------------------------------------------delete repetition and create matrix
        x_index = 0  # x-index for matrix
        y_index = 0  # y-index for matrix
        for index in range(len(self.key)):
            # check repeatation
            playFair[x_index][y_index] = self.key[index]
            y_index += 1
            if y_index >= 5:
                y_index = 0
                x_index += 1
        # ----------------------------------------------------------------filling matrix with your key
        for i in letters:
            if self.key.find(i) != -1 or i == 'J':
                continue
            playFair[x_index][y_index] = i
            y_index += 1
            if y_index >= 5:
                y_index = 0
                x_index += 1
        # ----------------------------------------------------------------filling matrix with other letters
        twoLetters = ['', '']
        for i in range(len(self.plainText)):
            if i % 2 == 0:
                twoLetters[0] = self.plainText[i]
            else:
                twoLetters[1] = self.plainText[i]
                [letter1, letter2] = self.encrypt2Letters(twoLetters, playFair)
                cipherText += letter1
                cipherText += letter2
        cipherText = cipherText.lower()
        return cipherText


# key = str(input("Enter key\n"))
# cipher = playFair()
# open('playfair_output.txt', 'w').close()
# with open('playfair_plain.txt') as f:
#     messages = f.read()
# for m in messages.splitlines():
#     cipherMessage = cipher.encrypt(m, key)
#     with open('playfair_output.txt', 'a') as s:
#         s.write(cipherMessage)
#         s.write('\n')