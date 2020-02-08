import random
from tkinter import *
from PIL import ImageTk, Image

BUTTON_HEIGHT = 100
BUTTON_WIDTH = 100

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

LABEL_WIDTH = 100
LABEL_HEIGHT = 50

WINDOW_X = 600
WINDOW_Y = 300

points = 0
points_per_sec = 0

main_img = Image.open("pics\\main.jpg")
main_img_resized = main_img.resize((3 * BUTTON_WIDTH, 2 * BUTTON_HEIGHT), Image.ANTIALIAS)


def plus_point():
    global points
    points += 1
    points_text.set(f"Points {points}")


def point_per_sec():
    global points, points_per_sec
    points = round(points + points_per_sec, 2)
    points_text.set(f"Points {points}")
    root.after(1000, bot)
    root.after(1000, point_per_sec)


class Item:
    def __init__(self, root, id, pic, price, profit):
        self.root = root
        self.id = id
        img_resized = Image.open(pic).resize((3 * BUTTON_WIDTH, 2 * BUTTON_HEIGHT), Image.ANTIALIAS)
        self.but_img = ImageTk.PhotoImage(img_resized)
        self.count = 0
        self.price = price
        self.profit = profit
        self.coefficient = self.profit / self.price

        self.text_count = StringVar()
        self.text_count.set(f"{self.count}")

        self.item_price = StringVar()
        self.item_price.set(f"{self.price}")

        self.profit_info = Label(self.root, text=f"+{self.profit}", font="Arial 14", justify=CENTER)
        self.price_info = Label(self.root, textvariable=self.item_price, font="Arial 14", justify=CENTER)
        self.item_count = Label(self.root, textvariable=self.text_count, font="Arial 14", justify=CENTER)
        self.item_but = Button(self.root, image=self.but_img, command=self.buy_item)

    def buy_item(self):
        global points, points_per_sec
        if points >= self.price:
            points = round(points - self.price, 2)
            points_text.set(f"Points {points}")
            self.count += 1
            self.text_count.set(f"{self.count}")
            self.price = round(self.price * (round(random.random(), 2) + 1), 2)
            self.item_price.set(f"{self.price}")
            points_per_sec += self.profit
            points_per_sec_text.set(f"Points per sec {points_per_sec}")
            self.coefficient = self.profit/self.price

    def draw_block(self):
        self.item_but.place(x=100 * (self.id - 1), y=WINDOW_HEIGHT - BUTTON_HEIGHT - 3 * LABEL_HEIGHT,
                            height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        self.profit_info.place(x=100 * (self.id - 1), y=WINDOW_HEIGHT - 3 * LABEL_HEIGHT, width=LABEL_WIDTH,
                               height=LABEL_HEIGHT)
        self.price_info.place(x=100 * (self.id - 1), y=WINDOW_HEIGHT - 2 * LABEL_HEIGHT, width=LABEL_WIDTH,
                              height=LABEL_HEIGHT)
        self.item_count.place(x=100 * (self.id - 1), y=WINDOW_HEIGHT - LABEL_HEIGHT, width=LABEL_WIDTH,
                              height=LABEL_HEIGHT)


def bot():
    cnt = 0
    id = 0
    cof = 0
    for item in items:
        if item.coefficient > cof:
            cof = item.coefficient
            id = cnt
        cnt += 1

    items[id].buy_item()


if __name__ == "__main__":
    root = Tk()
    C = Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
    filename = PhotoImage(file="pics\\back_1.png")
    back_label = Label(root, image=filename)
    back_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    items = [Item(root, 1, "pics\\Liza.jpg", 10, 1), Item(root, 2, "pics\\second_item.jpg", 100, 10),
             Item(root, 3, "pics\\Liza.jpg", 300, 30), Item(root, 4, "pics\\Liza.jpg", 500, 50)]
    root.title("Clicker")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}")

    points_text = StringVar()
    points_text.set(f"Points {points}")

    points_per_sec_text = StringVar()
    points_per_sec_text.set(f"Points per sec {points_per_sec}")

    points_label = Label(root, textvariable=points_text, font="Arial 14")
    points_label.place(x=0, y=0)

    points_per_sec_text_label = Label(root, textvariable=points_per_sec_text, font="Arial 14")
    points_per_sec_text_label.place(x=0, y=30)

    main_jpg = ImageTk.PhotoImage(main_img_resized)
    main_item = Button(root, image=main_jpg, command=plus_point)
    main_item.place(x=250, y=WINDOW_HEIGHT - 3 * BUTTON_HEIGHT - 3 * LABEL_HEIGHT - 20,
                    height=2 * BUTTON_HEIGHT, width=3 * BUTTON_WIDTH)

    for item in items: item.draw_block()
    root.after(0, point_per_sec)
    root.mainloop()
