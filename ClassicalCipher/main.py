from cesar import cesar
from playFair import playFair
from HillCipher import HillCipher
from vignere import Vigenere
from vernam import vernam
from numpy import array

def classicalCipher(cipherType):
    if cipherType == 1:  # Cesar
        print("You choose Cesar Cipher")
        plainText = input("Enter PlainText\n")
        key = int(input("Enter key number\n"))
        cipher = cesar()
        cipherText = cipher.encrypt(plainText, key)
        print("Cipher Text: " + str(cipherText))

    elif cipherType == 2:  # playFair
        print("You choose PlayFair Cipher")
        plainText = input("Enter PlainText\n")
        key = str(input("Note: Key is a string value in playfair cipher\nEnter key\n"))
        cipher = playFair()
        cipherText = cipher.encrypt(plainText, key)
        print("Cipher Text: " + str(cipherText))

    elif cipherType == 3:  # Hill Cipher
        print("You choose Hill Cipher")
        cipher = HillCipher()
        plainText = input("Enter PlainText\n")
        cipherText = ''
        keyType = int(input("Enter Key Type\n" + "1: 2*2 key matrix\n" + "2: 3*3 key matrix\n"))
        if keyType == 1:
            key = array([[5, 8], [17, 3]])
            print("we choose this key matrix")
            print(key)
            val = int(input("1: continue with this matrix\n" + "2: change matrix\n"))  # val--> user decision
            if val == 2:
                for i in range(2):
                    for j in range(2):
                        key[i][j] = int(input("Enter key Element [" + str(i) + "][" + str(j) + "]: "))
            cipherText = cipher.encrypt(plainText, key)
        elif keyType == 2:
            key = array([[2, 4, 12], [9, 1, 6], [7, 5, 3]])
            print("we choose this key matrix")
            print(key)
            val = int(input("1: continue with this matrix\n" + "2: change matrix\n"))  # val--> user decision
            if val == 2:
                for i in range(3):
                    for j in range(3):
                        key[i][j] = int(input("Enter key Element [" + str(i) + "][" + str(j) + "]: "))
            cipherText = cipher.encrypt(plainText, key)
        print("Cipher Text: " + str(cipherText))
    elif cipherType == 4:  # vigenere cipher
        print("You choose Vigenere Cipher")
        plainText = input("Enter PlainText\n")
        key = input("Enter key\n")
        mode = bool(input("Enter your mode\n" + "True: Auto key mode\n" + "False: Repeat key mode\n"))
        cipher = Vigenere()
        cipherText = cipher.encrypt(plainText, key, mode)
        print("Cipher Text: " + str(cipherText))

    else:  # Vernam Cipher
        print("You choose Vernam Cipher")
        plainText = input("Enter PlainText\n")
        # key = "SPARTANS"  # key Generator
        key = input("Enter Key\n")
        while len(key) < len(plainText):
            print("Please enter key with the same length of plainText\n")
            key = input("Enter Key\n")
        cipher = vernam()
        cipherText = cipher.encrypt(plainText, key)
        print("Cipher Text: " + str(cipherText))

cipherType = int(input("Choose Cipher Type\n" + "1: Cesar Cipher\n" + "2: PlayFair Cipher\n" + "3: Hill Cipher\n" +
                   "4: vignere Cipher\n" +"5: Vernam Cipher\n"))
classicalCipher(cipherType)
closeProgram = int(input("1: Exit\n" + "2: Try another cipher\n"))
while closeProgram != 1:
    if closeProgram == 1:
        break
    if closeProgram == 2:
        cipherType = int(
            input("Choose Cipher Type\n" + "1: Cesar Cipher\n" + "2: PlayFair Cipher\n" + "3: Hill Cipher\n" +
                  "4: vignere Cipher\n" + "5: Vernam Cipher\n"))
        classicalCipher(cipherType)
    else:
        pass
    closeProgram = int(input("1: Exit\n" + "2: Try another cipher\n"))
