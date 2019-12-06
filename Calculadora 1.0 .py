# Proyecto de calculadora basica y funcional, como parte de mi rutina de aprendizaje adictivo
# del lenguaje python y de programacion en general comenzado hace dos meses.
# Aunque puede quedar sujeto a eventuales modificacion voy a dar por finalizado el presente proyecto
# autor: Ariel G. Robotti
# email: arielrobotti@gmail.com

from tkinter import * 
from functools import * 
from math import*

raiz=Tk()
raiz.title("Calculadora 1.0")
raiz.geometry("600x530")
raiz.config(background="#9AA4A7")
raiz.iconbitmap("alma.ico")

fondoRaiz=PhotoImage(file="fondoRaiz.png")
fondo=Label(raiz,width=700,height=700,image=fondoRaiz).place(x=0,y=0)

colBoton="#66AACC"
colBtMem="#252500"
mostrar=StringVar()
mostrarMem=[StringVar(),StringVar(),StringVar()]

memoria=["","",""]
noConcatenar=0
buffer1=0
bufferOp=""

#-----------  display principal-----------------
display=Entry(raiz,width=26,font=("Eras Bold ITC",24),textvariable=mostrar,bd=10,justify="right")
display.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
display.config(background="black", fg="#DEDB89",justify="right")
mostrar.set("0")

#------------marco para memorias-------------------
memoFrame=Frame(raiz,bg="#9AA4A7",bd=5)
memoFrame.grid(row=2,column=1,columnspan=3)

#---------------marco para el teclado numerico----
fondo=PhotoImage(file="fondoNum.png")
teclado=Label(raiz,width=300,height=300,bg="#64788E",image=fondo)
teclado.grid(row=3,column=1)

#------marco para botones de operaciones y constantes-----
fondo2=PhotoImage(file="fondoNum2.png")
operFrame=Label(raiz,width=200,height=300,bg="#64788E",image=fondo2)
operFrame.grid(row=3,column=2)

def escribir(entrada):								#se introducen los numeros  a operar
	global noConcatenar	
	 
	if noConcatenar==1 or noConcatenar==2:					#si se presionó una tecla de operacion(caso 2),
		if entrada=="K" or entrada=="m" or entrada=="-":		#o se se introdujo una constante (caso 1)
			pass
		else:
			display.delete(0,END)					#limpia la pantalla
			
	#-------Este bloque imprime el primer digito ingresado ----------------------	
	if mostrar.get()=="0":  						#si la pantalla esta en 0 
		if entrada=="0" or entrada=="-" or entrada=="K" or entrada=="m":	
			pass
		elif entrada==",":
			mostrar.set("0,")
		else:
			mostrar.set(entrada)
	#----------------------------------------------------------------------------			
	else:									#si en cambio la pantalla no está en cero...
		if entrada=="-":						#si fué presionado un cambio de signo		
			if mostrar.get()[0]!="-":				#y si el signo no era negativo
				display.insert(0,"-")				#inserta el signo en la posicion 0 (a la izquierda)
			else:							#si el signo ya era negativo
				display.delete(0,1)				#lo borra

		elif entrada==",":						#si fue ingresada una ","
			if len(mostrar.get())==0:				
				mostrar.set("0,")
			else:
				if "," in mostrar.get():
					pass
				else:
					mostrar.set(mostrar.get()+',')
					
		elif entrada=="K":
			comaAPunto=mostrar.get().replace(",",".")		#reemplaza las comas por puntas para operar			
			aFloatK=float(comaAPunto)*1000
			if (aFloatK-int(aFloatK))==0: 				#muestra por ejemplo 9 en lugar de 9,0
				aFloatK=int(aFloatK)
			puntoAComa=str(aFloatK).replace(".",",")		#reemplaza los puntos por comas para mostrar 
			mostrar.set(puntoAComa)
		elif entrada=="m":
			comaAPunto=mostrar.get().replace(",",".")
			aFloatM=float(comaAPunto)/1000
			if (aFloatM-int(aFloatM))==0:
				aFloatM=int(aFloatM)
			puntoAComa=str(aFloatM).replace(".",",")
			mostrar.set(puntoAComa)

		else:
			mostrar.set(mostrar.get()+entrada)
	noConcatenar=0								#cada vez que se llama a esta funcion, la concatenacion 
										#queda habilitada, en realidad para evitar malos entendidos
										#tendria que renombrar la variable como "concatenar" y que
										#salga con valor 1
