'''
Class to hold nodes that represent articles
Each node holds the name of the current article and the name of the parent article.
'''

class WikiNode:
	def __init__(self, parent, name):
		self.parent = parent
		self.name = name

	def __getitem__(self, key):
		return self