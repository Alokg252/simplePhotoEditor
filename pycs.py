# -- Imports --

from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageEnhance, ImageFilter, ImageTk, ImageDraw, ImageFont, ImageOps
from tkinter import filedialog
from re import search
from random import choice
from os import getcwd, remove, rename
from time import sleep
from moviepy.editor import *
from keyboard import is_pressed

# -- values --

cursor_shape="dot"

# -- Album --

pic= Image.new("RGBA",(850,500),"#222222")
picz = []

# -- Functions --

def append_pic():
    picz.append(pic)

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

def create_side_pic(*args):
    global side_pic, pic

    side_pic = pic

    currdir = getcwd()
    tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Select New Picture')
    tempdir=str(tempdir)
    print(tempdir)
    txt = search('name=\'(.+?)\' mode=',tempdir)
    if txt:
        path = txt.group(1)
    pic = Image.open(path)    
    update_img()

    check_side_pic.place(x=5,y=496,height=30,width=85)
    B3.place(x=103,y=496,height=30,width=85)

def interchange_side_pic_and_pic(*args):
    global pic, side_pic
    pic, side_pic = side_pic, pic
    update_img()

# --- Help Functions---

def exp_size():
    sleep(0.5)
    msg1 = msg.showinfo('How to Resize','For Resizing a Picture type (Width)x(Height) in Entry box and press Resize button')
    sleep(0.5)

def exp_save():
    sleep(0.5)
    msg1 = msg.showinfo('How to save','For Save your edited image You just have follow this\n\nMenuBar -> File -> Save\nThan tye full name of image with format\nClick on Save button')
    sleep(0.5)

def exp_crop():
    sleep(0.5)
    msg1 = msg.showinfo('How to Crop','from croping a image you just have to Enter \npoint(X1,Y1) and point(X2,Y2) as X1xY1xX2xY2 in Entry box and press Crop button')
    sleep(0.5)

def exp_rotate():
    sleep(0.5)
    msg1 = msg.showinfo('How to rotate','For Rotate an image you just have to enter \nAngle(90,180,270,360) in Entry box and press Rotate button')
    sleep(0.5)

def exp_text():
    sleep(0.5)
    msg1 = msg.showinfo('How to Text','For text something in an image you just have to press Text button \nthen fill the required informations like(Sentence, Font, Fontsize, Colour, Etc) and press Draw button')
    sleep(0.5)

def exp_info():
    sleep(0.5)
    msg1 = msg.showinfo('How to info','To get informations about your photo just press info button')
    sleep(0.5)

def exp_filter():
    sleep(0.5)
    msg1 = msg.showinfo('How to apply filter','you can choose filter and apply using Filter option in menu bar')
    sleep(0.5)

def exp_merge():
    sleep(0.5)
    msg1 = msg.showinfo('How to merge another image','to merge another image you have to enter effect rate of new image on current image on Entry box and press mearge button to choose that new image \nbut the formate of that new image and current image should be same.')
    sleep(0.5)

def exp_border():
    sleep(0.5)
    msg1 = msg.showinfo('How to use border','to use border in image you have to enter border width and color in Entry box and press Border button\n\nFormate :- Width,Color')
    sleep(0.5)

def exp_flip():
    sleep(0.5)
    msg1 = msg.showinfo('How to flip image','to flip an image you have to enter y(for up side down) or x(for right side left) in Entry box and press Flip button')
    sleep(0.5)

def exp_paste():
    sleep(0.5)
    msg1 = msg.showinfo('How to paste image','to paste an image you have to enter new image size and new image position\n\nFormate : (width)x(height),(X)x(Y) in Entry box and press Paste button')
    sleep(0.5)

def exp_others():
    sleep(0.5)
    msg1 = msg.showinfo('How to apply simple editig','you can change image Brightness, Color, Contrast, Sharpness and Blurness\nBy entring Rate of change in Entry box \n\n rate 1 will remain the image same and 0 will remove that proprty from the image as you decrease rate from 1 to 0 that property will decrease and\nas you increase value from 1 that property will be increase ')
    sleep(0.5)

# --- Undo Functions ---

def undo_pic(*args):
    global pic, picz, flag1
    if len(picz)==1:
        pic=picz[0]
        msg.showwarning('Last Pic','This is the last picture in the Album')
    else:
        pic=picz[-1]
        picz.pop()
    update_img()

def undo_new():
    global pic, picz
    pic = picz[0]
    picz=[pic]
    update_img()

def undo_sup():
    global pic, pic1
    pic=pic1
    update_img()

# --- Filter Functions ---


