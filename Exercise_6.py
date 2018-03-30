*Exercise 6*

You have a list of integers, and for each index you want to find the
product of every integer except the integer at that index.
a list of integers and returns a list of the products.
For example, given:
[1, 7, 3, 4]
your function would return:
[84, 12, 28, 21]`
by calculating:
[7*3*4, 1*3*4, 1*7*4, 1*7*3]

def product_of_array(array):
    product = 1
    itorator = 0 

    if len(array) == 1:
        return array
    for item in array:
        product *=item
   
    for item in range(len(array)):
        if item != 0:
            array[itorator] = int( product/item)
        else:
            array[itorator] = product
        itorator +=1
    return array
array = [1,7,3,4]
print(product_of_array(a