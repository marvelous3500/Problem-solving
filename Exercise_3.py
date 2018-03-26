*EXERCISE 3.*
If we list all the natural numbers below 10 that are multiples of `3` or `5`, we get `3, 5, 6` and `9`. The sum of these multiples is `23`.
Find the sum of all the multiples of 3 or 5 below 1000. 

Exercise 3 pseudo code
Step 1.  create a array  (multiple_sum)
Step 2.. Loop from 0 to 1000
Step 3. Where looping check for multiple of 3 or 5 
Step 4. Add the multiple to multiple_sum
Step 6. return the sum of multiple_sum

def multiple():
    multiple_sum = 0
    for number in range(1000):
        if number%3 == 0 or number%5 == 0:
            multiple_sum+=number
    return   multiple_sum
print(multiple())
