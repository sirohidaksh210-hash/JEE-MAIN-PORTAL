import tkinter as tk
from tkinter import simpledialog, messagebox
import builtins
from random import *

window = tk.Tk()
window.title("JEE Main Simulator Pro")
window.geometry("900x700")
window.configure(bg="#1E293B") 

header = tk.Label(window, text="🎓 JEE Main Result Simulator", font=("Segoe UI", 26, "bold"), bg="#1E293B", fg="#38BDF8")
header.pack(pady=20)

output_screen = tk.Text(window, font=("Consolas", 12), bg="#0F172A", fg="#F8FAFC", wrap=tk.WORD, bd=0, padx=20, pady=20)
output_screen.pack(expand=True, fill='both', padx=40, pady=10)

output_screen.tag_config("info", foreground="#38BDF8")
output_screen.tag_config("success", foreground="#10B981") 
output_screen.tag_config("warning", foreground="#F59E0B") 
output_screen.tag_config("error", foreground="#EF4444")   
output_screen.tag_config("celebrate", foreground="#F0ABFC", font=("Consolas", 14, "bold")) 

def gui_print(*args, color="info", **kwargs):
    text = " ".join(map(str, args)) + kwargs.get("end", "\n")
    output_screen.insert(tk.END, text, color)
    output_screen.see(tk.END)
    window.update()

def gui_input(prompt=""):
    gui_print(prompt, end="", color="warning") 
    
    while True:
        user_answer = simpledialog.askstring("Input Needed", prompt, parent=window)
        
        # 1. Check for blank input or cancel
        if user_answer is None or user_answer.strip() == "":
            messagebox.showerror("Input Error", "This detail is required. Please enter a value.")
            continue
            
        user_answer = user_answer.strip()

        # 2. Context-Specific Validations based on the prompt keywords
        prompt_upper = prompt.upper()
        
        if "APPLICATION NO" in prompt_upper:
            if not user_answer.isdigit():
                messagebox.showerror("Validation Error", "Application Number must contain ONLY numbers. No letters or spaces allowed.")
                continue
                
        elif "DOB" in prompt_upper or "DATE" in prompt_upper:
            
            if len(user_answer) < 8 or not any(char.isdigit() for char in user_answer):
                messagebox.showerror("Validation Error", "Please enter a valid date format (e.g., DD/MM/YYYY).")
                continue
                
        elif "CATEGORY" in prompt_upper:
            valid_categories = ['GENERAL', 'OBC', 'SC', 'ST', 'PWD']
            if user_answer.upper() not in valid_categories:
                messagebox.showerror("Validation Error", f"Invalid Category. Please enter one of: {', '.join(valid_categories)}")
                continue

        
        gui_print(user_answer, color="success") 
        return user_answer

builtins.print = gui_print
builtins.input = gui_input

class JEE_MAIN:
    NO_OF_REGISTRATION = randint(1500000, 1600000)

    def __init__(self, no_of_shifts):
        self.no_of_shifts = no_of_shifts

    def abd(self, total_marks, subjects):
        self.total_marks = total_marks
        self.subjects = subjects
        print(f'THE TOTAL NO. OF FORM FILLED IS {self.NO_OF_REGISTRATION} AND THE TOTAL NO. OF SHIFTS ARE {self.no_of_shifts}.')
        print(f'THE TOTAL NO. OF STUDENTS WHO GAVE THE JEE MAIN EXAM IS {randint(1400000, 1500000)}.')
        print(f'THIS EXAM IS OF {self.total_marks} AND THE QUESTIONS ARE ASKED FROM {self.subjects}.')

class result(JEE_MAIN):
    def __init__(self, no_of_shifts):
        super().__init__(no_of_shifts)
        self.physics_marks = randint(-20, 100)
        self.chemistry_marks = randint(-20, 100)
        self.maths_marks = randint(-20, 100)
        self.get_marks = self.physics_marks + self.chemistry_marks + self.maths_marks

    def details(self, name, application_no, date_of_birth):
        self.name = name
        self.application_no = application_no
        self.date_of_birth = date_of_birth
    
    def session(self, month_attempt):
        self.month_attempt = month_attempt
        self.NO_OF_STUDENT_IN_EACH_SHIFT = int((self.NO_OF_REGISTRATION)//(self.no_of_shifts))
        print(f'YOU APPLIED FOR {self.month_attempt} ATTEMPT.')
        print(f'NO. OF STUDENTS PER SHIFT: {self.NO_OF_STUDENT_IN_EACH_SHIFT}')

    def status(self):
        gui_print(f'\n- SCORECARD -', color="warning")
        print(f'Physics: {self.physics_marks} | Chemistry: {self.chemistry_marks} | Maths: {self.maths_marks}')
        gui_print(f'YOU GOT {self.get_marks} OUT OF {self.total_marks}', color="success")

class qualification(result):
    def percentile(self):
        PERCENTILE = (self.get_marks / self.total_marks) * 100
        gui_print(f'THE PERCENTILE YOU GOT IS {abs(PERCENTILE):.2f}%', color="celebrate")
        
        category = input('ENTER THE CATEGORY (GENERAL/OBC/SC/ST/PWD): ').upper()
        qualified = False

        if category == 'GENERAL' and PERCENTILE >= 93.5: qualified = True
        elif category == 'OBC' and PERCENTILE >= 82.7: qualified = True
        elif (category == 'SC' or category == 'ST') and PERCENTILE >= 30: qualified = True
        elif category == 'PWD': 
            gui_print("🥳 CONGRATULATIONS,YOU QUALIFIED FOR JEE ADVANCED", color="celebrate")
            return

        if qualified:
            gui_print("\n✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ", color="celebrate")
            gui_print("CONGRATULATIONS! YOU QUALIFIED THIS EXAM!", color="celebrate")
            gui_print("✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ ", color="celebrate")
            gui_print("Time to prepare for JEE Advanced!", color="success")
        else:
            gui_print("\nSORRY, YOU DID NOT QUALIFY THIS TIME.", color="error")
            gui_print("Better luck next time. Don't give up!", color="info")


o1 = qualification(10)
o1.abd(300, ['PHYSICS', 'CHEMISTRY', 'MATHEMATICS'])

o1.details(input('ENTER YOUR NAME: '), 
           input('ENTER YOUR APPLICATION NO: '), 
           input('ENTER YOUR DOB (DD/MM/YYYY): '))

o1.session(input('ENTER YOUR EXAM MONTH: '))
o1.status()
o1.percentile()

gui_print("\n- Simulation Complete -", color="warning")
window.mainloop()