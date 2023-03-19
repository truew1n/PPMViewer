import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.img = self.load_image()
        self.width, self.height = self.img.size
        self.root.title(f"PPMViewer - {self.width}x{self.height}")
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.show_image()
        self.root.mainloop()

        
    def load_image(self):
        return Image.open("image.ppm")


    def show_image(self):
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(self.width/2, self.height/2, image=self.img)
        self.root.update()


if __name__ == "__main__":
    App(tk.Tk())