def filter_rate1():    
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.CONTOUR)
    update_img()


def filter_rate2():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.DETAIL)
    update_img()


def filter_rate3():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.FIND_EDGES)
    update_img()


def filter_rate4():    
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.EMBOSS)
    update_img()


def filter_rate5():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.SMOOTH)
    update_img()


def filter_rate6():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.SMOOTH_MORE)
    update_img()


def filter_rate7():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.EDGE_ENHANCE)
    update_img()


def filter_rate8():
    global pic
    append_pic()

    pic1 = pic
    pic = pic.filter(ImageFilter.EDGE_ENHANCE_MORE)
    update_img()

# --- Other Editing Functions ---

def border_pic():
    global pic
    append_pic()

    i = rate.get().split(',')

    if len(i)==1:
        pic = ImageOps.expand(pic,border=int(5),fill='black')
        pic = ImageOps.expand(pic,border=int(4),fill=rate.get())
        pic = ImageOps.expand(pic,border=int(5),fill='black')
    
    elif len(i)==3:
        pic = ImageOps.expand(pic,border=int(5),fill=i[0])
        pic = ImageOps.expand(pic,border=int(4),fill=i[1])
        pic = ImageOps.expand(pic,border=int(5),fill=i[2])
    
    elif len(i)==2:
        pic = ImageOps.expand(pic,border=int(i[0]),fill=i[1])

    else:
        pic = pic
        picz.pop()
        msg.showerror('Attribute error','Enter right attributes')    
    update_img()


def flip_pic():
    global pic
    append_pic()

    if rate.get() == 'y':
        pic = ImageOps.flip(pic)
    elif rate.get() == 'x':
        pic = ImageOps.mirror(pic)
    else:
        pic = pic
        picz.pop()
        msg.showerror('Attribute Error','Enter x or y in Entry box to flip image')       
    update_img()


def invert_rate():
    global pic
    append_pic()

    pic= ImageOps.invert(pic)
    update_img()


def fit_pic():
    global pic
    append_pic()
    size = rate.get().split('x')
    pic= ImageOps.fit(pic,(int(size[0]), int(size[1])) )
    update_img()


def scale_pic():
    global pic
    append_pic()
    pic= ImageOps.scale(pic, float(rate.get()))
    update_img()


def bright_rate():
    global pic
    append_pic()

    pic1 = pic
    pic = ImageEnhance.Brightness(pic)
    pic = pic.enhance(float(rate.get()))
    update_img()


def info_pic(*args):
    if check.get() == 1:
        size = side_pic.size
        form = side_pic.format    
    
    else:
        size = pic.size
        form = pic.format
    
    try:    
        msg.showinfo('Picture Info',f'Size: {size}\nForm: {form}\nPath: {pic_path}')
    except Exception as e:
        msg.showinfo('Picture Info',f'Size: {size}\nForm: {form}\nPath: Not Define')

def show_pic(*args):
    if check.get() == 1:
        side_pic.show()
    else:
        pic.show()

def show_album():
    msg.showinfo('Album Length',f'Length of your album is :\n\n{len(picz)}')

def contrast_rate():
    global pic
    append_pic()

    pic = ImageEnhance.Contrast(pic)
    pic = pic.enhance(float(rate.get()))
    update_img()


def colour_rate():
    global pic
    append_pic()

    pic = ImageEnhance.Color(pic)
    pic = pic.enhance(float(rate.get()))
    update_img() 


def resize_pic():
    global pic
    append_pic()

    i = str(rate.get())
    i = i.split('x')
    a1 = int(i[0])
    a2 = int(i[1]) 
    
    pic = pic.resize([a1,a2])    
    update_img()


def crop_rate():
    global pic
    append_pic()

    i = str(rate.get())
    i = i.split('x')
    x1 = int(i[0])
    y1 = int(i[1]) 
    x2 = int(i[2])
    y2 = int(i[3])
    area = (x1,y1,x2,y2) 
    
    pic = pic.crop(area)
    update_img() 


def sharpen_rate():
    global pic
    append_pic()

    pic = ImageEnhance.Sharpness(pic)
    pic = pic.enhance(float(rate.get()))
    update_img()


def blur_rate():
    global pic
    append_pic()

    pic = pic.filter(ImageFilter.BoxBlur(float(rate.get())))
    update_img()


