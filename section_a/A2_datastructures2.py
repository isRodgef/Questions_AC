import csv

filename = 'datastructures2.csv'

class Fullname:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
    def __str__(self) -> str:
        return self.firstname + " " + self.surname

    def __eq__(self, __value: object) -> bool:
        return self.firstname == __value.firstname and self.surname == __value.surname
    
    def __hash__(self) -> int:
        return hash(self.firstname) + hash(self.surname)

def load_file_list(filename):
    name_set = set()
    # open the csv file for reading
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # skip the header row
        next(reader)
        # iterate over the rows in the csv file
        for row in reader:
            name = Fullname(row[0], row[1])
            name_set.add(name) 
    return name_set


class NameList:
    def __init__(self,existing_map) -> None:
        self.existing_set = existing_map
    
    def search(self,first_name, last_name):
        key = Fullname(first_name, last_name)
        return key in self.existing_set
    
    def insert(self, first_name, last_name):
        key = Fullname(first_name, last_name)
        if key not in self.existing_set:
            self.existing_set.add(key)
    
    def delete(self, first_name, last_name):
        key = Fullname(first_name, last_name)
        if key in self.existing_set:
            self.existing_set.remove(key)

    def __str__(self) -> str:
        return str(self.existing_set)
    
    def __len__(self):
        return len(self.existing_set)

if __name__ == '__main__':
    name_set = load_file_list(filename)
    name_list = NameList(name_set)

    print ("Name list length after loading file: ", len(name_list))
    

    print("Does John Smith appear in list : ",  name_list.search('John', 'Smith'))

    print ("Inserting John Smith into list: ")
    name_list.insert('John', 'Smith')

    print ("Printing list length after inserting John Smith: ", len(name_list))

    print("Does John Smith appear in list : ",  name_list.search('John', 'Smith'))

    print ("Deleting John Smith from list: ")
    name_list.delete('John', 'Smith')

    print ("Printing list length after deleting John Smith: ", len(name_list))
    


