import hashlib

class Block:
	

	def __init__(self, number, data, phash):
		self.number = number
		self.data = data
		self.nounce = 0
		self.phash = phash
		self.hash = ""

	def __repr__(self):
		return '{}{}{}{}'.format(self.number, self.data, self.nounce, self.phash)

	def __str__(self):
		#hash for debug
		return 'blocknumber: {}\ndata: {}\nnounce: {}\npervious hash: {}\nhash: {}'.format(self.number, self.data, self.nounce, self.phash, self.hash)

	def hash256(self):
			repr = str(self).encode()
			return hashlib.sha256(repr).hexdigest()
	
	def mine(self):
		flag = True
		while(flag):
			if self.hash.startswith("00"):
				flag = False
			else:
				self.nounce += 1
				self.hash = self.hash256()