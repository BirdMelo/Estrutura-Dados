class Vector:
    """Simula um vetor para praticar em exercicios de Algoritmo e Estrutura de Dados

    Attributes:
        capacity (int): capacidade maxima do vetor
        data (list): estrutura do vetor
        quantity (int): quantidade de elementos no vetor
        data_type (type): defini o tipo de dado que o array é
    """
    def __init__(self,capacity: int, data_type: type):
        self.capacity = capacity
        self.data = [None] * capacity
        self.quantity = 0
        self.data_type = data_type
    def _is_egual_type(self, value):
        """Método privado para validar se o valor corresponde ao data_type exigido.
        Args:
            value(any): valor a ser verificado se possui a tipagem correta"""
        if not type(value) == self.data_type:
            raise TypeError(f"Tipo de dado errado.\nCorreto: {self.data_type.__name__}\nEnviado: {type(value).__name__}")
    def _is_full(self) -> bool:
        """Método que retorna um boleano verificando se o vetor está cheio ou não
        Returns:
            bool: se quantity está igual capacity"""
        return self.quantity == self.capacity
    def _is_empty(self) -> bool:
        """Método que retorna um boleano verificando se o vetor está vazio ou não
        Returns:
            bool: se quantity está igual a zero"""
        return self.quantity == 0
    def get_vetor(self) -> tuple:
        """Método que retorna o vetor
        Returns:
            tuple: uma tupla mostrando todos os dados do vetor"""
        return (self.data[:self.quantity])
    def get_by_id(self, index: int) -> any:
        """Método que retorna um elemento da lista
        Args:
            index(int): indice que está o elemento a ser buscado
        returns:
            any: elemento que está presente no indice no parametro"""
        if 0 <= index < self.quantity:
            return self.data[index]
        raise IndexError("Indice invalido")
    def update(self, index: int, value) -> None:
        """Método para atualizar um indice com um novo valor
        Args:
            index(int): indice que será atualizado
            value(any): valor que substituirá o atual"""
        self._is_egual_type(value)
        if 0 <= index < self.quantity:
            self.data[index] = value
        else:
            raise IndexError("Indice invalido")
    def insert(self, value, position: int = None):
        """Método para inserir um dano no vetor, empurrando os outros elementos para os lados
        Args:
            value(any): valor a ser inserido
            position=None(int): posição que o valor será inserido"""
        if self._is_full():
            raise OverflowError("vetor cheio")
        if position is None:
            position = self.quantity
        for i in range(self.quantity, position, -1):
            self.data[i] = self.data[i - 1]
        self.data[position] = value
        self.quantity += 1
    def remove(self, position: int) -> any:
        """Método para remover elemento do vetor
        Args:
            position(int): posição do valor que será removido
        Returns:
            any: valor removido"""
        if not (0 <= position < self.quantity):
            raise IndexError("Posição invalida")
        removed_value = self.data[position]
        for i in range(position, self.quantity - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.quantity - 1] = None
        self.quantity -= 1
        return removed_value
    def get_by_value(self, value) -> int:
        """Método para buscar indice pelo elemento presente no indice
        Args:
            value(any): elemento referencia para buscar o indice
        Returns:
            int: indice do valor
            int: -1 caso não encontrar o indice com o elemento"""
        for i in range(self.quantity):
            if self.data[i] == value:
                return i
        return -1