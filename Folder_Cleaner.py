import os,sys
import shutil
ptr=0

def rename(file,format):
    global ptr
    ptr+=1
    os.rename(file,f"{ptr}.{format}")
    return f"{ptr}.{format}"

def folder(fold):
    if not os.path.exists(fold):
        os.makedirs(fold)

def move(file,format,ren):
    # print(file,format)
    img=["png","jpeg","jpg","ico"]
    doc=["doc","docx","pdf","txt","xls","xlsx","ppt","pptx","html","htm"]
    med=["webm","mkv","flv","gif","avi","mov","wmv","mp4","mp3","svi","3gp",""]
    for i in img:
        if format==i:
            if "1" in ren:
                name=rename(file,format)
                shutil.move(f"{name}",f"1.Images")
            else:
                shutil.move(file,f"1.Images")
            break
        else:pass
    for i in doc:
        if format==i:
            if "2" in ren:
                name=rename(file,format)
                shutil.move(f"{name}",f"2.Documents")
            else:
                shutil.move(file,f"2.Documents")
            break
        else:pass
    for i in med:
        if format==i:
            if "3" in ren:
                name=rename(file,format)
                shutil.move(f"{name}",f"3.Media")
            else:
                shutil.move(file,f"3.Media")
            break
        else:pass
    if format not in img and format not in doc and format not in med:
        if "4" in ren:
            name=rename(file,format)
            shutil.move(f"{name}",f"4.Other Files")
        else:
            shutil.move(file,f"4.Other Files")

if __name__ == "__main__":
    # path=r"C:\Users\andyv\Desktop\MY FILE\Python\test"
    # rec=r"C:\Users\andyv\Desktop\MY FILE\Python\test\ani.txt"
    # ren=["1"]
    path=str(input("Enter the full path of folder: "))
    rec=str(input("Enter the full path of file: "))
    ren=(input("Enter the format you want to rename :\n1.Images\n2.Documents\n3.Media\n4.Other Files\n\t\t").split())
    path=rf"{path}"
    rec=rf"{rec}"
    os.chdir(path)
    folder("1.Images")
    folder("2.Documents")
    folder("3.Media")
    folder("4.Other Files")
    for j,i in enumerate(os.listdir()):
        if i!=os.path.basename(rec):
            f=open(rec,"r")
            content=f.readlines()
            # content=content.strip("\n")
            if f"{i}\n" not in content:
                a=os.path.isdir(i)
                if a==False:
                    format=i.split(".")
                    format=format[len(format)-1]

                    move(i,format,ren)
    print("Your Folder is cleaned")
    





