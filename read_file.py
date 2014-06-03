#/usr/bin/env/python
"""
read file and print all lines
"""
import sys
def process_file(filename):
    '''open ,read, and print a file. '''
    input_file=open(filename,'r');
    for line in input_file:
        line=line.strip()
        print(line)
    input_file.close()
if __name__=='__main__':
    process_file(sys.argv[1])