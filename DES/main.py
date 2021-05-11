from Des import DES
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
