from tkinter import *
# we do this for the init, so we can get autocompleted methods and error checking by python
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Calibri"


class QuizUI:
    # notice how we define the type of quiz_brain so python knows what to do with it
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", font=(FONT, 10, "bold"), foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1, sticky="EW")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            fill="black",
            text="Question here",
            font=(FONT, 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0,
                                   command=lambda answer="False": self.check_chosen_answer(answer))
        self.false_button.grid(column=1, row=2)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0,
                                  command=lambda answer="True": self.check_chosen_answer(answer))
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    # get the question from quiz brain and update the ui with it
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That's the end of the quiz, thanks for playing!")
            self.true_button["state"] = DISABLED
            self.false_button["state"] = DISABLED

    def check_chosen_answer(self, user_choice):
        if self.quiz.check_answer(user_choice):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # print(user_choice)
        self.window.after(1000, self.get_next_question)
