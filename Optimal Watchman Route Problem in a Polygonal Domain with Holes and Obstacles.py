import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Watchman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [(x, y)]

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.path.append((x, y))

    def __repr__(self):
         return f"Watchman({self.x},{self.y})"


def is_covered(grid, watchman_path, visibility_range=float('inf')):
    """Checks if all grid cells are covered by the watchman's path."""
    covered = [[False] * len(grid[0]) for _ in range(len(grid))]

    for x, y in watchman_path:
        # In this simplified version, with infinite visibility, every visited cell covers itself and neighbors
        for i in range(max(0, x - 1), min(len(grid), x + 2)):
            for j in range(max(0, y - 1), min(len(grid[0]), y + 2)):
                covered[i][j] = True

    for row in covered:
        if False in row:
            return False  # Not all cells covered
    return True


def create_grid(width, height):
    """Creates a simple grid representing the environment."""
    return [[0] * width for _ in range(height)]


def simple_coverage_path(grid, start_x, start_y):
    """Generates a simple (non-optimal) path that covers the entire grid."""
    watchman = Watchman(start_x, start_y)
    width = len(grid[0])
    height = len(grid)

    # Simple boustrophedon ("ox-turning") path - like mowing a lawn
    for y in range(height):
        if y % 2 == 0:  # Even rows: move right
            for x in range(width):
                if (x,y) != (watchman.x, watchman.y): #Skip starting position
                    watchman.move_to(x, y)
        else:  # Odd rows: move left
            for x in range(width - 1, -1, -1):
                 watchman.move_to(x, y)

    return watchman.path

def plot_environment(grid, watchman_path):
    """Plots the grid and the watchman's path."""
    fig, ax = plt.subplots()
    width = len(grid[0])
    height = len(grid)

    # Draw the grid
    for y in range(height):
        for x in range(width):
            rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='gray', facecolor='lightgray')
            ax.add_patch(rect)

    # Draw the watchman's path
    path_x, path_y = zip(*watchman_path)
    ax.plot(path_x, path_y, 'b-', marker='o', markersize=5)
    ax.plot(path_x[0],path_y[0],'go',markersize=8) # Start point

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    plt.title("Watchman's Path")
    plt.show()
# Example Usage:
width = 10
height = 8
grid = create_grid(width, height)
start_x = 0
start_y = 0

watchman_path = simple_coverage_path(grid, start_x, start_y)

if is_covered(grid, watchman_path):
    print("All grid cells are covered.")
else:
    print("Not all grid cells are covered.")

plot_environment(grid, watchman_path)

print(f"Path length: {len(watchman_path)}")
