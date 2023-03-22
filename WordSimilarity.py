import nltk
from nltk.corpus import stopwords

class WordSimilarity():
    stop_words = None
    def __init__(self) -> None:
        """
        Constructor that sets up all the required variables.
        """
        nltk.download("stopwords")
        self.stop_words = set(stopwords.words("english"))
    
    def nomarlizer(self, document) -> list():
        """
        Returns a list of all words, that have been normalized.
        Normalization here is performed as:
        1. Case Conversion into Lower for case consistency.
        2. Tokenization.
        """
        try:
            document = document.lower()
            tokens = document.split()
            for token in tokens:
                if token.isalpha() and token not in self.stop_words:
                    continue
                else:
                    tokens.remove(token)

            return tokens
        except Exception as e:
            print("[ERR] The following error occured while trying to normalize text: "+str(e))

    def compare_texts_w2v(file_one, file_two, k=10) -> None:
        """
        Find the top K words, and then find the cosine similarity.
        """
        try:
            pass
        except Exception as e:
            print("[ERR] The following error occured while trying to compare texts using w2v: "+str(e))