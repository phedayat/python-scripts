l = [1, 2] # list to be perumuted

'''
Heap's Algorithm

Prints every permutation of a list of elements
For a list with n elements, we have n! permutations
'''
def generate(k, ar):
    if k == 1:
        print(ar)
    else:
        generate(k-1, ar)
        for i in range(0, k-1):
            if k % 2 == 0:
                temp = ar[k-1]
                ar[k-1] = ar[i]
                ar[i] = temp
            else:
                temp = ar[k-1]
                ar[k-1] = ar[0]
                ar[0] = temp
            generate(k-1, ar)

generate(len(l), l)


