import enum


class ModelType(enum.Enum):
    GPT = "gpt"
    GPT2 = "gpt2"
    SIMPLE = "TF-IDF"
    RNN = "rnn"


class Character(enum.Enum):
    YODA = "yoda"
    SPONGEBOB = "sponge_bob"
