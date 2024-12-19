import os
import numpy as np
from encrypt import encrypted_message

def txt_encode(encrypted_message):
    add = ""
    for char in encrypted_message:
        t = int(char)
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

    res1 = add + "111111111111"
    print("Binary string after transformations: " + res1)
    length = len(res1)
    print("Length of binary data: ", length)

    HM_SK = ""
    ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}

    file_path = "Sample_cover_files/cover_text.txt"
    if not os.path.exists(file_path):
        print("Cover file not found!")
        return

    with open(file_path, "r") as file1:
        words = [word for line in file1 for word in line.split()]

    nameoffile = input("\nEnter the name of the Stego file after Encoding (with extension): ")
    with open(nameoffile, "w", encoding="utf-8") as file3:
        i = 0
        while i < len(res1):
            s = words[int(i / 12)]
            j = 0
            x = ""
            HM_SK = ""
            while j < 12:
                x = res1[j + i] + res1[i + j + 1]
                HM_SK += ZWC[x]
                j += 2
            s1 = s + HM_SK
            file3.write(s1 + " ")
            i += 12

        for remaining_word in words[int(len(res1) / 12):]:
            file3.write(remaining_word + " ")

    print("\nStego file has successfully been generated")


def encode_txt_data():
    file_path = "./Sample_cover_files/cover_text.txt"
    if not os.path.exists(file_path):
        print("\nCover file is missing!")
        return

    # Read encrypted text from the file
    encrypted_text_file = "encrypted_text.txt"
    if not os.path.exists(encrypted_text_file):
        print("\nEncrypted text file not found! Please run `encrypt.py` to generate it.")
        return

    with open(encrypted_text_file, "r") as enc_file:
        encrypted_message = enc_file.read().strip().split(",")  # Encrypted numbers in CSV format

    print("\nEncrypted text loaded successfully.")
    txt_encode(encrypted_message)


def BinaryToDecimal(binary):
    return int(binary, 2)


def decode_txt_data():
    ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
    stego = input("\nEnter the stego file name (with extension) to decode the message: ")

    if not os.path.exists(stego):
        print("\nStego file not found!")
        return

    temp = ''
    with open(stego, "r", encoding="utf-8") as file4:
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

    print("\nEncoded binary extracted:", temp)
    lengthd = len(temp)
    print("\nLength of encoded binary: ", lengthd)
    print("\nEncrypted message after decoding: ", temp)


def txt_steg():
    while True:
        print("\n\t\tTEXT STEGANOGRAPHY OPERATIONS")
        print("1. Encode the Text message (from encrypted file)")
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
