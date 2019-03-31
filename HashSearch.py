from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import hashlib

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/———`“”‘’'''
stop_words.update(punctuations)
count_comparator = 0
count_assignment = 0

class Word():
    def __init__(self, key, posting):
        self.key = key
        self.posting = [posting]

    def __str__(self):
        return self.key

    def get_pos(self):
        return self.posting

    def update_pos(self, posting):
        self.posting.append(posting)


def hashing_func(key):
    global count_comparator
    global count_assignment

    count_assignment += 1
    sum = hashlib.sha1(key.encode('utf8')).hexdigest()

    count_assignment += 1
    sum_int = int(sum, 16)
    #   sum=0
    #   sum=hash(key)
    return sum_int % 40000


def open_read_file(file):
    with open(file, 'r') as f:
        return f.read().lower()


def main():
    global count_comparator
    global count_assignment
    table = [[] for x in range(40000)]
    web_num = 50
    for i in range(1, web_num + 1):
        file = open_read_file(f'.\\web\\{i}.txt')
        tokens = word_tokenize(file)
        tokens = list(set([WordNetLemmatizer().lemmatize(w) for w in tokens if w not in stop_words]))

        for word in tokens:
            temp = Word(word, str(i + 1)+".txt")

            count_assignment += 1
            hash_key = hashing_func(word)

            count_comparator += 1
            if table[hash_key] != []:
                for j in table[hash_key]:

                    count_assignment += 1
                    f = True
                    count_comparator += 1
                    if temp.key == j.key:
                        count_assignment += 1
                        j.update_pos(str(i + 1)+".txt")
                        count_assignment += 1
                        f = False
                        break
                count_comparator += 1
                if f:
                    count_assignment += 1
                    table[hash_key].append(temp)
            else:
                count_comparator += 1
                count_assignment += 1
                table[hash_key].append(temp)

    keyword = "could".lower()

    count_assignment += 1
    hash_keyword = hashing_func(keyword)
    count_assignment += 1
    result = table[hash_keyword]
    count_assignment += 1
    not_found = True

    for word in result:
        count_comparator += 1
        if keyword == word.key:
            count_assignment += 1
            not_found = False
            for i in word.get_pos():
                print(i, end=" ")
            print()
    count_comparator += 1
    if not_found:
        print("Not Found")

    print('Assignment Count: ', count_assignment)
    print('Comparator Count: ', count_comparator)


if __name__ == '__main__':
    main()
