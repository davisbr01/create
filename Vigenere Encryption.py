import math
from tkinter import *
from random import randint

frame = Tk()
frame.geometry("900x400")
frame.title("Vigenere Encrypter")

"""Encryption Section"""

label_word = Label(text = "Please enter the word you want to encrypt.")
label_word.place(x = 127, y = 60)
box_word = Text(width = 40,height = 1)
box_word.place(x = 130, y = 80)

label_shift = Label(text = "Please enter the the shift key word.")
label_shift.place(x = 500, y = 60)
box_shift_key = Text(width = 40,height = 1)
box_shift_key.place(x = 503, y = 80)

text = StringVar()
label_result = Label(textvariable = text)
label_result.place(x=130,y=140)

#requesting input phrase
#includes user input
def get_word():
        test_word = box_word.get(1.0,'end-1c')
        return test_word

#requests shift key word
def get_key():
        shift_key = box_shift_key.get(1.0,'end-1c')
        return shift_key

#method that ignores all the non-alphabetical characters in the input
def helper_method(input_word):
        helped_word = input_word.replace(" ","")
        helped_word = helped_word.replace(",", "")
        helped_word = helped_word.replace(".", "")
        helped_word = helped_word.replace("?", "")
        helped_word = helped_word.replace("!", "")
        helped_word = helped_word.replace("'", "")
        helped_word = helped_word.replace("\"", "")
        helped_word = helped_word.replace("/", "")
        helped_word = helped_word.replace("-", "")
        helped_word = helped_word.replace("'", "")
        helped_word = helped_word.replace(";", "")
        helped_word = helped_word.lower()
        return helped_word

#method that encrypts the entered word
def encrypt(test_word, shift_key):
        encrypted_word = ""
        
        for index in range(len(test_word)):
                number_shifted = (  (ord(test_word[index]) - 97) + (ord(shift_key[index]) - 97) ) % 26
                encrypted_char = chr(number_shifted+97)
                encrypted_word += encrypted_char
                
        return encrypted_word

#method that returns the repeated shift key
def real_shift_key(test_word,shift_key):
        num_repeats = int(len(test_word) / len(shift_key)) - 1
        num_remainder = len(test_word) % len(shift_key)
        real_shift_key = shift_key
        for index in range(num_repeats):
                real_shift_key += shift_key
        real_shift_key += shift_key[:num_remainder]
        return real_shift_key

#method that button calls so that label can update
def determinec():
        text.set(encrypt(get_word(),real_shift_key(helper_method(get_word()),helper_method(get_key()))))

button_encrypt = Button(text = "Encrypt!", width = 10, height = 1, command = determinec)
button_encrypt.place(x=130,y=110)

"""Decryption Section"""

label_decrypt = Label(text = "Please enter the word you want to decrypt.")
label_decrypt.place(x = 127, y = 160)
box_decrypt = Text(width = 40,height = 1)
box_decrypt.place(x = 130, y = 180)

label_shift = Label(text = "Please enter the the shift key word.")
label_shift.place(x = 500, y = 160)
box_decrypt_key = Text(width = 40,height = 1)
box_decrypt_key.place(x = 503, y = 180)

text2 = StringVar()
label_result_decrypt = Label(textvariable = text2)
label_result_decrypt.place(x=130,y=240)

def get_decrypt_word():
        decrypt_word = box_decrypt.get(1.0,'end-1c')
        return decrypt_word

def get_decrypt_key():
        decrypt_key = box_decrypt_key.get(1.0,'end-1c')
        return decrypt_key

def decrypt(test_word, shift_key):
        decrypted_word = ""
        
        for index in range(len(test_word)):
                number_shifted = (  (ord(test_word[index]) - 97) - (ord(shift_key[index]) - 97) ) % 26
                decrypted_char = chr(number_shifted+97)
                decrypted_word += decrypted_char
                
        return decrypted_word

def determined():
        text2.set(decrypt(get_decrypt_word(),real_shift_key(helper_method(get_decrypt_word()),helper_method(get_decrypt_key()))))

button_decrypt = Button(text = "Decrypt!", width = 10, height = 1, command = determined)
button_decrypt.place(x=130,y=210)

frame.mainloop()

