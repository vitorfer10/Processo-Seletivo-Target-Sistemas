#Questão 2 Target Sistemas

def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        print(f"{n} pertence à sequência de Fibonacci.")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
verifica_fibonacci(num)

