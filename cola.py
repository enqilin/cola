class nodoCola(object):
    info, sig = None, None



class Cola(object):
    """Clase Cola"""
    def __init__(self):
        """Crea una cola vacia, tiene tres parametro"""
        self.frente, self.final = None, None
        self.tamanio = None

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
        dato = atencion(cola)
        arribo(cola, dato)
        return dato



    def barrido(cola):
        """Muestra el contenido de una cola sin perder datos."""
        caux = Cola()
        while(not cola_vacia(cola)):
            dato = atencion(cola)
            print(dato)
            arribo(caux,dato)

        while(not cola_vacia(caux)):
            dato = atencion(cola)
            arribo (cola,dato)

    def barrido2(cola):
        i = 0 
        while(i < tamanio(cola)):
            dato = mover_al_final(cola)
            print(dato)
            i += 1

