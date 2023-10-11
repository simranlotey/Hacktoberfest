import matplotlib.pyplot as plt
import random


# Function to generate a random color in RGB format
def random_color():
    return random.random(), random.random(), random.random()


# Function to generate a random shape and draw it on the canvas
def draw_random_shape(canvas):
    shape_type = random.choice(["circle", "rectangle", "triangle"])
    color = random_color()

    if shape_type == "circle":
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        size = random.uniform(0.1, 0.4)
        canvas.add_patch(plt.Circle((x, y), size, color=color))

    elif shape_type == "rectangle":
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        width, height = random.uniform(0.2, 0.5), random.uniform(0.2, 0.5)
        canvas.add_patch(plt.Rectangle((x, y), width, height, color=color))

    elif shape_type == "triangle":
        x = random.uniform(0, 1)
        y1, y2, y3 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        canvas.add_patch(plt.Polygon([[x, y1], [x - 0.2, y2], [x + 0.2, y3]], color=color))


# Main function to generate abstract art
def generate_abstract_art(num_shapes=50):
    canvas = plt.gca()
    canvas.set_aspect('equal', adjustable='box')
    canvas.set_axis_off()

    for _ in range(num_shapes):
        draw_random_shape(canvas)

    plt.show()


if __name__ == "__main__":
    num_shapes = 50
    generate_abstract_art(num_shapes)
