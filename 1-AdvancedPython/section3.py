
#Always remenber when you call hello_function()
#Need for decorators
import time
def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers :
        result.append(number*number)
    end = time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is {total_time}")
    return result


def calc_cube(numbers):
    start=time.time()
    result = []
    for number in numbers :
        result.append(number*number*number)
    end = time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution cube is {total_time}")
    return result

array = range (1,3)
out_square= calc_square(array)
out_cube = calc_cube(array)
