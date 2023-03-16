# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor,
# True se a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
# liga(): muda o estado da lâmpada para ligada
# desliga(): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
# Para testar sua classe: Ligue a Lampada , Imprima: A lâmpada está ligada? True
# Desligue a Lampada,  Imprima: A lâmpada ainda está ligada? False

class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada

# Criando uma lâmpada ligada
lampada = Lampada(True)

# Verificando se a lâmpada está ligada
print("A lâmpada está ligada?", lampada.esta_ligada()) # Saída: A lâmpada está ligada? True

# Desligando a lâmpada
lampada.desliga()

# Verificando se a lâmpada está desligada
print("A lâmpada ainda está ligada?", lampada.esta_ligada()) # Saída: A lâmpada ainda está ligada? False

