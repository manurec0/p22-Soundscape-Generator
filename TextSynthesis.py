#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from rake_nltk import Rake
from nltk.corpus import wordnet
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
# nltk.download('punkt')

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

rake_nltk_var = Rake()

text = input("Enter a phrase describing the soundscape you want to recreate: ")

keyword = keyword_extractor(text)

synonyms = []

for i in range(len(keyword)):
    
    synonyms.append(synonym_extractor(keyword[i]))
    

