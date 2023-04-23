# Simple chatbot using TF_IDF approach
The model code was taken from the [this repository](https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK) and modified.


## Setup environment

Install requirements
```
pip install -r requirements
```

## Chatbot data
All replies from PERSONA-CHAT dataset is stored in `dataset/personachat_train_statements.txt` (the ground truth candidates for each utterance). This data can be enough to talk about general topics with chatbot. But there is also a data of Master Yoda and Sponge Bob speech.  

### Master Yoda
All Master Yoda utterances parsed from [this source](https://www.kaggle.com/datasets/stefanocoretta/yoda-speech-corpus) is stored in `dataset/yoda/yoda_statements.txt`. Also here is merged data with PERSONA-CHAT dataset (`personachat_train_statements.txt` file) stored in `dataset/yoda/personachat_yoda_statements.txt`.

### Sponge Bob
All Sponge Bob utterances parsed from [this source](https://www.kaggle.com/datasets/mikhailgaerlan/spongebob-squarepants-completed-transcripts) is stored in `dataset/sponge_bob/sponge_bob_statements.txt`. Also here is merged data with PERSONA-CHAT dataset (`personachat_train_statements.txt` file) stored in `dataset/sponge_bob/personachat_sponge_bob_statements.txt`.

## Interact
```
python chatbot.py
```