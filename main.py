from tkinter import *
from color_list import colors_l
import random
from PIL import ImageGrab
import math
import time


class Paint(Frame):
    def __init__(self, parent):
        self.SIZE = 800  # size of canvas
        Frame.__init__(self, parent)
        self.parent = parent  # creation parent frame
        self.color = 'red'  # deflaut brush
        self.brush_size = 2
        self.brush_type = 0
        self.setUI()  # creating an interface
        self.back_list = []  # for memorizing the last line

    # Saving function
    def _canvas(self):  # find out the cutting area
        x = self.canv.winfo_rootx()+self.canv.winfo_x()
        y = self.canv.winfo_rooty()+self.canv.winfo_y()
        x1 = x+self.canv.winfo_width()
        y1 = y+self.canv.winfo_height()
        box = (x, y, x1, y1)
        print('box = ', box, end='')
        return box

    def save_canvas(self):
        canvas = self._canvas()
        time.sleep(1.0)
        self.grabcanvas = ImageGrab.grab(bbox=canvas)
        self.grabcanvas.save(
            'saves\\'+'cvs' + str(random.randint(10000, 30000))+'.png')
        print('save OK')

    # _______________________________________Drawing_Functions()________________________________________
    def set_color(self, new_color):
        self.color = new_color
        self.label_current_color['text'] = new_color
        self.label_current_color2['bg'] = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size
        self.label_current_size['text'] = str(new_size)

    def modofy_brush_size(self, size):
        self.label_current_size['text'] = str(self.brush_size + size)
        self.brush_size += size

    def brush_type_select(self, b_type):
        self.brush_type = b_type

    def select_brush(self):
        window = Toplevel(self)
        window.title('Brushes')
        window.attributes("-topmost", True)
        b_frame = Frame(window)
        b_frame.pack()
        b_1 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='deflaut', width=15, command=lambda: self.brush_type_select(0))
        canv1 = Canvas(b_frame, width=50, height=50, bg='white')

        b_2 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='color+black', width=15, command=lambda: self.brush_type_select(1))
        canv2 = Canvas(b_frame, width=50, height=50, bg='white')

        b_3 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='with_outline', width=15, command=lambda: self.brush_type_select(2))
        canv3 = Canvas(b_frame, width=50, height=50, bg='white')
        b_4 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='rectangle', width=15, command=lambda: self.brush_type_select(3))
        canv4 = Canvas(b_frame, width=50, height=50, bg='white')
        b_5 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='oval', width=15, command=lambda: self.brush_type_select(4))
        canv5 = Canvas(b_frame, width=50, height=50, bg='white')
        b_1.grid(row=0, column=0)
        canv1.grid(row=0, column=1)
        b_2.grid(row=1, column=0)
        canv2.grid(row=1, column=1)
        b_3.grid(row=2, column=0)
        canv3.grid(row=2, column=1)
        b_4.grid(row=3, column=0)
        canv4.grid(row=3, column=1)
        b_5.grid(row=4, column=0)
        canv5.grid(row=4, column=1)
        canv1.create_oval(5, 5, 45, 45, fill=self.color, outline=self.color)
        canv2.create_oval(5, 5, 45, 45, fill=self.color, outline=self.color)
        canv2.create_oval(8, 8, 42, 42, fill='black', outline=self.color)
        canv3.create_oval(5, 5, 45, 45, fill=self.color, outline='black')
        canv4.create_rectangle(
            5, 5, 45, 45, fill=self.color, outline=self.color)
        canv5.create_oval(5, 2, 45, 25, fill=self.color, outline=self.color)

    def select_color(self):
        def release(event):
            self.set_color(event.widget['bg'])
            self.label_current_color2['bg'] = event.widget['bg']
        COLORS = colors_l()
        window = Toplevel(self)
        window.title('Colors')
        window.attributes("-topmost", True)
        enter_frame = Frame(window)
        enter_frame.pack()
        r = 0
        c = 0
        for i in range(len(COLORS)):
            b = Button(enter_frame, bg=COLORS[i], width=3)
            b.bind('<Button-1>', release)
            if c <= 15:
                b.grid(row=r, column=c)
                c += 1
            else:
                r += 1
                c = 0
                b.grid(row=r, column=c)

    def position(self, event):
        self.movecheked = [0, 0]
        self.posits = (event.x, event.y)

    def back_clean(self, event):
        self.back_list = []

    def back(self, do, x, y):
        try:
            if do:
                self.back_list.append((x, y))
            else:
                c = self.color
                self.back_list.insert(
                    0, (self.back_list[0][0]-5, self.back_list[0][1]-5))
                self.back_list.insert(
                    0, (self.back_list[0][0]+5, self.back_list[0][1]+5))
                self.back_list.append(
                    (self.back_list[-1][0]-5, self.back_list[-1][1]-5))
                self.back_list.append(
                    (self.back_list[-1][0]+5, self.back_list[-1][1]+5))
                for i in range(len(self.back_list)-1):
                    self.draw(0, 0, aitoevent=(self.back_list[i]))
                    self.color = 'white'
                self.color = c
                self.back_list = []
        except:
            print('no to delite')

    def draw(self, event, typeofline, aitoevent=0):
        issm = self.issimmetric.get()
        if aitoevent != 0:
            x = aitoevent[0]
            y = aitoevent[1]
        else:
            x = event.x
            y = event.y
        if not issm:
            if typeofline:
                self.movecheked[0] += abs(self.posits[0] - x)
                self.movecheked[1] += abs(self.posits[1] - y)
                if self.movecheked[0] > self.movecheked[1]:
                    y = self.posits[1]
                else:
                    x = self.posits[0]
            self.back(1, x, y)

        def maindraw(sx=0, sy=0):
            xx = abs(sx - x)
            yy = abs(sy - y)
            if self.brush_type == 0:
                self.canv.create_oval(xx - self.brush_size,
                                      yy - self.brush_size,
                                      xx + self.brush_size,
                                      yy + self.brush_size,
                                      fill=self.color, outline=self.color)
            elif self.brush_type == 1:
                self.canv.create_oval(xx - self.brush_size,
                                      yy - self.brush_size,
                                      xx + self.brush_size,
                                      yy + self.brush_size,
                                      fill=self.color, outline=self.color)
                self.canv.create_oval(xx - self.brush_size + 2,
                                      yy - self.brush_size + 2,
                                      xx + self.brush_size - 2,
                                      yy + self.brush_size - 2,
                                      fill='black', outline=self.color)
            elif self.brush_type == 2:
                self.canv.create_oval(xx - self.brush_size,
                                      yy - self.brush_size,
                                      xx + self.brush_size,
                                      yy + self.brush_size,
                                      fill=self.color, outline='black')
            elif self.brush_type == 3:
                self.canv.create_rectangle(xx - self.brush_size,
                                           yy - self.brush_size,
                                           xx + self.brush_size,
                                           yy + self.brush_size,
                                           fill=self.color, outline=self.color)
            elif self.brush_type == 4:
                self.canv.create_oval(xx - self.brush_size//2 - self.brush_size,
                                      yy - self.brush_size,
                                      xx + self.brush_size//2 + self.brush_size,
                                      yy + self.brush_size,
                                      fill=self.color, outline=self.color)
        if issm:
            maindraw(self.SIZE, 0)
            maindraw(0, self.SIZE)
            maindraw(self.SIZE, self.SIZE)
            maindraw()
        else:
            maindraw()

    # __________________;

    def setUI(self):
        self.parent.title('Paint Pro v.1')  # Устанавливаем название окна
        self.grid(row=0, column=0)
        self.parent["bg"] = "gray72"
        # ------------------------------------------------
        #_Menu
        main_menu = Menu(self.parent)
        self.parent.configure(menu=main_menu)
        item = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='file', menu=item)
        item.add_command(label='Save(Canvas)',
                         command=lambda: self.save_canvas())
        item.add_command(label='clear_all',
                         command=lambda: self.canv.delete("all"))
        # ------------------------------------------------
        # _Canvas
        self.brush_frame = Frame(self.parent)
        self.brush_frame.grid(row=0, column=0)
        self.canvas_frame = Frame(self.parent)
        self.canvas_frame.grid(row=3, column=0)

        self.canv = Canvas(self.canvas_frame, width=self.SIZE,
                           height=self.SIZE, bg='white')
        self.canv.pack()
        self.canv.bind("<B1-Motion>", lambda event: self.draw(event, False))
        self.canv.bind('<Button-3>', self.position)
        self.canv.bind('<Button-1>', self.back_clean)
        self.canv.bind("<B3-Motion>", lambda event: self.draw(event, True))
        self.parent.bind("<z>", lambda event: self.back(0, 0, 0))
        # ------------------------------------------------
        # _Colors
        color_lab = Label(self.brush_frame, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self.brush_frame, bg='red', fg='white', bd=7, relief='ridge',
                         text="Red", width=10, command=lambda: self.set_color("red"))
        green_btn = Button(self.brush_frame, bg='green', fg='white', bd=7, relief='ridge',
                           text="Green", width=10, command=lambda: self.set_color("green"))
        blue_btn = Button(self.brush_frame, bg='blue', fg='white', bd=7, relief='ridge',
                          text="Blue", width=10, command=lambda: self.set_color("blue"))
        black_btn = Button(self.brush_frame, bg='black', fg='white', bd=7, relief='ridge',
                           text="Black", width=10, command=lambda: self.set_color("black"))
        white_btn = Button(self.brush_frame, bg='white', fg='black', bd=7, relief='ridge',
                           text="Erather", width=10, command=lambda: self.set_color("white"))
        red_btn.grid(row=0, column=1)
        green_btn.grid(row=0, column=2)
        blue_btn.grid(row=0, column=3)
        black_btn.grid(row=0, column=4)
        white_btn.grid(row=0, column=5)
        #       about Colors
        self.label_current_color = Label(
            self.brush_frame, text='red', bg='LightCyan3', width=15, bd=7)
        self.label_current_color2 = Label(
            self.brush_frame, bg='red', width=5, bd=7)
        self.label_current_size = Label(
            self.brush_frame, text='2', bg='LightCyan3', width=5, bd=7)
        self.label_current_color.grid(row=0, column=8)
        self.label_current_color2.grid(row=0, column=9)
        self.label_current_size.grid(row=0, column=10)
        new_color_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                               relief='ridge', text='Select_Color', width=10, command=lambda: self.select_color())
        new_color_btn.grid(row=0, column=6)
        #       Brush size
        size_lab = Label(self.brush_frame, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                         relief='ridge', text="Two", width=10, command=lambda: self.set_brush_size(2))
        two_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                         relief='ridge', text="Five", width=10, command=lambda: self.set_brush_size(5))
        five_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                          relief='ridge', text="Seven", width=10, command=lambda: self.set_brush_size(7))
        seven_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                           relief='ridge', text="Ten", width=10, command=lambda: self.set_brush_size(10))
        ten_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7, relief='ridge',
                         text="Twenty", width=10, command=lambda: self.set_brush_size(20))
        twenty_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                            relief='ridge', text="Fifty", width=10, command=lambda: self.set_brush_size(50))
        sizeplus_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                              relief='ridge', text=" + ", width=10, command=lambda: self.modofy_brush_size(1))
        sizemin_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                             relief='ridge', text=" - ", width=10, command=lambda: self.modofy_brush_size(-1))
        twenty_btn.grid(row=1, column=6, sticky=W)
        one_btn.grid(row=1, column=1)
        two_btn.grid(row=1, column=2)
        five_btn.grid(row=1, column=3)
        seven_btn.grid(row=1, column=4)
        ten_btn.grid(row=1, column=5)
        sizeplus_btn.grid(row=1, column=6)
        sizemin_btn.grid(row=1, column=7)
        #       select brush
        brushes_btn = Button(self.brush_frame, bg='LightCyan3', fg='black', bd=7,
                             relief='ridge', text='BRUSHES', width=10, command=lambda: self.select_brush())
        brushes_btn.grid(row=1, column=8)
        # simmetrion
        self.issimmetric = IntVar()
        self.checkbutton = Checkbutton(
            text="Симметрия", variable=self.issimmetric)
        self.checkbutton.grid(row=2, column=0)


def main():
    root = Tk()
    root.resizable(width=False, height=False)
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()
