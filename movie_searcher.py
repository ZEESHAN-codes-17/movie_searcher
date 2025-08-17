import requests
import tkinter as tk
from PIL import Image, ImageTk
import io



def movie_inf():

   movie = movie_entry.get()

   api_key = "paste_your_api_key_here"

   url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"

   response = requests.get(url) 

   data = response.json()

   if data["Response"] == "True":
    title_label.config(text=f"Title: {data['Title']}")
    year_label.config(text=f"Year: {data['Year']}")
    genre_label.config(text=f"Genre: {data['Genre']}")
    director_label.config(text=f"Director: {data['Director']}")
    plot_label.config(text=f"Plot: {data['Plot']}")

    # --- Poster handling ---
    poster_url = data["Poster"]
    if poster_url != "N/A":  
        img_data = requests.get(poster_url).content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((300, 450))  
        poster_img = ImageTk.PhotoImage(img)
        poster_label.config(image=poster_img)
        poster_label.image = poster_img  
    else:
        poster_label.config(image="", text="Poster not available")



# Create a simple GUI to display the movie information
root = tk.Tk()
root.config(bg="#1a1a2e")
root.title("Movie Searcher")
root.geometry("800x600")

movie_entry= tk.Entry(root, width=40, bg="#16213e", fg="white", insertbackground="white", font=("Arial", 12), relief="flat", bd=5)
movie_entry.pack(pady=20)

search_button = tk.Button(root, text="Search", command=movie_inf, bg="#0f3460", fg="white", font=("Arial", 12, "bold"), relief="flat", bd=0, padx=20, pady=8, activebackground="#533483", activeforeground="white")
search_button.pack(pady=20)

title_label = tk.Label(root, text="", font=("Arial", 16), bg="#1a1a2e", fg="#e94560")
title_label.pack(pady=10)

year_label = tk.Label(root, text="", font=("Arial", 14), bg="#1a1a2e", fg="#f5f5f5")
year_label.pack(pady=10)

genre_label = tk.Label(root, text="", font=("Arial", 14), bg="#1a1a2e", fg="#0f4c75")
genre_label.pack(pady=10)

director_label = tk.Label(root, text="", font=("Arial", 14), bg="#1a1a2e", fg="#3282b8")
director_label.pack(pady=10)

plot_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, bg="#1a1a2e", fg="#bbe1fa")
plot_label.pack(pady=10)

poster_label = tk.Label(root, bg="#1a1a2e")
poster_label.pack(pady=10)

root.mainloop()