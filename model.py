from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load knowledge base
kb = pd.read_csv("kb.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(kb['error_pattern'])

def get_solution(log):
    log_vec = vectorizer.transform([log])
    similarity = cosine_similarity(log_vec, X)
    idx = similarity.argmax()
    return kb.iloc[idx]['resolution']