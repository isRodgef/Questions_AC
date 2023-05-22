class Node:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.title < other.title
    def __gt__(self, other):
        return self.title > other.title
    def __eq__(self, other):
        return self.title == other.title  

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        parent = None
        current = self.root
        while current:
            parent = current
            if node < current:
                current = current.left
            else:
                current = current.right
        
        new_node = node
        if  new_node < parent:
            parent.left = new_node
        else:
            parent.right = new_node

    def bulk_insert(self, nodes):
        if not nodes:
            return

        mid = len(nodes) // 2
        self.insert(nodes[mid])

        self.bulk_insert(nodes[:mid])
        self.bulk_insert(nodes[mid+1:])

    def search(self, title):
        search_node = Node(title)
        current = self.root
        while current:
            if current.title == title:
                return current
            elif search_node < current:
                current = current.left
            else:
                current = current.right
        return None


def read_movies_from_file(file_path):
    movies = []
    with open(file_path, 'r') as file:
        for line in file:
            movie = line.strip()
            movies.append(Node(movie))
    return movies


def build_binary_tree(movies):
    binary_tree = BinaryTree()
    binary_tree.bulk_insert(movies)
    return binary_tree

if __name__ == '__main__':
    movies_file = 'section_a/datastructures3.csv'  
    movies = read_movies_from_file(movies_file)
    binary_tree = build_binary_tree(movies)
    
    search_title = '2nd Amendment: The Right To Bear Arms'
    result = binary_tree.search(search_title)
    if result:
        print(f"Movie found: {result.title}")
    else:
        print("Movie not found")
    
    search_title = "The life story of Rodger Rabbit"
    result = binary_tree.search(search_title)
    if result:
        print(f"Movie found: {result.title}")
    else:
        print("Movie not found")