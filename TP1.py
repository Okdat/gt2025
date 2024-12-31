from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, x, y):
        if x not in self.adjacency_list:
            self.adjacency_list[x] = []
        if y not in self.adjacency_list:
            self.adjacency_list[y] = []
        self.adjacency_list[x].append(y)
        self.adjacency_list[y].append(x)

    def path_exist(self, start, target):
        if start not in self.adjacency_list or target not in self.adjacency_list:
            return False
        
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            if current == target:
                return True
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

def main():
    graph = Graph()

    # Input number of edges 
    print("Enter edges (e.g., '1 2'). Write 'done' when finished:")
    while True:
        edge = input("Edge: ").strip()
        if edge.lower() == "done":
            break
        try:
            x, y = map(int, edge.split())
            graph.add_edge(x, y)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

    # Input start and target nodes
    try:
        start = int(input("Enter start node: "))
        target = int(input("Enter target node: "))
    except ValueError:
        print("Invalid input. Nodes must be integers.")
        return

    # Check path existence
    if graph.path_exist(start, target):
        print("Path exists")
    else:
        print("No path exists.")

if __name__ == "__main__":
    main()
