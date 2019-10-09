import sys
import os

userInput = raw_input("Enter file name here > ")
size = os.path.getsize(userInput)

file = open(userInput, "r+")
data = []

for i in range(0, size):
    file.seek(i)
    data.append(file.read(1))

file.truncate(0)

file.write(data[0])

for j in range(1, size):
    file.write(",")
    file.write(data[j])

file.close()
