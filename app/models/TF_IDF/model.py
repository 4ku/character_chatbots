
# import necessary libraries
from enums import ModelType, Character
from nltk.stem import WordNetLemmatizer
import nltk
import string  # to process standard python strings
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import sys
import os

warnings.filterwarnings('ignore')

sys.path.append("../..")

from dataset.yoda.personality import yoda_personality
from dataset.sponge_bob.personality import sponge_bob_personality

nltk.download('popular', quiet=True)  # for downloading packages

# uncomment the following only the first time
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only

# Preprocessing
lemmer = WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


class SimpleConvModel:
    def __init__(self, model_type: ModelType, character: Character):
        self.personality = yoda_personality if character == Character.YODA else sponge_bob_personality

        self.model_type = model_type
        self.character = character
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Reading in the corpus
        data_path = os.path.join(dir_path, '../../dataset', character.value,
                                 f"personachat_{character.value}_statements.txt")
        with open(data_path, 'r', encoding='utf8', errors='ignore') as fin:
            raw = fin.read().lower()

        # TOkenisation
        self.sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences

    def interact_single(self, message: str):
        # Generating response
        chatbot_response = ''
        self.sent_tokens.append(message)
        TfidfVec = TfidfVectorizer(
            tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        self.sent_tokens.remove(message)
        if req_tfidf == 0:
            chatbot_response = chatbot_response+"I am sorry! I don't understand you"
            return chatbot_response
        else:
            chatbot_response = chatbot_response+self.sent_tokens[idx]
            return chatbot_response

    def interact(self):
        while True:
            user_response = input()
            user_response = user_response.lower()
            chatbot_response = self.interact_single(user_response)
            print(">>>", chatbot_response)
