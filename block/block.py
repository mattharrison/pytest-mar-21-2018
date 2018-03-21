"""
Basic blockchain implementation

http://bitcoin.org/bitcoin.pdf

* Coin - chain of digital signatures
* Chain - sequence of hashes. Hash(block of items, prev hash)
* Block - header(prev hash, nonce, hash), transaction
* Proof of work - Create value when hash starts with
  a certain number of zeros.
* Nodes - Each node collects transactions, then node
  mines the block. Each node tries to find POW, and broadcast
  it. Nodes accepts the block by working on the next block.
* Transaction - inputs and outputs. Normally 2 outputs.

>>> a = Amount('matt', 5)
>>> a.todict()
{'uuid': 'matt', 'amount': 5}
  
"""

# this is a comment


class Amount:
    def __init__(self, uuid, amount):
        self.uuid = uuid
        self.amount = amount

    def todict(self):
        return {'uuid': self.uuid, 'amount': self.amount}


class Transaction:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def todict(self):
        return {'inputs': [i.todict() for i in self.inputs],
                'outputs': [o.todict() for o in self.outputs]}
        

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
