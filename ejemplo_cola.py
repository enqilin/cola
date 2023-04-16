from cola import Cola
from cola import Cola as arribo
from cola import Cola as atencion
from cola import Cola as cola_vacia

cdatos = Cola("LaCasaBuena")
cvocales = Cola()

letra= input("ingrese un caracter ")
def letra(cdatos):
    while (letra != ""):
        arribo(cdatos, letra)
        letra = input( "Ingrese un caracter")

    while(not cola_vacia(cdatos)):
        letra = atencion(cdatos)
        if letra.upper() in ['A', 'E','I','O','U']:
            arribo(cvocales ,letra)

    print('Datos cola vocales')
    while (not cola_vacia(cvocales)):
        dato = atencion(cvocales)
        print(dato)