## Conversational AI Chatbot with Transfer Learning

#### **What is this?**
This is a FastAPI web application, that allows user to interact with different chatbots models (GPT, GPT2, etc). User can select model and it's personality (Yoda or SpongeBob).

Code was inspired by "[Develop a Conversational Bot in 4 simple steps](https://towardsdatascience.com/develop-a-conversational-ai-bot-in-4-simple-steps-1b57e98372e2)" that explains how to create a ChatBot using PyTorch transformers, FastAPI and Docker

#### **What is included here?**

* `app/main.py`: Main app file and docker entrypoint. This defines the FastAPI logic;
* `app/model.py`: Utility file that defines the model's logic;
* `app/static/`: Contains the icons and CSS files
* `app/templates/`: Contains the `index.html` template file that will be modified at run time with the dialog HTML using jinja
* `app/dataset/`: Data used for training Yoda and Sponge Bob personalities
* `app/models/gpt`: Contains all files for inferencing and fine-tuning small GPT ang GPT-2 models.
* `app/models/rnn`: Contains all files for inferencing and fine-tuning Pytorch RNN model.
* `app/models/TF_IDF`: Contains all files for inferencing simple statistical model.
* `requirements.txt`: File that contains all dependencies to install.

#### **How to run?**
## 1. Clone the repository to your local machine.
### 1a. Create a virtual environment  if needed

Your environment should have Python 3.10 or newer as a main Python version.

## 2. Install Base Dependencies
  ``` 
    make install
   ```
## 3. Set up Model Specific Dependencies
### 3 a. Set up GPT-Models
``` 
    make gpt-models
 ```

### 3 b. Set up Pytorch-Models
``` 
    make rnn-models
 ```

### 3 c. Set up TFIDF-Models
``` 
    make tfidf-models
 ```

## 4. Run Project
```
make run
```

#### **User guide**
1. In the first page you can select model and character. After pressing ```Start chat``` you will be redirected to the chat page.
2. In this page you can chat with selected character about everything. Below you can see example of chats.

![Chat with Sponge Yoda](app/images/Yoda_screenshot.png "Chat with Yoda")

![Chat with Sponge Bob](app/images/Sponge_Bob_screenshot.png "Chat with Sponge Bob")

3. In chat page the is also a ```Go back``` button. After pressing it you will return to the first page.