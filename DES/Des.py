from Key import key
class DES():
    def __init__(self):
        pass

    def IP1(self, message):
        permutedMessage = ''
        P_i = [58, 50, 42, 34, 26, 18, 10, 2,
               60, 52, 44, 36, 28, 20, 12, 4,
               62, 54, 46, 38, 30, 22, 14, 6,
               64, 56, 48, 40, 32, 24, 16, 8,
               57, 49, 41, 33, 25, 17, 9, 1,
               59, 51, 43, 35, 27, 19, 11, 3,
               61, 53, 45, 37, 29, 21, 13, 5,
               63, 55, 47, 39, 31, 23, 15, 7]
        for i in range(64):
            permutedMessage += message[P_i[i] - 1]
        return permutedMessage

    def EP(self, message):
        finalMessage = ''
        E = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]
        for i in range(48):
            finalMessage += message[E[i] - 1]
        return finalMessage

    def XOR(self, message, key):#check
        result = ''
        for i in range(48):
            if message[i] == key[i]:
                result += '0'
            else:
                result += '1'
        return result
    def LRXOR(self, left, right):
        result = ''
        for i in range(32):
            if left[i] == right[i]:
                result += '0'
            else:
                result += '1'
        return result

    def binToDecimal(self, binary):
        row_number = int(binary[5]) * 1 + int(binary[0]) * 2
        column_number = int(binary[4]) * 1 + int(binary[3]) * 2 + int(binary[2]) * 4 + int(binary[1]) * 8
        return [row_number, column_number]
    def SBOX(self, message):
        S_BOX = [
                [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
                 ],

                [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
                 ],

                [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                 ],

                [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                 ],

                [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                 ],

                [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                 ],

                [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                 ],

                [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
                 ]
                ]
        messageIndex = 0
        m_box = ['', '', '', '', '', '', '', '']
        for i in range(8):
            m_box[i] = message[messageIndex: messageIndex + 6]
            messageIndex += 6
        #-----------------------------------------------------divide message into 8 parts (8 * 6bits)
        for i in range(8):
            [rowNumber, columnNumber] = self.binToDecimal(m_box[i])
            m_box[i] = str(bin(S_BOX[i][rowNumber][columnNumber]))
            m_box[i] = m_box[i][2:]
            temp = ''
            if len(m_box[i]) != 4:#0011 --> 11 computer neglect left Zeros
                 for j in range(4 - len(m_box[i])):
                     temp += '0'
                 temp += m_box[i]
            else:
                temp = m_box[i]
            m_box[i] = temp
        finalMessage = ''
        for i in m_box:
            finalMessage += i
        return finalMessage

    def PAfterSBox(self, message):
        P = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]
        finalMessage = ''
        for i in range(32):
            finalMessage += message[P[i] - 1]
        return finalMessage

    def inversePermutation(self, message):
        PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]

        finalMessage = ''
        for i in range(64):
            finalMessage += message[PI_1[i] - 1]
        return finalMessage

    def stringToHex(self, message):
        result = ''
        for i in range(0, 64, 4):
            result += hex(int(message[i:i + 4], 2))[2:].upper()
        return result

    def swap(self, message):
        finalLeft = message[:32]
        finalRight = message[32:]
        message = finalRight + finalLeft
        return message

    def round(self, plainText, key):#one round
        finalRightMessage = ''
        finalLeftMessage = ''
        #---------------------------------------------initial permutation
        leftMessage = plainText[:32]
        rightMessage = plainText[32:]
        finalLeftMessage = rightMessage
        #---------------------------------------------divide message to right and left
        rightMessage = self.EP(rightMessage) #permitution with expanation to right part to 48~bits
        #---------------------------------------------Generate Keys
        rightMessage = self.XOR(rightMessage, key)
        #----------------------------------------- xor key with message
        rightMessage = self.SBOX(rightMessage)
        # ------------------------------------S-Box
        rightMessage = self.PAfterSBox(rightMessage)
        #-------------------------------------------permutation after S-BOX
        rightMessage = self.LRXOR(rightMessage, leftMessage)
        #-------------------------------------------------XOR with left Part
        finalRightMessage = rightMessage
        plainText = finalLeftMessage + finalRightMessage
        return plainText

    def encrypt(self, plainText, keyInput, iterations):
        self.plainText = plainText
        keys = key()
        keyMatrix = keys.generatekeys(keyInput)
        for j in range(iterations):
            self.plainText = self.IP1(self.plainText)
            for i in range(len(keyMatrix)):
                self.plainText = self.round(self.plainText, str(keyMatrix[i]))
            self.plainText = self.swap(self.plainText)
            self.plainText = self.inversePermutation(self.plainText)
        print("CipherText: " + self.stringToHex(self.plainText))
        #-------------------------------------------------Encryption
        for j in range(iterations):
            i = len(keyMatrix) - 1
            self.plainText = self.IP1(self.plainText)
            while i >= 0:
                self.plainText = self.round(self.plainText, str(keyMatrix[i]))
                i = i - 1
            self.plainText = self.swap(self.plainText)
            self.plainText = self.inversePermutation(self.plainText)
        # -----------------------------------------------------------------------Decryption
        print("Deciphered text: " + self.stringToHex(self.plainText))

def prepareInput():
    print("3 lines of inputs:\n" +
          "line 1 consists of a key(16 Hex characters).\n" +
          "line 2 consists of a plaintext(16 Hex characters).\n"+
          "line 3 consists of a single number which represents the number of times you should run the encryption.")
    myKey = bin(int(input(), 16))
    message = bin(int(input(), 16))
    iterNumber = int(input(""))
    messageVal = ''
    keyVal = ''
    updatedKeyVal = ''
    updatedMessageVal = ''
    messageVal += message[2:]
    keyVal += myKey[2:]
    if len(keyVal) != 64:
        zeros_number = 64 - len(keyVal)
        for i in range(zeros_number):
            updatedKeyVal += '0'
        updatedKeyVal += keyVal
    else:
        updatedKeyVal = keyVal
    if len(messageVal) != 64:
        zeros_number = 64 - len(messageVal)
        for i in range(zeros_number):
            updatedMessageVal += '0'
        updatedMessageVal += messageVal
    else:
        updatedMessageVal = messageVal
    return [updatedMessageVal, updatedKeyVal, iterNumber]

[updatedMessageVal, updatedKeyVal, iterNumber] = prepareInput()
des = DES()
des.encrypt(updatedMessageVal, updatedKeyVal, iterNumber)
closeProgram = int(input("1: Exit\n" + "2: Try another Message\n"))
while closeProgram != 1:
    if closeProgram == 1:
        break
    elif closeProgram == 2:
        [updatedMessageVal, updatedKeyVal, iterNumber] = prepareInput()
        des = DES()
        des.encrypt(updatedMessageVal, updatedKeyVal, iterNumber)
        closeProgram = int(input("1: Exit\n" + "2: Try another Message\n"))
    else:
        closeProgram = int(input("1: Exit\n" + "2: Try another Message\n"))