#opening and reading from a file
#Alwayys remember to close the file opened - might run out of file handles if we don't do so and open many files

f= open('testfile.txt')
read_text = f.read()
#print(read_text)
f.close()

#writing to a file
# Writing to a file always removes the contents in the file. Use append instead to add to the file
#f = open('/my_path/my_file.txt','w')
#f.close()

#Using with to avoid closing the file everytime.
#With - Python allows you to open a file, do operations on it, and automatically close it afterwards using with.
with open('testfile.txt') as f:
    file_data = f.read()
    print(file_data)
#every line in the file ends with a new line character. we use .strip() will remove the newline character
