import numpy as np
import math


#a
def sum_list(n):
    list_1 = [i for i in range(n+1)]
    return(sum(list_1))


#b
def sum_numpy(n):
    return(np.sum([i for i in range(n+1)]))


#c
def print_to_number():
    i=1
    while(i<=10):
        print ("i = " , i)
        i = i+1


#d
def perfect_square(list_1):
    new_list = []
    for i in range(len(list_1)):
        sr = math.sqrt(list_1[i])
        if(sr - math.floor(sr) == 0):
            new_list.append(list_1[i])
    return(new_list)



#e
def generator (x):
    sqr = x * x
    return (sqr)

#f
def unittest():
    print(sum_list(50))

    print(sum_numpy(50))

    print_to_number()

    print(perfect_square([i for i in range(100) if i != 0]))

    print(generator(5))        

unittest()


#g
A = 529
B = 256

Sum = A + B
print (Sum)

