# import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from templates.data_content.quiz_data import quiz_data

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x750")
        self.style = Style(theme='flatly')

        self.setup_ui()
        self.current_question = 0
        self.score = 0
        self.show_question()

        self.style.configure('TLabel', font=('Helvetica', 20))
        self.style.configure('TButton', font=('Helvetica', 16))

    def setup_ui(self):
        self.qs_label = ttk.Label(
            self.root,
            anchor='center',
            wraplength=500,
            padding=50
        )
        self.qs_label.pack(pady=10)

        self.choice_btn = []
        for i in range(4):
            button = ttk.Button(
                self.root,
                command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5)
            self.choice_btn.append(button)

        self.feedback_label = ttk.Label(
            self.root,
            anchor='center',
            padding=10
        )
        self.feedback_label.pack(pady=10)

        self.score_label = ttk.Label(
            self.root,
            text='Score: 0/{}'.format(len(quiz_data)),
            anchor='center',
            padding=10
        )
        self.score_label.pack(pady=10)

        self.next_button = ttk.Button(
            self.root,
            text='Next',
            command=self.next_question,
            state='disabled'
        )
        self.next_button.pack(pady=10)

    def show_question(self):
        question = quiz_data[self.current_question]
        self.qs_label.config(text=question["question"])

        #  Mostramos las eleciones que se pueden selcionar
        choices = question["choices"]
        for i in range(4):
            self.choice_btn[i].config(text=choices[i], state='normal') # reseteamos el boton
        # Limpiamos los label y display de los botones
        self.feedback_label.config(text="")
        self.next_button.config(state="display")

    def check_answer(self, choice):
        question = quiz_data[self.current_question]
        selected_choice = self.choice_btn[choice].cget("text")

        if selected_choice == question['answer']:
            global score
            self.score +=1
            self.score_label.config(text='Score: {}/{}'.format(self.score, len(quiz_data)))
            self.feedback_label.config(text='Correct!', foreground='Green')
        else:
            self.feedback_label.config(text='Not Correct!', foreground='Red')
        #   Desactivamos los botones con las opciones y ponemos visible el next
        for button in self.choice_btn:
            button.config(state='disabled')
        self.next_button.config(state='normal')

    def next_question(self):
        global current_question
        self.current_question +=1

        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(self.score, len(quiz_data)))
            self.root.destroy()

# import tkinter as tk
#
#
# from tkinter import messagebox, ttk
# from ttkbootstrap import Style
# from templates.data_content.quiz_data import quiz_data
#
# root = tk.Tk()
# root.title("quiz app")
# root.geometry("600x700")
# style = Style(theme='flatly')
#
# # Confuguracion de texto y las perguntas en el Label
# style.configure('TLabel', font=('Helvetica', 20))
# style.configure('TButton', font=('Helvetica', 16))
#
# def show_question():
#     # obtener las preguntas de la quiz_data - la lista
#     question = quiz_data[current_question]
#     qs_label.config(text=question["question"])
#
#     #  Mostramos las eleciones que se pueden selcionar
#     choices = question["choices"]
#     for i in range(4):
#         choice_btn[i].config(text=choices[i], state='normal') # reseteamos el boton
#     # Limpiamos los label y display de los botones
#     feedback_label.config(text="")
#     next_button.config(state="display")
#
# # Comprobamos la respuesta selecionada
# def check_answer(choice):
#     question = quiz_data[current_question]
#     selected_choice = choice_btn[choice].cget("text")
#
#     if selected_choice == question['answer']:
#         global score
#         score +=1
#         score_label.config(text='Score: {}/{}'.format(score, len(quiz_data)))
#         feedback_label.config(text='Correct!', foreground='Green')
#     else:
#         feedback_label.config(text='Not Correct!', foreground='Red')
# #   Desactivamos los botones con las opciones y ponemos visible el next
#     for button in choice_btn:
#         button.config(state='disabled')
#     next_button.config(state='normal')
#
# # Funcion que nos llevara a la siguente pregunta
# def next_question():
#     global current_question
#     current_question +=1
#
#     if current_question < len(quiz_data):
#         show_question()
#     else:
#         messagebox.showinfo("Quiz Completed",
#                             "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
#         root.destroy()
#
# qs_label = ttk.Label(
#     root,
#     anchor='center',
#     wraplength=500,
#     padding=50
# )
# qs_label.pack(pady=10)
#
# choice_btn = []
# for i in range(4):
#     button = ttk.Button(
#         root,
#         command=lambda  i=i: check_answer(i)
#     )
#     button.pack(pady=5)
#     choice_btn.append(button)
#
# feedback_label = ttk.Label(
#     root,
#     anchor='center',
#     padding=10
# )
# feedback_label.pack(pady=10)
#
# # inicializamos la puntuacion
#
# score = 0
#
# score_label = ttk.Label(
#     root,
#     text='Score: 0/{}'.format(len(quiz_data)),
#     anchor='center',
#     padding=10
# )
# score_label.pack(pady=10)
#
# next_button = ttk.Button(
#     root,
#     text='Next',
#     command=next_question,
#     state='disabled'
# )
# next_button.pack(pady=10)
#
# current_question = 0
# show_question()
#
# root.mainloop()
