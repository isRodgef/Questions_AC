### Question 

Write a program that takes as input a list of numbers and finds the average number of all given numbers.

### Answer file

B0_algorithm.py

### How to run 

python B0_algorithm.py

### Approach

- Set a total to 0
- Iterate through a list add to total
- Return Total

## Additional note:

- using standard functions could be done  this way
```
    sum(list_var) / len(list_var)
```


### Question 

Given an unsorted number list of 5K numbers. Sort the list as fast as possible. Speed is a factor. Your marks are based on the relative speed of execution. You may not use the built in sorting function.

### Answer file

B1_algorithm.py

### How to run 

python B1_algorithm.py

### Approach

- function takes in an iterable (will already be read from file at this point)
- Create an empty list
- loop through iterable
- if return_list empty append current number
- if not
    - loop through resultant list
    - if the number is smaller than the value at result[current index]   prepend to resultant list
    - if we reach the end of the list append to list

## Additional note:

- This uses a variant of the selection sort algorithm
- Using lists in this case makes sense as we start out with a file buffer object
- If I needed to sort in place I would probably uses bubble or quick sort
