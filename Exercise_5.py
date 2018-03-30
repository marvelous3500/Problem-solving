*Exercise 5*
Write a function that take and ARRAY and removes all odd integers from the array recursively.
You must not use any extra array.


def remove_all_odd_number(array,size_of_array):
    if size_of_array == 0:
         return array
    current_value = array[size_of_array]
    if  current_value  % 2 == 1: 
        array.remove(current_value)
        remove_all_odd_number(array, size_of_array - 1)
    else:
           remove_all_odd_number(array, size_of_array - 1)
    return array
    
array = [2,3,4,5,6,7,8,9,10]
size_of_array = len(array) -1
print(remove_all_odd_number(array,size_of_array))
