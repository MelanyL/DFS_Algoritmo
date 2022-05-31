# Importamos la libreria Queue
from queue import Queue
#Creamos la clase denominada Grafo
class Grafo():
    """
    En esta clase mostrará a un grafo en conjunto con sus atributos y métodos respectivas de este, los atributos son los siguientes:

    Atributos:
        m_numero_nodos : int -----> Cantidad de nodos que contendrá el gráfo.
        m_nodos : int -----> Rango de nodos en donde trabajará el gráfo.
        m_dirigido : boolean ------> Tipo de nodo ya sea dirigido o no dirigido.
        m_lista_adyacencia : diccionario ------> Diccionario que almacena el valor de los nodos de la lista de adyacencia. 

    Métodos:

        __init__(self, num_de_nodos, dirigido=True), este método hará la función de constuctor de la clase denominada 'Grafo()', en donde recepta el número de nodos (m_num_nodos), y posteriormente crea el rango de nodos (numero_nodos), a continuación, determina el tipo de grafo si es dirigido o no dirigido dependiendo del caso (m_dirigido) y para finalizar se creará el diccionario de la lista de adyacencia.

        agregar_borde(self, nodo1, nodo2, peso=1), este método genera los bordes de la lista de adyacencia asignando el nodo 2 a la lista de adyacencia del nodo 1.
        
        Imprimir_lista_adyacencia(self), este método permite imprimir el grafo generado en base a la lista de adyacencia, bfs_transversal(self, nodo_de_inicio), este método imprime el recorrido BFS de un vértice fuente dado de la lista de adyacencia.
        
        dfs(self, inicio, objetivo, ruta = [], visitado = set()), este método imprime el recorrido BFS de un vértice fuente dado.
    """