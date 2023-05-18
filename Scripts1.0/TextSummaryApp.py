#!/usr/bin/env Python3

# This one is a Text Summary App, have fun!

import nltk
import numpy as np
import networkx as nx

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def generate_summary(text, num_sentences=3):
    # Split text into sentences
    sentences = sent_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    cleaned_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words if word.isalnum()]
        words = [word for word in words if word not in stop_words]
        cleaned_sentences.append(" ".join(words))

    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)

    # Calculate sentence similarity using cosine similarity
    similarity_matrix = np.dot(tfidf_matrix, tfidf_matrix.T)

    # Convert similarity matrix to a graph
    nx_graph = nx.from_numpy_array(similarity_matrix)

    # Use pagerank algorithm to rank sentences
    scores = nx.pagerank(nx_graph)

    # Sort the sentences based on their scores
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

    # Select top ranked sentences for the summary
    summary_sentences = [sentence for _, sentence in ranked_sentences[:num_sentences]]

    # Join the summary sentences into a single text
    summary = " ".join(summary_sentences)

    return summary


def main():
    # Example usage
    input_text = """
    Write or paste the article or book text here.
    """

    summary = generate_summary(input_text)
    print("Text Summary:")
    print(summary)


if __name__ == "__main__":
    # Download necessary NLTK resources
    nltk.download("punkt")
    nltk.download("stopwords")

    main()
	
	
	
# NLTK (Natural Language Toolkit): NLTK is a powerful library for natural language processing (NLP) in Python. It provides a wide range of 
# functionalities and resources for tasks such as tokenization, stemming, tagging, parsing, and more. In this script, NLTK is used for sentence 
# tokenization (sent_tokenize) and stop word removal (stopwords).

# NumPy: NumPy is a fundamental library for scientific computing in Python. It provides support for large, multi-dimensional arrays and 
# matrices, along with a collection of mathematical functions to operate on these arrays. In this script, NumPy is used for matrix operations, 
# particularly to calculate the cosine similarity between sentences and create the similarity matrix.

# NetworkX: NetworkX is a Python library for the study of complex networks and graph analysis. It provides data structures and algorithms to 
# create, manipulate, and analyze networks, including graphs and their properties. In this script, NetworkX is used to convert the similarity 
# matrix into a graph representation and apply the PageRank algorithm to rank sentences based on their scores.
