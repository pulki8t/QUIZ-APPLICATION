from tkinter import *
import requests
from random import shuffle
import html
from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface




def display_title():
    title= Label(main_window, text= "Quizairre - Quiz Application", width=50, bg="purple", fg="white", font=("aerial", 20, "bold")).grid(row=0, column=2)
    sub_title= Label(main_window, text= "Evaluate Yourself and Learn More", width=50, bg="blue", fg="white", font=("aerial", 16, "bold")).grid(row=1, column=2)
main_window= Tk()
main_window.title("Quizairre- Quiz Application")
main_window.geometry("850x530")
display_title()
name= Label(main_window, text= "Enter Your Name", width=30, fg="white", bg= "brown", font=("aerial", 14)).grid(row=2, column=2)
sub= Label(main_window, text= "Select The Subject", width=30, fg="white", bg= "brown", font=("aerial", 14)).grid(row=4, column=2)
diff= Label(main_window, text= "Select The Difficulty", width=30, fg="white", bg= "brown", font=("aerial", 14)).grid(row=6, column=2)
num= Label(main_window, text= "Select Number of Questions", width=30, fg="white", bg= "brown", font=("aerial", 14)).grid(row=8, column=2)


sub_opt= ["General Knowledge", "Sports", "History", "Politics", "Geography", "Art",
          "Animals", "Vehicles", "Science; Gadgets", "Science: Mathematics",
          "Science: Computers", "Science & Nature"]
diff_opt= ["easy", "medium", "hard"]
num_opt= ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50"]
sub_dict= {"General Knowledge": "9", "Sports": "21", "History": "23", "Politics": "24", "Geography": "22", "Art": "25",
          "Animals": "27", "Vehicles": "28", "Science: Gadgets": "30", "Science: Mathematics": "19",
          "Science: Computers": "18", "Science & Nature": "17"}


sub_type= StringVar()
diff_type= StringVar()
num_type= StringVar()
sub_type.set("Select Any")
diff_type.set("Select Any")
num_type.set("Select Any")


sub_menu= OptionMenu(main_window, sub_type, *sub_opt,).grid(row= 5, column= 2)
diff_menu= OptionMenu(main_window, diff_type, *diff_opt).grid(row= 7, column= 2)
num_menu= OptionMenu(main_window, num_type, *num_opt).grid(row= 9, column= 2)
name_in=StringVar()


name_var= Entry(main_window, textvariable=name_in, width=30, borderwidth=5).grid(row=3, column=2)

name=[]

question_data=[]

def start():
    parameters = {
        "amount": num_type.get(),
        "type": "multiple",
        "category": sub_dict[sub_type.get()],
        "difficulty": diff_type.get()
    }
    response= requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data.extend(response.json()["results"])
    name.extend(name_in.get())
    main_window.destroy()
begin= Button(main_window, text="Enter the Quiz", padx= 50, borderwidth=2, fg="blue", bg= "green", font=("aerial", 16, "bold"), command=start).grid(row=10, column=2)


main_window.mainloop()
