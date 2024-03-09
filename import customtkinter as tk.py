import customtkinter as tk
import random
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def validate_input():
    name = entry.get()
    if not name:
        label.configure(text="PLEASE ENTER A TEXT", text_color="red")
    else:
        color = random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple'])
        label.configure(text=name, text_color=color)

app = tk.CTk()
app.geometry("600x500")

entry = tk.CTkEntry(app)
entry.pack()

button = tk.CTkButton(app, text="Validate", command=validate_input)
button.pack()

label = tk.CTkLabel(app, text="")
label.pack()

app.mainloop()