class Node:
    """Classe para representar um nó de uma lista encadeada
    Attributes:
        value(any): elemento a ser inserido no nó
        next(any): próximo elemento que por padrão é igual a None"""
    def __init__(self, value):
        self.value = value
        self.next = None
class Linked_list:
    """Classe para representar uma lista encadeada
    Attrbutes:
        head(any): Elemento que está no inicio da lista usada como ponto de referencia da lista
        length(int): Tamanho da lista encadeada"""
    def __init__(self):
        self.head = None
        self.length = 0
    def append(self, value):
        """Método criado para inserir valores ao final da lista encadeada
        utilizando a variável head como referência para a inserção.
        
        Args:
            value(any): elemento a ser inserido ao final da lista"""
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
        self.length += 1
    def remove(self, value):
        """Método que remove um elemento da lista encadeada
        utilizando o valor do elemento como referência
        
        Args:
            value(any): valor que referenciar o elemento que será deletado da lista encadeada"""
        before: Node = None
        current = self.head
        while current is not None:
            if current.value == value:
                if before is None:
                    self.head = current.next
                else:
                    before.next = current.next
                self.length -= 1
                return True
            before = current
            current = current.next
        return False
    def get_index_by_value(self, value) -> int:
        """Método que busca o indice de um elemento da lista encadeada
        baseado no valor a ser referenciado.
        Args:
            value(any): valor a ser referenciado para a busca do indice
        Returns:
            index(int): indice do valor que foi inserido
            -1: caso o valor não referencie nem um indice presente na lista"""
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    def display_list(self) -> list:
        """Método que mostra a lista de elementos presentes nela
        Returns:
            values([]any): elementos na lista"""
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return values