# -- Imports --

from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageEnhance, ImageFilter, ImageTk, ImageDraw, ImageFont, ImageOps
from tkinter import filedialog, colorchooser
from tkinter.ttk import Combobox, Style
from re import search
from random import choice
from os import getcwd, walk, path
from time import sleep
from io import BytesIO
from requests import get
from sys import getsizeof

# -- values --

cursor_shape="dot"

# -- Album --

pic= Image.new("RGB",(850,500),"#222222")
picz = []
pic_pointer = -1

# -- Functions --

def append_pic() :
    global picz, pic_pointer
    pic_pointer += 1
    picz.insert(pic_pointer, pic)
    picz = picz[0:pic_pointer+1]

def update_img():
    w = pic.width
    h = pic.height

    if w>h:
        r = 850/w
        w = w*r
        h = h*r

        if h>500:
            r = 500/h
            w = w*r
            h = h*r

    elif h>w:
        r = 500/h
        w = w*r
        h = h*r

    elif h==w:
        r = 500/w
        w = w*r
        h = h*r

    img2=ImageTk.PhotoImage(pic.resize([round(w),round(h)]))
    scr_img.configure(image=img2)
    scr_img.image=img2

def update_new_img():
    append_pic()
    update_img()


# ---------------- Hovering -----------------------

def hover_em(button_set):
    def on_enter(event):
        event.widget["bg"] = "#444444"
    def on_leave(event):
        event.widget["bg"] = "#222222"

    for button in button_set:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

# ----------------- Side Imaging ------------------------

