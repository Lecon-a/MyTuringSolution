# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:31:12 2023

@author: DELL E3390
"""

print("Sunday P. Afolabi")

# sentence = "I love the advancement in NLP"
# sentence = "AI Planet Bootcamps are free and available to all."
try:

    def get_sentence():
        return input("Enter a sentence here: ")

    def tokenize(text):
        return [word for word in text.split(" ")]

    def tokens_ids(tks):
        vocab = {}
        for tk in tks:
            if tk not in vocab:
                vocab[tk] = len(vocab) + 1
        return vocab

    def tokenization_step():
        sentence = get_sentence()
        tokens = tokenize(sentence)
        return tokens_ids(tokens)
    
except:
    print("Error")
else:
    print(tokenization_step())

