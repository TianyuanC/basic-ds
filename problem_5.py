class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.all_suffixes = []

    def insert(self, char):
        node = None
        if char in self.children.keys():
            node = self.children[char]
        else:
            node = TrieNode()
            self.children[char] = node
        return node

    def suffixes(self, suffix=''):
        self.all_suffixes = []

        if self.is_word and suffix != "":
            self.all_suffixes.append(suffix)

        for char, node in self.children.items():
            for sub_suffix in node.suffixes(suffix+char):
                if sub_suffix not in self.all_suffixes:
                    self.all_suffixes.append(sub_suffix)

        return self.all_suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        next_node = self.root
        for char in word:
            next_node = next_node.insert(char)
        next_node.is_word = True

    def find(self, prefix):
        next_node = self.root
        for char in prefix:
            if char in next_node.children.keys():
                next_node = next_node.children[char]
            else:
                return None
        return next_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


f("w")
f("t")
f("tri")
f("trie")
f("fun")
