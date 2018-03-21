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
import hashlib
import json

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
        

class Block:
    def __init__(self, txns, prev_hash):
        self.prev_hash = prev_hash
        self.txns = txns
        self.nonce = None

    def todict(self, nonce=None):
        nonce = nonce if nonce is not None else self.nonce
        body = {'txns': [txns.todict() for txns in self.txns]}
        headers = {'prev_hash': self.prev_hash,
                   'body_hash': get_hash(body),
                   'nonce': nonce}
        data = {'header': headers,
                'body': body}
        return data


def get_hash(dict_data):
    sha = hashlib.sha256()
    data = json.dumps(dict_data, sort_keys=True)
    sha.update(data.encode('utf-8'))
    return sha.hexdigest()
    
    
                   

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
