import cv2
import numpy as np
import random
import math

def filtrar(op1, op2):
	frame = cv2.imread('lena.bmp',0)
	framec = frame.copy()
    
	if op1 == 1:
		frame_ruido = uniforme(framec)
	elif op1 == 2:
		frame_ruido = gausiano(framec)
	elif op1 == 3:
		frame_ruido = sal(framec)
	elif op1 == 4:
		frame_ruido = pimienta(framec)
	else:
		frame_ruido = salYpimienta(framec)

	framerc = frame_ruido.copy()
	if op2 == 1:
		frame_filtro = mediano(framerc)
	elif op2 == 2:
		frame_filtro = maximo(framerc)
	elif op2 == 3:
		frame_filtro = minimo(framerc)
	elif op2 == 4:
		frame_filtro = puntoMedio(framerc)
	elif op2 == 5:
		frame_filtro = medioAritmetico(framerc)
	else:
		frame_filtro = medioContraHarmonico(framerc)

	cv2.imshow('original', frame)
	cv2.imshow('con ruido', frame_ruido)
	cv2.imshow('aplicado filtro', frame_filtro)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


##########Filtros
def mediano(frame):
	result = cv2.medianBlur(frame,5)
	
	return result

def maximo(frame):
	mask = []
	fil, col = frame.shape
	print dim
	for f in range(fil-dim+1):
		for c in range(col-dim+1):
			mask = frame[f:f+dim, c:c+dim]
			maximo = mask.max()
			frame[f][c] = maximo
			
	return frame

def minimo(frame):
	mask = []
	fil, col = frame.shape
	
	for f in range(fil-dim+1):
		for c in range(col-dim+1):
			mask = frame[f:f+dim, c:c+dim]
			minimo = mask.min()
			frame[f][c] = minimo

	return frame

def medioAritmetico(frame):
	mask = []
	fil, col = frame.shape

	for f in range(fil-dim+1):
		for c in range(col-dim+1):
			mask = frame[f:f+dim, c:c+dim]
			promedio = np.mean(mask)
			frame[f][c] = promedio

	return frame

def puntoMedio(frame):
	mask = []
	fil, col = frame.shape
	result = frame.copy()
	for f in range(fil-dim+1):
		for c in range(col-dim+1):
			mask = frame[f:f+dim, c:c+dim]
			maximo = mask.max()
			minimo = mask.min()
			promedio = float((maximo+minimo)/2)
			result[f][c] = promedio

	return result

def medioContraHarmonico(frame):
	mask = []
	fil, col = frame.shape
	R=2
	result = frame.copy()
	for f in range(fil-dim+1):
		for c in range(col-dim+1):
			numerador = 0
			denominador = 0
			for i in range(dim):
				for j in range(dim):
					numerador = numerador + math.pow(frame[i+f][j+c],R+1)
					denominador = denominador + math.pow(frame[i+f][j+c],R) 
			if denominador!=0:
				result[f][c] = numerador/denominador

	return result

######funciones para generar ruido
def sal(frame):
	 fil, col = frame.shape
	 par = round(fil*col*0.01)
	 for i in range(int(par)):
	 	a = np.random.randint(0,fil)
	 	b = np.random.randint(0,col)
	 	frame[a][b] = 255

	 return frame

def pimienta(frame):
	 fil, col = frame.shape
	 par = round(fil*col*0.01)
	 for i in range(int(par)):
	 	a = np.random.randint(0,fil)
	 	b = np.random.randint(0,col)
	 	frame[a][b] = 0

	 return frame

def salYpimienta(frame):
	frame = sal(frame)
	frame = pimienta(frame)

	return frame

def uniforme(frame):
	fil = frame.shape[0]
	col = frame.shape[1]
	ruido = np.zeros(frame.shape, np.uint8)
	prob = np.ones([fil, col], float)
	a = 88
	b = 169
	p = float(1.0/(b-a))
	val = np.zeros([256], int)
	for i in range(256):
		if i>=a and i<=b:
			fact = fil*col*p
			val[i] = fact + 1


	mezcla = frame.copy()
	for i in range(fil):
		for j in range(col):
			if (i+j)%2 == 0:
				while(True):
					valor = random.randint(0, 255)
					if val[valor]>0:
						break
				mezcla[i][j] = valor + frame[i][j]

	return mezcla

def gausiano(frame):
	fil = frame.shape[0]
	col = frame.shape[1]
	ruido = np.zeros(frame.shape, np.uint8)
	media = 127
	var = 100.0
	div = 2.5 * var
	val = np.zeros([256], int)
	mezcla = frame.copy()
	for i in range(256):
		num = (i-media)**2
		dem = 2 *var*var
		e = math.exp(-num/dem)
		p = round(float(fil*col)*float((1/div)*e))
		val[i] = p + 20

	for i in range(fil):
		for j in range(col):
			if (i+j)%2 == 0:
				while(True):
					x = random.randint(0,255)
					valor = random.randint(0,255)
					if (val[valor]>0):
						break
				mezcla[i][j] = valor + frame[i][j]

	return mezcla
				


dim = 3
op = 0
while op != 6:
	print "Generar ruido"
	print "1. Uniforme"
	print "2. Gausiano"
	print "3. Sal"
	print "4. Pimienta"
	print "5. Sal y Pimienta"
	print "6. Salir"
	op1 = input("Elija el tipo de ruido: ")

	print "Elegir filtro"
	print "1. Mediano"
	print "2. Maximo"
	print "3. Minimo"
	print "4. Punto Medio"
	print "5. Medio Aritmetico"
	print "6. Medio Contra-Harmonico"
	op2 = input("Elija el tipo de filtro: ")

	if op1 >= 1 and op1 < 6:
		filtrar(op1, op2)



















