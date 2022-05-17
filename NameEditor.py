"""
abstract
    [] read files in given directory.
    [] look for the pattern '_-_n' in filename, where n is the episode number, if n <10, it should be in 0n form.
    [] renames file name to '<name> ep<n> where name and n are given.
"""

import os
import pdb
import tkinter as tk

root = tk.Tk()
root.title("Batch Editor")
root.resizable(False, False)
canvas = tk.Canvas(root, height=500, width=500, bg='black')
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
label = tk.Label(frame, text="Only works for files downloaded from animepahe.com", fg="cyan", bg="black")
label.pack()

tk.Label(frame, text="Path", fg="cyan", bg="black").pack()
input_path = tk.Text(frame, height=1.5, width=20, name="path", background="black", bd=7, foreground="cyan",insertbackground="cyan", undo=True)
input_path.pack()

tk.Label(frame, text="Name", fg="cyan", bg="black").pack()
input_name = tk.Text(frame, height=1.5, width=20, name="name", background="black", bd=7, foreground="cyan",insertbackground="cyan", undo=True)
input_name.pack()


def getInput():
    path = input_path.get(1.0, "end-1c")
    name = input_name.get(1.0, "end-1c")

    return path, name


def Process():
    tk.Label(frame, text="Files updated: ", fg="cyan", bg="black").pack()
    path, name = getInput()
    os.chdir(path)
    files = list(os.listdir())
    print(files)

    for i in range(1, len(files) + 1):
        if i < 10:
            snip = f"_-_0{i}"
        else:
            snip = f"_-_{i}"

        for file in files:
            if snip in file:
                new_name = fr"{path}\{name} ep{i}.mp4"
                tk.Label(frame, text=new_name, fg="cyan", bg="black").pack()
                os.rename(file, new_name)


submit = tk.Button(frame, text="Enter", padx=10, pady=5, fg="black", bg="cyan", anchor="s", command=Process)
submit.pack(pady=10)

root.mainloop()
