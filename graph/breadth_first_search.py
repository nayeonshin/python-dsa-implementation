from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited_nodes = set()  # Set to keep track of visited nodes
queue = deque([])  # Initializes a queue


def breadth_first_search(visited_nodes: set, graph: dict, node: str) -> None:
    """
    Time complexity: O(|V| + |E|)
    """
    visited_nodes.add(node)
    queue.append(node)

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)


# Driver code
breadth_first_search(visited_nodes, graph, "A")
