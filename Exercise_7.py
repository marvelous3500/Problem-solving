*Exercise 7*
Write a function that take and ARRAY and removes all odd integers from the array recursively. You must not use any extra array.

Psuodocode for Exercse 7 
Step 1 Create a function
* create a variable product = 1
* create an array list_of_product
Step 2
Check if length of input_array is equal to 1 return the input array
* loop through the input_array
* where looping
              product *=item
Step 3 loop through the input array
* for item in input array
* check if item =0
      Add product to list_of_product 
Else.  
* add product/ item to list_of_product 
Step 4. Display list_of_product


def multiple_of_values(array):
    total_multiple_of_values_in_array = 1
    for item in array:
        total_multiple_of_values_in_array *= item
    iterator = 0
    for item in array:
        if total_multiple_of_values_in_array:
            array[iterator] = int(total_multiple_of_values_in_array / item)
        else:
            array[iterator] = 0
        iterator += 1
    return array