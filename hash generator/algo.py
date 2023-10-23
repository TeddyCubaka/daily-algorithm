with open('hashes') as h :
    hashes = h.read().strip().split('\n\n')
    # alphabet = hashes[0]
    # nums = hashes[1]
    # blank = hashes[2]

class hash :
    def __init__(self, hashes) :
        self.hashes = [i.split("\n") for i in hashes]
        self.alphabet = hashes[0]
        self.nums = hashes[1]
    def letters (self, index) : 
        if index >= len(self.alphabet) or index < 0 : return "Invalid index"
        return self.alphabet(index)
    def nums (self,index) : return self.nums[index]
    def blank (self) : return self.hashes[2]

hash(hashes=hashes)
def crypter(str) :
    str = str.upper()
    strCrypted = ""
    for char in str :
        if ord(char) == 32 : strCrypted = strCrypted + hash.blank()
        elif ord(char) >= 65 and ord(char) <= 90 :
            strCrypted = strCrypted + hash.letters[ord(char) - 65]
        elif ord(char) >= 48 and ord(char) <= 57 :
            strCrypted = strCrypted + nums[ord(char) - 65]
        else : strCrypted = strCrypted + char + char
    return strCrypted

# print(crypter("Comment vas-tu ?"))
print(hash.letters(5))