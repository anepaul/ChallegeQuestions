class Node:
    def __init__(self, data, is_word=False):
        self.data = data
        self.children = {}
        self.is_word = is_word


class Trie:
    def __init__(self):
        self.root = Node('*')

    def add_word(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                child = Node(char, False)
                node.children[char] = child
            node = node.children[char]
            if i == len(word) - 1:
                node.is_word = True

    def find_word(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return 0

        return self.trie_size(node)

    @staticmethod
    def trie_size(node):
        size = 0
        if node.is_word:
            size += 1

        for k, v in node.children.items():
            size += Trie.trie_size(v)

        return size


# trie = Trie()
# trie.add_word('hack')
# trie.add_word('hackerrank')
# trie.add_word('maker')
# print(trie.find_word('hac'))
# print(trie.find_word('hak'))

n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add_word(contact)
    elif op == 'find':
        print(trie.find_word(contact))
    else:
        raise ValueError('Only ADD and FIND operations are supported')
