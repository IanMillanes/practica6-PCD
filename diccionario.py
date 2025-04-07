cadena='El profe Raul es un buen profe'
frecuencia = {} 

def frecuenciaDePalabras(cadena):
    palabras = cadena.lower().split() 
    
    for palabra in palabras:
        if palabra in frecuencia:  # Si la palabra ya está en el diccionario
            frecuencia[palabra] += 1
        else:  # Si es la primera vez que aparece
            frecuencia[palabra] = 1
    
    return frecuencia

def mayorFrecuencia(conteo): 
    palabra_max = ''
    frecuencia_max = 0
    
    for palabra, frecuencia in conteo.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return (palabra_max, frecuencia_max)

conteo = frecuenciaDePalabras(cadena)
print('Frecuencia de cada palabra:',conteo)
masFrecuencia = mayorFrecuencia(conteo)
print('Palabra mas frecuente:', masFrecuencia) 