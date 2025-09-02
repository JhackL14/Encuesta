#Joel Garcia

#nombre, carrera, idea de proyecto
def encuesta():
    Resultados ={}
    for i in range(6):
        nombre = input(f'Ingrese Nombre {i}: ')
        carrera = input(f'Ingrese carrera {i}: ')
        idea_proyecto = input(f'Ingrese idea de proyecto {i}: ')
        Resultados[f'{nombre}{i}'] = (carrera,idea_proyecto)
    print(Resultados)
   
def main():
    #descuento()
    encuesta()
if __name__ == '__main__':
    main()
