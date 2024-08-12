from tkinter import*
from tkinter import ttk

class todo:
    def __int__(self,root):
        self.root.title('to-do-list')
        self.root.geometry('560*310+150+75')
        self.label=Label(self.root,text='to-do-list-app',
        font='ariel,25 bold',width=10,bd=5,bg='blue',fg='red')
        self.label2=Label(self.root,text='add task',
        font='ariel,18 bold',width=15,bd=10,bg='black',fg=red)
        self.label2.place(x=50,y=64)
        self.label3.label(self.root,text='tasks',font='ariel,18 bolg',wieth=10,bd=5,bg=blue,bf=red)
        self.main_text.place(x=380,y=100)
        self.main_text=listbox(self.root,heigth=3,bd=6,width=33,font='ariel,20,italie')
        self.main_text=place(x=260,y=100)
        self.text=text(self.root,bd=5,heigth=3,width=30,font='ariel,10 bold')
        self.text.place(x=2,y=120)
    def add():
        content=self.get(1.0,END)
        self.main_text.insert(END,content)
        with open('data.txt','a') as file:
            file.write(content)
            file.sect(0)
            file.close()
            self.text,detele(1.0,END)
            def update():
                update_=self.main_text.curselection()
                look=self.main_text.get(update_)
                with open('data.txt','d-') as f:
                    new_f=f.readlines()
                    f.seck(0)
                    for line in new_f:
                        itme=str(look)
                if item in line:
                    f.write(line)
                f.truncate() 
            self.main_text.update(update_)
            def delete():
                delete_=self.main_text.curselection()
                look=self.main_text.get(delete_)
                with open('data.txt','d-') as f:
                    new_f=f.readlines()
                    f.seck(0)
                    for line in new_f:
                        itme=str(look)
                if item in line:
                    f.write(line)
                f.truncate() 
            self.main_text.delete(delete_)
            with open('data.txt','f')as file:
                readfile.readlines()
                for i in read:
                    ready=i.split()
                    self.main_text.insert(END,ready)
                    file.close()
                    self.button=button(self.root,text='add',font='saruf,30 bild italic',commond=add)
                    self.button,plase(x=30,y=280)
                    self.button=button(self.root,text='update',font='saruf,30 bild italic',commond=update)
                    self.button,plase(x=30,y=280)
                    self.button=button(self.root,text='delete',font='saruf,30 bild italic',commond=delete)
                    self.button,plase(x=30,y=280)
            def main():
                root=tk()
                ui=todolist(root)
                root.mainloop()
                if __name__=='__main__':
                    main() 