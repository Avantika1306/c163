from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Fever Report")
root.geometry("400x600")
q1_radioButton=StringVar(value="0")
q1=Label(root,text="Do you have headache and a sore throat?")
q1.pack()
q1_r1=Radiobutton(root,text="yes",variable=q1_radioButton,value="yes")
q1_r1.pack()
q1_r2=Radiobutton(root,text="no",variable=q1_radioButton,value="no")
q1_r2.pack()
q2_radioButton=StringVar(value="0")
q2=Label(root,text="Do You Have a high body temperature?")
q2.pack()
q2_r1=Radiobutton(root,text="yes",variable=q2_radioButton,value="yes")
q2_r1.pack()
q2_r2=Radiobutton(root,text="no",variable=q2_radioButton,value="no")
q2_r2.pack()
q3_radioButton=StringVar(value="0")
q3=Label(root,text="Are there any symptoms of eye redness?")
q3.pack()
q3_r2=Radiobutton(root,text="yes",variable=q3_radioButton,value="yes")
q3_r2.pack()
q3_r2=Radiobutton(root,text="no",variable=q3_radioButton,value="no")
q3_r2.pack()


def feverscore():
    score=0
    if q1_radioButton.get()=="yes":
        score=score+20 
        print(score)
    if q2_radioButton.get()=="yes":
        score=score+20
        print(score)
    if q3_radioButton.get()=="yes":
        score=score+20
        print(score)
    if score<=20:
        messagebox.showinfo("report","you dont need to visit the doctor!")
    elif score>20 and score<=40:
        messagebox.showinfo("report","you might perhaps have to visit the doctor")
    else:
        messagebox.showinfo("report","you have to visit the doctor")
button1=Button(root,text="click me",command=feverscore)
button1.pack()
root.mainloop()
