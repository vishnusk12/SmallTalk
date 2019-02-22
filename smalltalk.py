# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:10:44 2018

@author: Vishnu
"""

import random
import json
import spacy
nlp = spacy.load('en')

fallback = ['Sorry, could you say that again?']

class SmallTalk:
    def __init__(self, spacy_model):
        with open('smalltalk.json') as data_file:
            self.smalltalk = json.load(data_file)
            self.nlp = spacy_model

    def get_reply(self, query):
        score = 0.0
        reply = None
        for key, values in self.smalltalk.items():
            score = max(score,
                        max([self.similarity(query, val) for val in values[0]]))
            print (score)
            for val in values[0]:
                if self.similarity(query, val) == score:
                    reply = random.choice(values[1]) if isinstance(values[1], list) else values[1]

        return reply if score > 0.9 else random.choice(fallback)

    def similarity(self, query1, query2):
        query1 = query1.lower()
        query2 = query2.lower()
        return self.nlp(query1).similarity(self.nlp(query2))

st = SmallTalk(nlp)
print (st.get_reply('how old are glaciers'))