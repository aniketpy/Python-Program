import tkinter as tk
import os,sys
import shutil

def open_file():
    global text
    main=tk.Tk()
    main.geometry("300x100")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)

    butt=tk.Button(main,text="Open File", command=open_main)
    butt.grid(row=3,column=2,padx=12,pady=5)

    main.mainloop()

def open_main():
    global text
    path=text.get()
    try:
        os.startfile(path)
        text.delete("0","end")
    except:
        text.delete("0","end")
        text.insert("end","File not Found.")

def check_file():
    global text
    main=tk.Tk()
    main.geometry("300x100")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)

    butt=tk.Button(main,text="Check File", command=check_file_main)
    butt.grid(row=3,column=2,padx=12,pady=5)

    main.mainloop()

def check_file_main():
    global text
    path=text.get()
    if os.path.isfile(path):
        text.delete("0","end")
        text.insert("end","File Exits")
    else:
        text.delete("0","end")
        text.insert("end","File does not Exits")

def check_folder():
    global text
    main=tk.Tk()
    main.geometry("300x100")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)

    butt=tk.Button(main,text="Check Folder", command=check_folder_main)
    butt.grid(row=3,column=2,padx=12,pady=5)

    main.mainloop()

def check_folder_main():
    global text
    path=text.get()
    if os.path.isdir(path):
        text.delete("0","end")
        text.insert("end","Folder Exits")
    else:
        text.delete("0","end")
        text.insert("end","Folder does not Exits")

def delete_file():
    global text
    main=tk.Tk()
    main.geometry("300x100")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)

    butt=tk.Button(main,text="Delete", command=delete_main)
    butt.grid(row=3,column=2,padx=12,pady=5)

    main.mainloop()

def delete_main():
    global text
    path=text.get()
    text.delete("0","end")
    try:
        os.remove(path)
        text.insert("0","File Deleted")
    except:
        text.insert("0","File not Found")

def list_file():
    global text,msgs
    main=tk.Tk()
    main.geometry("320x470")

    label=tk.Label(main,text="Enter Folder Path")
    label.grid(row=1,column=1,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=1,padx=12,pady=5)

    butt=tk.Button(main,text="List File", command=list_file_main)
    butt.grid(row=3,column=1,padx=12,pady=5)

    sc = tk.Scrollbar(main)
    sc1 = tk.Scrollbar(main, orient="horizontal")

    msgs = tk.Listbox(main,yscrollcommand=sc.set,xscrollcommand=sc1.set)
    msgs.grid(row=4,column=1,padx=12,pady=5,ipadx=75,ipady=80)

    sc.grid(row=4, column=2,sticky='ns')
    sc1.grid(row=6, column=1,sticky='ew')
    sc.config(command=msgs.yview)
    sc1.config(command=msgs.xview)
    
    main.mainloop()

def list_file_main():
    global text,msgs
    path=text.get()
    try:
        a=os.listdir(path)
        for i in a:
            msgs.insert("end",f" {i}")
    except:
        text.delete("0","end")
        text.insert("end","Folder not Found")

def rename_file():
    global text,text1
    main=tk.Tk()
    main.geometry("300x300")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)
    
    label=tk.Label(main,text="Enter Name")
    label.grid(row=3,column=2,padx=12,pady=5)

    text1=tk.Entry(main,width=45)
    text1.grid(row=4,column=2,padx=12,pady=1)

    butt=tk.Button(main,text="Rename", command=rename_file_main)
    butt.grid(row=5,column=2,padx=12,pady=5)

    main.mainloop()

def rename_file_main():
    global text,text1
    path=text.get()
    dest=text1.get()
    dest=f"{os.path.dirname(path)}\{dest}"
    if os.path.isfile(path): 
        os.rename(path,dest)
        text.delete("0","end")
        text.insert("0","File Renamed")
        text1.delete("0","end")
        text1.insert("0","File Renamed")
    else:
        text.delete("0","end")
        text.insert("0","File not Found")

def move_file():
    global text,text1
    main=tk.Tk()
    main.geometry("300x300")

    label=tk.Label(main,text="Enter Source of file")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)
    
    label=tk.Label(main,text="Enter Destination")
    label.grid(row=3,column=2,padx=12,pady=5)

    text1=tk.Entry(main,width=45)
    text1.grid(row=4,column=2,padx=12,pady=1)

    butt=tk.Button(main,text="Move File", command=move_file_main)
    butt.grid(row=5,column=2,padx=12,pady=5)

    main.mainloop()

def move_file_main():
    global text,text1
    source=text.get()
    dest=text1.get()
    a=os.path.isfile(source)
    b=os.path.isdir(dest)
    if a==False and b==True:
        text.delete("0","end")
        text1.delete("0","end")
        text.insert("0","Source File Missing")    
        text1.insert("0","Source File Missing")    
    elif a==True and b==False:
        text.delete("0","end")
        text.insert("0","Destination Folder Missing")
        text1.delete("0","end")
        text1.insert("0","Destination Folder Missing")
    elif os.path.isfile(f"{dest}\{os.path.basename(source)}"):
        text.delete("0","end")
        text1.delete("0","end")
        text.insert("0","File already exist in destination folder")
        text1.insert("0","File already exist in destination folder")
    elif a==True and b==True:
        shutil.move(source,dest)
        text.delete("0","end")
        text.insert("0","File Moved")
        text1.delete("0","end")
        text1.insert("0","File Moved")
    else:
        text.delete("0","end")
        text.insert("0","Error Occur")
        text1.delete("0","end")
        text1.insert("0","Error Occur")

