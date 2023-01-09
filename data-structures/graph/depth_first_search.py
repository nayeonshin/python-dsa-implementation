# Using a Python dictionary to act as an adjacent list
graph = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "C": ["F"],
  "D": [],
  "E": ["F"],
  "F": []
}

visited_nodes = set()  # Set to keep track of visited nodes


def depth_first_search(visited_nodes: set, graph: dict, node: str) -> None:
    """
    Time complexity: O(|V| + |E|)
    """
    if node not in visited_nodes:
        print(node, end=" ")
        visited_nodes.add(node)

        for neighbor in graph[node]:
            depth_first_search(visited_nodes, graph, neighbor)


# Driver code
depth_first_search(visited_nodes, graph, "A")
