#pip install lm-scorer


import torch

from lm_scorer.models.auto import AutoLMScorer
scorer = AutoLMScorer.from_pretrained("gpt2-large")


# mean 
def score(sentence):
    return scorer.sentence_score(sentence, reduce="mean")


file1 = []



#with open('caption.txt','rU') as f1:
with open('text_spotted_word.txt','rU') as f1:  


    for line1 in f1:

       file1.append(line1.rstrip())
       #break

resutl=[]



f=open('LM.txt', "w")
for i in range(len(file1)):
    temp =[]
    messages  = file1[i]

    w = score(messages)
    print(w)

    temp.append(w)

    result= file1[i]+','+str(w)

    f.write(result)
    f.write('\n')
    print(result)

f.close()





