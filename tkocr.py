# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image
import pytesseract, tkinter.messagebox, tkinter.filedialog

NAMA_PROGRAM = "B.A.D. - Baca Aku Dong"
root = Tk()
path_img = {'path': 0}

def exitProg(event=None):
    if tkinter.messagebox.askokcancel("Confirm Exit", "Are you sure want to exit B.A.D.?"):
        root.destroy()

def convertImgToText():
	if path_img['path']:
		img = Image.open(path_img['path'])
		text = pytesseract.image_to_string(img, lang='eng')
		result_textbox.delete('1.0', END)
		result_textbox.insert(END, text)
		with open('output.txt', 'w') as f:
			f.write(text)
	else:
		result_textbox.delete('1.0', END)
		result_textbox.insert(END, "File gambar tidak dapat dibaca atau belum dibuka")

def openFile():
	name = tkinter.filedialog.askopenfilename(
		initialdir="/",
		filetypes=(
			("PNG file", "*.png"),
			("JPG file", "*.jpg"),
			("JPEG file", "*.jpeg")
		),
		title="Pilih satu file"
	)
	path_img['path'] = name

open_file_icon = PhotoImage(file='icons/open_file.gif')
exit_file_icon = PhotoImage(file="icons/exit.png")

text_image_icon = PhotoImage(file='icons/imgtext.gif')
text_convert_icon = PhotoImage(file='icons/text.png')

title1_lbl = Label(root, text="B.A.D. - Baca Aku Dong")
title1_lbl.grid(row=1, column=1, sticky=(E))
title2_lbl = Label(root, text="by Fadhiil Rachman")
title2_lbl.grid(row=1, column=2, sticky=(W))

convert_btn = Button(root, text="Konversi Gambar ke Teks", command=convertImgToText)
convert_btn.grid(row=2, column=1)

result_lbl = Label(root, text="Teks dari gambar:")
result_lbl.grid(row=3, column=1, sticky=(W))

result_textbox = Text(root, height=6)
result_textbox.grid(row=4, column=1, columnspan=2)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Buka..", accelerator='Ctrl+O', compound='left',
                      image=open_file_icon, underline=0, command=openFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", image=exit_file_icon, compound='left', command=exitProg)
menu_bar.add_cascade(label='File', menu=file_menu)

ocr_menu = Menu(menu_bar, tearoff=0)
ocr_menu.add_command(label='Buka file gambar', accelerator='Ctrl+O', compound='left',
			image=text_image_icon, underline=0, command=openFile)
ocr_menu.add_command(label='Konversi ke Teks', accelerator='Ctrl+T', compound='left',
			image=text_convert_icon, underline=0, command=convertImgToText)
menu_bar.add_cascade(label='Tesseract OCR', menu=ocr_menu)

root.geometry("600x180")
root.title(NAMA_PROGRAM)
root.config(menu=menu_bar)
root.mainloop()
