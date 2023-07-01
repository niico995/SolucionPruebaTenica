#Elementos 
listaNumeros= [] #Decido guardar los números generados en una lista para facilitar la busqueda con los indices
auxSum = 0 #Auxiliar donde voy a llevar las sumas obtenidas 

#Aqui pido datos para que funcione con mas números que solo los del ejemplo
a = int(input('''Ingrese el valor de arranque: 
(Recuerde que debe ser mayor a 4 digitos)
''' ))

#Esta parte la realizo para poder poner a prueba los resultados 
fin = int(input('Ingrese cuantas sumas desea realizar: '))
posicionDeseada = int(input('''Ingrese la posición deseada para obtener el resutaldo: 
(Recuerde que debe ser dentro del rango de sumas especificadas anteriormente)
'''))
#--------------------------------------------------------------------------------------

b = a + 1
c = b + 1

auxSum = a + b + c
listaNumeros.append(a)
listaNumeros.append(b)
listaNumeros.append(c)    
listaNumeros.append(auxSum)

for i in range(fin):
    auxSum = listaNumeros[i] + listaNumeros[i+1] + listaNumeros[i+2]
    listaNumeros.append(auxSum)
    print(f'''
          -------------------------------------------------------------------------------
          {listaNumeros[i]} || {listaNumeros[i+1]} || {listaNumeros[i+2]}\n
          -------------------------------------------------------------------------------
          ''')

ultimosCuatro = listaNumeros[posicionDeseada-1] % 10000
print(f'\n Ultimos 4 digitos del número en la posición deseada: {ultimosCuatro}')