def create_side_pic(*args):
    global side_pic, pic

    side_pic = pic

    def place_side_pic_widgets():
        check_side_pic.place(x=5,y=496,height=30,width=85)
        B3.place(x=103,y=496,height=30,width=85)


    def local_file():
        root4.destroy()
        set_pic()
        place_side_pic_widgets()

    def web_file():
        root4.destroy()
        from_web()
        place_side_pic_widgets()

    def create_file():
        root4.destroy()
        make_pic()
        place_side_pic_widgets()

    # --- Activating root4 ---

    root4 = Toplevel(root)
    root4.anchor(CENTER)
    root4.config(background='#111111')
    root4.title('Choose option for selecting image')
    root4.geometry('390x150+540+200')

    # --- Widgets for root4 ---

    iS = Label(root4, text="choose new image from",bd=0,bg='#111', fg="coral", font='calibri 15 bold')
    bs = Button(root4,text='Local',bd=0,bg='#222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=local_file)
    cs = Button(root4,text='Create',bd=0,bg='#222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=create_file)
    ws = Button(root4,text='Web',bd=0,bg='#222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=web_file)

    # --- Packing Widgets in root4 ---

    iS.pack(padx=0,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=30,pady=0,ipady=5,ipadx=12, side=LEFT)
    ws.pack(padx=30,pady=0,ipady=5,ipadx=13, side=RIGHT)
    cs.pack(padx=30,pady=25,ipady=5,ipadx=12)

    hover_em([bs, cs, ws])

    root4.grab_set() # untill root4 is open root will not work
    root4.transient(root) # root4 window will stay over root window
    root.wait_window(root4) # root window will wait untill root4 closes


def interchange_side_pic_and_pic(*args):
    global pic, side_pic
    pic, side_pic = side_pic, pic
    update_new_img()

# --- Help Functions---

def exp_size():
    sleep(0.5)
    msg.showinfo('How to Resize','For Resizing a Picture type (Width)x(Height) in Entry box and press Resize button')
    sleep(0.5)

def exp_save():
    sleep(0.5)
    msg.showinfo('How to save','For Save your edited image You just have follow this\n\nMenuBar -> File -> Save\nThan type full name of image with format\nClick on Save button')
    sleep(0.5)

def exp_create():
    sleep(0.5)
    msg.showinfo('How to Create','1. Choose Color\n2. MenuBar -> File -> Create\n3. Enter size in Dialog\n 4. Press create')
    sleep(0.5)

def exp_crop():
    sleep(0.5)
    msg.showinfo('How to Crop','from croping a image you just have to Enter \npoint(X1,Y1) and point(X2,Y2) as X1xY1xX2xY2 in Entry box and press Crop button')
    sleep(0.5)

def exp_rotate():
    sleep(0.5)
    msg.showinfo('How to rotate','For Rotating just press Rotate bytton and image will rotate by 90 deg every time')
    sleep(0.5)

def exp_text():
    sleep(0.5)
    msg.showinfo('How to Text','For text something in an image you just have to press Text button \nthen fill the required informations like(Sentence, Font, Fontsize, Colour, Etc) and press Draw button Erase will just Undo once')
    sleep(0.5)

def exp_info():
    sleep(0.5)
    msg.showinfo('How to info','To get informations about your photo just press info button')
    sleep(0.5)

def exp_filter():
    sleep(0.5)
    msg.showinfo('How to apply filter','you can choose filter and apply using Filter option in menu bar')
    sleep(0.5)

def exp_blend():
    sleep(0.5)
    msg.showinfo('How to blend another image','to blend another image you have to enter effect rate of new image on current image on Entry box and press Blend button to choose that new image')
    sleep(0.5)

def exp_border():
    sleep(0.5)
    msg.showinfo('How to use border','to use border in image you have to enter border width in Entry box and choose color and press Border button')
    sleep(0.5)

def exp_flip():
    sleep(0.5)
    msg.showinfo('How to flip image','to flip an image you have to enter y(for up side down) or x(for right side left) in Entry box and press Flip button')
    sleep(0.5)

def exp_paste():
    sleep(0.5)
    msg.showinfo('How to paste image','to paste an image you have to enter new image size and new image position\n\nFormate : (width)x(height),(X)x(Y) in Entry box and press Paste button')
    sleep(0.5)

def exp_others():
    sleep(0.5)
    msg.showinfo('How to apply simple editig','you can change image Brightness, Color, Contrast, Sharpness and Blurness\nBy entring Rate of change in Entry box \n\n rate 1 will remain the image same and 0 will remove that proprty from the image as you decrease rate from 1 to 0 that property will decrease and\nas you increase value from 1 that property will be increase ')
    sleep(0.5)

# --- Undo Functions ---


def undo_pic(*args):
    global pic, picz, pic_pointer

    if pic_pointer == 0:
        msg.showwarning('Last Pic','This is the last picture in the Album')
    
    elif len(picz):
        pic_pointer -= 1
        pic=picz[pic_pointer]
        update_img()

def redo_pic(*args):
    global pic, picz, pic_pointer

    if pic_pointer == (len(picz) -1):
        msg.showwarning('Final Pic','This is the Final picture in the Album')
    
    elif len(picz):
        pic_pointer += 1
        pic=picz[pic_pointer]
        update_img()

def undo_new():
    global pic, picz, pic_pointer
    ask = msg.askokcancel('Confirm','you will lost all changes you made\nare you sure you want to undo everything')
    
    if ask and len(picz):    
        pic = picz[0]
        picz=[pic]
        pic_pointer = 0
        update_img()

# --- Filter Functions ---


def filter_rate1():    
    global pic
    pic = pic.filter(ImageFilter.CONTOUR)
    update_new_img()
    


def filter_rate2():
    global pic
    pic = pic.filter(ImageFilter.DETAIL)
    update_new_img()
    


def filter_rate3():
    global pic
    pic = pic.filter(ImageFilter.FIND_EDGES)
    update_new_img()
    


def filter_rate4():    
    global pic
    pic = pic.filter(ImageFilter.EMBOSS)
    update_new_img()
    


def filter_rate5():
    global pic
    pic = pic.filter(ImageFilter.SMOOTH)
    update_new_img()
    


def filter_rate6():
    global pic
    pic = pic.filter(ImageFilter.SMOOTH_MORE)
    update_new_img()
    


def filter_rate7():
    global pic
    pic = pic.filter(ImageFilter.EDGE_ENHANCE)
    update_new_img()
    


def filter_rate8():
    global pic
    pic = pic.filter(ImageFilter.EDGE_ENHANCE_MORE)
    update_new_img()
    
# ----------------- Conversions -----------------------

def convert_RGB():
    global pic
    pic = pic.convert("RGB")
    update_new_img()

def convert_RGBA():
    global pic
    pic = pic.convert("RGBA")
    update_new_img()

def convert_CMYK():
    global pic
    pic = pic.convert("CMYK")
    update_new_img()

def convert_L():
    global pic
    pic = pic.convert("L")
    update_new_img()


# --- Other Editing Functions ---


def border_pic():
    global pic

    i = rate.get()

    try:
        i = int(i)
        pic = ImageOps.expand(pic,border=i,fill=color_now.get())

    except Exception as e:
        pic = ImageOps.expand(pic,border=int(5),fill='black')
        pic = ImageOps.expand(pic,border=int(4),fill=color_now.get())
        pic = ImageOps.expand(pic,border=int(5),fill='black')
        
    update_new_img()

def flip_pic():
    global pic

    if rate.get() == 'y':
        pic = ImageOps.flip(pic)
    elif rate.get() == 'x':
        pic = ImageOps.mirror(pic)
    else:
        pic = pic
        picz.pop()
        msg.showerror('Attribute Error','Enter x or y in Entry box to flip image')       
    
    update_new_img()


def invert_rate():
    global pic

    pic= ImageOps.invert(pic)
    
    update_new_img()

def scale_pic():
    global pic
    pic= ImageOps.scale(pic, float(rate.get()))
    
    update_new_img()

def make_pic():
    global pic

    def make_it():
        global pic
        par = url.get().split('x')
        w = int(par[0])
        h = int(par[1])
        pic = Image.new("RGB",(w, h), color_now.get())
        
        root5.destroy()
        update_new_img()

    
    # --- Activating root5 ---

    root5 = Toplevel(root)
    root5.anchor(CENTER)
    root5.config(background='#111111')
    root5.title('enter size width x height')
    root5.geometry('300x150+540+200')
    
    # --- Variable for root5 ---

    url = StringVar()
    url.set('1500x1500')

    # --- Widgets for root5 ---

    iS = Entry(root5,textvariable=url,bd=2,bg='black',fg='gray',font='calibri 13 bold',relief=SUNKEN,width=30,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)
    bs = Button(root5,text='Create',bd=0,bg='#222222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=make_it)

    # --- Packing Widgets in root5 ---

    iS.pack(padx=1,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=1,pady=25,ipady=7,ipadx=13)

    hover_em([bs])

    root5.transient(root) # root5 window will stay over root window
    root.wait_window(root5) # root window will wait untill root5 closes


def bright_rate():
    global pic

    pic = ImageEnhance.Brightness(pic)
    pic = pic.enhance(float(rate.get()))
    
    update_new_img()


def info_pic(*args):
    if check.get() == 1:
        shape = side_pic.size
        form = side_pic.format    
        size = getsizeof(side_pic)
        mode = side_pic.mode
        if mode == 'L' : mode = "grayscale"
    
    else:
        shape = pic.size
        form = pic.format
        size = getsizeof(pic)
        mode = pic.mode
        if mode == 'L' : mode = "grayscale"

    msg.showinfo('Picture Info',f'Shape: {shape}\nForm: {form}\nSize: {size}\nMode: {mode}')

def show_pic(*args):
    if check.get() == 1:
        side_pic.show()
    else:
        pic.show()

def show_album():
    msg.showinfo('Album Length',f'Length of your album is :\n\n{len(picz)}\nsize of album : {getsizeof(picz)}')

def contrast_rate():
    global pic

    pic = ImageEnhance.Contrast(pic)
    pic = pic.enhance(float(rate.get()))
    
    update_new_img()


def colour_rate():
    global pic

    pic = ImageEnhance.Color(pic)
    pic = pic.enhance(float(rate.get()))
    
    update_new_img() 


def resize_pic():
    global pic

    i = str(rate.get())
    i = i.split('x')
    a1 = int(i[0])
    a2 = int(i[1]) 
    pic = pic.resize([a1,a2])    
    
    update_new_img()


def crop_rate():
    global pic

    i = str(rate.get())
    i = i.split('x')
    x1 = int(i[0])
    y1 = int(i[1]) 
    x2 = int(i[2])
    y2 = int(i[3])
    area = (x1,y1,x2,y2) 
    
    pic = pic.crop(area)

    update_new_img() 


def sharpen_rate():
    global pic
    pic = ImageEnhance.Sharpness(pic)
    pic = pic.enhance(float(rate.get()))    
    update_new_img()


def blur_rate():
    global pic
    pic = pic.filter(ImageFilter.BoxBlur(float(rate.get())))
    update_new_img()


def rotate_pic():
    global pic
    pic = pic.transpose(Image.ROTATE_90)
    update_new_img()


def blend_rate():
    global pic
    if check.get()==1:
        pic_1 = side_pic

    else:        
        currdir = getcwd()
        tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please Select a Picture')
        tempdir=str(tempdir)
        txt = search('name=\'(.+?)\' mode=',tempdir)
        if txt:
            path = txt.group(1)
        pic_1 = Image.open(path)

    s = pic.size
    pic_1 = pic_1.resize([s[0],s[1]])
    pic_1.format = pic.format
    
    pic_1 = pic_1.convert(pic.mode)

    try:
        pic = Image.blend(pic,pic_1,float(rate.get()))
    except Exception as e:
        msg.showerror("Problem Occured",e)

    update_new_img()


def paste_pic():
    global pic
    
    pic_ratio = rate.get().split(',')
    pic_ratio1 = pic_ratio[0].split('x')
    pic_ratio2 = pic_ratio[1].split('x')

    if check.get()==1:
        overlay = side_pic
    else:
        currdir = getcwd()
        tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please Select a Picture')
        tempdir=str(tempdir)

        txt = search('name=\'(.+?)\' mode=',tempdir)
        if txt:
            path = txt.group(1)   
        overlay = Image.open(path) 
    
    pic = pic.copy()
    overlay = overlay.resize([int(pic_ratio1[0]),int(pic_ratio1[1])])
    Image.Image.paste(pic, overlay, [int(pic_ratio2[0]),int(pic_ratio2[1])])
    
    update_new_img()


def get_fonts(*event):
    font_dir = r"C:/Windows/Fonts"
    fonts = {}
    for root, dirs, files in walk(font_dir):
        for file in files:
            if file.lower().endswith(('.ttf','.otf')):
                key = file.split('.')[0]
                value = path.join(root, file)
                fonts[key] = value
    return fonts

def text_pic():
    global pic, text_color_picker

# -- Creating Second Window --

    root1 = Toplevel(root)
    root1.config(background='#111111')
    root1.geometry('300x400+540+150')

# -- root1 Functions --

    def draw_pic_():
        global pic, text_color_picker
        pic = pic.copy()
        draw= ImageDraw.Draw(pic)
        font= ImageFont.truetype(fonts[i5.get()],v2.get())

        axis = v5.get()
        axis = axis.split('x')
        x=int(axis[0])
        y=int(axis[1])
        points= x,y
        string=f"{v1.get()}"

        draw.text(points, string, color_now.get(), font=font)
        update_new_img()

        bt2.place(x=160,y=320,height=40,width=70)
            
# -- Variables for root1 --

    
    words='Flower , Fruit , Hello , Image , Picture , Happy New Year , Great , Thunder , Text , Storm'
    words=words.split(',')
    word=choice(words)

    v1=StringVar()
    v1.set(word) # random word
    v2=IntVar()
    v2.set(50)
    v5=StringVar()
    v5.set(f'{round((pic.width)/2)}x{round((pic.height)/2)}') #preexpected position
    fonts = get_fonts() # all fonts key:value
    fonts_list = list(fonts.keys()) # fonts list

# -- Creating root1 Widgets --

    l1 = Label(root1,text='Text : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l2 = Label(root1,text='Size : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l3 = Label(root1,text='Font : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l4 = Label(root1,text='Color: ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l5 = Label(root1,text='Axis : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 

    i3 = Entry(root1,textvariable=v1,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i4 = Entry(root1,textvariable=v2,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i7 = Entry(root1,textvariable=v5,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 

    bt1 = Button(root1,text='Draw',bd=2,bg='#222222',fg='coral',font='calibri 10 bold',relief=RAISED,command=draw_pic_)
    bt2 = Button(root1,text='Erase',bd=2,bg='#222222',fg='coral',font='calibri 10 bold',relief=RAISED,command=undo_pic)

    text_color_picker = Button(root1,textvariable=color_now,font='calibri 10 bold',bg=color_now.get(),width=18, command=choose_color) 

# -- Combobox dropdown For Fonts

    style = Style()
    style.theme_use("clam")
    style.configure('TCombobox',background='#222',selectbackground="black",selectforeground="gray",foreground='gray',borderwidth=2, state='readonly', fieldbackground="black")
    style.map('TCombobox', selectbackground=[('hover','black')],selectforeground=[('hover','gray')],foreground=[('hover','gray')],background=[('hover','black')],arrowcolor=[('hover','#00bfff')])

    i5 = Combobox(root1, values=fonts_list, font="calibri 10 bold", style='TCombobox', width=18)
    i5.set(fonts_list[0])

# -- Packing root1 widgets --

    l1.grid(row=1,padx=(20,0),pady=(40,0),ipadx=15,ipady=10)
    l2.grid(row=2,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l3.grid(row=3,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l4.grid(row=4,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l5.grid(row=5,padx=(20,0),pady=(10,0),ipadx=17,ipady=10)

    i3.grid(column=1,row=1,padx=(10,0),pady=(40,0),ipadx=15,ipady=10)
    i4.grid(column=1,row=2,padx=(10,0),pady=(10,0),ipadx=15,ipady=10)
    i5.grid(column=1,row=3,padx=(10,0),pady=(10,0),ipadx=15,ipady=10)
    text_color_picker.grid(column=1,row=4,padx=(10,0),pady=(10,0),ipadx=17,ipady=8)
    i7.grid(column=1,row=5,padx=(10,0),pady=(10,0),ipadx=17,ipady=10)
    
    bt1.place(x=75,y=320,height=40,width=70)
    
    hover_em([bt1,bt2])

    root1.grab_set() # untill root3 is open root will not work
    root1.transient(root) # root4 window will stay over root window
    root.wait_window(root1) # root window will wait untill root4 closes


def from_web(*args):
    global pic

# --- Functions for root2 ---


    def open_from_web():
        global pic, pic_pointer

        try:
            res = get(url.get())
            img_data = res.content
            temp_pic = Image.open(BytesIO(img_data))
            pic = temp_pic
            
            update_new_img()

        except EXCEPTION as e:
            msg.showerror("Cannot Open",e)
        
        finally:
            root3.destroy()

# --- Activating root3 ---

    root3 = Toplevel(root)
    root3.anchor(CENTER)
    root3.config(background='#111111')
    root3.title('fetch image from web')
    root3.geometry('300x150+540+200')
    
# --- Variable for root3 ---

    url = StringVar()
    url.set('URL')

# --- Widgets for root3 ---

    iS = Entry(root3,textvariable=url,bd=2,bg='black',fg='gray',font='calibri 13 bold',relief=SUNKEN,width=30,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)
    bs = Button(root3,text='Open',bd=0,bg='#222222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=open_from_web)

# --- Packing Widgets in root3 ---

    iS.pack(padx=1,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=1,pady=25,ipady=7,ipadx=13)

    hover_em([bs])

    root3.grab_set() # untill root3 is open root will not work
    root3.transient(root) # root3 window will stay over root window
    root.wait_window(root3) # root window will wait untill root3 closes


def set_pic(*args):
    global pic, pic_path, picz, pic_pointer

    currdir = getcwd()
    tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please Select an Image')
    tempdir=str(tempdir)

    txt = search('name=\'(.+?)\' mode=',tempdir)
    if txt:
        path = txt.group(1)

    pic_path = path
    pic = Image.open(path)

    update_new_img()


def save_gui(*args):
    global pic


# --- Functions for root2 ---

    def save_pic():
        global pic
        
        try:
            pic.save(vs.get())
            root2.destroy()
            msg.showinfo('Image Saved',f'{vs.get()} Saved Successfully')
        except EXCEPTION as e:
            root2.destroy()
            msg.showerror("Cannot Save",e)

        sleep(0.8)

# --- Activating root2 ---

    root2 = Toplevel(root)
    root2.anchor(CENTER)
    root2.config(background='#111111')
    root2.title('Save Image')
    root2.geometry('300x150+540+200')
    
# --- Variable for root2 ---

    vs = StringVar()
    vs.set('pic.png')

# --- Widgets for root2 ---

    iS = Entry(root2,textvariable=vs,bd=2,bg='black',fg='gray',font='calibri 13 bold',relief=SUNKEN,width=30,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)
    bs = Button(root2,text='Save',bd=0,bg='#222222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=save_pic)

# --- Packing Widgets in root2 ---

    iS.pack(padx=1,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=1,pady=25,ipady=7,ipadx=13)

    hover_em([bs])

    root2.grab_set() # untill root2 is open root will not work
    root2.transient(root) # root2 window will stay over root window
    root.wait_window(root2) # root window will wait untill root2 closes


# -- Activating Tkinter --

root = Tk()
root.geometry('1450x1000+0+0')
root.title('Photo-Editor')
root.config(background='#111111')


# ------------------------- Shortcut Keys ------------------------- 

root.bind("<Control-z>",undo_pic)
root.bind("<Control-y>",redo_pic)
root.bind("<Control-i>",info_pic)
root.bind("<Control-n>",set_pic)
root.bind("<Control-w>",from_web)
root.bind("<Control-s>",save_gui)
root.bind("<Control-o>",show_pic)
root.bind("<Control-c>",interchange_side_pic_and_pic)
root.bind("<Control-+>",create_side_pic)

# -- Variable --

rate=StringVar()
rate.set(1)
new_name=StringVar()
new_name.set('Photo.jpg')
check = IntVar()
check.set(0)
color_now=StringVar()

# -- Menu Styles --

style = Style()
style.theme_use('clam')
style.configure('TMenu',foreground='#00bfff',background='#222')

# --- Menu ---

Menu1 = Menu(root) # main menu

m1 = Menu(Menu1, tearoff=0,bg='black',fg='#00bfff',font='calibri 9 bold') 
m1.add_command(label='NEW',command=set_pic) 
m1.add_separator()
m1.add_command(label='WEB',command=from_web)
m1.add_separator()
m1.add_command(label='CREATE',command=make_pic) 
m1.add_separator()
m1.add_command(label='SIDE IMG',command=create_side_pic)
m1.add_separator()
m1.add_command(label='SCALE',command=scale_pic)
m1.add_separator()
m1.add_command(label='INFO',command=info_pic) 
m1.add_separator()
m1.add_command(label='SHOW',command=show_pic)
m1.add_separator()  
m1.add_command(label='SAVE',command=save_gui)

m2 = Menu(Menu1, tearoff=0,bg='black',fg='orange',font='calibri 9 bold') 
m2.add_command(label='Info Image',command=exp_info) 
m2.add_separator()
m2.add_command(label='Save Help',command=exp_save)
m2.add_separator()
m2.add_command(label='Resize Image',command=exp_size)
m2.add_separator()
m2.add_command(label='Crop Image',command=exp_crop)
m2.add_separator()
m2.add_command(label='Rotate Image',command=exp_rotate)
m2.add_separator()
m2.add_command(label='Blend new Image',command=exp_blend)
m2.add_separator()
m2.add_command(label='Create Image',command=exp_create)
m2.add_separator()
m2.add_command(label='Apply Filter',command=exp_filter)
m2.add_separator()
m2.add_command(label='Text on Image',command=exp_text)
m2.add_separator()
m2.add_command(label='Flip Image',command=exp_flip)
m2.add_separator()
m2.add_command(label='Paste Image',command=exp_paste)
m2.add_separator()
m2.add_command(label='Use Border',command=exp_border)
m2.add_separator()
m2.add_command(label='Other Helps',command=exp_others)

m3 = Menu(Menu1, tearoff=0,bg='black',fg='#00bfff',font='calibri 9 bold') 
m3.add_command(label='Undo Single',command=undo_pic) 
m3.add_separator()
m3.add_command(label='Redo',command=redo_pic) 
m3.add_separator()
m3.add_command(label='Undo All',command=undo_new)
m3.add_separator()
m3.add_command(label='Album Length',command=show_album)

m4 = Menu(Menu1, tearoff=0,bg='black',fg='orange',font='calibri 9 bold')
m4.add_command(label='1- CONTOUR',command=filter_rate1) 
m4.add_separator()
m4.add_command(label='2- DETAIL',command=filter_rate2) 
m4.add_separator()
m4.add_command(label='3- FIND_EDGES',command=filter_rate3) 
m4.add_separator()
m4.add_command(label='4- EMBOSS',command=filter_rate4) 
m4.add_separator()
m4.add_command(label='5- SMOOTH',command=filter_rate5) 
m4.add_separator()
m4.add_command(label='6- SMOOTH_MORE',command=filter_rate6) 
m4.add_separator()
m4.add_command(label='7- EDGE_ENHANCE',command=filter_rate7) 
m4.add_separator()
m4.add_command(label='8- EDGE_ENHANCE_MORE',command=filter_rate8) 

m5 = Menu(Menu1, tearoff=0,bg='black',fg='#00bfff',font='calibri 9 bold')
m5.add_command(label='RGB',command=convert_RGB) 
m5.add_separator()
m5.add_command(label='RBGA',command=convert_RGBA) 
m5.add_separator()
m5.add_command(label='CMYK',command=convert_CMYK) 
m5.add_separator()
m5.add_command(label='GrayScale',command=convert_L) 

#-- packing _ Menu ----

root.config(menu=Menu1)
Menu1.add_cascade(label='File', menu=m1)
Menu1.add_cascade(label='Help', menu=m2)
Menu1.add_cascade(label='Undo', menu=m3)
Menu1.add_cascade(label='Filter', menu=m4)
Menu1.add_cascade(label='Convert', menu=m5)

# -- Screen_Image --

img1= ImageTk.PhotoImage(pic.resize([800,450]))
scr_img= Label(root,image= img1, bd= 0, bg="#222222")

# -- Color Chooser --

color_now.set("#ffffff")
def choose_color():
    color_code = colorchooser.askcolor(title="choose color")
    
    if color_code and color_code[1] is not None:
        color_label.config(bg=color_code[1])
        
        try:
            text_color_picker.config(bg=color_code[1])
        except Exception:
            pass

        color_now.set(color_code[1])


def set_hex():

    def set_hex_code():
        color_label.config(bg=hex.get())
        
        try:
            text_color_picker.config(bg=hex.get())
        except Exception:
            pass
        
        color_now.set(hex.get())
        root6.destroy()
    

    # --- Activating root6 ---

    root6 = Toplevel(root)
    root6.anchor(CENTER)
    root6.config(background='#111111')
    root6.title('Enter hex code')
    root6.geometry('300x150+540+200')
    
    # --- Variable for root6 ---

    hex = StringVar()
    hex.set(color_now.get())

    # --- Widgets for root6 ---

    iS = Entry(root6,textvariable=hex,bd=2,bg='black',fg='gray',font='calibri 13 bold',relief=SUNKEN,width=30,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)
    bs = Button(root6,text='set hex',bd=0,bg='#222222',fg='#ca5cdd',font='calibri 13',relief=RAISED,command=set_hex_code)

    # --- Packing Widgets in root6 ---

    iS.pack(padx=1,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=1,pady=25,ipady=7,ipadx=13)

    root6.grab_set() # untill root6 is open root will not work
    root6.transient(root) # root6 window will stay over root window
    root.wait_window(root6) # root window will wait untill root6 closes


color_label = Button(root,textvariable=color_now,font='calibri 12 bold',bd=0, bg=color_now.get(), width=12, height=4, command=choose_color, relief=RIDGE)
color_hex = Button(root,text='hex code',bg='#111',fg='#ca5cdd',font='calibri 12',bd=2,relief=RAISED,command=set_hex,activeforeground="#da8ee7",activebackground="#111",cursor=cursor_shape)

# -- GUI LOOK --

h1 = Label(text='Photo-Pyditor',bd=0,bg='#222',fg='coral',font='calibri 25 bold',relief='groove') 
i1 = Entry(bg='#000000',fg='gray',bd=2,relief=SUNKEN,font='calibri 16 bold',textvariable=rate,width=10,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)

b1 = Button(text='Bright',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=bright_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b2 = Button(text='Contrast',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=contrast_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b3 = Button(text='Colour',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=colour_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b4 = Button(text='Sharpen',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=sharpen_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b5 = Button(text='Blur',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=blur_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b6 = Button(text='Resize',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=resize_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
B1 = Button(text='Border',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=border_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)

b_1 = Button(text='Rotate',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=rotate_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_2 = Button(text='Crop',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=crop_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_3 = Button(text='Blend',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=blend_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_4 = Button(text='Invert',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=invert_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_5 = Button(text='Text',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=text_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_6 = Button(text='Flip',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=flip_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
B2 = Button(text='Paste',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=paste_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)

B3 = Button(text='InterChange',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=interchange_side_pic_and_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
check_side_pic = Checkbutton(text="side image",bg="#222222",fg="#00bfff",font="calibri 10 bold",bd=0,variable=check,selectcolor="black",activeforeground="#00bfff",activebackground="#555555")

# -- PACKING --

scr_img.place(x=290,y=125)

h1.place(x=0,y=0,height=60,width=1380)
i1.place(x=5,y=125,height=40,width=185)

color_label.place(x=1250,y=130)
color_hex.place(x=1250,y=230, width=101, height=40)

b1.grid(row=2,column=1,pady=(180,0),padx=(5,0),ipadx=23,ipady=10)
b2.grid(row=3,column=1,pady=(2,0),padx=(5,0),ipadx=16,ipady=10)
b3.grid(row=4,column=1,pady=(2,0),padx=(5,0),ipadx=21,ipady=10)
b4.grid(row=5,column=1,pady=(2,0),padx=(5,0),ipadx=17,ipady=10)
b5.grid(row=6,column=1,pady=(2,0),padx=(5,0),ipadx=28,ipady=10)
b6.grid(row=7,column=1,pady=(2,0),padx=(5,0),ipadx=22,ipady=10)
B1.grid(row=8,column=1,pady=(2,0),padx=(5,0),ipadx=20,ipady=10)

b_1.grid(row=2,column=3,pady=(180,0),padx=(10,0),ipadx=21,ipady=10)
b_2.grid(row=3,column=3,pady=(2,0),padx=(10,0),ipadx=27,ipady=10)
b_3.grid(row=4,column=3,pady=(2,0),padx=(10,0),ipadx=24,ipady=10)
b_4.grid(row=5,column=3,pady=(2,0),padx=(10,0),ipadx=23,ipady=10)
b_5.grid(row=6,column=3,pady=(2,0),padx=(10,0),ipadx=28,ipady=10)
b_6.grid(row=7,column=3,pady=(2,0),padx=(10,0),ipadx=30,ipady=10)
B2.grid(row=8,column=3,pady=(2,0),padx=(10,0),ipadx=24,ipady=10)

hover_em([b1, b2, b3, b4, b5, b6, B1, b_1, b_2, b_3, b_4, b_5, b_6, B2])

# ------------------------ END ---------------------------

root.mainloop()