'''Write a program that reads a text file and writes its every odd line in another file. Line numbers starts from 0.'''

with open('Input.txt','r') as r:
    with open('Input_result.txt', 'w') as wr:
        for num,line in enumerate(r):
            if num % 2 == 1:
              wr.write(line)


''' Here we read the text from the existing file and create the new  file, 
where we print all odd lines from the old text file'''






