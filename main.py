from lists.vector import Vector
# from lists.linked_list import Linked_list
# from lists.doble_linked_list import Doble_linked_list
# from lists.circle_linked_list import Circle_linked_list

#Testes da classe Vetor
vetor = Vector(5,int)
vetor.insert(10)
vetor.insert(20)
vetor.insert(30)
print(vetor.get_vetor())
print(f'Busca: {vetor.get_by_value(20)}')
vetor.remove(1)
print(vetor.get_vetor())