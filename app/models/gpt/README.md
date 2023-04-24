# Conversational AI with Transfer Learning based on GPT and GPT-2

The model code was adopted from the [simpletransformers repository](https://github.com/ThilinaRajapakse/simpletransformers), which is derived from the [State-of-the-Art Conversational AI with Transfer Learning repository](https://github.com/huggingface/transfer-learning-conv-ai), and subsequently a little refined.

## Datasets
### Master Yoda corpus

The Yoda speech corpus was obtained from [this source](https://www.kaggle.com/datasets/stefanocoretta/yoda-speech-corpus). However, as the available data was insufficient, We utilized GPT-4 to generate additional data. The resultant training and test JSON files were saved as `train.json` and `test.json`, respectively. For all details on the data preprocessing steps, please refer to the `create_yoda_dataset.ipynb` file.

### Sponge Bob dataset
The Sponge Bob dataset has been parsed from [this kaggle dataset](https://www.kaggle.com/datasets/mikhailgaerlan/spongebob-squarepants-completed-transcripts). For all details on the data preprocessing steps, please refer to the `create_sponge_bob_dataset.ipynb` file in `dataset/sponge_bob` folder. The preprocessing is very similar to the Yoda data. 

## Models
You can train a conversational chatbot using either the GPT or GPT-2 model. However, for optimal performance, it is recommended to train a personalized chatbot using a pretrained model on the PERSONA-CHAT dataset.

### Train
The training process is described in the `train.ipynb` file. Select the character you want to train the model on. Then follow the described steps to train your own model.
**Note**: To train GPT and GPT-2 models you need at least 6Gb GPU memory.

### PERSONA-CHAT models
#### Pretrained GPT on PERSONA-CHAT

```
wget https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/gpt_personachat_cache.tar.gz
mkdir -p models/gpt_personachat/ && tar -xzvf gpt_personachat_cache.tar.gz -C models/gpt_personachat/
```

#### Pretrained GPT-2 on PERSONA-CHAT
A pretrained GPT-2 model was found in [gutenberg-dialog repository](https://github.com/ricsinaruto/gutenberg-dialog) and uploaded it to [Ivan's Hugging Face repository](https://huggingface.co/4ku/gpt2-personachat).

```
sudo apt install -y git-lfs
git lfs install
cd models && git-lfs clone https://huggingface.co/4ku/gpt2-personachat
```

