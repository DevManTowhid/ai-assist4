import tkinter as tk
import requests

API_URL = "http://127.0.0.1:5000"

def send_message():
    user_input = user_entry.get()
    response = requests.post(f"{API_URL}/chat", json={"message": user_input}).json()
    chat_text.insert(tk.END, f"You: {user_input}\nBot: {response['response']}\n\n")
    user_entry.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("AI Assistant")

chat_text = tk.Text(root, height=15, width=50)
chat_text.pack()

user_entry = tk.Entry(root, width=40)
user_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
