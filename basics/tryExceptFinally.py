file = None

try:
    file = open("example.txt", "a")
    file.write("\nI am learning to use try-except-finally.\n")
    print("Text has been written to the file.")
except FileNotFoundError:
    print("The file was not found.")
finally:
    if file:
        file.close()
        print("File has been closed.")