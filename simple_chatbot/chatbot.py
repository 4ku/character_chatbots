
# import necessary libraries
from nltk.stem import WordNetLemmatizer
import nltk
import string  # to process standard python strings
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)  # for downloading packages

# uncomment the following only the first time
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only


# Reading in the corpus
DATA_PATH = "../dataset/yoda/personachat_yoda_statements.txt"
with open(DATA_PATH, 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# TOkenisation
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


print(">>> Hi!")
while (True):
    user_response = input()
    user_response = user_response.lower()
    robo_response = response(user_response)

    print(">>>", robo_response)
    sent_tokens.remove(user_response)
