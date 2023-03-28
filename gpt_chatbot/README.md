# Conversational AI with Transfer Learning based on GPT and GPT-2

The model code was adopted from the [simpletransformers repository](https://github.com/ThilinaRajapakse/simpletransformers), which is derived from the [State-of-the-Art Conversational AI with Transfer Learning repository](https://github.com/huggingface/transfer-learning-conv-ai), and subsequently a little refined.

## Setup environment
```
python3 -m venv env
. env/bin/activate
```

Install appropriate PyTorch version
```
pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
```

Install other requirements
```
pip install -r requirements
```
## Datasets
### Master Yoda corpus

The Yoda speech corpus was obtained from [this source](https://www.kaggle.com/datasets/stefanocoretta/yoda-speech-corpus). However, as the available data was insufficient, I utilized GPT-4 to generate additional data. The resultant training and test JSON files were saved as `train_yoda_corpus.json` and `test_yoda_corpus.json`, respectively. For all details on the data preprocessing steps, please refer to the `create_yoda_dataset.ipynb` file.


## Models
You can train a conversational chatbot using either the GPT or GPT-2 model. However, for optimal performance, it is recommended to train a personalized chatbot using a pretrained model on the PERSONA-CHAT dataset.

### Pretrained GPT on PERSONA-CHAT

```
wget https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/gpt_personachat_cache.tar.gz
mkdir models/gpt_personachat_cache/ && tar -xzvf gpt_personachat_cache.tar.gz -C models/gpt_personachat_cache/
```

### Pretrained GPT-2 on PERSONA-CHAT
I found a pretrained GPT-2 model in [gutenberg-dialog repository](https://github.com/ricsinaruto/gutenberg-dialog) and upload it to [my Hugging Face repository](https://huggingface.co/4ku/gpt2-personachat).

```
sudo apt install -y git-lfs
git lfs install
cd models && git-lfs clone https://huggingface.co/4ku/gpt2-personachat
```

## Interact

```
python3 interact.py gpt
```

or

```
python3 interact.py gpt2
```