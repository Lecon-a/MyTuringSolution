def token2number(sentence) -> {}:
    tokens = sentence.split(" ")
    t2n = {}
    for token in tokens:
        if token not in t2n:
            t2n[token] = 1
        else:
            t2n[token] += 1
    return t2n

def totalWords(tokens) -> int:
    return sum(tokens.values())

def func(token):
    return {"Prob": "value"}


def fred(tokens) -> {}:
    return tokens.map(func, token)

if __name__=='__main__':
    sentence = input("Enter the sentence: ")
    print('\n', token2number(sentence))
    words_count = totalWords(token2number(sentence))
    print(f'\nTotal words in the sentence is {words_count}\n')
    print(f'\nTotal words in the sentence is {words_count.map(func)}\n')
    