# Text-Summarizer
Automatic summarization is the process of shortening a text document with software, in order to create a summary with the major points of the original document.The main idea of summarization is to find a subset of data which contains the "information" of the entire set.






<center><h1>Methodology</h1></center>
<h1>The TextRank Model</h1> <br/>
Graph-based ranking algorithms are essentially a way of deciding the importance of a vertex within a graph, based on global information
recursively drawn from the entire graph. The basic idea implemented by a graph-based ranking model is that of “voting” or “recommendation”. When one vertex links to another one, it is basically casting a vote for that other vertex. The higher the number of votes that are cast for a vertex, the higher the importance of the vertex. Moreover, the importance of the vertex casting the vote determines how important the vote itself is, and this information is also taken into account by the ranking model. Hence, the score associated with a vertex is determined based on the votes that are cast for it, and the score of the vertices casting these votes. Formally, let be a directed graph
with the set of vertices V and set of edges E For a given vertex Vi.

<br/>
<h1>TextRank Algorithm</h1> <br/>
TextRank is an extractive and unsupervised text summarization technique. TextRank algorithm that we will be following:
• The first step would be to concatenate all the text contained in the
articles<br/>
• Then split the text into individual sentences<br/>
• In the next step, we will find vector representation (word embeddings)
for each and every sentence<br/>
• Similarities between sentence vectors are then calculated and stored
in a matrix<br/>
• The similarity matrix is then converted into a graph, with sentences as
vertices and similarity scores as edges, for sentence rank calculation<br/>
• Finally, a certain number of top-ranked sentences form the final
summary<br/>






<h1>Sentence Extraction</h1>-<br/>
The other TextRank application that we investigate consists of sentence extraction for automatic summarization. In a way, the problem
of sentence extraction can be regarded as similar to keyword extraction, since both applications aim at identifying sequences that are more “representative” for the given text. In keyword extraction, the candidate text units consist of words or phrases, whereas in sentence extraction, we deal with entire sentences. TextRank turns out to be well suited for this type of applications, since it allows for a ranking over text units that is recursively computed based on information drawn from the entire text.

<h1>TextRank for Sentence Extraction</h1><br/>
To apply TextRank, we first need to build a graph associated with the text,where the graph vertices are representative for the units to be ranked. For the task of sentence extraction, the goal is to rank entire sentences, and therefore a vertex is added to the graph for each sentence in the text. The co-occurrence relation used for keyword extraction cannot be applied here, since the text units in consideration are significantly larger than one or few words, and “co-occurrence” is not a meaningful relation for such large
contexts. Instead, we are defining a different relation, which determines a connection between two sentences if there is a “similarity” relation between them, where “similarity” is measured as a function of their content overlap. Such a relation between two sentences can be seen as a process of “recommendation”: a sentence that addresses certain concepts in a text, gives the reader a “recommendation” to refer to other sentences in the text that address the same concepts, and therefore a link can be drawn between any two such sentences that share common content. The overlap of two sentences can be determined simply as the number of common tokens between the lexical representations of the two sentences, or it can be run through syntactic ilters, which only count words of a certain syntactic category, e.g. all open class words, nouns and verbs, etc. Moreover, to avoid promoting long sentences, we are using a normalization factor, and divide the content overlap of two sentences with the length of each sentence.

