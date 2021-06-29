import hashlib
import time

class Block(object):
    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
        self.index = index
        self.proof_number = proof_number
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def compute_hash(self):
        #come back later
        print("unfinished")

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genesis()

    def build_genesis(self):
        self.build_block(proof_number=0, previous_hash=0)

    def build_block(self, proof_number, previous_hash):
        block = Block(
            index=len(self.chain),
            proof_number=proof_number,
            previous_hash=previous_hash,
            data=self.current_data
        )

        self.current_data = []
        self.chain.append(block)

        return block

    @staticmethod
    def confirm_validity(block, previous_block):
        if previous_block.index + 1 != block.index:
            return False

        elif previous_block.compute_hash() != block.previous_hash:
            return False

        elif block.timestamp >= previous_block.timestamp:
            return False

        return True

    def get_data(self, sender, receiver, amount):
        self.current_data.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

        return True

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):
        self.get_data(
            sender="0",
            receiver=details_miner,
            quantity=1,
        )

        last_block = self.latest_block
        last_proof_number = last_block.proof_number
        proof_number = self.proof_of_work(last_proof_number)
        last_hash = last_block.compute_hash

        block = self.build_block(proof_number, last_hash)

        return vars(block)

bc = Blockchain()
print("READY")
print(bc.chain)
