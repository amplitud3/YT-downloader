import tkinter as tk
from tkinter import messagebox, StringVar , OptionMenu
from tkinter import ttk 
from pytubefix import YouTube
import threading
import time 



class YoutTubeDownloaderApp:
	def __init__(self,root):
		self.root = root
		self.root.title("YT Downloader")
		self.root.geometry("400x400")

	
		self.icon_image = tk.PhotoImage(file="icon.png")
		self.root.iconphoto(False, self.icon_image)


		self.bg_image = tk.PhotoImage(file="background.png")
		self.bg_label = tk.Label(root, image=self.bg_image)
		self.bg_label.place(relwidth=1, relheight=1)


		

		self.url_entry = tk.Entry(root,width=40)
		self.url_entry.pack(pady=90)


	

		self.quality_var = StringVar(root)
		self.quality_options = ["Highest", "720p", "480p", "360p","Audio"]
		self.quality_var.set(self.quality_options[0])


		self.quality_menu = OptionMenu(root, self.quality_var, *self.quality_options)
		self.quality_menu.pack(pady=10)

		self.download_button = tk.Button(root, text="Download", command=self.download, font=('Arial', 14, 'bold'), bg='green', fg='white',
                                          relief='raised', bd=3)
		self.download_button.pack(pady=20)

	def download(self):
		url = self.url_entry.get()
		quality = self.quality_var.get()


		if not url:
			messagebox.showerror("Error", "Please enter a YouTube URL.")
			return

		try:
			yt = YouTube(url)

			if quality == "Highest":
				stream = yt.streams.get_highest_resolution()
			elif quality == "720p":
				stream = yt.streams.filter(res="720p").first()
			elif quality == "480p":
				stream = yt.streams.filter(res="480p").first()
			elif quality == "360p":
				stream = yt.streams.filter(res="360p").first()
			elif quality == "Audio":
				stream = yt.streams.filter(only_audio=True).first()



			if stream:
				stream.download()
				messagebox.showinfo("Success",f"Downloaded: {yt.title}")
			else:
				messagebox.showerror("Error","No streams available for the selected quality.")

		except Exception as e:
			messagebox.showerror("Error",str(e))				
	

    
    


      

if __name__ == "__main__":
	root = tk.Tk()
	app = YoutTubeDownloaderApp(root)
	root.mainloop()









