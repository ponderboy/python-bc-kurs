import time
from hashlib import sha256


class BlockChain:

    def __init__(self, init_hash="0000", difficulty=2):
        self.init_hash = init_hash
        self.blocks = []
        self.index = 0
        self.difficulty = difficulty
        self.currentNonce = 0

    def append(self, transactions):
        self.index += 1
        if len(self.blocks) > 0:
            previous_hash = self.blocks[-1].hash
        else:
            previous_hash = self.init_hash
        block = Block(self.index, transactions, time.time(), previous_hash, self.difficulty)
        self.blocks.append(block)
        self.currentNonce += block.nonce

class Block:

    # Konstruktor
    def __init__(self, index, transactions, timestamp, previous_hash, difficulty):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self):
        hash = ""
        while not hash.startswith("0" * self.difficulty):
            self.nonce += 1
            string_to_hash = "{0} {1} {2} {3} {4}".format(
                self.index,
                self.transactions,
                self.timestamp,
                self.previous_hash,
                self.nonce
            )
            hash = sha256(string_to_hash.encode("utf-8")).hexdigest()
        return hash