#-------------------------------------------------------------------------------------------------------
def escribirConst(entrada,mem=0):
	global noConcatenar
	noConcatenar=1
	if entrada=="Pi":
		mostrar.set(str(pi).replace('.',','))
		
	elif entrada=="euler":
		mostrar.set(str(e).replace('.',','))
		
	elif entrada=="raizD2":
		mostrar.set(str(sqrt(2)).replace('.',','))

	elif entrada=="12raiz2":
		mostrar.set(str(pow(2,1/12)).replace('.',','))
			
	elif entrada=="CE":
		mostrar.set("0")

	elif entrada =="au":
		mostrar.set("1,6180339887498949")

	elif entrada=="cred":
		mostrar.set("*Autor: arielrobotti@gmail.com *")

	elif entrada=="mem":
		if memoria[mem]=="":
			pass
		else:
			mostrar.set(str(memoria[mem]).replace('.',','))

#---------------------- Barra de retroceso -------------------

def backSpace():
	if '*' in mostrar.get():
		pass
	else:
		if len(mostrar.get())==1 or (len(mostrar.get())==2 and mostrar.get()[0]=="-"):
			mostrar.set("0")
		else:
			display.delete(len(mostrar.get())-1,END)

#--------- Operaciones que requieren ingresar un nuevo valor ------------------

def operarConSiguiente(oper):	
	global buffer1
	global bufferOp
	global noConcatenar
	enPantalla = mostrar.get().replace(",",".")
	if "*" in enPantalla:
		pass
	else:
		getValor=float(enPantalla)
		if noConcatenar==0 or noConcatenar==1:
			noConcatenar=2
			if bufferOp!="":
				if bufferOp=="+":
					buffer1+=getValor

				elif bufferOp=="-":
					buffer1-=getValor

				elif bufferOp=="*":
					buffer1*=getValor

				elif bufferOp=="/":
					divisor=getValor
					if divisor==0:
						borrar()
						buffer1="E"
					else:
						buffer1/=divisor

				elif bufferOp=="rYdeX":
					if buffer1<=0:					
						if getValor%2 ==0:			# Error si es un entero negativo par 
							buffer1="E2"					
						elif getValor%2==1:			# Si es un entero negativo impar el resultado es negativo
							buffer1*=-1
							buffer1=-(buffer1**(1/getValor))
						else:						# si es un negativo no entero
							buffer1*=-1
							buffer1=buffer1**(1/getValor)
					else:
						buffer1=buffer1**(1/getValor)
					
				elif bufferOp=="XexpY":
					buffer1=buffer1**getValor

				if buffer1=="E":
					mostrar.set("* ERROR (Resultado infinito) *")

				elif buffer1=="E2":
					mostrar.set("* Operacion no soportada *")

				else:
					if buffer1-int(buffer1)==0:
					 	buffer1=int(buffer1)
					mostrar.set(str(buffer1).replace(".",","))
				
			else:
				buffer1=getValor
				bufferOp=oper
	
		else:
			bufferOp=oper 
			noConcatenar=2
		if oper=="=":
			
			bufferOp=""
		else:
			bufferOp=oper
			
