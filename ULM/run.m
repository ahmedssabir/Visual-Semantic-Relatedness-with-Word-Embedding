runMap = containers.Map(opensub_google_ngram_W, opensub_google_ngram_N)
w1 = runMap('quartos') % get word
w2 = runMap('quotas') % get word
w3 = runMap('quarters') % get word

w1 = w1/302372376
w2 = w2/302372376
w3 = w3/302372376

w1 = 9.92E-09
w2 = 5.67E-06
w3 = 1.7725e-04


