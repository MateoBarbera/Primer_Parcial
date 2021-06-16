from tda_cola import Cola, arribo, tamanio, atencion, mover_final, en_frente
from tda_pila import Pila, apilar, mostrar_elementos
'''Dada una Cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el
mensaje, resolver las siguientes actividades:
c. escribir una función que elimine de la Cola todas las notificaciones de
Facebook;
d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
mensaje incluya la palabra ‘Python’, si perder datos en la Cola;
e. utilizar una pila para almacenar temporalmente las notificaciones de
Instagram y mostrar el contenido de dicha pila.'''


cola= Cola()
pila = Pila()
dato = ['', '', '']


dato=['16:45','facebook','te etiquetaron en una publicacion' ]
arribo(cola, dato)
dato=['12:07','github','walter actualizo su repositorio' ]
arribo(cola, dato)
dato=['22:50','Twitter','carlos sigue a tutoriales Python, siguelo tu tambien' ]
arribo(cola, dato)
dato=['17:30','instagram','mel agrego contenido a su perfil despues de mucho tiempo' ]
arribo(cola, dato)


for i in range(tamanio(cola)):
    x = en_frente(cola)
    if x[1] == 'facebook':
        atencion(cola)
    else:
        print(x)
        mover_final(cola)

print('\n')



for i in range(tamanio(cola)):
    x = en_frente(cola)
    if x[1] == 'Twitter' and 'Python' in x[2]:
        print(x)
    else:   
     mover_final(cola)

for i in range(tamanio(cola)):
    x = en_frente(cola)
    if x[1] == 'Instagram':
        atencion(cola)
        apilar(pila, x)
    else: 
        mover_final(cola)
    

    