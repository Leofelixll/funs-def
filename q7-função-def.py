# Exercício Python 07: Crie um programa que leia o valor de um produto e imprima o
# valor com desconto, tendo em vista que o desconto aplicado é de 10%.

def produto(a):
    valor_descontado = a * 0.1
    novo_valor = a * 0.90
    print(valor_descontado)
    print(novo_valor)
    
a = int(input("diguite o falor do produto: "))

produto(a)