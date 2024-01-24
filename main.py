import string
from collections import Counter
import matplotlib.pyplot as plt

# open and read the txt file
text = open('read.txt', encoding='utf-8').read()

# covert to lowercase
lower_case = text.lower()
print(lower_case)

# cleaning the data 1- for replacing 2- which one to replace 3- deleting
clean_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print(clean_text)

# tokenization
tokenized_words = clean_text.split()
print(tokenized_words)

# removing stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

print(final_words)

# nlp emotions from emotions file

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        clear_line = clear_line  # Replace this with the actual content of clear_line

        # Check if the line contains the expected delimiter ':'
        if ':' in clear_line:
            words, emotion = clear_line.split(':')
            if words in final_words:
                emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Plotting the emotions on the graph

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart
ax1.bar(w.keys(), w.values())
ax1.set_title('Emotion Distribution (Bar Chart)')

# Pie chart
ax2.pie(w.values(), labels=w.keys(), autopct='%1.1f%%', startangle=90)
ax2.set_title('Emotion Distribution (Pie Chart)')

fig.tight_layout()
plt.savefig('graph.png')
plt.show()