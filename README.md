#  Semantic Relatedness with Word Embedding (SWE)


![image](figure.jpg)



The visual re-ranker is based on probability from similarity aka [Belief Revision Theorem](https://www.aaai.org/Papers/Symposia/Spring/2003/SS-03-05/SS03-05-005.pdf). The Belief Revision Theorem is a conditional probability model which assumes that the preliminary probability finding is revised to the extent warranted by the hypothesis proof.  

<img src="https://render.githubusercontent.com/render/math?math=\text{P}(w \mid c)=\text{P}(w)^{\alpha}"> 


where the main components of hypothesis revision:

1. Original Hypothesis  <img src="https://render.githubusercontent.com/render/math?math=\text{P}(w)">  baseline model softmax score  (gray block)

2. Initialized Hypothesis by common observation  <img src="https://render.githubusercontent.com/render/math?math=\text{P}(\text{ULM})"> (ie language model) (blue block)
  
3. Informativeness  <img src="https://render.githubusercontent.com/render/math?math=1-\text{P}(c)"> of the visual context. (green block)
 
4. Similarities <img src="https://render.githubusercontent.com/render/math?math=\alpha=\left[\frac{1 - \text{sim}(w, c)}{1%2B\text{sim}(w, c)}\right]^{1-\text{P}(c)}"> the relatedness between the two concepts (visual context and hypothesis) with respect to the informativeness of the visual information. (red block)

Here is a [Demo](visual_re-re-ranker_demo.ipynb) to show the word embedding based Visual Re-ranking with Belief Revision theorem 
 
 ## Model 
 
 <!--ts-->
   * Count-based word embedding visual re-ranker  
   * [Knowleage-based word embedding  visual re-ranker](https://github.com/sabirdvd/visual-re-ranker-with-w2v/tree/main/knowledge-base-embedding)
   * [Contextual-based embedding BERT visual re-ranker](https://github.com/sabirdvd/visual-re-ranker-with-w2v/tree/main/BERT-based)
<!--te-->



 
## Count-based word embedding visual re-ranker 
 
 
### Requirement  
```
conda create -n Visual_w2v python=3.8 anaconda
conda activate Visual_w2v
pip install gensim==4.1.0
```




## Data

Install GloVe [pre-trained word vectors  glove.6B.300d.txt](https://nlp.stanford.edu/projects/glove/)
bigger is better, the 840B pre-trained word vectors is recommneded. We use [Glove](https://nlp.stanford.edu/pubs/glove.pdf) as main in this work. The advantage of Glove over Word2Vec is that it  does  not  rely  on  local  word-context  information,  but  it incorporates global co-occurrence statistics.

For w2v install [GoogleNews-vectors-negative300.bin](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)

For [fastext](https://arxiv.org/pdf/1607.04606.pdf) install [crawl-300d-2M.vec](crawl-300d-2M-subword.zip)

## How to run 
To be able to use w2v/Glove as visual re-ranker, we need the following information 



- The spotted text `text_spotted.txt`: word candidates from the baseline  
- The original hypothesis from the baseline ``baseline.txt`` softmax output 
- The hypothesis `LM.txt`: initialized by common observation (ie [LM](https://github.com/sabirdvd/visual-re-ranker-with-w2v/tree/main/ULM))
- Visual information from the image `visual-context_label.txt`: initialized visual context or classifer confident 
- Visual information  confidence `visual-context_prob.txt` from the classifier -ie RseNet152


After having all the required information ``run``  as shown in **Example 1** (below) 

For GloVe
```
quarters-example/python glove-visual.py --ulm LM.txt --bl baseline.txt --text spotted-text.txt --vis visual-context_label.txt --vis_prob visual-context_prob.txt
```

For w2v 

```
quarters-example/python w2v-visual.py --ulm LM.txt --bl baseline.txt --text spotted-text.txt --vis visual-context_label.txt --vis_prob visual-context_prob.txt
``` 

For fasttext 

```
quarters-example/python fastext-visual.py --ulm LM.txt --bl baseline.txt --text spotted-text.txt --vis visual-context_label.txt --vis_prob visual-context_prob.txt
``` 

## Example 1

![full image](COCO_train2014_000000201409.jpg)
-->
<img src="COCO_train2014_000000201409-1.jpg" width="70">

Orignial baseline softmax score
``` 
quartos  0.060192
quotas   0.040944	
quarters 0.03037
``` 

After visual re-ranking  `` visual_glove_result.txt ``  
``` 
quarters 7.040899415659617e-06
quotas   4.0903987856408736e-07
quartos  2.0644119047556385e-09
``` 



## Example 2
![full image](COCO_train2014_000000320382_v1.jpg)
-->
<img src="COCO_train2014_000000320382.jpg" width="70">


Orignial baseline softmax score
``` 
stook 0.4865732956	
sioux 0.0919743552	
stock 0.0703927792
``` 
After visual re-ranking `` visual_glove_result.txt ``   
``` 
stock 0.00018136249963338343
sioux 7.23838175424e-06
stook 8.07711670696e-07
``` 

## Citation

Please use the following bibtex entry:
```bibtex
@inproceedings{sabir2018visual,
  title={Visual re-ranking with natural language understanding for text spotting},
  author={Sabir, Ahmed and Moreno-Noguer, Francesc and Padr{\'o}, Llu{\'\i}s},
  booktitle={Asian Conference on Computer Vision},
  pages={68--82},
  year={2018},
  organization={Springer}
}
```
