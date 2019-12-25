from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = 'black'  # кисть по умолчанию
        self.brush_size = 2
        self.brush_type = 0
        self.setUI()
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
        b_frame = Frame(window)
        b_frame.pack()
        b_1 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='deflaut', width=15, command=lambda: self.brush_type_select(0))
        b_2 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='color+black', width=15, command=lambda: self.brush_type_select(1))
        b_3 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='with_outline', width=15, command=lambda: self.brush_type_select(2))
        b_4 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='rectangle', width=15, command=lambda: self.brush_type_select(3))
        b_5 = Button(b_frame, bg='LightCyan3', fg='white', bd=7, relief='ridge',
                     text='oval', width=15, command=lambda: self.brush_type_select(4))
        b_1.pack()
        b_2.pack()
        b_3.pack()
        b_4.pack()
        b_5.pack()

    def draw(self, event):
        if self.brush_type == 0:
            self.canv.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)
        elif self.brush_type == 1:
            self.canv.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)
            self.canv.create_oval(event.x - self.brush_size + 2,
                                  event.y - self.brush_size + 2,
                                  event.x + self.brush_size - 2,
                                  event.y + self.brush_size - 2,
                                  fill='black', outline=self.color)
        elif self.brush_type == 2:
            self.canv.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline='black')
        elif self.brush_type == 3:
            self.canv.create_rectangle(event.x - self.brush_size,
                                       event.y - self.brush_size,
                                       event.x + self.brush_size,
                                       event.y + self.brush_size,
                                       fill=self.color, outline=self.color)
        elif self.brush_type == 4:
            self.canv.create_oval(event.x - self.brush_size//2 - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size//2 + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)

    def select_color(self):
        def release(event):
            self.set_color(event.widget['bg'])
            self.label_current_color2['bg'] = event.widget['bg']
        #COLORS  =  colors_l()
        #window = Toplevel(self)
        # window.title('Colors')
        #enter_frame = Frame(window)
        # enter_frame.pack()
        #r = 0; c = 0
        # for i in range(len(COLORS)):
        #    b = Button(enter_frame, bg = COLORS[i], width = 5)
        #    b.bind('<Button-1>', release)
        #    if c<=11:
        #        b.grid(row = r, column = c)
        #        c+=1
        #    else:
        #        r+=1
        #        c = 0
        #        b.grid(row = r, column = c)
    # __________________;

    # __________________;

    def setUI(self):
        self.parent.title('Paint Pro v.1')  # Устанавливаем название окна
        self.grid(row=0, column=0)
        self.parent["bg"] = "gray72"
        # ------------------------------------------------
        # _DRAWING
        self.brush_frame = Frame(self.parent)
        self.brush_frame.grid(row=0, column=0)
        color_lab = Label(self.brush_frame, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)
        # ------------------------------------------------
        # _Canvas
        self.canvas_frame = Frame(self.parent)
        self.canvas_frame.grid(row=1, column=0)

        self.canv = Canvas(self.canvas_frame, width=1200,
                           height=800, bg='white')
        self.canv.pack()
        self.canv.bind("<B1-Motion>", self.draw)
        # ------------------------------------------------
        #       Colors
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
            self.brush_frame, text='black', bg='LightCyan3', width=15, bd=7)
        self.label_current_color2 = Label(
            self.brush_frame, bg='black', width=5, bd=7)
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



def main():
    root = Tk()
    root.resizable(width=False, height=False)
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()
