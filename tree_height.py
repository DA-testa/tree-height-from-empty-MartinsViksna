# python3
# Mārtiņš Vīksna 221RDB220
import sys
import threading
import numpy as np


def compute_height(n, parents):
    heights = np.zeros(n)
    # Write this function
    max_height = 0
    for i in range(n):
        if heights[i] == 0:
            height =1
            p = parents[i]
            while p!= -1:
                if heights[p] !=0:
                    height += heights[p]
                    break
                height +=1
                p = parents[p]
        max_height = max(max_height, height)

    # Your code here
    return max_height


def main():
    x = input("input from where will you input information?")
    if 'F' in x:
        file_name = input("input the name of the file(make sure it has no a's)")
        file_name = "test/" + file_name
        if 'a' in file_name:
            print("a in file name")
        try:

            with open(file_name)as file:
                n = int(file.readline())
                parents = np.frombuffer(file.readline().strip(), dtype=int)
        except IOError:
            print("no such file")
            return

    elif 'I' in x:
        n = int(input("how long will be the tree"))
        parents = np.array(list(map(int, input("input the numbers").strip().split())))
    else:
        print("wrong input")
        return
    
    print(compute_height(n, parents))


        


    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# print(np.array([1,2,3]))
