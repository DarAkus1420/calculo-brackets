#Se importan las librerias requeridas
from tkinter import *
from tkinter.ttk import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

root = Tk() #Se crea una instancia de tkinter frame
root.title('Metodo de brackets') #Se fija el titulo de la ventanta
root.geometry("800x600") #Se define el tamaño de la ventana

def clear(): #Se define una funcion para limpiar los datos ingresados
	my_text.delete(1.0, END)

def calculate():
	function_string = my_text.get(1.0, END) #Se reciben los datos ingresados para la funcion
	symbol1 = my_symbol.get(1.0, END) #Se reciben los datos ingresados para el simbolo
	f = parse_expr(function_string) #Convierte el texto recivido a una expresion
	x = symbols(f'{symbol1}') #Convierte el texto recivido a un simbolo para trabajar con el
	fun = Integral(f, (x, 0, oo)) #Se muestra los datos a calcular
	resultado = integrate(f, (x, 0, oo)) #Se calcula la integral y se almacena en resultado
		
	value_label.config(text=f'Value: {resultado}')#Se muestra el resultado
	graph(resultado)

#Se define una funcion para generar la figura del resultado
def graph(text):

	tmptext = latex(text) #Se convierte resultado a latex
	tmptext = "$"+tmptext+"$"
	#Se limpia los resultados anteriores de la figura
	ax.clear()
	ax.text(0.2, 0.6, tmptext, fontsize = 50)  
	canvas.draw() #se genera la figura



function_label = Label(root, text='Funcion: ') #Se crea la etiqueta que pide ingresar una funcion
function_label.pack()
my_text = Text(root, width=30, height=1) #Se define el tamaño del cuadro de texto que recibira la funcion
my_text.pack()
symbol_label = Label(root, text='Simbolo: ') #Se crea la etiqueta que pide ingresar el simbolo
symbol_label.pack()
my_symbol = Text(root, width=30, height=1) #Se define el tamaño del cuadro de texto que recibira el simbolo
my_symbol.pack()



button_frame = Frame(root)
button_frame.pack(pady=20)

clear_button = Button(button_frame, text='Limpiar', command=clear)#Se crea un boton para limpiar los datos ingresados
clear_button.grid(row=0, column=0) 

calculate_button = Button(button_frame, text='Calcular', command=calculate) #Se crea boton para realizar el calculo con los datos ingresados

value_label = Label(root)
value_label.pack()

#Se define el tamaño de la figura y se muestra la figura
fig = matplotlib.figure.Figure(figsize=(12, 6), dpi=50)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=value_label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

#Se establece la visibilidad de la figura de Canvas
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


root.bind('<Return>', graph)
root.mainloop()


