class Node:
    def __init__(self, nombre, path):
        self.nombre = nombre
        self.path = path
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    