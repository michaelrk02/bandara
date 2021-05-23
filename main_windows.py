from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from csv import *

jenis_penerbangan = []
with open('dom_nondom.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        jenis_penerbangan.append(row)


def frame_1(frame):
    frame.tkraise()


root = Tk()
root.geometry('500x500')
#  root.state('zoomed')
root.title('Soetta-Loka')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


logo = Image.open('logo soettaloka.png')
logo_ico = ImageTk.PhotoImage(logo)
root.wm_iconphoto(False, logo_ico)

main_page = Frame(root)
main_page.grid(row=0, column=0, sticky='nsew')
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')
input_frame = Frame(root)
input_frame.grid(row=0, column=0, sticky='nsew')

for frame in (main_page, main_frame, input_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# main page
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)

pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold',
                   command=lambda: frame_1(input_frame))
pesan_btm.place(x=250, y=450, anchor='center')


# frame 1
Label(main_frame, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(main_frame, text='Selamat Datang di Soetta-Loka\nMasukkan data diri anda!',
                  bg='black', fg='#8cc53d', font='Helvetica 15 bold')
top_label.grid(row=0, column=1, sticky='nsew')

label_nama = Label(main_frame, text='Nama', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=1, column=0, sticky='w')
label_ttl = Label(main_frame, text='TTL', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=2, column=0, sticky='w')
label_noktp = Label(main_frame, text='No. KTP', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=3, column=0, sticky='w')
label_anggota = Label(main_frame, text='No. Keanggotaan', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=4, column=0, sticky='w')

input_nama = Entry(main_frame, width=40, borderwidth=3, fg='#8cc53d', bg='black', font='Helvetica 10')
input_ttl = Entry(main_frame, width=40, borderwidth=3, fg='#8cc53d', bg='black', font='Helvetica 10')
input_noktp = Entry(main_frame, width=40, borderwidth=3, fg='#8cc53d', bg='black', font='Helvetica 10')
input_anggota = Entry(main_frame, width=40, borderwidth=3, fg='#8cc53d', bg='black', font='Helvetica 10')
input_nama.grid(row=1, column=1, columnspan=3)
input_ttl.grid(row=2, column=1, columnspan=3)
input_noktp.grid(row=3, column=1, columnspan=3)
input_anggota.grid(row=4, column=1, columnspan=3)


def cek_data1():
    Label(main_frame, text='Data Diri', font='Helvetica 13 bold', fg='#8cc53d', bg='black').place(x=240, y=175)

    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Nama').place(x=0, y=200)
    Label(main_frame, text=': ' + input_nama.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=200)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='TTL').place(x=0, y=227)
    Label(main_frame, text=': ' + input_ttl.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=227)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='No. KTP').place(x=0, y=252)
    Label(main_frame, text=': ' + input_noktp.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=252)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='No. Keanggotaan').place(x=0, y=277)
    Label(main_frame, text=': ' + input_anggota.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=277)
#    tombol2 = Button(main_frame, text='Input', width=10, command=lambda: frame_1(main_frame)).place(x=120, y=305)


tombol1 = Button(main_frame, text='Cek Data', width=10, command=cek_data1).place(x=120, y=150)


# frame 2, input frame
Label(input_frame, text='On-Booking Site', font='Helvetica 15 bold').place(x=170, y=5)
jenis_label = Label(input_frame, text='Jenis Penerbangan').place(x=0, y=50)
tujuan_label = Label(input_frame, text='Tujuan').place(x=0, y=75)
asal_label = Label(input_frame, text='Waktu keberangkatan').place(x=0, y=100)
maskapai_label = Label(input_frame, text='Maskapai').place(x=0, y=125)
waktu_label = Label(input_frame, text='Kelas penerbangan').place(x=0, y=150)

n = StringVar()
m = StringVar()

jenis_input = ttk.Combobox(input_frame, width=37, textvariable=n)
jenis_input['values'] = ('Domestik',
                         'Non-domestik')
jenis_input['state'] = 'readonly'
maskapai_input = Entry(input_frame, width=40, borderwidth=3)
asal_input = Entry(input_frame, width=40, borderwidth=3)
tujuan_input = ttk.Combobox(input_frame, width=37, textvariable=m)
tujuan_input['state'] = 'readonly'
waktu_input = Entry(input_frame, width=40, borderwidth=3)
jenis_input.place(x=140, y=50)
tujuan_input.place(x=140, y=75)
asal_input.place(x=140, y=100)
maskapai_input.place(x=140, y=125)
waktu_input.place(x=140, y=150)

Button(input_frame, text='Next', width=10, command=lambda: frame_1(main_frame)).place(x=140, y=175)


frame_1(main_page)
root.mainloop()
