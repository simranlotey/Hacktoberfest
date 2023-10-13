function dfs(graph, start) {
    var stack = [start];
    var visited = [];
    var node;

    while (stack.length) {
        node = stack.pop();
        if (visited.indexOf(node) == -1) {
            visited.push(node);
            stack.push.apply(stack, graph[node]);
        }
    }

    return visited;
}

var graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

console.log(dfs(graph, 'a')); // ['a', 'c', 'e', 'b', 'd', 'f']
