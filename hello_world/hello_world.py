from vinpytools import generator

s = "Hello, world!"

print(s)

for index, char in generator.reverse_enumerate(s):
    print(index, char)
