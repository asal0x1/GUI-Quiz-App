from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.background = self.window.config(pady=20, padx=20, bg= THEME_COLOR)

        self.score_board = Label(text= f"Score: 0",
                                 fg= "white",
                                 highlightthickness=0,
                                 font= ("Arial", 10, "bold"),
                                 bg= THEME_COLOR)
        self.score_board.grid(column= 2, row= 1)

        self.canvas = Canvas(width= 300, height= 250, highlightthickness=0)
        self.canvas.grid(column= 1, row= 2, columnspan=2, pady= 50)

        self.true = PhotoImage(file="true.png")
        self.t_button = Button(image= self.true, highlightthickness=0, bg= THEME_COLOR, command= self.true_pressed)
        self.t_button.grid(row= 3, column= 1)
        self.t_button.config(pady=40, padx=40)

        self.false = PhotoImage(file="false.png")
        self.f_button = Button(image= self.false, highlightthickness=0, bg= THEME_COLOR, command= self.false_pressed)
        self.f_button.grid(row= 3, column= 2)
        self.f_button.config(pady=40, padx=40)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text= "",
                                                     font= ("Arial", 20, "italic"),
                                                     width = 280,
                                                     )
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_board.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end!")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






