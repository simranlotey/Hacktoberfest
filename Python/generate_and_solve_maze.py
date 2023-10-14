import random

class NewMaze:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = [['#'] * (2 * width + 1) for _ in range(2 * height + 1)]
        self.solution = []

    def generate(self):
        for y in range(self.height):
            for x in range(self.width):
                self.maze[2*y+1][2*x+1] = ' '

        walls = []
        start_cell = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        walls += self.get_adjacent_walls(start_cell)

        while walls:
            wall = random.choice(walls)
            walls.remove(wall)
            x, y = wall

            if x % 2 == 0 and (self.is_inside((x//2-1, y//2)) != self.is_inside((x//2, y//2))):
                self.maze[y][x] = ' '
                if self.is_inside((x//2-1, y//2)):
                    cell = (x//2, y//2)
                else:
                    cell = (x//2-1, y//2)
                walls += self.get_adjacent_walls(cell)
            elif y % 2 == 0 and (self.is_inside((x//2, y//2-1)) != self.is_inside((x//2, y//2))):
                self.maze[y][x] = ' '
                if self.is_inside((x//2, y//2-1)):
                    cell = (x//2, y//2)
                else:
                    cell = (x//2, y//2-1)
                walls += self.get_adjacent_walls(cell)

    def get_adjacent_walls(self, cell):
        x, y = cell
        walls = []

        if x > 0:
            walls.append((2*x, 2*y+1))
        if x < self.width-1:
            walls.append((2*x+2, 2*y+1))
        if y > 0:
            walls.append((2*x+1, 2*y))
        if y < self.height-1:
            walls.append((2*x+1, 2*y+2))

        return walls

    def is_inside(self, cell):
        x, y = cell
        return 0 <= x < self.width and 0 <= y < self.height

    def solve(self, start=(1, 1), end=None):
        if not end:
            end = (2*self.width-1, 2*self.height-1)

        stack = [start]
        visited = set()

        while stack:
            x, y = stack[-1]
            if (x, y) == end:
                self.solution = stack.copy()
                return True

            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            unvisited_neighbors = [nb for nb in neighbors if nb not in visited and self.maze[nb[1]][nb[0]] == ' ']

            if unvisited_neighbors:
                stack.append(unvisited_neighbors[0])
                visited.add(unvisited_neighbors[0])
            else:
                stack.pop()

        return False

    def display(self):
        for y in range(2*self.height+1):
            for x in range(2*self.width+1):
                if (x, y) in self.solution:
                    print('.', end='')
                else:
                    print(self.maze[y][x], end='')
            print()

if __name__ == "__main__":
    maze = NewMaze(10, 10)
    maze.generate()
    maze.solve()
    maze.display()
