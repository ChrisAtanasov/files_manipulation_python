'''Write a program that reads a text file and inserts line numbers in front of each of its lines.
The result should be written to another text file.'''


with open('Input_lines.txt','r') as r:
    with open('number_of_lines.txt','w') as wr:
        for num,lines in enumerate(r):
            numbers = int(num+1)
            wr.writelines(f'{str(numbers)}. {lines}')




''' Here we read the from the existing text file and create a new text file with the numbers of each line
 from the old text.'''
