import tkinter as tk
from tkinter import messagebox

QUESTIONS = [
    {"q":"Which keyword defines a function in Python?","o":["class","def","return","import"],"a":"def"},
    {"q":"2 + 5 = ?","o":["5","6","7","8"],"a":"7"},
    {"q":"Which data type is mutable?","o":["tuple","list","str","int"],"a":"list"},
    {"q":"HTML stands for?","o":["Hyper Text Markup Language","High Text Machine Language","Hyper Tool ML","None"],"a":"Hyper Text Markup Language"},
    {"q":"Python is?","o":["Compiler","Interpreter","Browser","OS"],"a":"Interpreter"},
    {"q":"Largest planet?","o":["Mars","Earth","Jupiter","Venus"],"a":"Jupiter"},
    {"q":"5*6=?","o":["30","25","20","35"],"a":"30"},
    {"q":"Which loop repeats while condition is True?","o": ["for","while","if","def"],"a":"while"},
    {"q":"Capital of India?","o":["Delhi","Mumbai","Lucknow","Kolkata"],"a":"Delhi"},
    {"q":"File extension of Python?","o":[".java",".py",".cpp",".html"],"a":".py"},
]

class Quiz:
    def __init__(self,root):
        self.root=root
        self.root.title("Smart Quiz Platform")
        self.root.geometry("700x450")
        self.score=0
        self.i=0
        self.name=tk.StringVar()
        self.ans=tk.StringVar()

        tk.Label(root,text="SMART QUIZ PLATFORM",font=("Arial",20,"bold")).pack(pady=10)
        tk.Label(root,text="Enter Your Name").pack()
        tk.Entry(root,textvariable=self.name).pack()

        self.start=tk.Button(root,text="Start Quiz",command=self.start_quiz,bg="green",fg="white")
        self.start.pack(pady=10)

        self.frame=tk.Frame(root)

    def start_quiz(self):
        if not self.name.get().strip():
            messagebox.showwarning("Name","Enter your name")
            return
        self.start.pack_forget()
        self.frame.pack(fill="both",expand=True,padx=20,pady=20)
        self.show()

    def show(self):
        for w in self.frame.winfo_children():
            w.destroy()
        if self.i>=len(QUESTIONS):
            percent=self.score/len(QUESTIONS)*100
            msg=f"Congratulations {self.name.get()}!\n\nScore: {self.score}/{len(QUESTIONS)}\nPercentage: {percent:.0f}%"
            tk.Label(self.frame,text=msg,font=("Arial",16)).pack(pady=20)
            tk.Button(self.frame,text="Play Again",command=self.restart).pack(pady=5)
            tk.Button(self.frame,text="Exit",command=self.root.destroy).pack()
            return

        q=QUESTIONS[self.i]
        self.ans.set("")
        tk.Label(self.frame,text=f"Question {self.i+1}/{len(QUESTIONS)}",font=("Arial",14,"bold")).pack(anchor="w")
        tk.Label(self.frame,text=q["q"],font=("Arial",13),wraplength=650).pack(anchor="w",pady=10)
        for opt in q["o"]:
            tk.Radiobutton(self.frame,text=opt,variable=self.ans,value=opt,font=("Arial",12)).pack(anchor="w")
        tk.Button(self.frame,text="Next",bg="blue",fg="white",command=self.next_q).pack(pady=15)
        tk.Label(self.frame,text=f"Current Score: {self.score}").pack()

    def next_q(self):
        if self.ans.get()=="":
            messagebox.showwarning("Answer","Select an option")
            return
        if self.ans.get()==QUESTIONS[self.i]["a"]:
            self.score+=1
        self.i+=1
        self.show()

    def restart(self):
        self.score=0
        self.i=0
        self.show()

root=tk.Tk()
Quiz(root)
root.mainloop()