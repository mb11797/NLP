import numpy as np
from nltk import PorterStemmer as ps
from collections import Counter


text_1 = 'Hello this is python programming and python is mainly used for machine learning and deep learning.'
text_2  = 'python programming is one of the most popular programming in today world'

#text_1_words = []

text_1_words = text_1.split()
text_2_words = text_2.split()

stopwords = ['is','am','are','the','that','this','use','for']

#print(cmp(text_1_words,stopwords))

#diff = text_1_words - stopwords

#diff = [x for x in text_1_words if x not in stopwords]
diff_1 = []
diff_2 = []
#for x,y in zip(text_1_words,text_2_words):
#    if x not in stopwords:
#        diff_1.append(x)
#    
#    if y not in stopwords:
#        diff_2.append(y)
# 
for x in text_1_words:
    if x not in stopwords:
        diff_1.append(x)

for x in text_2_words:
    if x not in stopwords:
        diff_2.append(x)

# Making all the words to lower case
diff_1 = [x.lower() for x in diff_1]
diff_2 = [x.lower() for x in diff_2]
        
#diff_1 = [ps.stem(x) for x in diff_1]
#diff_2 = [ps.stem(x) for x in diff_2]


#diff_1 = np.unique(diff_1,return_counts=True)
#diff_2 = np.unique(diff_2,return_counts=True)

   
#words = set(diff_1)


#while text_1 != null:
#
#words = []
#freq = []
count_1 = {}
count_2 = {}

#
#for i in range(len(diff_1)):
#    if x not in diff_1[i]:
#        word.append()
#        freq[i] = 1
#    else:
#        freq[i] = freq[i] + 1
#    

#

for word in diff_1:
    count_1[word] = 0


for word in diff_1:
#    freq = diff_1.count(word)
    count_1[word] = count_1[word] + 1


for word in diff_2:
    count_2[word] = 0


for word in diff_2:
#    freq = diff_1.count(word)
    count_2[word] = count_2[word] + 1



counts_1 = Counter(diff_1)
counts_2 = Counter(diff_2)