def rotate_rate():
    global pic
    append_pic()

    w = pic.width
    h = pic.height
    
    if pic.height < pic.width :
        pic = pic.resize([w,w])
    else:   
        pic = pic.resize([h,h])

    pic = pic.rotate(int(rate.get()))

    if int(rate.get()) == 90 or int(rate.get()) == 270:
        pic = pic.resize([h,w])
    elif int(rate.get()) == 180 or int(rate.get()) == 370:
        pic = pic.resize([w,h])
    else:
        pic = pic.resize([w,h])

    update_img()


def merge_rate():
    global pic
    append_pic()
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
    try:
        pic = Image.blend(pic,pic_1,float(rate.get()))
    except Exception as e:
        msg.showerror("Problem Occured",e)

    update_img()


def paste_pic():
    global pic
    append_pic()
    
    pic_ratio = rate.get().split(',')
    pic_ratio1 = pic_ratio[0].split('x')
    pic_ratio2 = pic_ratio[1].split('x')

    try:
        remove('pic.jpg')
    except Exception as e:
        pass  

    try:
        remove('pic1.jpg')
    except Exception as e:
        pass  
    
    if check.get()==1:
        side_pic.resize([pic_ratio1[0],pic_ratio1[1]])
        side_pic.save("pic1.png")
        pic1 = (ImageClip("pic1.png").margin(right=8,top=8,opacity=0).set_pos([int(pic_ratio2[0]),int(pic_ratio2[1])]).resize(height=int(pic_ratio1[1]),width=int(pic_ratio1[0])))
    else:
        currdir = getcwd()
        tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please Select a Picture')
        tempdir=str(tempdir)

        print(tempdir)
        txt = search('name=\'(.+?)\' mode=',tempdir)
        if txt:
            path = txt.group(1)    
        pic1 = (ImageClip(path).margin(right=8,top=8,opacity=0).set_pos([int(pic_ratio2[0]),int(pic_ratio2[1])]).resize(height=int(pic_ratio1[1]),width=int(pic_ratio1[0])))
    pic.save('pic.png')
    pic = (ImageClip('pic.png')).margin(right=8,top=8,opacity=0).set_pos([0,0]).resize(height=pic.height,width=pic.width)
    
    try:
        remove('pic.png')
    except Exception as e:
        pass
    
    try:
        remove('pic1.png')
    except Exception as e:
        pass

    pic = CompositeVideoClip([pic,pic1])
    pic.save_frame("pic.png",t=1)
    rename('pic.png','pic.jpg')
    pic = Image.open('pic.jpg')
    append_pic()
    pic=picz[-1]
    update_img()
    remove("pic.jpg")


def text_pic():

# -- Creating Second Window --

    root1 = Toplevel(root)
    root1.config(background='#111111')
    root1.geometry('300x400+540+150')

# -- root1 Functions --


    def show_font():
        msg.askokcancel('Fonts','algerian , arial , elephant , forte , gigi , marlet\nmidtral , onyx , verdana , webdings , broadway\ncastellar , centaur , chiller , dauphin , impact , kids , playbill\npristina , ravie , rockwell , stencil , tahoma , technical')

    def draw_pic_():
        global pic, flag1
        flag1 = True

# -- Texting on image can effect other photos of album so,
#  adding 2 photos in the album to escape other photos from this effect

        pic = ImageEnhance.Sharpness(pic)
        pic = pic.enhance(float(1.00000000000000000001))
        append_pic()
        
        pic = ImageEnhance.Sharpness(pic)
        pic = pic.enhance(float(1.00000000000000000002))
        append_pic()
        bt2.place(x=155,y=320,height=40,width=70)


        def write_text():

            draw= ImageDraw.Draw(pic)
            font= ImageFont.truetype(v3.get()+'.ttf',v2.get())
            color= v4.get()

            axis = v5.get()
            axis = axis.split('x')
            x=int(axis[0])
            y=int(axis[1])

            points= x,y
            string=f"{v1.get()}"
            draw.text(points, string, color, font=font)

            update_img() 
            picz.pop() # we had added 2 photos so, removing one and one will remain in album
        write_text()

# -- Variables for root1 --

    v1=StringVar()
    
    words='Flower , Fruit , Hello , Image , Picture , Happy New Year , Great , Thunder , Text , Storm'
    words=words.split(',')
    word=choice(words)
    v1.set(word)
    
    v2=IntVar()
    v2.set(50)
    v3=StringVar()
    v3.set('impact')
    v4=StringVar()
    v4.set('white')
    v5=StringVar()
    # v5.set(f'{int((pic.width)/2) - int((pic.width)/3)}x{int((pic.height)/2) + int((pic.height)/4)}')
    v5.set(f'{round((pic.width)/2)}x{round((pic.height)/2)}')

