import sys
import csv
from nltk import *
from urllib import *
from urllib.parse import urljoin
from urllib.request import pathname2url

if len(sys.argv) !=3:
    print ("Usage:  python3 ngramfreq pathOfInputTxt pathOfOutputCsv")
    sys.exit(0)
url = sys.argv[1]
url = urljoin('file:', pathname2url(url))
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)
text = Text(tokens)
n_raw = input('Specify n-gram type - e.g. Enter 3 for 3-gram, 11 for 11-gram etc.')
n = int(n_raw)
ngr = ngrams(tokens, n)
ngr = [' '.join(t) for t in ngr]
fdist = FreqDist(ngr)
results_raw = input('Specify maximum number of results') 
results = int(results_raw)
common_ngrams = fdist.most_common(results)


with open(sys.argv[2], 'w') as output:
    wr = csv.writer(output, quoting=csv.QUOTE_ALL)
    for item in common_ngrams:
        wr.writerow(item)
