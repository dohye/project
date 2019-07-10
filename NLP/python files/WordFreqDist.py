# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter

f = open('Hamlet.txt', 'r')

wordDict = Counter()

sentences = f.readlines()

for sentence in sentences:
    for word in sentence.split():
        wordDict[word] += 1
        
for word, freq in wordDict.most_common(10):
    print(word, freq)
    

# 가장 많이 나오는 단어 10개
most_common = wordDict.most_common(10)
most_common

# 단어의 빈도 분포 그래프 그리기
import matplotlib.pyplot as plt

names, values = zip(*most_common)
plt.bar(names, values, color='orange')
plt.xlabel('words')
plt.ylabel('frequency')
plt.title('Frequency of words')

# 워드클라우드 만들기
from wordcloud import WordCloud

wc = WordCloud(width = 1000, height = 600, background_color="white", random_state=0)
plt.imshow(wc.generate_from_frequencies(wordDict))
plt.axis("off")
plt.show()
