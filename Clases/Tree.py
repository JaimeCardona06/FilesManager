from Clases.Node import Node
import os

class Tree:
    def construir_arbol(path):
        #Construye un nuevo árbol utilizando la clase Node a partir un path como argumento
        raiz = Node(os.path.basename(path), path)

        for root, dirs, files in os.walk(path):
            nodo_actual = raiz

            for dir in root.split(os.sep)[1:]:
                nodo_hijo = None

                for hijo in nodo_actual.hijos:
                    if hijo.nombre == dir:
                        nodo_hijo = hijo
                        break

                if not nodo_hijo:
                    nodo_hijo = Node(dir, os.path.join(nodo_actual.path, dir))  # Actualizar el path
                    nodo_actual.agregar_hijo(nodo_hijo)

                nodo_actual = nodo_hijo

            for file in files:
                nodo_hijo = Node(file, os.path.join(nodo_actual.path, file))  # Actualizar el path
                nodo_actual.agregar_hijo(nodo_hijo)

        return raiz


def imprimir_arbol(nodo, nivel=0):
    print('  ' * nivel + '- ' + nodo.nombre)

    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)