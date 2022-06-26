try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError,TypeError):
    print(f'Problema com os tipos de dados')
except ZeroDivisionError:
    print('Divisão por zero')
except KeyboardInterrupt:
    print('O usuário não informou os dados')
except Exception as erro:
    print(erro.__cause__)
else:
    print(f'O numero digitado foi o: {r:.1f}')
finally:
    print('Volte sempre')