from pizza import Pizza,validar,pedido_pizza

# A
print(f'Pizza.vegetales: {Pizza.vegetales}\nPizza.proteicos: {Pizza.proteicos}\nPizza.tipo_masa: {Pizza.tipo_masa}\nPizza.precio: {Pizza.precio}\nPizza.tamaño: {Pizza.tamaño}')

# B
salsas = ["salsa de tomate", "salsa bbq"]
salsa = 'salsa de tomate'

if validar(salsa,salsas):
    print(f'La {salsa} se encuentra presente en la lista {salsas}')
else:
    print(f'La {salsa} no se encuentra presente en la lista {salsas}')
    
# C
my_pizza = Pizza()
pedido_pizza(my_pizza)

# D
print(f'''  Pizza con ingrediente proteico de {my_pizza.proteicos},
            ingredientes vegetales: {my_pizza.vegetales_1} y {my_pizza.vegetales_2},
            el tipo de masa es {my_pizza.tipo_masa},
            la pizza validada es: {my_pizza.valida}
''')

# E
my_pizza.proteicos = Pizza.proteicos
my_pizza.vegetales_1 = Pizza.vegetales
my_pizza.vegetales_2 = Pizza.vegetales
my_pizza.tipo_masa = Pizza.tipo_masa
pedido_pizza(my_pizza)

if not (validar(my_pizza.pizza.proteicos, Pizza.proteicos) and validar(my_pizza.pizza.vegetales_1, Pizza.vegetales) and validar(my_pizza.pizza.vegetales_2, Pizza.vegetales) and validar(my_pizza.pizza.tipo_masa, Pizza.tipo_masa)):
    print(f'Es una pizza no válida')
    my_pizza.pizza.valida = False
else:
    print(f'Es una pizza válida')
    my_pizza.pizza.valida = True