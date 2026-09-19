from lists.vector import Vector
from lists.linked_list import Linked_list
# from lists.doble_linked_list import Doble_linked_list
# from lists.circle_linked_list import Circle_linked_list

#Testes da classe Vector
vetor = Vector(5,int)
vetor.insert(10)
vetor.insert(20)
vetor.insert(30)
print(vetor.get_vetor())
print(f'Busca: {vetor.get_by_value(20)}')
vetor.remove(1)
print(vetor.get_vetor())

#Testes da classe Linked_list
lista_simples = Linked_list()
lista_simples.append(5)
lista_simples.append(10)
lista_simples.append(9)
lista_simples.append(14)
lista_simples.append(2)
lista_simples.append(12)
print(lista_simples.display_list())
print(lista_simples.length)
lista_simples.remove(10)
print(lista_simples.display_list())
print(lista_simples.length)
print(lista_simples.get_index_by_value(5))