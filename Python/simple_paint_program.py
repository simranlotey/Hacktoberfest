import tkinter as tk
from tkinter.colorchooser import askcolor

class Paint:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Paint - Draw & Shape")

        # Canvas
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.draw)

        # Controls
        self.controls_frame = tk.Frame(self.root, padx=5, pady=5)
        self.controls_frame.pack(pady=20)

        # Mode Selection
        self.mode = tk.StringVar(value="draw")
        self.draw_button = tk.Radiobutton(self.controls_frame, text="Draw", variable=self.mode, value="draw")
        self.draw_button.grid(row=0, column=0, padx=5, pady=5)
        self.rectangle_button = tk.Radiobutton(self.controls_frame, text="Rectangle", variable=self.mode, value="rectangle")
        self.rectangle_button.grid(row=0, column=1, padx=5, pady=5)
        self.circle_button = tk.Radiobutton(self.controls_frame, text="Circle", variable=self.mode, value="circle")
        self.circle_button.grid(row=0, column=2, padx=5, pady=5)

        # Color Picker
        self.color_button = tk.Button(self.controls_frame, text="Pick Color", command=self.pick_color)
        self.color_button.grid(row=0, column=3, padx=20, pady=5)

        self.color = "black"
        self.last_x = None
        self.last_y = None

    def draw(self, event):
        x, y = event.x, event.y
        if self.mode.get() == "draw":
            if self.last_x and self.last_y:
                self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.color, width=2)
                self.last_x = x
                self.last_y = y
            else:
                self.last_x = x
                self.last_y = y
        elif self.mode.get() == "rectangle":
            self.canvas.create_rectangle(x-15, y-15, x+15, y+15, outline=self.color, width=2)
        elif self.mode.get() == "circle":
            self.canvas.create_oval(x-15, y-15, x+15, y+15, outline=self.color, width=2)

    def pick_color(self):
        self.color = askcolor()[1] if askcolor()[1] else self.color

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    paint_app = Paint()
    paint_app.run()
