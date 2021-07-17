
## Visual Semantic Relatedness with Sense Word Embedding
One of the limitations of word embedding, that mentions in the main repository, is that it computes
a single representation for each word independently from the context in which
they appear, context insensitive. In contrast to word embedding, which single
representation limited to one sense, sense embedding is representing each word
with multiple senses. These approaches rely on
sense-annotated corpus from sense inventory, such as [BabelNet](https://www.sciencedirect.com/science/article/pii/S0004370212000793).



## Word with right sense or meaning  
Example: Top-k2 ``  tennis racket`` senses from underlying sense inventory database [BabelNet](https://babelnet.org/search?word=racket&lang=EN)
```
racket_bn:00036297n <-- An illegal enterprise
racket_bn:00065848n <-- A sports implement
``` 
[BabelNet-How-to-use](https://babelnet.org/how-to-use)


## Data
SEW (Semantically Enriched Wikipedia) is a sense-annotated corpus, automatically built from Wikipedia, in which the overall number of linked mentions has been more than tripled solely by exploiting the hyperlink structure of Wikipedia pages and categories, along with the wide-coverage sense inventory of BabelNet.

Download the [pre-computed vector](http://lcl.uniroma1.it/sew/) from [Semantically Enriched Wikipedia](http://lcl.uniroma1.it/sew/papers/IJCAI16.pdf) 
SEW-EMBED - Vectors [ zip: 14.9 GB ]


## How to run 
To be able to use sense embedding as visual re-ranker, we need the following information 



- The spotted text `text_spotted.txt`: word candidates from the baseline  
- The original hypothesis from the baseline ``baseline.txt`` softmax output 
- The hypothesis `LM.txt`: initialized by common observation (ie LM)
- Visual information from the image `visual-context_label.txt`: initialized visual context or classifer confident 
- Visual information  `visual_context_sense.txt`: from  a database 
- Visual information  confidence `visual-context_prob.txt` from the classifier (ie ResNet) 

However, here for simplicity we use pre-computed vector from [SENSEMBED](https://www.aclweb.org/anthology/P15-1010.pdf). Therefore, we dont need ``visual_context_sense.txt`` as in `` data.txt`` for this model.

```
python stock-example-Sense/python sense-visual.py --ulm LM.txt --bl baseline.txt --text spotted-text.txt --vis visual-context_label.txt --vis_prob visual-context_prob.txt
```


## Example 1
We will use the same example to compare the two types of word embedding.  

![full image](COCO_train2014_000000320382_v1.jpg)
-->
<img src="COCO_train2014_000000320382.jpg" width="70">


**Count based Embedding** Glove 

```
stock 0.00018136249963338343
sioux 3.1327470941288846e-06
stook 8.07711670696e-07
``` 

**Knowleage based Embedding** (sense embedding) with actual meaning, exact vector of the word, of the viusal context information [refrigerator](https://babelnet.org/search?word=refrigerator&lang=EN) as ``White goods in which food can be stored at low temperatures  ``  



``` 
stock 0.00022946505149673056
sioux 7.23838175424e-06
stook 8.07711670696e-07
``` 




