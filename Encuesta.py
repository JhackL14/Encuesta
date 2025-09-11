#Joel Garcia

#nombre, carrera, idea de proyecto
class Encuesta:
    def __init__(self):
        self.resultados ={}
        print('Las preguntas de la encuesta son: Nombre, Edad, Idea de proyecto, ¿Conoces alguna libreria de python?')
        if self.resultados != {}:
            print(self.resultados)
            
    def encuesta(self):
        self.resultados
        for i in range(10):
            nombre = input(f'Ingrese Nombre {i+1}: ')
            idea_proyecto = input(f'Ingrese idea de proyecto {i+1}: ')
            edad = input('Ingrese su edad: ')
            equipo = input('¿Le gusta trabajar en equipo?: ')
            self.resultados[f'{i}'] = (nombre,idea_proyecto,edad, equipo)
            print('----------------')
        print(self.resultados)

    def mostrar_resultados(self):
        if self.resultados != {}:
            for i in range(10):
                n = str(i)
                print(f'{self.resultados[n][0]}, {self.resultados[n][1]}, {self.resultados[n][2]}, {self.resultados[n][3]}\n----------------')
        else: print('No hay respuestas')

    def resumen(self):
        for i in range(10):
            n = str(i)
            print(f'{self.resultados[n][0]}, {self.resultados[n][1]} \n----------------')


    class Estudiante:
        def __init__(self):
            self.nombre = input(f'Ingrese Nombre: ')
            self.edad = input(f'Ingrese carrera: ')
            self.respuesta_proyecto = input('Ingresa Idea de proyecto')
        def respuestas(self):
            print(self.nombre, self.edad, self. respuesta_proyecto)
            
        
            

    
    # def agregar_respuesta(self):
    #     nombre = input(f'Ingrese Nombre: ')
    #     edad = input(f'Ingrese carrera: ')
    #     idea_proyecto = input(f'Ingrese idea de proyecto: ')
    #     self.resultados[f'{nombre}'] = (edad ,idea_proyecto)
    #     print(self.resultados)


Encuesta1 = Encuesta()
Encuesta1.encuesta()
Encuesta1.mostrar_resultados()
Encuesta1.resumen()
