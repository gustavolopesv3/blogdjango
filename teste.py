class Pilha :
    def __init__(self, tamanho) :
        self.tamanho = tamanho
        self.items = []
    def empilhar(self, item) :
        if self.__len__() < self.tamanho:
            self.items.append(item)
        else:
            print("A pilha está cheia")
    def desempilhar(self):
        if self.isEmpty():
            print("A pilha já está vazia.")
        else:
            return self.items.pop()
    def isEmpty(self) :
        return (self.items == [])
    def __len__(self):
        return len(self.items)
a = Pilha(1)

a.empilhar("A")
a.empilhar("B")
a.desempilhar()
a.desempilhar()
