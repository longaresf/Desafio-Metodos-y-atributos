class Pizza():
    vegetales:list = ['tomate','aceitunas','champiñones']
    proteicos:list = ['pollo', 'vacuno','carne vegetal']
    tipo_masa:list = ['tradicional','delgada']
    precio:int = 10000
    tamaño:str = 'familiar'

pizza = Pizza()
pizza.proteicos = ''
pizza.vegetales_1 = ''
pizza.vegetales_2 = ''
pizza.tipo_masa = ''
pizza.valida = False

@staticmethod
def validar(item,lista_item):
    return item in lista_item

def pedido_pizza(pizza):
    pizza.proteicos = input('¿Qué tipo de proteína deseas? \n Pollo\n Vacuno\n Carne Vegetal\n Opcion: ')
    pizza.vegetales_1 = input(f'\n¿Cual vegetal desea agregar como primer ingrediente? \n Tomate\n Aceitunas\n Champiñones\n Opcion: ')
    pizza.vegetales_2 = input(f'\n¿Cual vegetal desea agregar como segundo ingrediente? \n Tomate\n Aceitunas\n Champiñones\n Opcion: ')
    pizza.tipo_masa = input('¿Cuál tipo de masa desea para su pizza? \n tradicional\n delgada\n Opcion: ')

    print(f'Pizza de: {pizza.proteicos}, 1er ingrediente vegetal: {pizza.vegetales_1}, 2do ingrediente vegetal: {pizza.vegetales_2}, tipo de masa: {pizza.tipo_masa}')

    if not (validar(pizza.proteicos, Pizza.proteicos) and validar(pizza.vegetales_1, Pizza.vegetales) and validar(pizza.vegetales_2, Pizza.vegetales) and validar(pizza.tipo_masa, Pizza.tipo_masa)):
        print(f'Es una pizza no válida')
        pizza.valida = False
    else:
        print(f'Es una pizza válida')
        pizza.valida = True

pedido_pizza(pizza)

