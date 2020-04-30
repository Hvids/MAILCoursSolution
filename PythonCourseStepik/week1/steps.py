import sys

def printSpace(k):
    for i in range(k):
        print(' ', end="")

def printHash(k):
    for i in range(k):
        print('#',end="")

if __name__ == '__main__':
    num_steps = int(sys.argv[1])
    for i in range(num_steps):
        printSpace(num_steps-i-1)
        printHash(i+1)
        print('')
