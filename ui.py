from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):  # type hint: quizbrain parameter's datatype should be QuizBrain class
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)
        self.window.resizable(width=0, height=0)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("ariel", 20))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text((150, 125), text="", fill=THEME_COLOR, width=285, font=("ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, bg=THEME_COLOR, bd=0, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0,)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, bg=THEME_COLOR, bd=0, highlightthickness=0, command=self.wrong_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"you've reached the end of quiz.\nyour score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





