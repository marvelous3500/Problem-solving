
*Exercise 1*
Create a method that takes an array of numbers and a targeted number and returns similar number pairs that when added gives the same result as the targeted number. 
_For Example_:  `array = [1,2,3,4,5,6,1,3,2,1,4,5,3,5,2,5]` and `Target = 8` it should 
[[5,3],[3,5]]` because when you added them it give `8` which is the target


def pairs (array , target ):
    current_number = 0 
    next_number = len(array) - 1 
    new_array = []
    while(current_number < next_number): 
        if array[current_number] + array[next_number] == target :       
             new_array.append(array[current_number]), new_array.append( array[next_number])  
             return new_array
        elif array[current_number] + array[next_number] < target:
             current_number += 1
        else:
             next_number -=1
target = 8
array = [1,2,3,4,5,6,1,3,2,1,4,5,3,5,2,5]
