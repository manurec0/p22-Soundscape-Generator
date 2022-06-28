#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from rake_nltk import Rake
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt')
rake_nltk_var = Rake()

"""This file contains the necessary functions to operate Language Processing part of the project using Rake NLTK.
"""


def synonym_extractor(text):
    synonyms = []

    for syn in wordnet.synsets(text):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


def keyword_extractor(text):
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()

    return keyword_extracted


def query(text):

    keyword = keyword_extractor(text)

    synonyms = []

    for i in range(len(keyword)):
        synonyms.append(synonym_extractor(keyword[i]))

    result = []
    for item in synonyms:
        for synonym in item:
            if synonym not in result:
                result.append(synonym)

    synonyms = result

    return keyword, synonyms


