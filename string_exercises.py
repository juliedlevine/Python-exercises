#uppercase a string
# name = "julie"
# print name.upper()

#capitalize a string
# name = "julie"
# print name.capitalize()

#reverse a string
# name = "julie dyer"
# print name[::-1]

#Leetspeak
# word = raw_input("Please enter a word: ").upper()
# for letter in word:
#     if letter == "A":
#         word = word.replace("A", "4")
#     elif letter == "E":
#         word = word.replace("E", "3")
#     elif letter == "G":
#         word = word.replace("G", "6")
#     elif letter == "I":
#         word = word.replace("I", "1")
#     elif letter == "O":
#         word = word.replace("O", "0")
#     elif letter == "S":
#         word = word.replace("S", "5")
#     elif letter == "T":
#         word = word.replace("T", "7")
# print word.lower()

#Long-long Vowels
# word = raw_input("Enter a word: ")
# for i in range(len(word) - 1):
#     if (word[i] + word[i + 1]) == "aa":
#         word = word.replace("aa", "aaa")
#         break
#     elif (word[i] + word[i + 1]) == "ee":
#         word = word.replace("ee", "eeeee")
#         break
#     elif (word[i] + word[i + 1]) == "ii":
#         word = word.replace("ii", "iiiii")
#         break
#     elif (word[i] + word[i + 1]) == "oo":
#         word = word.replace("oo", "ooooo")
#         break
#     elif (word[i] + word[i + 1]) == "uu":
#         word = word.replace("uu", "uuuuu")
#         break
# print word

#Caesar Cipher
# key = 13
# code = "lbh zhfg hayrnea jung lbh unir yrnearq"
# code_break = ''
# for i in range(len(code)):
#     ASCII_code = ord(code[i])
#     if ASCII_code == 32:
#         code_break = code_break + " "
#     else:
#         new_ASCII_code = ord(code[i]) + key
#         if new_ASCII_code > 122:
#             new_ASCII_code = new_ASCII_code - 26
#         new_letter = chr(new_ASCII_code)
#         code_break = code_break + new_letter
# print code_break