#--------- Operaciones que requieren solo el valor en pantalla --------------
def operar(oper):
	global noConcatenar
	noConcatenar=1
	enPantalla = mostrar.get().replace(",",".")
	if "*" in enPantalla:
		pass
	else:
		getValor=float(enPantalla)
		if oper=="ln":
			if getValor <= 0:
				borrar()
				mostrar.set("* Entrada no válida *")
			else:
				y=log(getValor,e)
				if y-int(y)==0:
					y=int(y)	
				mostrar.set(str(y).replace(".",","))

		elif oper=="log":
			if getValor<=0:
				borrar()
				mostrar.set("* Entrada no válida *")
			else:
				x=log(getValor,10)
				if x-int(x)==0:
					x=int(x)
				mostrar.set(str(x).replace(".",","))

		elif oper=="R2":
			if getValor<0:
				mostrar.set("* Operacion no soportada *")
			else:
				r2=getValor**0.5
				if r2-int(r2)==0:
					r2=int(r2)
				mostrar.set(str(r2).replace(".",","))

		elif oper=="XCuad":
			X2=getValor**2
			if X2-int(X2)==0:
				X2=int(X2)
			mostrar.set(str(X2).replace(".",","))

		elif oper=="1/x":
			if getValor==0:
				borrar()
				mostrar.set("* ERROR *")				
			else:
				invert=1/getValor
				if invert-int(invert)==0:
					invert=int(invert)
				mostrar.set(str(invert).replace('.',','))
		elif oper=="nFact":
			if getValor-int(getValor)!=0:
				borrar()
				mostrar.set("* ERROR, solo valores enteros *")
			else:
				mostrar.set(factorial(getValor))

#-- Guarda el valor del display en la posicion (mem) de memoria[] ----

def guardar(aMemoria,mem):
	global memoria
	if aMemoria=="":
		memoria[mem]=""
		mostrarMem[mem].set("")

	else: 
		if '*' in mostrar.get():
			pass
		else: 
			memoria[mem]=mostrar.get()
			mostrarMem[mem].set(mostrar.get())

#---------- Funcion Borrar (boton C) ------------------------

def borrar():
	global buffer1
	global bufferOp
	buffer1=0
	bufferOp=""
	mostrar.set("0")


#--------------------- Memoria 1 ------------------------

memo1In=Button(memoFrame,text=">> ENTRADA MEMO 1",font=("Eras Bold ITC",9),command= partial(guardar,"display",0))
memo1In.grid(row=1,column=1)
memo1In.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo1Out=Button(memoFrame,text="SALIDA MEMO 1 >>",font=("Eras Bold ITC",9),command= partial(escribirConst,"mem",0))
memo1Out.grid(row=1,column=3)
memo1Out.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo1Borrar=Button(memoFrame,text="BORRAR",font=("Eras Bold ITC",9),command= partial(guardar,"",0))
memo1Borrar.grid(row=1,column=4)
memo1Borrar.config(background="#9AA4A7", fg=colBtMem,justify="right")

displayMemo=Entry(memoFrame,width=20,font=("Eras Bold ITC",12),textvariable=mostrarMem[0],justify="right")
displayMemo.grid(row=1,column=2)
displayMemo.config(background="black", fg="#FFFFFF",justify="right")

#--------------------- Memoria 2 --------------------------

memo2In=Button(memoFrame,text=">> ENTRADA MEMO 2",font=("Eras Bold ITC",9),command= partial(guardar,"display",1))
memo2In.grid(row=2,column=1)
memo2In.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo2Out=Button(memoFrame,text="SALIDA MEMO 2 >>",font=("Eras Bold ITC",9),command= partial(escribirConst,"mem",1))
memo2Out.grid(row=2,column=3)
memo2Out.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo2Borrar=Button(memoFrame,text="BORRAR",font=("Eras Bold ITC",9),command= partial(guardar,"",1))
memo2Borrar.grid(row=2,column=4)
memo2Borrar.config(background="#9AA4A7", fg=colBtMem,justify="right")

displayMemo=Entry(memoFrame,width=20,font=("Eras Bold ITC",12),textvariable=mostrarMem[1],justify="right")
displayMemo.grid(row=2,column=2)
displayMemo.config(background="black", fg="#FFFFFF",justify="right")

