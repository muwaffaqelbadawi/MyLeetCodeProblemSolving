# This is the implementation of Hashmap in python

def hash_formula(string_key, bucket_num) -> int:
        hash_var = 0
        for i in range(string_key.length):
            hash_var += ord(i)
        index = hash_var % bucket_num
        return index

class Hash_Table:
    def __init__(self, string_key, bucketNum) -> None:
        self.arr = []
        self.string_key = string_key
        self.bucketNum = bucketNum

    def Add(self, key, value) -> None:
        # creating the index after runing it through hash formula
        index = hash_formula(key)
        # if key does not exist
        if self.arr[index] == None:
            return None
        # loop through the entire list
        for i in range(0, len(self.arr)):
            # if the key is in the ith position
            if(self.arr[index][i][0] == key):
                # insert the value next to its key
                self.arr[index] = [[key, value]]
            else:
                # if location is not empty
                inserted = False # initialize inserted flag and set it to false
                for i in range(0, len(self.arr)):
                    if(self.arr[index][i][0] == key):
                        # 0 is the key and 1 is the key
                        self.arr[index][i][1] == value
                        inserted = True
                # if the position is not empty (already has key and value pair)
                if inserted == False:
                    # add a new key, value pair along side of the first one
                    # [ [[key, value], [key, value]], [[key, value]] ]
                    self.arr[index].append([key, value])

            
    def remove(self, key) -> None:
        # creating the index after runing it through hash formula
        index = hash_formula(key)
        # if key does not exist
        if self.arr[index] == None:
            return None
        
        # loop through the entire list
        for i in range(0, len(self.arr)):
            # if there's only one element in the array and key exist
            if(len(self.arr) == 1 & key == self.arr[index][i][0]): 
              # remove the item
                self.arr[index].remove()
            else:
                # loop through the entire list
               for i in range(0, len(self.arr)):
                # if key exist
                   if(self.arr[index][i][0] == key):
                    # remove the [key, value] pair
                       self.arr[index][i][0].remove()

                
    def lookup(self, key) -> None:
        # creating the index after runing it through hash formula
        index = hash_formula(key)
        # if key does not exist
        if self.arr[index] == None:
            pass
        # loop through the entire list
        for i in range(0, len(self.arr)):
            # if there's only one element in the array and key exist
            if(len(self.arr) == 1 & key == self.arr[i][0]):
                pass
            
            
    
    
my_hash_table = Hash_Table("hash", 5)