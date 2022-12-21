#I did it alone, Im proud of myself. Now the best is about to start! I will be so fucking success!

menu = """
Welcome to the currency converter, my first code 😉💵 

1 - Colombian pesos
2 - Argentinan pesos
3 - Mexican pesos

please choose and option to become it to U.S dollars: """

option = int(input(menu))

if option == 1:
    pesos = input('¿Cuantos pesos colombianos quieres convertir?: ')
    pesos = int(pesos)
    valor_dolar = 5000
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Hola, tienes ' + dolares + ' dolares')
elif option == 2:
    pesos = input('¿Cuantos pesos argentinos quieres convertir?: ')
    pesos = int(pesos)
    valor_dolar = 160
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Hola, tienes ' + dolares + ' dolares')
elif option == 3:
    pesos = input('¿Cuantos pesos mexicanos quieres convertir?: ')
    pesos = int(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Hola, tienes ' + dolares + ' dolares')
else:
    print('Please, select one of the options above.')



#dolares = input('How many dolars do you have?: ')
#dolares = int(dolares)
#valor_pesos = 5000
#pesos = dolares * valor_pesos
#pesos = str(pesos)
#print('Hello, you have ' + pesos + ' pesos')

#euros = input('How many Euros do you have? ')
#euros = int(euros)
#valor_pesos = 4700
#pesos = euros * valor_pesos
#pesos = str(pesos)
#print('Hello, my fren do you have ' + pesos + ' pesos')

# euros = input('how many euros do you have?: ')
# euros = int(euros)
# Valor_dolar = 1.03
# dolares = euros * Valor_dolar
# dolares = str(dolares)
# print('Great, you have ' + dolares + ' dolares')






