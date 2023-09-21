# This is the implementation of Hashmap in python
def hash_formula(string_key, bucket_num) -> int:
        # Initializing the hash variable
        hash_var = 0
        # loop through the entire string key
        for i in range(0, len(string_key)):
            # add up string Unicode representation to hash variable 
            hash_var += ord(string_key[i])
            # this function will return the index of the [key, value] pair
            # index will always be from 0 to bucket_num
        index = hash_var % bucket_num
        # returning the created index
        return index
    
class Hash_Table:
    def __init__(self) -> None:
        self.bucket_num = 4
        # Initializing array with size bucket_num + 1
        # This is done by default in JavaScript
        self.arr = list([None for _ in range(self.bucket_num + 1)])
        # specifying the number of buckets

    def add(self, key, value):
        # return creating the index after runing it through hash formula
        index = hash_formula(key, self.bucket_num)
        # if key does not exist
        if self.arr[index] == None:
            # add new [key, value] pair with the provided index
            self.arr[index] = [[key, value]]
            # return inserted [key, value] pair
            return list(self.arr[index][0])
        else:
            inserted = False
            # loop through the the indexed bucket
            for i in range(0, len(self.arr[index])):
                # if key is in the ith position
                if(self.arr[index][i][0] == key):
                    # print("yeah")
                    # insert the value next to its key
                    self.arr[index][i][1] = value
                    inserted = True
                # if the position is not empty (already has [key, value] pair)
            if inserted == False:
                # add a new [key, value] pair along side of the first one
                self.arr[index].append([key, value])
                # return inserted [key, value] pair
                return list(self.arr[index][1])
                
    def remove(self, key):
        print(self.arr)
        # return creating the index after runing it through hash formula
        index = hash_formula(key, self.bucket_num)

        if(len(self.arr[index]) == 1 and self.arr[index][0][0] == key): 
        # remove [key, value] pair
            del(self.arr[index])
        else:
            for i in range(0, len(self.arr[index])):
                # if key exists
                if(self.arr[index][i][0] == key):
                    # remove the [key, value] pair
                    del(self.arr[index][i])
                            
    def lookup(self, key):
        # return created index after runing it through hash formula
        index = hash_formula(key, self.bucket_num)
            
        # if key does not exists
        if self.arr[index] == None:
            # return not found
            return None
        else:
            # print(len(self.arr))
            # loop through the entire list
            for i in range(0, len(self.arr)):
                # if key exists in ith position
                if(self.arr[index][i][0] == key):
                    # return the value associated with the key
                    return list(self.arr[index][i][1])


def add(key, value):
    myHashTable = Hash_Table()
    return myHashTable.add(key, value)
   
    
def lookup(key):
    myHashTable = Hash_Table()
    return myHashTable.lookup(key)