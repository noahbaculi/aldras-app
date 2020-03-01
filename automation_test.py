import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(row=0, column=0)
        # container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # frame = tk.Frame(self)
        # frame.grid(row=1, column=1, padx=(100, 100), pady=(20, 20))
        load = Image.open("logo.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        # # logo_img = ImageTk.PhotoImage(Image.open('logo.png').resize((250, 250)))
        # # logo_img_label = tk.Label(frame, image=logo_img)
        img.grid(row=0, column=0, columnspan=4)
        # # self.grid_rowconfigure(0, weight=1)
        # # self.grid_columnconfigure(0, weight=1)
        # program_name = tk.Label(frame, text='Aldras Automation')
        # program_name.config(font=('Verdana', 20))
        # # program_name.config(font=('Times', 20))
        # program_name.grid(row=1, column=0, columnspan=4, pady=(0, 20))
        # tk.Label(frame, text='Workflow:').grid(row=2, column=1)
        # workflow_name_entry = tk.Entry(frame)
        # workflow_name_entry.grid(row=2, column=2)
        tk.Button(self, text='OK').grid(row=3, column=3)
        # button = tk.Button(self, text="Go to the 1st page", command=lambda: controller.show_frame("PageOne"))
        # button.grid(row=4, column=3)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()