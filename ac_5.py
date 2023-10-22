'''Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

n = int(input('Digite um valor para "n", sendo "n" a quantidade de linhas: '))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


print('-'*70)
'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''

num_int = input('Digite um número inteiro qualquer: ')
print('Esse número possue', len(num_int), 'digito(s)')

print('-'*70)

try:
    numero1 = int(input('Digite o primeiro número inteiro: '))
    numero2 = int(input('Digite o segundo número inteiro: '))
    resultado = numero1 / numero2
except ValueError:
    print('Algo está errado! Um ou ambos os valores não são números inteiros válidos.')
except ZeroDivisionError:
    print('Algo está errado! Divisão por zero não é permitida.')
else:
    print('Resultado da divisão:', resultado)
finally:
    print('Fim do script.')