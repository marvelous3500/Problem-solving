# *Exercise 8*

# Write a function that takes an ARRAY and prints the item in the array in reversed order. This should be 
# done recursively! (edited)

def item_in_reverse_order(array, size_of_array):
    # me = "hi"
    reversed_item = []
    current_item = size_of_array  
    if size_of_array <= 0:
        return  
    elif current_item > 0:
        item = array[current_item]
        print("index",item)
        reversed_item.append(item)
        item_in_reverse_order(array,size_of_array  - 1) 
        print(reversed_item)
    else:    
          return reversed_item
    
    #  total_deferent_sensor_value += get_sum_of_sensor_values(sensor_A, sensor_B, length - 1)

    # return total_deferent_sensor_value

array =  ["r","e","t","s","e","v"]
size_of_array = len(array) - 1      
print(item_in_reverse_order(array,size_of_array))   