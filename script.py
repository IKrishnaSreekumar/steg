import numpy as np
from encrypt import encrypted_message

def txt_encode(text):
    l = len(text)
    i = 0
    add = ''
    while i < l:
        t = ord(text[i])
        if 32 <= t <= 64:
            t1 = t + 48
            t2 = t1 ^ 170  # 170: 10101010
            res = bin(t2)[2:].zfill(8)
            add += "0011" + res
        else:
            t1 = t - 48
            t2 = t1 ^ 170
            res = bin(t2)[2:].zfill(8)
            add += "0110" + res
        i += 1
    res1 = add + "111111111111"
    print("The string after binary conversion applying all transformations: " + res1)
    length = len(res1)
    print("Length of binary after conversion: ", length)
    HM_SK = ""
    ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
    file1 = open("Sample_cover_files/cover_text.txt", "r+")
    nameoffile = input("\nEnter the name of the Stego file after Encoding (with extension): ")
    file3 = open(nameoffile, "w+", encoding="utf-8")
    word = []
    for line in file1:
        word += line.split()
    i = 0
    while i < len(res1):
        s = word[int(i / 12)]
        j = 0
        x = ""
        HM_SK = ""
        while j < 12:
            x = res1[j + i] + res1[i + j + 1]
            HM_SK += ZWC[x]
            j += 2
        s1 = s + HM_SK
        file3.write(s1)
        file3.write(" ")
        i += 12
    t = int(len(res1) / 12)
    while t < len(word):
        file3.write(word[t])
        file3.write(" ")
        t += 1
    file3.close()
    file1.close()
    print("\nStego file has successfully been generated")


def encode_txt_data():
    count2 = 0
    file_path = "./Sample_cover_files/cover_text.txt"
    file1 = open(file_path, "r")
     
    
    # Print raw content of the file for debugging
    print("Raw content of the cover file:")
    for line in file1:
        print(repr(line))  # This will print special characters as their escape sequences
        count2 += len(line.split())
    
    file1.close()

    if count2 == 0:
        print("\nCover file is empty or has no words.")
        return
    
    bt = int(count2)
    print("Maximum number of words that can be inserted: ", int(bt / 6))
    
    text1 = input("\nEnter data to be encoded: ")
    l = len(text1)
    
    if l <= bt:
        print("\nInputted message can be hidden in the cover file.")
        txt_encode(text1)
    else:
        print("\nString is too big. Please reduce string size.")
        encode_txt_data()



def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string


def decode_txt_data():
    ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
    stego = input("\nPlease enter the stego file name (with extension) to decode the message: ")
    file4 = open(stego, "r", encoding="utf-8")
    temp = ''
    for line in file4:
        for words in line.split():
            T1 = words
            binary_extract = ""
            for letter in T1:
                if letter in ZWC_reverse:
                    binary_extract += ZWC_reverse[letter]
            if binary_extract == "111111111111":
                break
            else:
                temp += binary_extract
    print("\nEncrypted message presented in code bits:", temp)
    lengthd = len(temp)
    print("\nLength of encoded bits: ", lengthd)
    i = 0
    a = 0
    b = 4
    c = 4
    d = 12
    final = ''
    while i < len(temp):
        t3 = temp[a:b]
        a += 12
        b += 12
        i += 12
        t4 = temp[c:d]
        c += 12
        d += 12
        if t3 == '0110':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) + 48)
        elif t3 == '0011':
            decimal_data = BinaryToDecimal(t4)
            final += chr((decimal_data ^ 170) - 48)
    print("\nMessage after decoding from the stego file: ", final)


def txt_steg():
    while True:
        print("\n\t\tTEXT STEGANOGRAPHY OPERATIONS")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            encode_txt_data()
        elif choice1 == 2:
            decode_txt_data()
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")


def main():
    print("\t\t      STEGANOGRAPHY")
    while True:
        print("\nMain Menu")
        print("1. Text Steganography {Hiding Text in a Text Cover File}")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            txt_steg()
        elif choice == "2":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
