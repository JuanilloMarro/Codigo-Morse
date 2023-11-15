from binary_tree import BinaryTree

tree = BinaryTree()

tree.metodo_constructor()

while True:
	print('Laboratorio 3 - Código Morse\n1.Codificar\n2.Decodificar\n3.Salir')
	opcion = int(input('Ingrese una opción: '))

	if opcion == 1:

		sentence = input('Ingrese una palabra: ')

		morse = ''
		for i in sentence:
			morse = tree.get_path(i)

		print(f'Codigo en morse: {morse}')

		input('Presione alguna tecla para continuar...')
	elif opcion == 2:

		sentence = input('Ingrese una código en morse: ')

		text = tree.decode(sentence)

		print(f'Texto traducido: {text}')

		input('Presione alguna tecla para continuar...')
	elif opcion == 3:
		break
	else:
		raise Exception('No ingresaste una de las opciones disponibles :(')

