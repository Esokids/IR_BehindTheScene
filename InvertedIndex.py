from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/———`“”‘’'''
stop_words.update(punctuations)
count_comparator = 0
count_assignment = 0


def quickSort(arr):
    quickSortHelper(arr,0,len(arr)-1)
    return arr


def quickSortHelper(arr, low, high):
    global count_comparator
    global count_assignment

    count_comparator += 1
    if low < high:
        count_assignment += 1
        pi = partition(arr, low, high)
        quickSortHelper(arr, low, pi - 1)
        quickSortHelper(arr, pi + 1, high)


def partition(arr, low, high):
    global count_comparator
    global count_assignment

    count_assignment += 1
    i = low - 1

    count_assignment += 1
    pivot = arr[high]

    for j in range(low, high):
        count_comparator += 1
        if arr[j] <= pivot:

            count_assignment += 1
            i += 1

            count_assignment += 3
            arr[i], arr[j] = arr[j], arr[i]

    count_assignment += 3
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def open_read_file(file):
    with open(file, 'r') as f:
        return f.read().lower()


class Dictionary:
    def __init__(self, word, index):
        self.word = word
        self.index = index

    def __repr__(self):
        return f"{self.word} {self.index}"


def main(search = 'could'.lower()):
    global count_assignment
    global count_comparator
    posting_list = list()
    posting = list()
    dic = defaultdict(list)
    web_num = 50

    for i in range(1, web_num+1):
        file = open_read_file(f'.\\web\\{i}.txt')
        tokens = word_tokenize(file)
        tokens = list(set([WordNetLemmatizer().lemmatize(w) for w in tokens if w not in stop_words]))
        for token in tokens:
            posting.append(Dictionary(token, str(i)+".txt"))

    # grouping
    for token in posting:
        count_assignment += 1
        dic[token.word].append(token.index)

    for e in dic.items():
        count_assignment += 1
        posting_list.append(e)

    quickSort(posting_list)

    count_assignment += 1
    count_assignment += 1

    flagSearch = False
    for e in posting_list:
        count_comparator += 1
        if e[0] == search:
            count_assignment += 1
            flagSearch = True
            print('Posting of this word : ', e[1])
            return e[1], count_assignment, count_comparator
    count_comparator += 1
    if not flagSearch:
        print("Not Found")
        return False

    print('Assignment Count: ', count_assignment)
    print('Comparator Count: ', count_comparator)


if __name__ == '__main__':
    main()
