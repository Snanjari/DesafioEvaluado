import preguntas as p
eleccion = ""

def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    if alternativas == eleccion:
        alternativa = ['a', 'b', 'c','d'].index(eleccion)
        if eleccion in alternativas == eleccion:
            if eleccion == b:
                print("correcto")
            elif eleccion != b: 
                print("'Respuesta Incorrecta'")
    return alternativas



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)

