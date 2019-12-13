# N-Gram-Freq
A script for taking a text file as an input and generating a csv file of n-grams sorted by frequency.

Prerequisites: Python3, nltk (can be installed by running ```pip install nltk```).
The script uses the nltk Punkt tokenizer, so before using the script for the first time, run Python, then: 

```
import nltk
nltk.download('punkt')
```
Usage:  
```python ngramfreq pathOfInputTxt pathOfOutputCsv```
