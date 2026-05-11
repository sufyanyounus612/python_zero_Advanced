try:
    file = open("/Users/macbookpro/Downloads/python_zero_Advanced/indroduction/Exception handling/errors.txt","r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
    print("file operation")