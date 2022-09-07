from tkinter import *

#Setting configurations of the window
root = Tk()
root.geometry('450x600')
root.resizable(0, 0)
root['bg'] = 'Lightblue'
root.title('Calculator')

Label(root, text='CALCULATOR', font=('CALIBRI', 30, 'bold'), bg='Lightblue').grid(row=0, column=0, columnspan=4)
equation = Entry(root, width=30, font=('ARIAL', 15, 'bold'))
equation.grid(row=1, column=0, columnspan=4, padx=15)

def show(to_print):
    """Function that update the output screen everytime a button is clicked"""
    old_equation = equation.get()
    equation.delete(0, END)
    equation.insert(0, old_equation + to_print)
    return


def show_result():
    """Function that show result after Button('=')"""
    try:
        r = eval(equation.get())
        equation.delete(0, END)
        equation.insert(0, r)
    except:
        return

def clear():
    """Function that clear the output"""
    equation.delete(0, END)
    return

def delete_1digit():
    """Function that act like a backspace, deleting the last digit pressed"""
    copy = equation.get()
    length = len(copy)-1
    equation.delete(length, END)

# Creation of Buttons
n0 = Button(root, text='0', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('0'))
n1 = Button(root, text='1', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('1'))
n2 = Button(root, text='2', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('2'))
n3 = Button(root, text='3', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('3'))
n4 = Button(root, text='4', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('4'))
n5 = Button(root, text='5', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('5'))
n6 = Button(root, text='6', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('6'))
n7 = Button(root, text='7', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('7'))
n8 = Button(root, text='8', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('8'))
n9 = Button(root, text='9', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('9'))

percent = Button(root, text='%', font=('Arial', 13, 'bold'), relief=RAISED, command=lambda: show('/100'))
mult = Button(root, text='  *  ', font=('Arial', 13, 'bold'), relief=RAISED, command=lambda: show('*'))
div = Button(root, text=' / ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('/'))
sum = Button(root, text=' + ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('+'))
sub = Button(root, text=' - ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('-'))
sqrt = Button(root, text='√', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda :show('**(1/2)'))
result = Button(root, text=' = ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=show_result)
parentheses1 = Button(root, text=' ( ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('('))
parentheses2 = Button(root, text=' ) ', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show(')'))
CE = Button(root, text='CE', font=('Arial', 13, 'bold'), padx=10, relief=RAISED, command=clear)
comma = Button(root, text=',', font=('Arial', 13, 'bold'), padx=10, relief=RAISED, command=lambda: show(','))
exp = Button(root, text='^', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda :show('**'))
delete = Button(root, text='DEL', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=delete_1digit)
exp10 = Button(root, text='10^x', font=('Arial', 13, 'bold'), relief=RAISED, padx=10, command=lambda: show('10**'))

#Setting buttons inside the window (root)
percent.grid(row=2, column=0, padx=15, pady=30)
parentheses1.grid(row=2, column=1, padx=15, pady=30)
parentheses2.grid(row=2, column=2, padx=15, pady=30)
CE.grid(row=2, column=3, padx=15, pady=30)

sqrt.grid(row=3, column=0, padx=15, pady=15)
exp.grid(row=3, column=1, padx=15, pady=15)
exp10.grid(row=3, column=2, padx=15, pady=15)
delete.grid(row=3, column=3, padx=15, pady=15)

n7.grid(row=4, column=0, padx=15, pady=15)
n8.grid(row=4, column=1, padx=15, pady=15)
n9.grid(row=4, column=2, padx=15, pady=15)
mult.grid(row=4, column=3, padx=15, pady=15)

n4.grid(row=5, column=0, padx=15, pady=15)
n5.grid(row=5, column=1, padx=15, pady=15)
n6.grid(row=5, column=2, padx=15, pady=15)
sub.grid(row=5, column=3, padx=15, pady=15)

n1.grid(row=6, column=0, padx=15, pady=15)
n2.grid(row=6, column=1, padx=15, pady=15)
n3.grid(row=6, column=2, padx=15, pady=15)
sum.grid(row=6, column=3, padx=15, pady=15)

n0.grid(row=7, column=0, padx=15, pady=15)
comma.grid(row=7, column=1, padx=15, pady=15)
div.grid(row=7, column=2, padx=15, pady=15)
result.grid(row=7, column=3, padx=15, pady=15)

if __name__ == '__main__':
    mainloop()
