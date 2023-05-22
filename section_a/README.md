### Question

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward, such as “madam” or “racecar”. Capital letters and spaces do not break the palindrome property. “Dammit Im mad” is considered a palindrome. Given a string inputted from the user, write a program that would determine whether or not the given string is a palindrome. Your software should output “Yes” if the word is a palindrome and “No” if the word is not a palindrome. You may not use the built in reverse function of strings. 

### Answer file:

A1_palindrome.py

### How to run

python A1_palindrome.py

### Approach:

To solve it, I set and index to the start and the end of the list. Iterating the first index while decrementing the seccond index up until the middle of the list (where the index used to represent the start of the list is greater than the one used to point to the end of the list).

 
### Question 

Given files with contact information, write a program that can read, edit, find, add and remove records to the data as efficient as possible. The data can be stored in memory and does not need to be written to a file or a database. You do not need to provide a GUI. You get marked on insertion time, searching time, deleting time and space requirements for your algorithm. 2 Marks per property. The more efficient, the better the marks. You will receive no marks for a property if the time or space complexity exceeds O(n).

### Answer file:

A2_datastructures2.py

### How to run

python section_a/A2_datastructures2.py

### Approach:

Setup 2 main classes 

- FullName
    - Contains the name and surname as attributes
    - Has some operators overloaded
        - eq for use with == operator
        - str for formatting display from print function
        - hash sets require hashable objects to be ys
- NameList 
    - encapsulates a set that contains the list of names
    - uses set.add in it's insert function
    - uses set.remove in it's delete
    - uses the in operator in the search function


### Question

Given a list of movies in a text file, read the data into memory, and using one of the following algorithms: Binary-Tree, AVL Tree, Splay Tree, Skip List, write a search function based on the title of the movie. Searching can be case sensitive. You get full marks if the algorithm is correctly implemented for all general cases. Losing marks for problem specific code, memory issues or cases not considered.

### Answer file:

A3_datastructures3.py   

### How to run:

python A3_datastructures3.py 

### Approach:

Setup 2 main classes:

- Node
    - Class that encapsulates title (str)
    - Overloaded comparisons operators
- BinaryTree Class 
    - Generic Binary Tree Class
    - Insert function inserts by placing the latest element left of the latest node if the value is less than the end of the tree otherwise placing it on the right.
    - Search function works by iterating through the tree (moving left if the currently looked at is greater than search node moving right if less than and returning if equal).


Caveats:

- The insertions function was to slow to do inserts so the bulk insert does it by using a divide and conquer strategy

Main block

- Loads the file into memory and building using bulk insert
- Searches the tree for a title found in the file
- Searches tree for a title not found in the file


