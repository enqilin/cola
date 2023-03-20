from cola import Cola , arribo , atencion , cola_vacia

cdatos = Cola()
cvocales = Cola()

letra= input("ingrese un caracter ")

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