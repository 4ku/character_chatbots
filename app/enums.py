import enum 

class ModelType(enum.Enum):
    GPT = "gpt"
    GPT2 = "gpt2"


class Character(enum.Enum):
    YODA = "yoda"
    SPONGEBOB = "sponge_bob"