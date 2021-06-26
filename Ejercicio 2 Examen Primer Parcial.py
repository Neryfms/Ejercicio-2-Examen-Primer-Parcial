print('Lista de paises')
print('1. Honduras')
print('2. Panama')
print('3. Guatemala') 
print('4. Nicaragua')
print('5. Salvador')
Pais = {'Honduras':9.746, 'Panama':4.246, 'Guatemala':16.6, 'Nicaragua':6.44,'Salvador':6.454}
Poblacion = input('Ingrese un nombre de la lista de Paises tal y como están escritos: ').title()

if Poblacion in Pais:
    print( 'La poblacion de', Poblacion, 'es', Pais[Poblacion], 'millones')
else: 
    print("Lo siento, el Pais", Poblacion, "no está disponible, por favor ingrese un pais correcto de la lista.")