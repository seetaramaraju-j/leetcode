class LRUCache:

    def __init__(self, capacity: int):
        self.mydict = OrderedDict(zip(range(1,capacity+1), [None]* capacity)) 
 

    def get(self, key: int) -> int:
        if self.mydict.get(key) != None :
            self.mydict.move_to_end(key, last=False)
            return self.mydict.get(key)
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.mydict.keys():        
                self.mydict[key] = value
                self.mydict.move_to_end(key, last=False)
        else:
            self.mydict.popitem(last=True)
            self.mydict.update({key: value})
            self.mydict.move_to_end(key, last=False)