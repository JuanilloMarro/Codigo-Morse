from __future__ import annotations
from node import Node
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class BinaryTree(Generic[T]):
	def __init__(self):
		self.root: Node = Node('0')
		self.tree: str = ''

	def insert_left(self, data: T, ref: T|None = None):
		if ref is None:
			new_node = Node(data)
			self.root = new_node
		else:
			node = self.search(self.root, ref)
			if node is not None:
				new_node = Node(data)
				node.left = new_node
			else:
				raise Exception('Elemento no encontrado')

	def insert_right(self, data: T, ref:  T|None = None):
		if ref is None:
			new_node = Node(data)
			self.root = new_node
		else:
			node = self.search(self.root, ref)
			if node is not None:
				new_node = Node(data)
				node.right = new_node
			else:
				raise Exception('Elemento no encontrado')

	def search(self, subtree: Node[T] | None, ref:T) -> Node | None:

		if subtree is None:
			return None
		else:
			value = subtree.data
			if value == ref:
				return subtree

			node = self.search(subtree.left, ref)

			if node is not None:
				return node

			node = self.search(subtree.right, ref)
			return node


	def metodo_constructor(self):
		self.insert_left('_')

		self.insert_left('E', '_')
		self.insert_right('T', '_')

		self.insert_left('I', 'E')
		self.insert_right('A', 'E')

		self.insert_left('N', 'T')
		self.insert_right('M', 'T')

		self.insert_left('S', 'I')
		self.insert_right('U', 'I')

		self.insert_left('R', 'A')
		self.insert_right('W', 'A')

		self.insert_left('D', 'N')
		self.insert_right('K', 'N')

		self.insert_left('G', 'M')
		self.insert_right('O', 'M')

		self.insert_left('H', 'S')
		self.insert_right('V', 'S')

		self.insert_left('F', 'U')

		self.insert_left('L', 'R')

		self.insert_left('P', 'W')
		self.insert_right('J', 'W')

		self.insert_left('B', 'D')
		self.insert_right('X', 'D')

		self.insert_left('C', 'K')
		self.insert_right('Y', 'K')

		self.insert_left('Z', 'G')
		self.insert_right('Q', 'G')

	def __get_path(self, ref: T, subtree: Node[T] | None) -> str:
		if subtree is None:
			return ''
		else:
			root = subtree.data
			if root == ref:
				self.tree += ' '
				return self.tree

			left = self.__get_path(ref, subtree.left)

			if left != '':
				self.tree += '.'
				return self.tree

			right = self.__get_path(ref, subtree.right)

			if right != '':
				self.tree += '-'
				return self.tree
			else:
				return ''


	def get_path(self, i):
		return self.__get_path(i, self.root)

	def decode(self, sentence: str) -> str:
		result = ''
		node = self.root
		for i in sentence:
			if i == '.':
				node = node.left
			elif i == '-':
				node = node.right
			elif i == ' ':
				result += node.data
				node = self.root
		result += node.data
		return result

	def __preorder(self, subtree: Node[T] | None) -> str:

		if subtree is None:
			return '_'
		else:
			root = str(subtree.data)
			left = self.__preorder(subtree.left)
			right = self.__preorder(subtree.right)
			result = f'{root}({left}, {right})'

			return result

	def preorder(self):
		return self.__preorder(self.root)
