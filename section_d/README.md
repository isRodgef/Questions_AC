### Question 

To check whether an account number is genuinely a number allocated by the bank, the Pomme Bank of Paris uses the following technique. All the non-zero digits in the number are multiplied by each other. All the non-zero digits of the resulting number are again multiplied by each other – and so on until a single digit is left. That is the security digit.

### Answer file

D_easy1_pomme.py

### How to run 

python D_easy1_pomme.py

### Approach

- Set a total to 0
- Iterate through a str
- cast to an int
- add to total
- if total less than 10
- Return Total
- else 
- call pomme function repeatedly

### Question 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
Prime Algorithm – 2 Marks
Correct Answer – 3 Marks

### Answer file

D_medium1_sum_primes.py

### How to run 

python D_medium1_sum_primes.py

### Approach

- I used an algorithm called the sieve of atkin  (https://en.wikipedia.org/wiki/Sieve_of_Atkin)
- Build a boolean list up until the stop point
- initialise lis at [2,3]
- start at 1
            - apply n = 4*x*x + y**2
                if n is less than limit  and (12 mod n == 5 or 12 mod n == 1) set index to true
                    - sieve[n] = not sieve[n]
            apply n = 3*x**2+y**2
                if n is less than limit set index to true  and 12 mod n == 7  set index to true
            apply n = 3*x**2 - y**2
                if n is less than limit set index to true and 12 mod n == 11  set index to true

### Links I used to assist in implementation

https://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python

https://www.geeksforgeeks.org/sieve-of-atkin/

### Question 

To check whether an account number is genuinely a number allocated by the bank, the Pomme Bank of Paris uses the following technique. All the non-zero digits in the number are multiplied by each other. All the non-zero digits of the resulting number are again multiplied by each other – and so on until a single digit is left. That is the security digit.

### Answer file

D_hard2_froggon.py

### How to run 

python section_d/D_hard2_froggon.py

### Approach

- initial factorial list to [1] = 1!
- Check while the head of list is < n 
    - prepend next factorial
- iterate through factorial list
    - divide n by factorial 
        - if n is greater than factorial prepend the result of division
    - set n <- n mod factorial to work with the rest of the remainder
