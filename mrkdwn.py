#This is a simple Markdown editor that allows user to write Markdown in one text area and render the HTML in another text area.
#User can also save the HTML to a file.

import tkinter as tk
from tkinter import scrolledtext
import markdown

def render_markdown():
    markdown_text = input_text.get("1.0", "end-1c")
    html_text = markdown.markdown(markdown_text)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", html_text)

def save_to_file():
    markdown_text = input_text.get("1.0", "end-1c")
    file_name = "output.html"
    with open(file_name, "w") as file:
        file.write(markdown_text)

app = tk.Tk()
app.title("Markdown Editor")

# Create input text area
input_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=10)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Create a button to render Markdown
render_button = tk.Button(app, text="Render Markdown", command=render_markdown)
render_button.grid(row=1, column=0, padx=10)

# Create a button to save the content to a file
save_button = tk.Button(app, text="Save to File", command=save_to_file)
save_button.grid(row=1, column=1, padx=10)

# Create output text area for HTML rendering
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=40, height=10)
output_text.grid(row=0, column=1, padx=10, pady=10)

app.mainloop()