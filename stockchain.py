from dataclasses import dataclass
from datetime import datetime
import hashlib
from typing import Any, List

@dataclass
class Block(): 
    shares: Any
    buyer_id: int
    seller_id: int
    trade_time: str = datetime.utcnow().strftime('%H:%M:%S')
    prev_hash: str = '0'
        
    def hash_block(self): 
        hash_algo=hashlib.sha256()
        trade_time=self.trade_time
        trade_time_encoded=trade_time.encode()
        hash_algo.update(trade_time_encoded)

        data=f'{self.shares}|{self.buyer_id}|{self.seller_id}'
        data_encoded=data.encode()
        hash_algo.update(data_encoded)
        
        prev_hash_encoded=self.prev_hash.encode()
        hash_algo.update(prev_hash_encoded)

        return hash_algo.hexdigest()

@dataclass
class StockChain(): 
    chain: List[Block]
    
    def add_block(self, new_block): 
        self.chain.append(new_block)