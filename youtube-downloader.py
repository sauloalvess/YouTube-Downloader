from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()
ROOT.withdraw()

def input_data(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result

video_link = input_data("Video Link", "Insert Video URL: ")

yt = YouTube(video_link)

print(f'Titulo: {yt.title}')
print(f'Views: {yt.views}')

yd = yt.streams.get_highest_resolution()

download_path = input_data("Download", "Insert Download Path: ")

yd.download(download_path)

messagebox.showinfo("Mensagem", f'Download completed in {download_path}')