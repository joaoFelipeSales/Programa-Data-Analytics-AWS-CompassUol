# Escreva um código Python para imprimir todos os números primos entre 1 até 100.
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
#Importante: Aplique a função range().


def eh_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

for i in range(1, 100):
    if eh_primo(i):
        print(i)