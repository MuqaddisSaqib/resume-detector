import pickle
def load_model():
    with open('Resume_screeing/models/tfidf.pkl', 'rb') as f:
        tfidf = pickle.load(f)

    with open('Resume_screeing/models/clf.pkl', 'rb') as f:
        clf = pickle.load(f)

    return tfidf,clf
