from tkinter import *
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
import time

# get bet money
def get_bet_money():
    global bet_money
    bet_money = money_text_box.get(1.0, "end-1c")

    try:
        bet_money_int = int(bet_money)

        if bet_money_int <= 0 or bet_money_int > current_money:
            messagebox.showwarning("Lưu ý", "Số tiền cược không phù hợp!")
        else:
            money_bet_label.config(text='Số tiền cược: {}'.format(bet_money_int))
            return True
    except ValueError:
        messagebox.showwarning("Lưu ý", "Số tiền cược không phù hợp!")
        money_text_box.delete('1.0', END)


# get dice number
def get_number(x):
    if x == '\u2680':
        return 1
    elif x == '\u2681':
        return 2
    elif x == '\u2682':
        return 3
    elif x == '\u2683':
        return 4
    elif x == '\u2684':
        return 5
    elif x == '\u2685':
        return 6

# roll the dice
def first_start():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    d3 = random.choice(my_dice)
    
    # update labels
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    dice_label3.config(text=d3)
    # pre gen fig
    fig = Figure(figsize=(3,2.5), dpi=100)
    chart_canvas = FigureCanvasTkAgg(fig, master=my_frame)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().grid(row=3, column=0, rowspan=3, columnspan=5, padx=5, pady=10)

def plot(fig):
    if roll_count != 0:
        under_percent = under/roll_count*100
        over_percent = over/roll_count*100
    else:
        under_percent = 0
        over_percent = 0
    plot1 = fig.add_subplot(1,1,(1,2))
    plot1.bar(['% xỉu {}'.format(under), '% tài {}'.format(over)],[under_percent, over_percent], width=0.2 )
    # figure canvas for chart
    
    chart_canvas = FigureCanvasTkAgg(fig, master=my_frame)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().grid(row = 3, column=0, rowspan=2, columnspan=5, padx=5, pady=10)


def roll_dice_effect():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    d3 = random.choice(my_dice)
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    dice_label3.config(text=d3)