# -- Creating root1 Widgets --

    h2 = Label(root1,text='Text-Details',bd=4,bg='black',fg='coral',font='calibri 16 bold',relief=GROOVE,width=40) 
    l1 = Label(root1,text='Text : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l2 = Label(root1,text='Size : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l3 = Label(root1,text='Font : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l4 = Label(root1,text='Color: ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 
    l5 = Label(root1,text='Axis : ',bd=3,bg='black',fg='#00bfff',font='calibri 10 bold',relief=RIDGE) 

    i3 = Entry(root1,textvariable=v1,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i4 = Entry(root1,textvariable=v2,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i5 = Entry(root1,textvariable=v3,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i6 = Entry(root1,textvariable=v4,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 
    i7 = Entry(root1,textvariable=v5,bd=3,bg='black',fg='gray',font='calibri 10 bold',relief=SUNKEN,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False) 

    bt1 = Button(root1,text='Draw',bd=2,bg='#222222',fg='coral',font='calibri 10 bold',relief=RAISED,command=draw_pic_)
    bt2 = Button(root1,text='Erase',bd=2,bg='#222222',fg='coral',font='calibri 10 bold',relief=RAISED,command=undo_pic)

# -- Packing root1 widgets --

    l1.grid(row=1,padx=(20,0),pady=(40,0),ipadx=15,ipady=10)
    l2.grid(row=2,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l3.grid(row=3,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l4.grid(row=4,padx=(20,0),pady=(10,0),ipadx=15,ipady=10)
    l5.grid(row=5,padx=(20,0),pady=(10,0),ipadx=17,ipady=10)

    i3.grid(column=1,row=1,padx=(10,0),pady=(40,0),ipadx=15,ipady=10)
    i4.grid(column=1,row=2,padx=(10,0),pady=(10,0),ipadx=15,ipady=10)
    i5.grid(column=1,row=3,padx=(10,0),pady=(10,0),ipadx=15,ipady=10)
    i6.grid(column=1,row=4,padx=(10,0),pady=(10,0),ipadx=15,ipady=10)
    i7.grid(column=1,row=5,padx=(10,0),pady=(10,0),ipadx=17,ipady=10)
    
    bt1.place(x=75,y=320,height=40,width=70)

    root1.mainloop()

def set_pic(*args):
    global pic, pic_path, picz, pic1

    #root.withdraw()

    currdir = getcwd()
    tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please Select an Image')
    tempdir=str(tempdir)

    print(tempdir)
    txt = search('name=\'(.+?)\' mode=',tempdir)
    if txt:
        path = txt.group(1)

    pic_path = path
    pic = Image.open(path)
    pic1 = Image.open(path)
    picz = []
    picz.append(pic)
    update_img()



def save_gui(*args):
    global pic

# --- Functions for root2 ---

    def save_pic1():
        global pic
        pic.save(vs.get())
        root2.withdraw()
        m = msg.showinfo('Image Saved',f'{vs.get()} Saved Successfully')
        sleep(0.8)
        print(m)
        

# --- Activating root2 ---

    root2 = Toplevel(root)
    root2.anchor(CENTER)
    root2.config(background='#111111')
    root2.title('Save Image')
    root2.geometry('300x150+540+200')
# --- Variable for root2 ---

    vs = StringVar()
    vs.set('PyImage.jpg')

# --- Widgets for root2 ---

    iS = Entry(root2,textvariable=vs,bd=2,bg='black',fg='gray',font='calibri 13 bold',relief=SUNKEN,width=30,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)
    bs = Button(root2,text='Save',bd=0,bg='#222222',fg='#00bfff',font='calibri 13 bold',relief=RAISED,command=save_pic1)

# --- Packing Widgets in root2 ---

    iS.pack(padx=1,pady=(20,0),ipady=5,ipadx=1)
    bs.pack(padx=1,pady=25,ipady=7,ipadx=13)

    root2.mainloop() 


# -- Activating Tkinter --

root = Tk()
root.geometry('1450x1000+0+0')
root.title('Photo-Editor')
root.config(background='#111111')

# ------------------------- Shortcut Keys ------------------------- 

root.bind("<Control-z>",undo_pic)
root.bind("<Control-i>",info_pic)
root.bind("<Control-n>",set_pic)
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

# --- Menu ---

Menu1 = Menu(root,) # main menu

m1 = Menu(Menu1, tearoff=0,bg='black',fg='#00bfff',font='calibri 9 bold') 
m1.add_command(label='NEW',command=set_pic) 
m1.add_separator()
m1.add_command(label='INFO',command=info_pic) 
m1.add_separator()
m1.add_command(label='SHOW',command=show_pic)
m1.add_separator()
m1.add_command(label='FIT',command=fit_pic)
m1.add_separator()
m1.add_command(label='SCALE',command=scale_pic)
m1.add_separator()
m1.add_command(label='SIDE IMG',command=create_side_pic)
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
m2.add_command(label='Merge new Image',command=exp_merge)
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
m3.add_command(label='Undo All',command=undo_new)
m3.add_separator()
m3.add_command(label='Undo Super',command=undo_sup)
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


#-- packing _ Menu ----

root.config(menu=Menu1)
Menu1.add_cascade(label='File', menu=m1)
Menu1.add_cascade(label='Help', menu=m2)
Menu1.add_cascade(label='Undo', menu=m3)
Menu1.add_cascade(label='Filter', menu=m4)

# -- Screen_Image --
img1= ImageTk.PhotoImage(pic.resize([800,450]))
scr_img= Label(root,image= img1, bd= 0, bg="#222222")

# -- GUI LOOK --

h1 = Label(text='Photo-Editor',bd=4,bg='black',fg='coral',font='calibri 25 bold',relief='groove') 
i1 = Entry(bg='#000000',fg='gray',bd=2,relief=SUNKEN,font='calibri 16 bold',textvariable=rate,width=10,insertbackground="#aaaaaa",insertwidth=1,insertofftime=False)

b1 = Button(text='Bright',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=bright_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b2 = Button(text='Contrast',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=contrast_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b3 = Button(text='Colour',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=colour_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b4 = Button(text='Sharpen',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=sharpen_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b5 = Button(text='Blur',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=blur_rate,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
b6 = Button(text='Resize',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=resize_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
B1 = Button(text='Border',bg='#222222',fg='#00bfff',font='calibri 10 bold',bd=0,relief=RAISED,command=border_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)

b_1 = Button(text='Rotate',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=rotate_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_2 = Button(text='Crop',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=crop_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_3 = Button(text='Merge',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=merge_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_4 = Button(text='Invert',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=invert_rate,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_5 = Button(text='Text',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=text_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
b_6 = Button(text='Flip',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=flip_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)
B2 = Button(text='Paste',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=paste_pic,activeforeground="coral",activebackground="#555555",cursor=cursor_shape)

B3 = Button(text='InterChange',bg='#222222',fg='coral',font='calibri 10 bold',bd=0,relief=RAISED,command=interchange_side_pic_and_pic,activeforeground="#00bfff",activebackground="#555555",cursor=cursor_shape)
check_side_pic = Checkbutton(text="side image",bg="#222222",fg="#00bfff",font="calibri 10 bold",bd=0,variable=check,selectcolor="black",activeforeground="#00bfff",activebackground="#555555")

# -- PACKING --

scr_img.place(x=350,y=125)

h1.place(x=80,y=8,height=60,width=1200)
i1.place(x=5,y=125,height=40,width=185)

b1.grid(row=2,column=1,pady=(180,0),padx=(5,0),ipadx=23,ipady=10)
b2.grid(row=3,column=1,pady=(2,0),padx=(5,0),ipadx=16,ipady=10)
b3.grid(row=4,column=1,pady=(2,0),padx=(5,0),ipadx=21,ipady=10)
b4.grid(row=5,column=1,pady=(2,0),padx=(5,0),ipadx=17,ipady=10)
b5.grid(row=6,column=1,pady=(2,0),padx=(5,0),ipadx=28,ipady=10)
b6.grid(row=7,column=1,pady=(2,0),padx=(5,0),ipadx=22,ipady=10)
B1.grid(row=8,column=1,pady=(2,0),padx=(5,0),ipadx=20,ipady=10)

b_1.grid(row=2,column=3,pady=(180,0),padx=(10,0),ipadx=23-2,ipady=10)
b_2.grid(row=3,column=3,pady=(2,0),padx=(10,0),ipadx=29-2,ipady=10)
b_3.grid(row=4,column=3,pady=(2,0),padx=(10,0),ipadx=24-2,ipady=10)
b_4.grid(row=5,column=3,pady=(2,0),padx=(10,0),ipadx=25-2,ipady=10)
b_5.grid(row=6,column=3,pady=(2,0),padx=(10,0),ipadx=30-2,ipady=10)
b_6.grid(row=7,column=3,pady=(2,0),padx=(10,0),ipadx=32-2,ipady=10)
B2.grid(row=8,column=3,pady=(2,0),padx=(10,0),ipadx=26-2,ipady=10)

root.mainloop()