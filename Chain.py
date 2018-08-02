from queue import Queue
from Block import Block

class Chain:
	
	trans = Queue()
	block_chain = []
	block_size = 1

	def __init__(self):
		gen_block = Block(1, "50 coin to miner", 0)
		gen_block.mine()
		Chain.add_block(gen_block)

	def add_block(block):
		Chain.block_chain.append(block)
		Chain.block_size += 1

	@staticmethod
	def add_data(data):
			Chain.trans.put(data)

	def create_block(self):
		print(Chain.trans.qsize())
		if Chain.trans.qsize() < 2:
			return "not enough transactions"
		else:
			data = '{}, {}'.format(Chain.trans.get(), Chain.trans.get())
			new_block = Block(Chain.block_size, data, Chain.last_hash())
			new_block.mine()
			Chain.add_block(new_block)
			return "added a block"
	
	def last_hash():
		return Chain.block_chain[-1].hash