def roll_dice(result_text):
    global under, over, roll_count
    global double, triple
    global current_money, bet_money
    
    if get_bet_money():
        # d1 = random.choice(my_dice)
        # d2 = random.choice(my_dice)
        # d3 = random.choice(my_dice)

        # d1 = my_dice[1]
        # d2 = my_dice[1]
        # d3 = my_dice[0]
        d1 = random.choice(my_dice)
        d2 = random.choice(my_dice)
        d3 = random.choice(my_dice)
        # determine dice number
        sd1 = get_number(d1)
        sd2 = get_number(d2)
        sd3 = get_number(d3)
        # update labels
        dice_label1.config(text=d1)
        dice_label2.config(text=d2)
        dice_label3.config(text=d3)
        
        # update sub labels
        sub_label1.config(text=sd1)
        sub_label2.config(text=sd2)
        sub_label3.config(text=sd3)
        
        # update total label
        total = sd1 + sd2 + sd3
        if 4 <= total <= 10:
            if sd1 == sd2 and sd2 == sd3:
                triple += 1
                over_under_label.config(text="Xỉu + Ba")
                triple_count_label.config(text="Số lần ba: {}".format(triple))
            elif sd1 == sd2 or sd2 == sd3 or sd3 == sd1:
                double += 1
                over_under_label.config(text="Xỉu + Đôi")
                double_count_label.config(text="Số lần đôi: {}".format(double))
            else:
                over_under_label.config(text="Xỉu")
            under += 1
            roll_count += 1
        elif 11 <= total <= 17:
            
            if sd1 == sd2 and sd2 == sd3:
                triple += 1
                over_under_label.config(text="Tài + Ba")
                triple_count_label.config(text="Số lần ba: {}".format(triple))
            elif sd1 == sd2 or sd2 == sd3 or sd3 == sd1:
                double += 1
                over_under_label.config(text="Tài + Đôi")
                double_count_label.config(text="Số lần đôi: {}".format(double))
            else:
                over_under_label.config(text="Tài")
            over +=1
            roll_count+=1
        elif total == 3 or total == 18:
            triple += 1
            over_under_label.config(text="Ba")
            triple_count_label.config(text="Số lần ba: {}".format(triple))

        fig = Figure(figsize=(3,2.5), dpi=100)
        plot(fig)
        
        roll_count_label.config(text= "Số lần roll: {}".format(roll_count))
        
        # Result 
        if sd1 == sd2 == sd3 and result_text == "Ba":
            result_label.config(text="Bạn ăn ba!", fg='black')
            current_money += int(bet_money)*60
            current_money_label.config(text='Current money: {}'.format(current_money))
        elif (sd1 == sd2 == sd3 == 1 and result_text == "111") or (sd1 == sd2 == sd3 == 2 and result_text == "222") or (sd1 == sd2 == sd3 == 3 and result_text == "333") or (sd1 == sd2 == sd3 == 4 and result_text == "444") or (sd1 == sd2 == sd3 == 5 and result_text == "555") or (sd1 == sd2 == sd3 == 6 and result_text == "666"):
            result_label.config(text="Bạn ăn ba!", fg='black')
            current_money += int(bet_money)*180
            current_money_label.config(text='Current money: {}'.format(current_money))
        elif  (((sd1 == sd2 == 1  or sd2 == sd3 == 1 or sd3 == sd1 == 1) and result_text=='11') or ((sd1 == sd2 == 2  or sd2 == sd3 == 2 or sd3 == sd1 == 2) and result_text=='22') or ((sd1 == sd2 == 3  or sd2 == sd3 == 3 or sd3 == sd1 == 3) and result_text=='33') or ((sd1 == sd2 == 4  or sd2 == sd3 == 4 or sd3 == sd1 == 4) and result_text=='44') or ((sd1 == sd2 == 5  or sd2 == sd3 == 5 or sd3 == sd1 == 5) and result_text=='55') or ((sd1 == sd2 == 6  or sd2 == sd3 == 6 or sd3 == sd1 == 6) and result_text=='66')) and not (sd1 == sd2 == sd3):
            result_label.config(text="Bạn ăn đôi!", fg='magenta')
            current_money += int(bet_money)*11
            current_money_label.config(text='Current money: {}'.format(current_money))
        elif ((4 <= total <= 10) and result_text == "Xỉu") or ((11 <= total <= 17) and result_text == "Tài"):
            result_label.config(text="Bạn thắng!", fg='green')
            current_money += int(bet_money)
            current_money_label.config(text='Current money: {}'.format(current_money))
        else:
            result_label.config(text="Bạn thua!", fg='red')
            current_money -= int(bet_money)
            current_money_label.config(text='Current money: {}'.format(current_money))

###################################################################
root = Tk()
root.title('Roll to die')
root.geometry("600x900")
###################################################################
# GLOBAL VARIABLE
# over and under
over = 0
under = 0
double = 0
triple = 0
roll_count = 0
current_money = 1000000
bet_money = 0
# create a dice list
my_dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]

# ---------------------------------------------------------------
# FRAME 
# money - frame
money_frame = Frame(root, height=50)
money_frame.pack(pady=10)

# create a frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# --------------------------------------------------------------
# MONEY FRAME - LABEL
current_money_label = Label(money_frame, text='Current money: {}'.format(current_money), font=("Helvetica", 16), fg="green")
current_money_label.grid(row=0, column=0, padx=5)

# MY FRAME - LABEL
# create dice labels
dice_label1 = Label(my_frame, text='', font=("Helvetica", 120), fg="red")
dice_label1.grid(row=0, column=1, padx=5, columnspan=2)
sub_label1 = Label(my_frame, text='')
sub_label1.grid(row=1, column=1, padx=5, columnspan=2)

dice_label2 = Label(my_frame, text='', font=("Helvetica", 120), fg="blue")
dice_label2.grid(row=0, column=3, padx=5, columnspan=2)
sub_label2 = Label(my_frame, text='')
sub_label2.grid(row=1, column=3, padx=5, columnspan=2)

dice_label3 = Label(my_frame, text='', font=("Helvetica", 120), fg="green")
dice_label3.grid(row=0, column=4, padx=5, columnspan=3)
sub_label3 = Label(my_frame, text='')
sub_label3.grid(row=1, column=4, padx=5, columnspan=3)

# create total label
over_under_label = Label(my_frame, text='Thần điêu đại bịp', font=("Helvetica", 20), fg="grey")
over_under_label.grid(row=2, column=0, columnspan=7, pady=10)

