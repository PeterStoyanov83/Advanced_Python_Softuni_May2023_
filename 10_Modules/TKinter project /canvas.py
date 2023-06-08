from tkinter import Tk


def create_root():
    root = Tk()
    root.title("GUI SHOP")
    root.geometry("700x600")
    root.resizable(False, False)

    root.mainloop()


root = create_root()
