import tkinter as tk
import quiz_brain
import time



THEME_COLOR = "#375362"


class InterfaceUser():

    def __init__(self, quiz_br: quiz_brain.QuizBrain):
        self.quiz = quiz_br
        self.score_main = self.quiz.score
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        
        self.score = tk.Label(text="Score: 0",bg=THEME_COLOR, fg="white",highlightthickness=0)
        self.score.grid(column=1,row=0)

        self.can = tk.Canvas(width=300,height=300)
        self.question_text = self.can.create_text(150,150,text="Questions",font=('Arial',20,"italic"),fill=THEME_COLOR,width=300)
        self.can.grid(column=0,row=1,columnspan=2,pady=20)

        true_image = tk.PhotoImage(file="quiz_app_python/images/true.png")
        self.true_button = tk.Button(image=true_image,highlightthickness=0,command=self.check_true)
        self.true_button.grid(column=0,row=3)

        false_image = tk.PhotoImage(file="quiz_app_python/images/false.png")
        self.false_button = tk.Button(image=false_image,highlightthickness=0,command=self.check_false)
        self.false_button.grid(column=1,row=3)
        

        self.get_next_qestion()
        self.window.mainloop()

    def get_next_qestion(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.can.itemconfig(self.question_text, text=q_text)
            self.can.config(bg='white')
        else:
            self.can.itemconfig(self.question_text, text='we reached all question')
            self.can.config(bg='white')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def check_true(self):
        is_right = self.quiz.check_answer('true')    
        self.feedback(is_right)
    def check_false(self):
        is_right = self.quiz.check_answer('false')
        self.feedback(is_right)
    def feedback(self,n):
        if n:
            self.can.config(bg='green')
            self.score_main+=1
            self.score.config(text=f"Score: {self.score_main}")
        else:
            self.can.config(bg='red')
            
        self.window.after(1000,self.get_next_qestion)
        print(self.score_main)