import tkinter

import star_tkinter

width = 700
height = 700
speed = 2

StarField = []

def main():
    root = tkinter.Tk()
    root.resizable(True, True)
    #root.maxsize(width, height)
    root.title("Starfield Simulation with Python and Tkinter")

    global canvas, width, height
    canvas = tkinter.Canvas(root, width=width, height=height, bg="#000000")
    canvas.pack(fill = "both", expand="True")

    for i in range(400):
       StarField.append(star_tkinter.Star(width, height, speed))

    draw()
    
    for i in range(len(StarField)):
        StarField[i].update()
    tkinter.mainloop()


def draw():
    global canvas, width, height

    canvas.delete("all")

    
    if (canvas.winfo_width() != width or canvas.winfo_height != height):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        for i in range(len(StarField)):
            StarField[i].resize(width, height)

    for i in range(len(StarField)):
        stern = StarField[i]
        (x, y, radius) = stern.get_screen_coords()
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=stern.color, outline = stern.color)
        stern.update()


    canvas.after(20, draw)

if __name__ == "__main__":
    main()