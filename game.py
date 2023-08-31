# import tkinter as tk
# from tkinter import messagebox

# class QuizGameApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Quiz Game")

#         self.questions = [
#             {
#                 "question": "What is the capital of France?",
#                 "options": ["Paris", "Madrid", "Rome", "Berlin"],
#                 "correct_answer": "Paris"
#             },
#             {
#                 "question": "Who wrote 'Romeo and Juliet'?",
#                 "options": ["Mark Twain", "William Shakespeare", "Jane Austen", "Charles Dickens"],
#                 "correct_answer": "William Shakespeare"
#             }
#             # Add more questions here...
            
#         ]

#         self.question_index = 0
#         self.score = 0

#         self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
#         self.question_label.pack(pady=10)

#         self.option_buttons = []
#         for i in range(4):
#             button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
#             button.pack(pady=5)
#             self.option_buttons.append(button)

#         self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
#         self.feedback_label.pack(pady=10)

#         self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
#         self.next_button.pack()
#         self.next_button["state"] = "disabled"

#         self.load_question()

#     def load_question(self):
#         if self.question_index < len(self.questions):
#             question_data = self.questions[self.question_index]
#             self.question_label.config(text=question_data["question"])
#             for i, option in enumerate(question_data["options"]):
#                 self.option_buttons[i].config(text=option)
#             self.next_button["state"] = "disabled"
#         else:
#             self.show_final_results()

#     def check_answer(self, selected_index):
#         selected_option = self.questions[self.question_index]["options"][selected_index]
#         correct_answer = self.questions[self.question_index]["correct_answer"]

#         if selected_option == correct_answer:
#             self.score += 1
#             feedback = "Correct!"
#         else:
#             feedback = f"Incorrect. The correct answer is: {correct_answer}"

#         self.feedback_label.config(text=feedback)
#         self.next_button["state"] = "active"

#         for button in self.option_buttons:
#             button["state"] = "disabled"

#     def next_question(self):
#         self.question_index += 1
#         self.feedback_label.config(text="")
#         for button in self.option_buttons:
#             button["state"] = "active"
#         self.load_question()

#     def show_final_results(self):
#         messagebox.showinfo("Quiz Results", f"You scored {self.score}/{len(self.questions)}!")

# def main():
#     root = tk.Tk()
#     app = QuizGameApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()




Import tkinter as tk
from tkinter import messagebox

class QuizGameApp:
    def __init__(self, root):
        self.Root = root
        self.Root.Name("Quiz Game")

        self.Questions = [
            
                "query": "What is the capital of France?",
                "options": ["Paris", "Madrid", "Rome", "Berlin"],
                "correct_answer": "Paris"
            ,
            
                "query": "Who wrote 'Romeo and Juliet'?",
                "alternatives": ["Mark Twain", "William Shakespeare", "Jane Austen", "Charles Dickens"],
                "correct_answer": "William Shakespeare"
            
            # Add greater questions here...
            
        ]

        self.Question_index = 0
        self.Rating = zero

        self.Question_label = tk.Label(root, textual content="", font=("Helvetica", 14))
        self.Question_label.P.C.(pady=10)

        self.Option_buttons = []
        for i in variety(four):
            button = tk.Button(root, textual content="", command=lambda i=i: self.Check_answer(i))
            button.%(pady=5)
            self.Option_buttons.Append(button)

        self.Feedback_label = tk.Label(root, textual content="", font=("Helvetica", 12))
        self.Feedback_label.P.C.(pady=10)

        self.Next_button = tk.Button(root, textual content="Next Question", command=self.Next_question)
        self.Next_button.%()
        self.Next_button["state"] = "disabled"

        self.Load_question()

    def load_question(self):
        if self.Question_index < len(self.Questions):
            question_data = self.Questions[self.Question_index]
            self.Question_label.Config(textual content=question_data["question"])
            for i, alternative in enumerate(question_data["options"]):
                self.Option_buttons[i].Config(textual content=option)
            self.Next_button["state"] = "disabled"
        else:
            self.Show_final_results()

    def check_answer(self, selected_index):
        selected_option = self.Questions[self.Question_index]["options"][selected_index]
        correct_answer = self.Questions[self.Question_index]["correct_answer"]

        if selected_option == correct_answer:
            self.Rating += 1
            remarks = "Correct!"
        else:
            comments = f"Incorrect. The correct answer is: correct_answer"

        self.Feedback_label.Config(text=remarks)
        self.Next_button["state"] = "active"

        for button in self.Option_buttons:
            button["state"] = "disabled"

    def next_question(self):
        self.Question_index += 1
        self.Feedback_label.Config(textual content="")
        for button in self.Option_buttons:
            button["state"] = "lively"
        self.Load_question()

    def show_final_results(self):
        messagebox.Showinfo("Quiz Results", f"You scored self.Rating/len(self.Questions)!")

def fundamental():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.Mainloop()

if __name__ == "__main__":
    principal()