import tkinter as tk
import requests

# Replace with your Edamam API credentials
APP_ID = "YOUR_APP_ID"
APP_KEY = "YOUR_APP_KEY"

# Function to perform recipe search and display results
def search_recipes():
    query = entry.get()  # Get user's search query
    response = requests.get(
        f"https://api.edamam.com/search?q={query}&app_id={APP_ID}&app_key={APP_KEY}"
    )
    data = response.json()

    results.delete(1.0, tk.END)  # Clear the results area

    # Display recipe results in the text area
    for hit in data.get("hits", []):
        recipe = hit.get("recipe")
        label = recipe.get("label")
        ingredients = ", ".join(recipe.get("ingredientLines"))
        results.insert(tk.END, f"Recipe: {label}\nIngredients: {ingredients}\n\n")

# Create the main application window
app = tk.Tk()
app.title("Recipe Finder")

# Create a frame to hold the GUI components
frame = tk.Frame(app)
frame.pack(pady=10)

# Label for search input
label = tk.Label(frame, text="Enter an ingredient or dish:")
label.pack()

# Entry field for user input
entry = tk.Entry(frame)
entry.pack(pady=10)

# Button to initiate the recipe search
search_button = tk.Button(frame, text="Search", command=search_recipes)
search_button.pack()

# Text area to display recipe results
results = tk.Text(app, width=50, height=20, wrap=tk.WORD)
results.pack()

# Start the Tkinter main loop
app.mainloop()
