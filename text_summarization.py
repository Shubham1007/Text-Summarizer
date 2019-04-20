import numpy as np
import io
import pandas as pd
from google.colab import files
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import networkx as nx
from nltk.tokenize import sent_tokenize
nltk.download('punkt') # one time execution
import re

uploaded = files.upload()

df = pd.read_csv(io.StringIO(uploaded['tennis_articles_v4.csv'].decode("utf-8")))

df.head()

sentences = []
for s in df['article_text']:
  sentences.append(sent_tokenize(s))

sentences = [y for x in sentences for y in x]

clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
clean_sentences = [s.lower() for s in clean_sentences]

nltk.download('stopwords')# one time execution

stop_words = stopwords.words('english')

def remove_stopwords(sen):
  sen_new = " ".join([i for i in sen if i not in stop_words])
  return sen_new

clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

sentence_vectors = []
for i in clean_sentences:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((100,))
  sentence_vectors.append(v)

sim_mat = np.zeros([len(sentences), len(sentences)])

for i in range(len(sentences)):
  for j in range(len(sentences)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

sn = 10
for i in range(sn):
  print(ranked_sentences[i][1])