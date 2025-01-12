
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
print (file_contents)

words = file_contents.split()
total = 0
for word in words:
    total += 1
print (total)