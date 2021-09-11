from Blockchainv2 import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

blockchain = Blockchain()
transactions = []

block = Block(transactions, time(), 0)
blockchain.addBlock(block)

block = Block(transactions, time(), 1)
blockchain.addBlock(block)

print(blockchain.chainJSONencode())
