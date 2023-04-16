class nodoCola(object):
    def __init__(self):
        self.info = None
        self.sig = None



class Cola(object):
    """Clase Cola"""
    def __init__(self):
        """Crea una cola vacia, tiene tres parametro"""
        self.frente, self.final = None,None
        self.tamanio = 0

    def arribo(cola, dato):
        """Arriba el dato al final de la cola"""

        nodo = nodoCola()
        nodo.info= dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamanio += 1
    
    def atencion(cola):
        """Antiende el elemento en el frente da la cola y lo devuelve"""
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
        cola.tamanio -= 1
        return dato

    def cola_vacia(cola):
        """Devuelve true si la cola esta vacia"""
        return cola.frente is None
    
    def en_frente(cola):
        """Devuelve el valor almacenado en el frente de la cola"""
        return cola.frente.info

    def tamanio(cola):
        """Devuelve el tamanio de la cola"""
        return cola.tamanio

    def mover_al_final(cola):
        """Mueve el elemento del frente de la cola al final"""
        dato = Cola.atencion(cola)
        Cola.arribo(cola, dato)
        return dato



    def barrido(cola):
        """Muestra el contenido de una cola sin perder datos."""
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux,dato)

        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(cola)
            Cola.arribo (cola,dato)

    def barrido2(cola):
        i = 0
        while(i < Cola.tamanio(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1




cdatos = Cola()
cvocales = Cola()
letra= input("ingrese un caracter ")
while (letra!= ""):
    Cola.arribo(cdatos, letra)
    letra = input( "Ingrese un caracter ")
    
while(not Cola.cola_vacia(cdatos)):
    letra = Cola.atencion(cdatos)
    if letra.upper() in ['A','E','I','O','U']:
        Cola.arribo(cvocales ,letra)

print('Datos cola vocales')
while (not Cola.cola_vacia(cvocales)):
    dato = Cola.atencion(cvocales)
    print(dato)
