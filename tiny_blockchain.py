import hashlib as hashme
import datetime as dt

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashme.sha256()
        sha.update((str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.prev_hash)).encode())
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, dt.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    new_index = last_block.index + 1
    new_timestamp = dt.datetime.now()
    new_data = "This is block " + str(new_index)
    new_hash = last_block.hash
    return Block(new_index, new_timestamp, new_data, new_hash)

myblockchain = [create_genesis_block()]
prev_block = myblockchain[0]

num = 20

for i in range(num):
    block_to_add = next_block(prev_block)
    myblockchain.append(block_to_add)
    prev_block = block_to_add
    print("Block #{} has been added to your blockchain".format(prev_block.index))
    print("Hash: {}\n".format(prev_block.hash))
