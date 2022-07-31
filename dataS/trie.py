
class BTrie:
	class Node:
		def __init__(self):
			self.l = None
			self.r = None
			self.freq = 0

		def __str__(self) -> str:
			return "{ 0 : " + str(self.l) + ', 1 : ' + str(self.r)+ ' }'

	def __init__(self, MAX_BINARY_LEN = 32):
		self.root = self.Node()
		self.MAX_L = MAX_BINARY_LEN

	def __str__(self) -> str:
		return str(self.root)

	def insert(self, x):
		_node = self.root
		_node.freq += 1
		for i in range(self.MAX_L, -1, -1):
			bit = (x>>i)&1
			if not bit:
				if not _node.l:
					_node.l = self.Node()
				_node = _node.l
			else:
				if not _node.r:
					_node.r = self.Node()
				_node = _node.r
			_node.freq += 1

	def search(self, x):
		'''
		Search the element in the container and returns the count of element.
		Example: 
			arr = [1, 3, 5, 5, 6, 7, 9]

			search(3) => 1
			search(5) => 2
			search(4) => 0

		'''

		_node = self.root
		for i in range(self.MAX_L, -1, -1):
			_node = _node.r if (x>>i)&1 else _node.l
		if _node:
			return _node.freq
		return 0

	def get_count_less_then(self, k, or_equals_to = False):
		'''
		Find the count of elements less then the given value.

		Example:
			arr = [1, 3, 4, 6, 6, 7 ,7, 8]

			get_count_less_then(5) => 3
			get_count_less_then(7) => 5
			get_count_less_then(7, or_equals_to=True) => 7
		'''

		_node = self.root
		result = 0
		for i in range(self.MAX_L, -1, -1):
			if _node == None:
				break
			bit = (k>>i)&1
			if (bit == 1):
				if _node.l != None:
					result += _node.l.freq
				_node = _node.r
			else:
				_node = _node.l
		if or_equals_to and _node:
			result += _node.freq
		return result

	# def get_sum_less_then(self, k, x):
    #     _node = self.root
    #     result = 0
    #     for i in range(MAX_L, -1, -1):
    #         if _node == None:
    #             break
    #         prefixBit = (x>>i)&1
    #         bit = (k>>i)&1
    #         if (prefixBit == bit):
    #             if (prefixBit == 1) and _node.r != None:
    #                 result += _node.r.freq
    #             _node = _node.l
    #         else:
    #             if (prefixBit == 0) and _node.l != None:
    #                 result += _node.l.freq
    #             _node = _node.r


class Trie:
	class TrieNode:
		def __init__(self):
			self._children = {}
			self._end = 0
			self._freq = 0

		def __repr__(self):
			return self._children.__str__()

		def __sizeof__(self):
			return self._freq

	def __init__(self):
		self.root = self.TrieNode()

	def __repr__(self) -> str:
		return self.root._children.__str__()

	def __sizeof__(self) -> int:
		return len(self.root)

	def _charToIndex(self, ch):
		return ord(ch)-ord('a')

	def insert(self, key):
		_node = self.root
		for s in key:
			if s not in _node._children:
				_node._children[s] = self.TrieNode()
			_node._freq += 1
			_node = _node._children[s]
		_node._end += 1
		_node._freq += 1

	def search(self, key):
		_node = self.root
		for s in key:
			if s not in _node._children or _node._freq == 0:
				return 0
			_node = _node._children[s]
		return _node._end
	
	def prefix(self, key):
		_node = self.root
		for s in key:
			if s not in _node._children or _node._freq == 0:
				return 0
			_node = _node._children[s]
		return _node._freq
	
	def delete(self, key):
		_node = self.root
		if not self.search(key):
			return 0
		for s in key:
			_node._freq -= 1
			_node = _node._children[s]
		_node._end -= 1
		_node._freq -= 1
		return 1

if __name__ == '__main__':	

	# binary Trie
	BT = BTrie()
	BT.insert(12)
	BT.insert(5)
	BT.insert(5)
	BT.insert(2)
	print(BT)
	print(BT.get_count_less_then(5, or_equals_to=True))
	print(BT.search(5))

	print('='*100)

	# General Trie
	trie = Trie()
	trie.insert('shivam')
	trie.insert('prince')
	trie.insert('shiva')
	trie.insert('shiv')
	trie.insert('princes')
	trie.insert('shivsankar')
	print(trie)
	print(trie.prefix('shiv'))
	print(trie.search('shivam'))
	print(trie.delete('shivam'))
	print(trie.prefix('shiv'))