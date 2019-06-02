class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char):
        node = None
        if char in self.children.keys():
            node = self.children[char]
        else:
            node = TrieNode()
            self.children[char] = node
        return node

    def suffixes(self, suffix=''):
        all_suffixes = []

        if self.is_word and suffix != "":
            all_suffixes.append(suffix)

        for char, node in self.children.items():
            for sub_suffix in node.suffixes(suffix+char):
                if sub_suffix not in all_suffixes:
                    all_suffixes.append(sub_suffix)

        return all_suffixes


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


def search_display(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            return prefixNode.suffixes()
        else:
            return prefix + " not found"
    else:
        return ""


def test_function(test_case):
    output = search_display(test_case[0])
    solution = test_case[1]
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# empty or no match cases
test_function(["", ""])
test_function(["w", "w not found"])
test_function(["tt", "tt not found"])

# partial matches
test_function(["t", ['rie', 'rigger', 'rigonometry', 'ripod']])
test_function(["ant", ['hology', 'agonist', 'onym']])

# full match
test_function(["factory", []])
