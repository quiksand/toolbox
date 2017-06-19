import random
import vector

def clear():
    """clearing for python interpreter"""
    for i in range(30):
        print()

def main():
    time = 4 #time in seconds
    res = 30 #resolution (points per second)
    t = [t/(res*time) for t in range(res*time)]
    acc = Vector(3,4,5)
    vel = Vector(0.5, 0, 2)
    h=1.6 # 53
    #E=.5kxx
    #E=mgd
    #E=.5mvv
    #limit 14,5

if __name__ == '__main__':
    main()