#---------------------- Memoria 3 -------------------------

memo3In=Button(memoFrame,text=">> ENTRADA MEMO 3",font=("Eras Bold ITC",9),command= partial(guardar,"display",2))
memo3In.grid(row=3,column=1)
memo3In.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo3Out=Button(memoFrame,text="SALIDA MEMO 3 >>",font=("Eras Bold ITC",9),command= partial(escribirConst,"mem",2))
memo3Out.grid(row=3,column=3)
memo3Out.config(background="#9AA4A7", fg=colBtMem,justify="right")

memo3Borrar=Button(memoFrame,text="BORRAR",font=("Eras Bold ITC",9),command= partial(guardar,"",2))
memo3Borrar.grid(row=3,column=4)
memo3Borrar.config(background="#9AA4A7", fg=colBtMem,justify="right")

displayMemo=Entry(memoFrame,width=20,font=("Eras Bold ITC",12),textvariable=mostrarMem[2],justify="right")
displayMemo.grid(row=3,column=2)
displayMemo.config(background="black", fg="#FFFFFF",justify="right")

#------------------------- botones de numeros ------------------------------

botonMasMenos=Button(teclado,text="+/-",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"-"))
botonMasMenos.grid(row=5,column=1,padx=5,pady=5)

boton0=Button(teclado,text="0",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"0"))
boton0.grid(row=5,column=2,padx=5,pady=5)

botonComa=Button(teclado,text=",",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,","))
botonComa.grid(row=5,column=3,padx=5,pady=5)

#------------------------ Fila 2 ----------------------------

boton1=Button(teclado,text="1",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"1"))
boton1.grid(row=4,column=1,padx=5,pady=5)

boton2=Button(teclado,text="2",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"2"))
boton2.grid(row=4,column=2,padx=5,pady=5)

boton3=Button(teclado,text="3",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"3"))
boton3.grid(row=4,column=3,padx=5,pady=5)

#------------------------ Fila 3 ----------------------------

boton4=Button(teclado,text="4",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"4"))
boton4.grid(row=3,column=1,padx=5,pady=5)

boton5=Button(teclado,text="5",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"5"))
boton5.grid(row=3,column=2,padx=5,pady=5)

boton6=Button(teclado,text="6",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"6"))
boton6.grid(row=3,column=3,padx=5,pady=5)

#------------------------ Fila 4 ----------------------------

boton7=Button(teclado,text="7",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"7"))
boton7.grid(row=2,column=1,padx=5,pady=5)

boton8=Button(teclado,text="8",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"8"))
boton8.grid(row=2,column=2,padx=5,pady=5)

boton9=Button(teclado,text="9",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"9"))
boton9.grid(row=2,column=3,padx=5,pady=5)

#------------------------Fila 5--------------------------------

botonKilo=Button(teclado,text="Kilo",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"K"))
botonKilo.grid(row=6,column=1,padx=5,pady=5)

botonBack=Button(teclado,text="<<",font=("Arial",18),bg=colBoton,width=4,command= partial(backSpace))
botonBack.grid(row=6,column=2,padx=5,pady=5)

botonMili=Button(teclado,text="mili",font=("Arial",18),bg=colBoton,width=4,command= partial(escribir,"m"))
botonMili.grid(row=6,column=3,padx=5,pady=5)

#-------------Botones de operaciones------------------

suma=Button(operFrame,text="+",font=("Arial",18),bg=colBoton,width=4,command= partial(operarConSiguiente,"+"))
suma.grid(row=1,column=1,padx=5,pady=5)

resta=Button(operFrame,text="-",font=("Arial",18),bg=colBoton,width=4,command= partial(operarConSiguiente,"-"))
resta.grid(row=2,column=1,padx=5,pady=5)

