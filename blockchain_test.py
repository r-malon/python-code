from hashlib import sha256
import json
from time import ctime

class BlockChain:
	def __init__(self):
		self.chain = []
		self.new_block('abcde', 1)
	def new_block(self, proof=None, prev_hash=None):
		block = {'index': len(self.chain), 'timestamp': ctime(),
		 'proof': proof or self.validate_proof(),
		 'prev_hash': prev_hash or self.hash(self.last_block)}
		self.chain.append(block)
		return block
	@staticmethod
	def hash(block):
		return sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
	@property
	def last_block(self):
		return self.chain[-1]
	def validate_proof(self):
		proof = 0
		while True:
			if self.hash(f"{self.last_block['proof']}{proof}")[:5] == 'abcde':
				#print(self.hash(f"{self.last_block['proof']}{proof}"))
				return proof
			proof += 1

if __name__ == '__main__':
	x = BlockChain()
	for i in range(40):
		print(x.new_block())