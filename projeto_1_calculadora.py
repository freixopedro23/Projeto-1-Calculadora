# Código que simula o funcionamento de uma calculadora simples
while True:

    # Entrada dos valores
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')

    # Teste para verificar se o usuário não digitou letras ao invés de números
    try:
      num1_float = float(num1)
      num2_float = float(num2)
    except ValueError:
      print('Você digitou algum caracter errado. Tente novamente!')
      continue

    # Lógica das operações matemáticas
    operacao = input('\nPor favor digite o sinal da operação desejada:\n[+]ADIÇÃO [-]SUBTRAÇÃO [*]MULTIPLIAÇÃO [/]DIVISÃO\n')
    valor_final = 0
    if operacao == '+':
      valor_final = num1_float + num2_float
      print(f'\nO resultado da SOMA é {valor_final:.2f}\n')
    elif operacao == '-':
      valor_final = num1_float - num2_float
      print(f'\nO resultado da SUBTRAÇÃO é {valor_final:.2f}\n')
    elif operacao == '*':
      valor_final = num1_float * num2_float
      print(f'\nO resultado da MULTIPLICAÇÃO é {valor_final:.2f}\n')
    elif operacao == '/':
      valor_final = num1_float / num2_float
      print(f'\nO resultado da DIVISÃO é {valor_final:.2f}\n')
    else:
      print('\nVocê não digitou uma operação válida. Tente novamente.\n')
      continue

    # Breaks do loop
    decisao = input('Deseja encerrar a calculadora?\n[S]IM [N]ÃO\n')
    if decisao == 'S' or decisao == 's':
      break
    elif decisao != 'N' and decisao != 'n':
      print('Você digitou um caracetere inválido. Encerraremos a calculadora')
      break
