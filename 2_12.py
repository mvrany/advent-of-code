import numpy as np

if __name__ == '__main__':
    #intcode = [1,1,1,4,99,5,6,0,99]
    def_intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]
    pointer = 0
    multipliers = []
    result = []
    def run_code(intcode, i):
        if intcode[i]== 1:
            res = intcode[intcode[i+1]]+intcode[intcode[i+2]]
            #print("{0} + {1} = {2}".format(intcode[intcode[i + 1]], intcode[intcode[i + 2]], res))
            intcode[intcode[i+3]] = res

        elif intcode[i] == 2:
            if intcode[intcode[i+1]] <= intcode[intcode[i+2]]:
                multipliers.append(intcode[intcode[i+1]])
            else:
                multipliers.append(intcode[intcode[i + 2]])
            res = intcode[intcode[i+1]]*intcode[intcode[i+2]]
            #print("{0} * {1} = {2}".format(intcode[intcode[i + 1]], intcode[intcode[i + 2]], res))
            intcode[intcode[i + 3]] = res

        elif intcode[i] == 99:
            print('found end')
        else:
            print('Unknown value: ' + str(intcode[i]))
            return None
        return intcode

    intcode = def_intcode
    intcode[1] = 64



    for x in range(100):
        pointer = 0
        intcode = def_intcode.copy()
        intcode[1] = 64
        intcode[2] = x
        while intcode and intcode[pointer]!=99:
            intcode = run_code(intcode, pointer)
            pointer += 4
        if intcode and intcode[0]==19690720:
            print(x)
            break



