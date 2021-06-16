'''Dado un vector con personaje de las películas de la saga de Star Wars resolver las
siguientes actividades:
a. Realizar un barrido recursivo del vector. 
b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el vector y en que posición.'''

personajes = ['Luke','Han Solo','Obi-Wan','R2-D2','Yoda' ,'C-3PO','Leia','Chewbacca']


def barrido(v,i):
    if i != len(v):
        print (v[i])
        barrido(v, i + 1)

print(barrido(personajes,0))

def busqueda(v,i,buscado):
    if buscado != str(v[i]) and i <= len(v):
        busqueda(v,i+1,buscado)
    else:
        return print('se encontro a', buscado,'en la posicion', i)
        

buscado='Yoda'
busqueda(personajes,0,buscado)
