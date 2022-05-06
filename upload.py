import customtkinter
import tkinter
import requests
import pyshorteners as sh
s = sh.Shortener()
from pydantic import FilePath
customtkinter.set_appearance_mode("System")
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("600x500")
root_tk.title("Anonfile uploader made by cracked.io/pfp")
from tkinter.filedialog import askopenfile 
def open_file():
    file_path = askopenfile(mode='r')
    if file_path is not None:
        pass
    files = {'file': (file_path.name,open(file_path.name, 'rb')),}

    url = 'https://api.anonfiles.com/upload'
    response = requests.post(url, files=files)

    data = response.json()

    print(data['data']['file']['url']['short'])
    label = customtkinter.CTkLabel(master=root_tk, text=s.tinyurl.short(data['data']['file']['url']['short']))
    label.place(relx=0.75, rely=0.75, anchor=tkinter.N)

button = customtkinter.CTkButton(master=None, text="Load file", command=open_file)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



root_tk.mainloop()
