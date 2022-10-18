from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # self.quiz = QuizBrain()
        # self.current_question = self.quiz.current_question
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        # White Background
        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0, highlightbackground=THEME_COLOR)
        # self.canvas.create_text(150,125, text=self.current_question, font=FONT)
        self.canvas_text = self.canvas.create_text(150,125, width=280, text='Some Text Here as a placeholder', fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Score Label
        self.score_label = Label(text=f'Score: 0', highlightcolor=THEME_COLOR, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # Green Button
        self.green_image = PhotoImage(file='./images/true.png')
        self.green_button = Button(image=self.green_image, highlightthickness=0, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR, command=self.choosing_true)
        self.green_button.config(padx=20, pady=20)
        self.green_button.grid(row=2, column=0)
        # Red Button
        self.red_image = PhotoImage(file='./images/false.png')
        self.red_button = Button(image=self.red_image, highlightthickness=0, highlightbackground=THEME_COLOR, highlightcolor=THEME_COLOR, command=self.choosing_false)
        self.red_button.config(padx=20, pady=20)
        self.red_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='white')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        else:
            self.canvas.config(bg='white')
            self.green_button.config(state='disabled')
            self.red_button.config(state='disabled')
            self.canvas.itemconfig(self.canvas_text,
                                   text=f'You\'ve reached the end of the quiz!\nYour score is {self.quiz.score} / {self.quiz.question_number} ')

    def choosing_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
        # self.get_next_question()

    def choosing_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)