def copy_file():
    global text,text1
    main=tk.Tk()
    main.geometry("300x300")

    label=tk.Label(main,text="Enter Source of file")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)
    
    label=tk.Label(main,text="Enter Destination")
    label.grid(row=3,column=2,padx=12,pady=5)

    text1=tk.Entry(main,width=45)
    text1.grid(row=4,column=2,padx=12,pady=1)

    butt=tk.Button(main,text="Copy File", command=copy_file_main)
    butt.grid(row=5,column=2,padx=12,pady=5)

    main.mainloop()

def copy_file_main():
    global text,text1
    source=text.get()
    dest=text1.get()
    a=os.path.isfile(source)
    b=os.path.isdir(dest)
    if a==False and b==True:
        text.delete("0","end")
        text1.delete("0","end")
        text.insert("0","Source File Missing")    
        text1.insert("0","Source File Missing")    
    elif a==True and b==False:
        text.delete("0","end")
        text.insert("0","Destination Folder Missing")
        text1.delete("0","end")
        text1.insert("0","Destination Folder Missing")
    elif os.path.isfile(f"{dest}\{os.path.basename(source)}"):
        text.delete("0","end")
        text1.delete("0","end")
        text.insert("0","File already exist in destination folder")
        text1.insert("0","File already exist in destination folder")
    elif a==True and b==True:
        shutil.copyfile(source,dest)
        text.delete("0","end")
        text.insert("0","File Moved")
        text1.delete("0","end")
        text1.insert("0","File Moved") 
    else:
        text.delete("0","end")
        text.insert("0","Error Occur")
        text1.delete("0","end")
        text1.insert("0","Error Occur")

def create_folder():
    global text,text1
    main=tk.Tk()
    main.geometry("300x300")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)
    
    label=tk.Label(main,text="Enter Folder Name")
    label.grid(row=3,column=2,padx=12,pady=5)

    text1=tk.Entry(main,width=45)
    text1.grid(row=4,column=2,padx=12,pady=1)

    butt=tk.Button(main,text="Create Folder", command=create_folder_main)
    butt.grid(row=5,column=2,padx=12,pady=5)

    main.mainloop()

def create_folder_main():
    global text,text1
    source=text.get()
    dest=text1.get()
    a=os.path.isdir(source)
    # b=os.path.isdir(dest)
    if a==False:
        text.delete("0","end")
        text1.delete("0","end")
        text.insert("0","Source File Missing")    
        text1.insert("0","Source File Missing")
    elif a==True:
        if os.path.isdir(f"{source}\{dest}"):
            text.delete("0","end")
            text1.delete("0","end")
            text.insert("0","Folder already exits")    
            text1.insert("0","Folder already exits")
        else:
            os.mkdir(f"{source}\{dest}")
            text.delete("0","end")
            text1.delete("0","end")
            text.insert("0","Folder Created")    
            text1.insert("0","Folder Created")

def remove_folder():
    global text,text1
    main=tk.Tk()
    main.geometry("300x300")

    label=tk.Label(main,text="Enter Path")
    label.grid(row=1,column=2,padx=12,pady=5)

    text=tk.Entry(main,width=45)
    text.grid(row=2,column=2,padx=12,pady=5)

    butt=tk.Button(main,text="Delete Folder", command=remove_folder_main)
    butt.grid(row=5,column=2,padx=12,pady=5)

    main.mainloop()

def remove_folder_main():
    path=text.get()
    a=os.path.isdir(path)
    if a==False:
        text.delete("0","end")
        text.insert("0","Folderr Missing")
    else:
        shutil.rmtree(path) 
        text.delete("0","end")
        text.insert("0","Folder Deleted")


root = tk.Tk()
root.geometry("500x500")
label=tk.Label(root, text="File Manager", fg="Black", font=("Arial Bold",30),bd=20).pack()
b1=tk.Button(root, text="Open File", bg="SteelBlue1", command=open_file).place(x=15, y=80, width=150, height=50)
b2=tk.Button(root, text="Check File", bg="Dodgerblue1", command=check_file).place(x=15, y=150, width=150, height=50)
b3=tk.Button(root, text="Check Folder", bg="Dodgerblue2", command=check_folder).place(x=15, y=221, width=150, height=50)
b4=tk.Button(root, text="Delete File", bg="Dodgerblue3", command=delete_file).place(x=15, y=290, width=150, height=50)
b5=tk.Button(root, text="List File", bg="Dodgerblue4", command=list_file).place(x=15, y=360, width=150, height=50)
b6=tk.Button(root, text="Rename File", bg="SteelBlue1", command=rename_file).place(x=330, y=80, width=150, height=50)
b7=tk.Button(root, text="Move File", bg="Dodgerblue1", command=move_file).place(x=330, y=150, width=150, height=50)
b8=tk.Button(root, text="Copy File", bg="Dodgerblue2", command=copy_file).place(x=330, y=220, width=150, height=50)
b9=tk.Button(root, text="Create Folder", bg="Dodgerblue3", command=create_folder).place(x=330, y=290, width=150, height=50)
b10=tk.Button(root, text="Remove Folder", bg="Dodgerblue4", command=remove_folder).place(x=330, y=360, width=150, height=50)
root.mainloop()     

