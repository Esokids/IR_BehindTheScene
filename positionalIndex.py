from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~/—`'''
stop_words.update(punctuations)
count_comparator = 0
count_assignment = 0


def open_read_file(file):
    with open(file, 'r') as f:
        return f.read().lower()


def main():
    global count_comparator
    global count_assignment
    dic = defaultdict(list)
    web_num = 50
    for i in range(1, web_num + 1):
        file = open_read_file(f'.\\web\\{i}.txt')
        tokens = word_tokenize(file)
        tokens = [WordNetLemmatizer().lemmatize(w) for w in tokens if w not in stop_words]
        tokens_set = list(set(tokens))

        for word in tokens_set:
            dic_pos = {}

            count_comparator += len(tokens)
            position = [j for j, x in enumerate(tokens, 1) if x == word]
            count_assignment += len(position)

            count_assignment += 1
            dic_pos[i] = position
            count_assignment += 1
            dic[word].append(dic_pos)

    for keys, values in [(keys, values) for x in dic['could'] for (keys, values) in x.items()]:
        print(keys, values)

    ''''' **** same ****
    # for x in dic['sport']:
    #     for key, value in x.items():
    #         print(key, value)
    #         print(type(keys), type(value))
    '''''

    print('Assignment Count: ', count_assignment)
    print('Comparator Count: ', count_comparator)


if __name__ == '__main__':
    main()
