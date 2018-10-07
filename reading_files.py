'''This is a simple way to read a text file from the current directory.'''

with open('hello.txt') as f:
    content = f.read()
    print(content)


''' Here will try to write some text to the new file.'''

with open('hello2.txt','w') as new_f:
    new_f.write('Hello, nice to meet you.')
