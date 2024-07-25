import os
from re import MULTILINE
import tkinter as tk
import google.generativeai as genai

window = tk.Tk()
window.title("Lyrical Resolve")
window.geometry("400x500")

tk.Label(window, text="Song Genre").pack()
genretextbox = tk.Text(width=20,height=1, wrap="word")
genretextbox.pack()
tk.Label(text="Topics or keywords to include in the song").pack()
keywordstextbox = tk.Text(width=20,height=1, wrap="word")
keywordstextbox.pack()
tk.Label(text="Number of verses or a whole song").pack()
versestextbox = tk.Text(width=20,height=1, wrap="word")
versestextbox.pack()
tk.Button(text="Generate",command=lambda:generate()).pack()
output = tk.Text()
output.pack()

print("LYRICAL RESOLOVE [TUI EDITION]")

GEMENI_API_KEY = os.environ['GEMENI_API_KEY']

genai.configure(api_key=GEMENI_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate():
  genre = genretextbox.get("1.0", "end")
  keywords = keywordstextbox.get("1.0", "end")
  verses = versestextbox.get("1.0", "end")
  prompt = f"Write lyrics for a song in the genre of {genre} and is about the following keywords {keywords} in {verses} verses"
  response = model.generate_content(prompt)
  output.insert("end", "\n"+response.text)


window.mainloop()