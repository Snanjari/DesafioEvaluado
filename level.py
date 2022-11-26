
def choose_level(n_pregunta, p_level):
        if n_pregunta in [1, 2] and p_level == 2:
            level = "basicas"
        elif n_pregunta in [1, 2, 3] and p_level ==3:
            level = "basicas"
        if n_pregunta in [3, 4] and p_level == 2:
            level = "intermedias"
        elif n_pregunta in [4,5,6] and p_level == 3:
            level = "intermedias"
        if n_pregunta in [5,6] and p_level == 2:
            level = "avanzadas"
        elif n_pregunta in [7, 8, 9] and p_level == 3:
            level = "avanzas"
        return level 

if __name__ == '__main__':
    # verificamos los resultados
        print(choose_level(2, 2)) # básicas
        print(choose_level(3, 2)) # intermedias
        print(choose_level(6, 2)) # avanzadas
        print(choose_level(4, 3)) # intermedias
