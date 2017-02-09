# 1 to 10
# for number in range(1, 11):
#     print(number)

# n to m
# start = int(raw_input("Start from: "))
# end = int(raw_input("End on: "))
# for number in range(start, (end + 1)):
#     print(number)

#odd numbers
# for number in range(1, 11):
#     if number % 2 != 0:
#         print(number)

#print a square
# for number in range(5):
#     print "*" * 5

#Print a Square II
# size = int(raw_input("How big is the square? "))
# for number in range(size):
#     print("*" * size)

# #Print a box
# width = int(raw_input("Width? "))
# height = int(raw_input("Height? "))
# print ("*" * width)
# for number in range(height - 2):
#     print("*" + (" ") * (width - 2) + "*")
# print ("*" * width)

#Print a traiangle
# spaces = 3
# for number in range(1, 8, 2):
#     print " " * spaces + "*" * number
#     spaces -= 1

#Print a triangle II
# height = int(raw_input("How tall is your triangle? "))
# spaces = height
# for number in range(1, (height*2 + 1), 2):
#     print " " * spaces + "*" * number
#     spaces -= 1

#Multiplication Table
# for j in range(1, 11):
#     for i in range(1, 11):
#         value = j * i
#         print "%d X %d = %d" % (j, i, value)

#Python banner
# text = raw_input("Text? ")
# print "*" * (len(text) + 4)
# print "* %s *" % text
# print "*" * (len(text) + 4)

#Triangle numbers
# for i in range(1, 101):
#     print (i * (i + 1)) / 2

#Factor a number
# number = int(raw_input("Give me a number and I'll tell you it's factors: "))
# for factor in range(1, (number + 1)):
#     if number % factor == 0:
#         print factor
