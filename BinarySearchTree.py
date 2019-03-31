from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/———`“”‘’'''
stop_words.update(punctuations)
count_comparator = 0
count_assignment = 0


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

            # A utility function to do inorder tree traversal


def inorder(root, word):
    if root:
        inorder(root.left, word)
        # print(root.val)
        if root.val[0] == word:
            print(root.val[1])
        inorder(root.right, word)


def open_read_file(file):
    with open(file, 'r') as f:
        return f.read().lower()


def chdic(data, word):
    arr = []
    for i, v in data.items():
        if i == word:
            arr.append(i), arr.append(set(v))
    return arr


def main():
    dic = defaultdict(list)
    web_num = 50
    for i in range(1, web_num+1):
        file = open_read_file(f'.\\web\\{i}.txt')
        tokens = word_tokenize(file)
        tokens = list(set([WordNetLemmatizer().lemmatize(w) for w in tokens if w not in stop_words]))
        for token in tokens:
            dic[token].append(str(i)+".txt")

    l = len(dic) - 1
    m = l // 2
    ma = ""
    a = []

    for i, v in enumerate(dic):
        if i == m:
            a = chdic(dic, v)
            ma = v

    r = Node(a)

    for i, v in dic.items():
        if i == ma:
            pass
        else:
            ar = chdic(dic, i)
            insert(r, Node(ar))

    word = "could"
    inorder(r, word)


if __name__ == '__main__':
    main()