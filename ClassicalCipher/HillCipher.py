from numpy import array, dot

class HillCipher():
    def __init__(self):
        self.letters = []
        alpha = 'A'
        for i in range(0, 26):
            self.letters.append(alpha)
            alpha = chr(ord(alpha) + 1)

    def updateplainText(self):
        self.plainText = self.plainText.upper()
        self.plainText = self.plainText.replace(' ', '')
        if len(self.plainText) % 2 != 0:
            self.plainText += 'X'
        for i in range(len(self.plainText)):
            if i == 0:
                continue
            if self.plainText[i] == self.plainText[i - 1]:
                self.plainText = self.plainText[:i] + 'X' + self.plainText[i:]

    def encrypt2Letters(self, twoletters):
        orderLetters = array([1], [2])
        cipheredOrderLetters = array([1], [2])
        cipheredLetters = array(['', ''])
        for i in range(2):
            orderLetters[i][0] = ord(twoletters[i][0]) - 65  # upper letter starts at 97
        cipheredOrderLetters = dot(self.key, orderLetters)
        cipheredOrderLetters = cipheredOrderLetters % 26
        for i in range(2):
            cipheredLetters[i][0] = self.letters[cipheredOrderLetters[i][0]]
        return cipheredLetters[0][0], cipheredLetters[1][0]

    def encrypt3Letters(self, threeLetters):
        orderLetters = array([1], [2], [3])
        cipheredOrderLetters = array([1], [2], [3])
        cipheredLetters = array([''], [''], [''])
        for i in range(3):
            orderLetters[i][0] = ord(threeLetters[i][0]) - 65  # upper letter starts at 97
        cipheredOrderLetters = dot(orderLetters, self.key)
        cipheredOrderLetters = cipheredOrderLetters % 26
        for i in range(3):
            cipheredLetters[i][0] = self.letters[cipheredOrderLetters[i][0]]
        return cipheredLetters[0][0], cipheredLetters[1][0], cipheredLetters[2][0]
    # def encrypt2Letters(self, twoletters):
    #     orderLetters = array([1, 2])
    #     cipheredOrderLetters = array([1, 2])
    #     cipheredLetters = array(['', ''])
    #     for i in range(2):
    #         orderLetters[i] = ord(twoletters[i]) - 65 #upper letter starts at 97
    #     cipheredOrderLetters = dot(orderLetters, self.key)
    #     cipheredOrderLetters = cipheredOrderLetters % 26
    #     for i in range(2):
    #         cipheredLetters[i] = self.letters[cipheredOrderLetters[i]]
    #     return cipheredLetters[0], cipheredLetters[1]
    #
    # def encrypt3Letters(self, threeLetters):
    #     orderLetters = array([1, 2, 3])
    #     cipheredOrderLetters = array([1, 2, 3])
    #     cipheredLetters = array(['', '', ''])
    #     for i in range(3):
    #         orderLetters[i] = ord(threeLetters[i]) - 65  # upper letter starts at 97
    #     cipheredOrderLetters = dot(orderLetters, self.key)
    #     cipheredOrderLetters = cipheredOrderLetters % 26
    #     for i in range(3):
    #         cipheredLetters[i] = self.letters[cipheredOrderLetters[i]]
    #     return cipheredLetters[0], cipheredLetters[1], cipheredLetters[2]

    def encrypt(self, plainText, key):
        self.plainText = plainText
        self.key = key
        twoletters = ['a', 'b']#if key is square matrix
        threeLetters = ['a', 'b', 'c']#if key is 3*3 matrix
        cipherText = ''
        count = 1
        if self.key.shape == (2, 2): #2*2 key matrix
            for i in range(len(self.plainText)):
                if i % 2 == 0:
                    twoletters[0] = self.plainText[i]
                else:
                    twoletters[1] = self.plainText[i]
                    [letter1, letter2] = self.encrypt2Letters(twoletters)
                    cipherText += letter1
                    cipherText += letter2
        elif self.key.shape == (3, 3):#3*3 key matrix
            count = 1
            for i in range(len(self.plainText)):
                if count == 1:
                    threeLetters[0] = self.plainText[i]
                    count += 1
                elif count == 2:
                    threeLetters[1] = self.plainText[i]
                    count += 1
                elif count == 3:
                    threeLetters[2] = self.plainText[i]
                    [letter1, letter2, letter3] = self.encrypt3Letters(threeLetters)
                    cipherText += letter1
                    cipherText += letter2
                    cipherText += letter3
                    count = 1
        return cipherText

# key1 = array([[5, 8], [17, 3]])
# key2 = array([[2, 4, 12], [9, 1, 6], [7, 5, 3]])
# keyType = int(input("Key Type\n" + "1: 2*2 key matrix\n" + "2: 3*3 key matrix\n"))
# cipher = HillCipher()
# if keyType == 1:
#     open('hill_plain_2x2Output.txt', 'w').close()
#     with open('hill_plain_2x2.txt') as f:
#         messages = f.read()
#     for m in messages.splitlines():
#         cipherMessage = cipher.encrypt(m, key1)
#         with open('hill_plain_2x2Output.txt', 'a') as s:
#             s.write(cipherMessage)
#             s.write('\n')
# elif keyType == 2:
#     open('hill_plain_3x3Output.txt', 'w').close()
#     with open('hill_plain_3x3.txt') as f:
#         messages = f.read()
#     for m in messages.splitlines():
#         cipherMessage = cipher.encrypt(m, key2)
#         with open('hill_plain_3x3Output.txt', 'a') as s:
#             s.write(cipherMessage)
#             s.write('\n')
# else:
#     print("please Choose your key matrix type")
