class key():
    def __init__(self):
        self.key = ''
        self.keyMatrix = ['', '', '', '', '', '', '', '',
                          '', '', '', '', '', '', '', '']


    def PC1(self, key):
        finalKey = ''
        self.PC_1 = [57, 49, 41, 33, 25, 17, 9,
                            1, 58, 50, 42, 34, 26, 18,
                            10, 2, 59, 51, 43, 35, 27,
                            19, 11, 3, 60, 52, 44, 36,
                            63, 55, 47, 39, 31, 23, 15,
                            7, 62, 54, 46, 38, 30, 22,
                            14, 6, 61, 53, 45, 37, 29,
                            21, 13, 5, 28, 20, 12, 4]
        for i in range(56):
            finalKey += key[self.PC_1[i] - 1]
        return finalKey

    def shiftLeft(self, samount, leftKey, rightKey):
        leftKeyShifted  = ''
        rightKeyShifted = ''

        leftKeyShifted = leftKey[samount:]
        leftKeyShifted += leftKey[0: samount]
        rightKeyShifted = rightKey[samount:]
        rightKeyShifted += rightKey[0: samount]
        return [leftKeyShifted, rightKeyShifted]

    def PC2(self, keyVal):
        pc2_Key = ''
        self.PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
                            15, 6, 21, 10, 23, 19, 12, 4,
                            26, 8, 16, 7, 27, 20, 13, 2,
                            41, 52, 31, 37, 47, 55, 30, 40,
                            51, 45, 33, 48, 44, 49, 39, 56,
                            34, 53, 46, 42, 50, 36, 29, 32]
        for i in range(48):
            pc2_Key += keyVal[self.PC_2[i] - 1]
        return pc2_Key

    def generatekeys(self, keyinput):
        leftKeys = ['', '', '', '', '', '', '', '',
                     '', '', '', '', '', '', '', '']
        rightKeys = ['', '', '', '', '', '', '', '',
                     '', '', '', '', '', '', '', '']
        shamontMatrix = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        self.key = ''
        self.key = self.PC1(keyinput)
        #-------------------------------------------------------- initial permutation
        leftKeys[0] = self.key[:28]  # string Val
        rightKeys[0] = self.key[28:]  # string val
        [leftKeys[0], rightKeys[0]] = self.shiftLeft(1, leftKeys[0], rightKeys[0])
        self.keyMatrix[0] = leftKeys[0] + rightKeys[0]
        for i in range(16):
            if i == 0:
                continue
            [leftKeys[i], rightKeys[i]] = self.shiftLeft(shamontMatrix[i], leftKeys[i - 1], rightKeys[i - 1])
            self.keyMatrix[i] = leftKeys[i] + rightKeys[i]
            self.keyMatrix[i] = self.PC2(self.keyMatrix[i])
        return self.keyMatrix


