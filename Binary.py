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
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        global count_comparator
        global count_assignment

        children = []
        count_comparator += 1
        if self.left is not None:
            children.append(self.left)
        count_comparator += 1
        if self.right is not None:
            children.append(self.right)
        return children

    def __str__(self):
        return self.val


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        global count_assignment
        global count_comparator
        count_comparator += 1
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        global count_assignment
        global count_comparator

        count_comparator += 1
        if val <= currentNode.val:
            count_comparator += 1
            count_assignment += 1
            if currentNode.left:
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        elif val > currentNode.val:
            count_comparator += 1
            count_assignment += 1
            if currentNode.right:
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        global count_assignment
        global count_comparator

        count_comparator += 1
        if currentNode is None:
            return False
        elif val == currentNode.val[0]:
            return currentNode.val[1]
        elif val < currentNode.val[0]:
            return self.findNode(currentNode.left, val)
        else:
            return self.findNode(currentNode.right, val)

    def inOrder(self):
        self.inOrder_helper(self.root)

    def inOrder_helper(self, node):
        global count_assignment
        global count_comparator

        count_comparator += 1
        if node is not None:
            self.inOrder_helper(node.left)
            print(node.val)
            self.inOrder_helper(node.right)


def open_read_file(file):
    with open(file, 'r') as f:
        return f.read().lower()


def main():
    global count_assignment
    global count_comparator
    posting_list = list()
    dic = defaultdict(list)
    web_num = 50

    for i in range(1, web_num+1):
        file = open_read_file(f'.\\web\\{i}.txt')
        tokens = word_tokenize(file)
        tokens = list(set([WordNetLemmatizer().lemmatize(w) for w in tokens if w not in stop_words]))
        for token in tokens:
            dic[token].append(i + 1)

    for e in dic.items():
        count_assignment += 1
        posting_list.append(e)

    bst = BST()
    for e in posting_list:
        bst.insert(e)

    search = 'could'
    if bst.find(search) is not None:
        print(bst.find(search))
    else:
        print("Not Found")

    print('Assignment Count: ', count_assignment)
    print('Comparator Count: ', count_comparator)


if __name__ == '__main__':
    main()