prod=Button(operFrame,text="*",font=("Arial",18),bg=colBoton,width=4,command= partial(operarConSiguiente,"*"))
prod.grid(row=3,column=1,padx=5,pady=5)

div=Button(operFrame,text="/",font=("Arial",18),bg=colBoton,width=4,command= partial(operarConSiguiente,"/"))
div.grid(row=4,column=1,padx=5,pady=5)

nFact=Button(operFrame,text="n!",font=("Arial",18),bg=colBoton,width=4,command= partial(operar,"nFact"))
nFact.grid(row=5,column=1,padx=5,pady=5)

#-------------------------------------------------------

invertir=Button(operFrame,text="1/x",font=("Arial",18),bg=colBoton,width=4,command= partial(operar,"1/x"))
invertir.grid(row=1,column=2,padx=5,pady=5)

imgXcuadr=PhotoImage(file="XCuadr.gif",height=42,width=60)
Xcuad=Button(operFrame,image=imgXcuadr,bg=colBoton,command= partial(operar,"XCuad"))
Xcuad.grid(row=2,column=2,padx=5,pady=5)

imgRaiz2=PhotoImage(file="Raiz2.gif",height=42,width=60)
raiz2=Button(operFrame,image=imgRaiz2,bg=colBoton,command= partial(operar,"R2"))
raiz2.grid(row=3,column=2,padx=5,pady=5)

imgXaLaY=PhotoImage(file="XaLaY.gif",height=42,width=60)
XaLaY=Button(operFrame,image=imgXaLaY,bg=colBoton,command= partial(operarConSiguiente,"XexpY"))
XaLaY.grid(row=4,column=2,padx=5,pady=5)

imgRaizNdeX=PhotoImage(file="rNdeX.gif",height=42,width=60)
raizNdeX=Button(operFrame,image=imgRaizNdeX,bg=colBoton,command= partial(operarConSiguiente,"rYdeX"))
raizNdeX.grid(row=5,column=2,padx=5,pady=5)

#----------------------------------------------------------

Pi=Button(operFrame,text="PI",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,"Pi"))
Pi.grid(row=1,column=3,padx=5,pady=5)

euler=Button(operFrame,text="e",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,"euler"))
euler.grid(row=2,column=3,padx=5,pady=5)

ln=Button(operFrame,text="ln",font=("Arial",18),bg=colBoton,width=4,command= partial(operar,"ln"))
ln.grid(row=3,column=3,padx=5,pady=5)

raizD2=Button(operFrame,text="√2",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,"raizD2"))
raizD2.grid(row=4,column=3,padx=5,pady=5)

botonC=Button(operFrame,text="C",font=("Arial",18),bg=colBoton,width=4,command= partial(borrar))
botonC.grid(row=5,column=3,padx=5,pady=5)

#-------------------------------------------------------------------

aureo=Button(operFrame,text="Au",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,"au"))
aureo.grid(row=1,column=4,padx=5,pady=5)

cred=Button(operFrame,text="¿?",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,"cred"))
cred.grid(row=2,column=4,padx=5,pady=5)

log10=Button(operFrame,text="log",font=("Arial",18),bg=colBoton,width=4,command= partial(operar,"log"))
log10.grid(row=3,column=4,padx=5,pady=5)

imgRaiz12ava2=PhotoImage(file="Raiz12de2.gif",height=42,width=60)
raiz12ava2=Button(operFrame,image=imgRaiz12ava2,bg=colBoton,command= partial(escribirConst,"12raiz2"))
raiz12ava2.grid(row=4,column=4,padx=5,pady=5)

botonCe=Button(operFrame,text="CE",font=("Arial",18),bg=colBoton,width=4,command= partial(escribirConst,'CE'))
botonCe.grid(row=5,column=4,padx=5,pady=5)

igual=Button(raiz,text="=",font=("Arial",18),bg=colBoton,width=40,command= partial(operarConSiguiente,"="))
igual.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

raiz.mainloop()

