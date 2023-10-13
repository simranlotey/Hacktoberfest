// add breadth first search algorithm in js

function bfs(graph, start) {
    var queue = [start];
    var result = [];
    var visited = {};
    var current;

    visited[start] = true;

    while (queue.length) {
        current = queue.shift();
        result.push(current);

        graph[current].forEach(function (neighbor) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.push(neighbor);
            }
        });
    }

    return result;
}

var graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
};

console.log(bfs(graph, 'A')); // ["A", "B", "C", "D", "E", "F"]