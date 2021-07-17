# Unigram Language Model 
We use this [opensubtitle](https://www.duo.uio.no/bitstream/handle/10852/50459/947_Paper.pdf?sequence=4) basd corpora. You can use any ULM to init the hypothesis.

## Requiremnst 
``` Matlab```

## Data 
Downlaod the [Dictionary](https://www.dropbox.com/sh/1af43nvlmac54ib/AADyRtK4ztyTS65hull1gyxMa?dl=0)
[opensubtitle](https://www.duo.uio.no/bitstream/handle/10852/50459)

## How to use

```matlab
% load dic
runMap = containers.Map(opensub_google_ngram_W, opensub_google_ngram_N)

% Map word to freq 
w1 = runMap('quartos')
w2 = runMap('quotas') 
w3 = runMap('quarters') 

%Compute prob 
w1 = w1/302372376
w2 = w2/302372376
w3 = w3/302372376

w1 = 9.92E-09
w2 = 5.67E-06
w3 = 1.7725e-04

w1 = runMap('stook') 
w2 = runMap('sioux')
w3 = runMap('stock') 

w1 =  17.9372e-08
w2 = 1.9879e-05
w3 = 2.7990e-04
```
   
