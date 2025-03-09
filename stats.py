def count_words(file_contents):
    words = file_contents.split()
    total = 0
    for word in words:
        total += 1
    print (f"{total} words found in the document")