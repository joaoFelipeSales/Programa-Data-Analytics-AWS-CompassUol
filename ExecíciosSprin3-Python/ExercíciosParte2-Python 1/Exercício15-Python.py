# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor,
# True se a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
# liga(): muda o estado da lâmpada para ligada
# desliga(): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
# Para testar sua classe: Ligue a Lampada , Imprima: A lâmpada está ligada? True
# Desligue a Lampada,  Imprima: A lâmpada ainda está ligada? False

class Lampada:
    def __init__(self, estado):
        self.estado = estado

    def liga(self):
        self.estado = True

    def desliga(self):
        self.estado = False

    def esta_ligada(self):
        return self.estado
    
    # Criando objeto lampada com estado inicial como True
lampada = Lampada(True)

# Ligar a lâmpada
lampada.liga()

# Verificar se a lâmpada está ligada
print("A lâmpada está ligada?", lampada.esta_ligada())

# Desligar a lâmpada
lampada.desliga()

# Verificar se a lâmpada ainda está ligada
print("A lâmpada ainda está ligada?", lampada.esta_ligada())
