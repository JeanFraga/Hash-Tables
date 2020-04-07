# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)] is None:
            # print(value)
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
            # self.storage[self._hash(key)].next = None
            return
        else:
            current_pointer = self.storage[self._hash_mod(key)]
            if current_pointer.key == key:
                current_pointer.value = value
                return
            while current_pointer.next:
                current_pointer = current_pointer.next
                if current_pointer.key == key:
                    current_pointer.value = value
                    return
                # if self.storage[self._hash_mod(key)].key == key:
                #     self.storage[self._hash_mod(key)].value = value
                #     return
            # current_pointer = current_pointer.next
            current_pointer.next = LinkedPair(key, value)
            return
            # return "error"



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # while self.storage[self._hash_mod(key)].next:

        starting_pointer = self.storage[self._hash_mod(key)]
        if self.storage[self._hash_mod(key)].key == key:
            if self.storage[self._hash_mod(key)].next:
                self.storage[self._hash_mod(key)] = self.storage[self._hash_mod(key)].next
                # print("test1")
                # print(f"{key}")
                return
            self.storage[self._hash_mod(key)] = None
            return
        # current_pointer = self.storage[self._hash_mod(key)]
        while self.storage[self._hash_mod(key)].next:
            if self.storage[self._hash_mod(key)].next.key == key:
                if self.storage[self._hash_mod(key)].next.next:
                    self.storage[self._hash_mod(key)] = self.storage[self._hash_mod(key)].next.next
                self.storage[self._hash_mod(key)].next = None
                self.storage[self._hash_mod(key)] = starting_pointer
                return
            self.storage[self._hash_mod(key)] = self.storage[self._hash_mod(key)].next
        print("key is not found")
        self.storage[self._hash_mod(key)] = starting_pointer

            # previous_pointer = self.storage[self._hash_mod(key)]
            # self.storage[self._hash_mod(key)] = self.storage[self._hash_mod(key)].next
            # if self.storage[self._hash_mod(key)].key == key:
            #     if self.storage[self._hash_mod(key)].next:
            #         next_pointer = self.storage[self._hash_mod(key)].next
            #         previous_pointer.next = next_pointer
            #     self.storage[self._hash_mod(key)] = None
                # current_pointer = None
                # return
            # current_pointer = current_pointer.next
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)]:
            # values = []
            # values.append(self.storage[self._hash_mod(key)].value)
            current_pointer = self.storage[self._hash_mod(key)]
            if current_pointer.key == key:
                # print(current_pointer.value)
                return current_pointer.value
            while current_pointer.next:
                current_pointer = current_pointer.next
                if current_pointer.key == key:
                    # print(current_pointer.value)
                    return current_pointer.value
                # values.append(current_pointer.value)
        # print(f"not found value for key: {key}")
        return None
            # return self.storage[self._hash_mod(key)].value
        # else:
        #     return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        tempstorage = self.storage
        self.storage = [None] * self.capacity
        for i in tempstorage:
            if i:
                self.insert(i.key, i.value)
                while i.next:
                    i = i.next
                    self.insert(i.key, i.value)




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
