import requests
import tkinter
import ttkbootstrap as ttk


window = ttk.Window(themename="darkly")
window.geometry("500x650")
window.title("GPT-2 Basic Sentence Completion")

API_TOKEN = "GET YOUR API TOKEN FROM THE API URL"
API_URL = "https://api-inference.huggingface.co/models/gpt2-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query():
    try:
        payload = {
            "inputs": input_box.get("1.0", "end-1c"),
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        #print(response.json()[0]['generated_text'])
        input_box.delete("1.0", "end")
        input_box.insert("1.0", response.json()[0]['generated_text'])
        input_box.config(foreground="white", font=("Arial", 10))
    except Exception as e:
        input_box.delete("1.0", "end")
        input_box.insert("1.0", "An error occured, that's all we know ¯\_(ツ)_/¯")
        input_box.config(foreground="red", font=("Arial Bold", 10))
        print(e)


response_label = ttk.Label(window, text="Type a sentence to get completed.", font=("Arial", 20))
response_label.pack(pady=20)

input_box = ttk.Text(window, width=50, font=("Arial", 10))
input_box.pack(pady=10)

button = ttk.Button(window, text="Get response", command=query)
button.pack(pady=10)


window.mainloop()
