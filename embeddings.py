from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_vectorizer():
    return TfidfVectorizer(stop_words='english')

def calculate_novelty(text1, text2):
    vectorizer = get_vectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    novelty = 1 - similarity
    return round(novelty, 3)
