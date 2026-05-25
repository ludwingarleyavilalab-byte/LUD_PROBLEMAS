#Universidad nacional y abierta a distancia
#Fundamentos de programacion
#Fase 5: Evaluacion final POA
#Problema #4
#Ludwing Arley Avila Barrios



columnas = ["TITULO","AÑO_LANZAMIENTO","CALIFICACION","GENERO",]
filas = [ ]
cantidad_columnas=4
cantidad_filas=0
dx= "SI"

print("BIENVENIDO A LA VIDEOTECA BONITA")

while dx == "SI":
 fila=[]
 for uwu in range(0,cantidad_columnas):
    if uwu == 1 or uwu == 2:
       valores = int(input(f"DIGITE {columnas[uwu]}: "))
    else:
       valores = str(input(f"DIGITE {columnas[uwu]}: "))

    fila.append(valores)
 filas.append(fila)
 cantidad_filas+= 1 
 dx = input("¿VA A AGREGAR MAS VIDEOS? SI/NO: ").upper()

def analisis( cantidad_filas,filas ):
    cont = 0
    calificacion = int(input("DIGITE QUE CALIFICACION ESTA CONSIDERANDO: "))
    fechita = int(input("DIGITE LA FECHA QUE ESTA CONSIDERANDO: "))

    for unu in range(0, cantidad_filas):
        if filas[unu][2] >= calificacion and filas[unu][1] >= fechita:
            print(filas[unu])
            cont += 1
    print(f"LA CANTIDAD DE VIDEOS CON ESOS CRITERIOS ES: {cont}")



print("LOS VIDEOS DISPONIBLES SON:" ) 
print(columnas)
print(filas)
analizar = input("¿DESEA USTED BUSCAR ALGUNA EN ESPECIAL? SI/NO: ").upper()
if analizar == "SI":
    analisis(cantidad_columnas, cantidad_filas,filas,columnas )
