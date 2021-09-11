from time import time
import json
import hashlib


class Blockchain(object):
    def __init__(self):
        self.chain = []

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, block):
        if len(self.chain) > 0:
            block.prev = self.getLastBlock().hash
        else:
            block.prev = None
        self.chain.append(block)

    def chainJSONencode(self):
        blockArrJSON = []
        for block in self.chain:
            blockJSON = {}
            blockJSON['index'] = block.index
            blockJSON['hash'] = block.hash
            blockJSON['prev'] = block.prev
            blockJSON['time'] = block.time
            # blockJSON['nonse'] = block.nonse
            # blockJSON['tech'] = block.tech

            transactionsJSON = []
            tJSON = {}
            # for transaction in block.transactions:
            #     tJSON["time"] = transaction.time
            #     tJSON["sender"] = transaction.sender
            #     tJSON["reciever"] = transaction.reciever
            #     tJSON["amt"] = transaction.amt
            #     tJSON["hash"] = transaction.hash
            #     transactionsJSON.append(tJSON)

            # blockJSON['transactions'] = transactionsJSON

            blockArrJSON.append(blockJSON)

        return blockArrJSON

class Block(object):
    def __init__(self, transations, time, index):
        self.index = index # Block number
        self.transations = transations # Transation data
        self.time = time
        self.prev = '' # Hash of the previous block
        self.hash = self.calculateHash() # Hash of the block

    def calculateHash(self):
        hashTransations = ""
        for transation in self.transations:
            hashTransations += transation.hash

        hashString = str(self.time) + hashTransations + self.prev + str(self.index)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()


class Transaction(object):
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.time = time()
        self.hash = self.calculateHash()
    
    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amount) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()
