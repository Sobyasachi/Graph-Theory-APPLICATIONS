import nltk
import networkx as nx
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

f=open("test","r")
if f.mode=='r':
    contents=f.read()
#print(contents)
sentences=sent_tokenize(contents)
print(sentences)

G=nx.Graph()
print('Print number of words as a ')

