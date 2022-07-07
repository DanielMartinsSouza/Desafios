import os
os.system('cls')

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
def fib(n):
    fibo = 0
    if n == 1:
        n = 1
        return n
    
    if n == 2:
        n = 1
        return n

    fibo = fib(n-2) + fib(n-1)
    return fibo

a = fib(7)

print(a)

#5) Escreva um programa que inverta os caracteres de um string
texto1 = str(input(print("Insira o texto: ")))
texto2 = ""

for i in texto1:
    texto2 = i + texto2

print(texto2)


