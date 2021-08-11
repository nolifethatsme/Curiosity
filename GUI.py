import tkinter as tk


# introduces page class for the frames to function.
class page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


# users will be greeted with home page first and can then navigate via task bar at the top
class home(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the home page/possibly a login page if we have time?")
        label.pack(side="top", fill="both", expand=True)


# shows the page which is used for uploading/downloading by covering over the previous frame.
class upload_download(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the download and upload page")
        label.pack(side="top", fill="both", expand=True)

        # upload button, with placement
        upload_button = tk.Button(self, text="Upload").pack(side="left")


# this page will be used for automation as detailed in brief, connect to CMD/bash
class command_line(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Command Line interface for automation")
        label.pack(side="top", fill="both", expand=True)


# this will be visible throughout each page and will act as a menu bar at the top
class main_view(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = home(self)
        p2 = upload_download(self)
        p3 = command_line(self)

        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False, anchor="center")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # page placement
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # button creation... can make this look better with colours etc
        b1 = tk.Button(button_frame, text="Home/Login", command=p1.show)
        b2 = tk.Button(button_frame, text="Upload/Download", command=p2.show)
        b3 = tk.Button(button_frame, text="Command Line", command=p3.show)

        # button placement and alignment
        b1.pack(anchor="center", side="left")
        b2.pack(anchor="center", side="left")
        b3.pack(anchor="center", side="left")

        p1.show()


# the creation of the window... name can be changed
if __name__ == "__main__":
    root = tk.Tk()
    root.title("CuriosityFiles")
    main = main_view(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x600")
    root.mainloop()
