# for given input N, generate int array size of N, with numbers in range -N to N where  0 < N <= 100,
# sum has to be equal to 0 and numbers have to be unique
import sys

N = int(sys.argv[1])

if not (N % 2):
    # "even"
    # fill out the array interleaving oppostie numbers ex. [-1] [1] [-2] [2]
    output_array_1 = [x for x in range(1, (N // 2)+1)]
    output_array_2 = [-x for x in range(1, (N // 2)+1)]
    output_array = output_array_1 + output_array_2
    print("N: ", N, "resulting array:", output_array, "sum is:", sum(output_array))

if N % 2:
    print("odd")
    # array starting from -N and continue as with 'even' array until array[N] which fill with -1*sum(previous cells)
    # ex. N=5 [-5] [1] [-1] [2] [(-5+1-1+2)*-1=3]
    output_array = list()
    output_array.append(-N)
    output_array_1 = [x for x in range(1, (N // 2) + 1)]
    output_array_2 = [-x for x in range(1, (N // 2) + 1)]
    output_array_2[-1] = -1 * (sum(output_array_1)+(-N)+sum(output_array_2[:-1]))
    output_array = output_array+output_array_1 + output_array_2
    print("N: ", N, "resulting array:", output_array, "sum is:", sum(output_array))

#TODO: add some tests