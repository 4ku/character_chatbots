install:
	pip install -r requirements.txt

gpt-models:
	pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
	git-lfs clone https://huggingface.co/4ku/gpt-persona-yoda app/models/gpt/models/gpt-persona-yoda
	git-lfs clone https://huggingface.co/4ku/gpt2-persona-yoda app/models/gpt/models/gpt2-persona-yoda
	git-lfs clone https://huggingface.co/4ku/gpt-persona-sponge_bob app/models/gpt/models/gpt-persona-sponge_bob
	git-lfs clone https://huggingface.co/4ku/gpt2-persona-sponge_bob app/models/gpt/models/gpt2-persona-sponge_bob

tfidf-models:
	pip install scikit-learn==1.2.2 nltk==3.8.1

rnn-models:
	wget https://huggingface.co/stblacq/yoda-rnn/resolve/main/yoda-rnn.tar -O app/models/rnn/models/yoda-rnn.tar
	wget https://huggingface.co/stblacq/yoda-rnn/resolve/main/formatted_movie_lines.txt -O app/models/rnn/models/formatted_movie_lines.txt


run:
	cd ./app && python3 main.py