# roll count
roll_count_label = Label(my_frame, text='Số lần roll: ', font=("Helvetica", 16), fg="grey")
roll_count_label.grid(row=3, column=5, padx=5)

# double count
double_count_label = Label(my_frame, text='Số lần đôi: ', font=("Helvetica", 16), fg="grey")
double_count_label.grid(row=4, column=5, padx=5)

# triple count
triple_count_label = Label(my_frame, text='Số lần ba: ', font=("Helvetica", 16), fg="grey")
triple_count_label.grid(row=5, column=5, padx=5)

# result
result_label = Label(my_frame, text='', font=("Helvetica", 20))
result_label.grid(row=6, column=0, pady=10, columnspan=3)

# money bet label
money_bet_label = Label(my_frame, text='Số tiền cược: ', font=("Helvetica", 15))
money_bet_label.grid(row=6, column=3, pady=10, columnspan=2)

# ------------------------------------------------------------
# BUTTON
under_button = Button(my_frame, text='Xỉu', height=2, width=5, command=lambda result_text= "Xỉu": roll_dice(result_text))
under_button.grid(row=7, column=1, pady=5, columnspan=2)

over_button = Button(my_frame, text='Tài', height=2, width=5, command=lambda result_text= "Tài": roll_dice(result_text))
over_button.grid(row=7, column=2, padx=10, pady=5, columnspan=2)

# Money text box
money_text_box =Text(my_frame, height=1, width= 18, font=("Helvetica", 15))
money_text_box.grid(row=7, column= 4, columnspan=2)
######

# Bet button
bet_button = Button(my_frame, text='Cược', height=2, width=5, command=get_bet_money)
bet_button.grid(row=7, column=6, pady=5)

# double button
double_one_button = Button(my_frame, text='11', height=2, width=5, command=lambda result_text='11': roll_dice(result_text))
double_one_button.grid(row=8, column=0, pady=5)

double_two_button = Button(my_frame, text='22', height=2, width=5, command=lambda result_text='22': roll_dice(result_text))
double_two_button.grid(row=8, column=1, pady=5)

double_three_button = Button(my_frame, text='33', height=2, width=5, command=lambda result_text='33': roll_dice(result_text))
double_three_button.grid(row=8, column=2, pady=5)

double_four_button = Button(my_frame, text='44', height=2, width=5, command=lambda result_text='44': roll_dice(result_text))
double_four_button.grid(row=8, column=3, pady=5)

double_five_button = Button(my_frame, text='55', height=2, width=5, command=lambda result_text='55': roll_dice(result_text))
double_five_button.grid(row=8, column=4, pady=5)

double_six_button = Button(my_frame, text='66', height=2, width=5, command=lambda result_text='66': roll_dice(result_text))
double_six_button.grid(row=8, column=5, pady=5)

# triple
triple_button = Button(my_frame, text='Ba', height=2, width=5, command=lambda result_text= "Ba": roll_dice(result_text))
triple_button.grid(row=9, column=0, padx=10, pady=5)

triple_one_button = Button(my_frame, text='111', height=2, width=5, command=lambda result_text= "111": roll_dice(result_text))
triple_one_button.grid(row=9, column=1, padx=10, pady=5)

triple_two_button = Button(my_frame, text='222', height=2, width=5, command=lambda result_text= "222": roll_dice(result_text))
triple_two_button.grid(row=9, column=2, padx=10, pady=5)

triple_three_button = Button(my_frame, text='333', height=2, width=5, command=lambda result_text= "333": roll_dice(result_text))
triple_three_button.grid(row=9, column=3, padx=10, pady=5)

triple_four_button = Button(my_frame, text='444', height=2, width=5, command=lambda result_text= "444": roll_dice(result_text))
triple_four_button.grid(row=9, column=4, padx=10, pady=5)

triple_five_button = Button(my_frame, text='555', height=2, width=5, command=lambda result_text= "555": roll_dice(result_text))
triple_five_button.grid(row=9, column=5, padx=10, pady=5)

triple_six_button = Button(my_frame, text='666', height=2, width=5, command=lambda result_text= "666": roll_dice(result_text))
triple_six_button.grid(row=9, column=6, padx=10, pady=5)

first_start()
root.mainloop()
