#importar libreria para generar codigos aleatorios
import random
import string

#clase base para representar cualquier material de la biblioteca
class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        #atributos privados
        self._titulo = titulo
        self._autor = autor
        self._codigo = self._generar_codigo()
        self._prestado = False
    
    #metodo privado para generar un codigo aleatorio de 8 caracteres 
    def _generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    #metodo para prestar el material
    def prestar(self):
        if not self._prestado:
            self._prestado = True
            print('***material prestado con exito')
        else:
            print('***el material no esta disponible, pendiente de devolver')
    
    #metodo para devolver el material
    def devolver(self):
        if self._prestado:
            self._prestado = False
            print('***material devuelto con exito')
        else:
            print('***el material no estaba prestado')
    
    #metodo para mostrar la informacion general
    def mostrar_info(self):
        print('codigo:', self._codigo)
        print('titulo:', self._titulo)
        print('autor:', self._autor)
        print('prestado:', 'si' if self._prestado else 'no')

#clase libro fisico que hereda de materialbiblioteca
class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self._numero_ejemplar = numero_ejemplar
        self._dias_prestamo = 7  #tiempo maximo
    
    #sobrescritura de mostrar_info para incluir atributos adicionales
    def mostrar_info(self):
        super().mostrar_info()
        print('numero de ejemplar:', self._numero_ejemplar)
        print('dias maximo de prestamo:', self._dias_prestamo)

#clase libro digital que hereda de materialbiblioteca
class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamano_mb):
        super().__init__(titulo, autor)
        self._tamano_mb = tamano_mb
        self._dias_prestamo = 3  #tiempo maximo
    
    #sobrescritura de mostrar_info para incluir atributos adicionales
    def mostrar_info(self):
        super().mostrar_info()
        print('tamano del archivo (mb):', self._tamano_mb)
        print('dias maximo de prestamo:', self._dias_prestamo)

#lista para almacenar los materiales registrados
biblioteca = []

#funcion para registrar un nuevo material
def registrar_material():
    print('1. libro fisico')
    print('2. libro digital')
    opcion = input('seleccione tipo de material: ')
    

    
    if opcion == '1':
        titulo = input('ingrese titulo: ')
        autor = input('ingrese autor: ')
        ejemplar = input('ingrese numero de ejemplar: ')
        libro = LibroFisico(titulo, autor, ejemplar)
        biblioteca.append(libro)
        print('libro fisico registrado con exito')
    elif opcion == '2':
        titulo = input('ingrese titulo: ')
        autor = input('ingrese autor: ')
        tamano = input('ingrese tamano del archivo en MB: ')
        libro = LibroDigital(titulo, autor, tamano)
        biblioteca.append(libro)
        print('***libro digital registrado con exito!!')
    else:
        print('no existe ese tipo de libro')

#funcion para gestionar materiales existentes
def gestionar_material():
    if not biblioteca:
        print('***no hay materiales registrados')
        return
    
    #mostrar lista de materiales
    for i, mat in enumerate(biblioteca):
        print(i+1, '~', mat._titulo)
    
    indice = int(input('seleccione numero de material: ')) - 1
    if 0 <= indice < len(biblioteca):
        material = biblioteca[indice]
        print('1. prestar')
        print('2. devolver')
        print('3. mostrar informacion')
        opcion = input('seleccione una opcion: ')
        
        if opcion == '1':
            material.prestar()
        elif opcion == '2':
            material.devolver()
        elif opcion == '3':
            material.mostrar_info()
        else:
            print('opcion invalida')
    else:
        print('indice invalido')

#funcion principal con menu
def menu():
    while True:
        print('~~~~~~ MENU ~~~~~~')
        print('1. registrar material')
        print('2. gestionar material')
        print('3. salir')
        opcion = input('***seleccione una opcion: ')
        
        if opcion == '1':
            registrar_material()
        elif opcion == '2':
            gestionar_material()
        elif opcion == '3':
            print('hasta luego!! :D')
            break
        else:
            print('***opcion invalida')

#ejecutar menu
if __name__ == '__main__':
    menu()
3