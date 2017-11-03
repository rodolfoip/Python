teclado = input('Digite algo: ')
numerico = bool(teclado.isnumeric())
alpha = bool(teclado.isalpha())
alphaNum = bool(teclado.isalnum())
decimal = bool(teclado.isdecimal())
print('O valor digitado tem as seguintes informações: Numerico:', numerico, '| Alfabetico:', alpha, '| Alfa-numerico:',
      alphaNum, '| Decimal', decimal)
