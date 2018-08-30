import os
import io

DIC_EVAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'crosslingual', 'dictionaries')
path = os.path.join(DIC_EVAL_PATH, '%s-%s.txt' % ('ar', 'en'))
dict1={}
with io.open(path, 'r', encoding='utf-8') as f:
    for _, line in enumerate(f):
        word1, word2 = line.rstrip().split()
        dict1.setdefault(word1, []).append(word2)
path = os.path.join(DIC_EVAL_PATH, '%s-%s.txt' % ('en', 'he'))
dict2={}
with io.open(path, 'r', encoding='utf-8') as f:
    for _, line in enumerate(f):
        word1, word2 = line.rstrip().split()
        dict2.setdefault(word1, []).append(word2)

path = os.path.join(DIC_EVAL_PATH, '%s-%s.5000-6500.txt' % ('ar', 'he'))
f = io.open(path, 'w', encoding='utf-8')
count =0
for word in dict1 :
    list = dict1[word]
    for enWord in list:
        if enWord in dict2:
            for heWord in dict2[enWord]:
              f.write('%s\t%s\n'%(word,heWord))
              count+=1