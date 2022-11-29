from tkinter import *

window = Tk()
window.title('calculadora')

I = 0
value_text = Entry(window, font=("Calibri 18"))
value_text.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=5,
    pady=5
)

# function
def click_button(value):
    global I;
    value_text.insert(I, value);
    I += 1;

def delete():
    value_text.delete(0, END)
    I = 0;
    
    
def operation():
    ecuation = value_text.get();
    result = eval(ecuation);
    value_text.delete(0, END);
    value_text.insert(0, result)
    I = 0;

#buttons numbers
button1 = Button(window, text="1", width="5", height="2", command= lambda: click_button("1"));
button2 = Button(window, text="2", width="5", height="2", command= lambda: click_button("2"));
button3 = Button(window, text="3", width="5", height="2", command= lambda: click_button("3"));
button4 = Button(window, text="4", width="5", height="2", command= lambda: click_button("4"));
button5 = Button(window, text="5", width="5", height="2", command= lambda: click_button("5"));
button6 = Button(window, text="6", width="5", height="2", command= lambda: click_button("6"));
button7 = Button(window, text="7", width="5", height="2", command= lambda: click_button("7"));
button8 = Button(window, text="8", width="5", height="2", command= lambda: click_button("8"));
button9 = Button(window, text="9", width="5", height="2", command= lambda: click_button("9"));
button0 = Button(window, text="0", width="14", height="2", command= lambda: click_button("0"));

#buttons operators
button_mul = Button(window, text='x', width="5", height="2", command= lambda: click_button("x"));
button_div = Button(window, text='/', width="5", height="2", command= lambda: click_button("/"));
button_sum = Button(window, text='+', width="5", height="2", command= lambda: click_button("+"));
button_res = Button(window, text='-', width="5", height="2", command= lambda: click_button("-"));

#buttons other
button_parentesis1 = Button(window, text='(', width="5", height="2", command= lambda: click_button("("));
button_parentesis2 = Button(window, text=')', width="5", height="2", command= lambda: click_button(")"));
button_point = Button(window, text='.', width="5", height="2", command= lambda: click_button("."));
button_delete = Button(window, text='AC', width="5", height="2", command= lambda: delete());
button_iqual = Button(window, text='=', width="5", height="2", command= lambda: operation());

#style buttons
button_delete.grid(row = 1, column = 0, padx = 5, pady = 5);
button_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5);
button_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5);
button_div.grid(row = 1, column = 3, padx = 3, pady = 5);

button7.grid(row = 2, column = 0, padx = 5, pady = 5);
button8.grid(row = 2, column = 1, padx = 5, pady = 5);
button9.grid(row = 2, column = 2, padx = 5, pady = 5);
button_mul.grid(row = 2, column = 3, padx = 5, pady = 5);

button4.grid(row = 3, column = 0, padx = 5, pady = 5);
button5.grid(row = 3, column = 1, padx = 5, pady = 5);
button6.grid(row = 3, column = 2, padx = 5, pady = 5);
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5);

button1.grid(row = 4, column = 0, padx = 5, pady = 5);
button2.grid(row = 4, column = 1, padx = 5, pady = 5);
button3.grid(row = 4, column = 2, padx = 5, pady = 5);
button_res.grid(row = 4, column = 3, padx = 5, pady = 5);

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5);
button_point.grid(row = 5, column = 2, padx = 5, pady = 5);
button_iqual.grid(row = 5, column = 3, padx = 5, pady = 5);

window,mainloop();