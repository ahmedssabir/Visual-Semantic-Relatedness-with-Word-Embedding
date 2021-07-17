#!/usr/bin/env python3
import sys
import argparse
import torch
import re
import gensim #4.0.1
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec


parser=argparse.ArgumentParser(description='call all scores and compute the visual context based Belief-revision')
parser.add_argument('--ulm',  default='LM.txt', help='unigram language model init', type=str,required=True)  
parser.add_argument('--bl', default='baseline.txt', help='baseline_score', type=str,required=True)  
parser.add_argument('--vis', default='visual-context_label.txt',help='class-label from the classifier (Resent152)', type=str, required=True)  
parser.add_argument('--vis_prob', default='visual-context_prob.txt', help='classifier_confidence (Resent152)', type=str, required=True) 
parser.add_argument('--text',  default='spotted-text.txt', help='spotted words from the baseline', type=str, required=True) 
args = parser.parse_args()


# https://nlp.stanford.edu/projects/glove/
model_path = 'glove.6B.300d.txt'

glove_file = datapath(model_path)

tmp_file = get_tmpfile("test_word2vec.txt")

_ = glove2word2vec(glove_file, tmp_file)

model = KeyedVectors.load_word2vec_format(tmp_file)

def cos_sim(a, b):
    return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))


def get_lines(file_path):
    with open(file_path) as f:
            return f.read().strip().split('\n')



# GloVe based visual re-ranker
class Visual_re_ranker:
        def __init__(self, ULM, visual_context_prob, sim, baseline):
            self.ULM = ULM
            self.visual_context_prob = visual_context_prob
            self.sim = sim
            self.basline = baseline
        def belief_revision(self):
            score = pow(float(ULM),pow((1-float(sim))/(1+ float(sim)),1-float(visual_context_prob)))
            score = float(score) * float(baseline)
            return score
        @staticmethod
        def re_rank_top_K_word(input_path):
            re_ranked_scores = []
            with open(input_path) as f:
                for line in f:
                    word, score = line.split(',')
                    score = float(score)
                    re_ranked_scores.append((word, score))
            re_ranked_scores.sort(key=lambda s: float(s[1]), reverse=True)
            with open(input_path, 'w') as f:
                for word, score in re_ranked_scores:
                    f.write("%s %s\n" % (word, score))


input_path = 'visual_glove_result.txt'

f=open(input_path, "w")
for i in range(len(get_lines(args.ulm))):
    temp =[]
    ULM  = get_lines(args.ulm)[i]
    #sim = get_lines('sim-score.txt')[i]
    visual_context_label = get_lines(args.vis)[i]
    visual_context_prob = get_lines(args.vis_prob)[i]
    word = get_lines(args.text)[i]
    baseline =  get_lines(args.bl)[i]

	
    try:
       sim = model.similarity(visual_context_label,word)
       #print(sim)
    except KeyError: 
        #print('out_of_dict')
       sim = 0.0  #OVV to 0 
 
    try:
       #score = visual_reranker(ULM, visual_context_prob, sim, baseline_score)
       score = Visual_re_ranker(ULM, visual_context_prob, sim, baseline)
       score = score.belief_revision()   
       temp.append(score)
       #print(score)
    except KeyError: 
       score = 0.0
    #score = float(score) * float(baseline_score) 
    temp.append(score)

   
    # show result 
    result_1 = ','.join((word, ULM, str(score))) 
    result_1 = re.sub(r'\s*,\s*', ',', result_1) 
    print (result_1)
    
    # print to file 
    result = ','.join((word, str(score))) 
    result = re.sub(r'\s*,\s*', ',', result)   
      

    f.write(result)
    f.write('\n')
    
   
f.close()

if __name__ == "__main__":
    Visual_re_ranker.re_rank_top_K_word(input_path)
   

