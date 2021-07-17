#!/usr/bin/env python3
import sys
import argparse
import torch
import re
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity


parser=argparse.ArgumentParser(description='call all scores and compute the visual context based Belief-revision')
parser.add_argument('--ulm',  default='LM.txt', help='unigram language model init', type=str,required=True)  
parser.add_argument('--bl', default='baseline.txt', help='baseline_score', type=str,required=True)  
parser.add_argument('--vis', default='visual-context_label.txt',help='class-label from the classifier (Resent152)', type=str, required=True)  
parser.add_argument('--vis_prob', default='visual-context_prob.txt', help='classifier_confidence (Resent152)', type=str, required=True) 
parser.add_argument('--text',  default='spotted-text.txt', help='spotted words from the baseline', type=str, required=True) 
parser.add_argument('--sim',  default='sim-score.txt', help='sim(text,visual_class_label)', type=str, required=True) 
args = parser.parse_args()



# SBERT_with_Roberta
model = SentenceTransformer('roberta-large-nli-stsb-mean-tokens')

def cos_sim(a, b):
    return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))


def get_lines(file_path):
    with open(file_path) as f:
            return f.read().strip().split('\n')

resutl=[]

# compute the score 
f=open('visual_re-ranker_with_SBERT.txt', "w")
for i in range(len(get_lines(args.ulm))):
    temp =[]
    ULM  = get_lines(args.ulm)[i]
    #sim = get_lines('sim-score.txt')[i]
    visual_context_label = get_lines(args.vis)[i]
    visual_context_prob = get_lines(args.vis_prob)[i]
    word = get_lines(args.text)[i]
    baseline_score =  get_lines(args.bl)[i]

    # S-BERT embedding
    visual_context_emb = model.encode(word, convert_to_tensor=True)
    word_emb = model.encode(visual_context_label, convert_to_tensor=True)
   
	
    
    sim =  cosine_scores = util.pytorch_cos_sim(visual_context_emb, word_emb)
    

    
    score = pow(float(ULM),pow((1-float(sim))/(1+ float(sim)),1-float(visual_context_prob)))    
    
    score = float(score) * float(baseline_score) 
    temp.append(score)

    #def cos_sim(a, b):

    result = ','.join((word, ULM, str(score))) 
    result = re.sub(r'\s*,\s*', ',', result)   
    print(result)     

    f.write(result)
    f.write('\n')
    

    
f.close()





