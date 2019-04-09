from rouge import Rouge 
rouge = Rouge()
scores = rouge.get_scores(hypothesis, reference)
print("Accuracy of Text Summarizer is:")
print(scores)
