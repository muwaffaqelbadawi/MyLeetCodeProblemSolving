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
        self.arr = [None for _ in range(self.bucket_num + 1)]
        # specifying the number of buckets

    def add(self, key, value):
        # return creating the index after runing it through hash formula
        index = hash_formula(key, self.bucket_num)
        
        # if key does not exist
        if self.arr[index] == None:
            # add new [key, value] pair with the provided index
            self.arr[index] = [[key, value]]
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
                # [ [ [key, value], [key, value] ], [ [key, value] ] ]
                self.arr[index].append([key, value])
                
    def remove(self, key):
        # return creating the index after runing it through hash formula
        index = hash_formula(key, self.bucket_num)
        
        # if key does not exists
        if self.arr[index] == None:
            # loop through the entire list
            for i in range(0, len(self.arr)):
                # if there's only one element in the array and key exists
                # in the specified index
                if(len(self.arr) == 1 and self.arr[index][i][0] == key): 
                # remove the item [key, value] pair uding the returned index
                    self.arr[index].remove()
                else:
                    # loop through the entire list
                    for i in range(0, len(self.arr)):
                        # if there are more than one item in the array and key exists
                        if(self.arr[index][i][0] == key):
                            # remove the key
                            self.arr[index][i][0].remove()

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
                    return self.arr[index][i][1]


    
my_hash_table = Hash_Table()
my_hash_table.add("muwaffaq", "person")
my_hash_table.add("max", "music")
my_hash_table.add("Alice", "girl")
my_hash_table.add("Tesla", "car")

print(my_hash_table.lookup("Tesla"))
