from .conv_ai import ConvAIModel, ConvAIArgs
import os
import torch
import sys

sys.path.append("../..")

from enums import ModelType, Character
from dataset.yoda.personality import yoda_personality
from dataset.sponge_bob.personality import sponge_bob_personality


class ConvGPTModel:
    def __init__(self, model_type: ModelType, character: Character):
        model_args = ConvAIArgs()
        model_args.max_history = 2
        model_args.max_length = 30
        model_args.num_candidates = 1
        model_args.reprocess_input_data = True

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.model = ConvAIModel(
            model_type.value,
            os.path.join(dir_path, "models", f"{model_type.value}-persona-{character.value}"),
            use_cuda=torch.cuda.is_available(),
            args=model_args
        )
        self.personality = yoda_personality if character == Character.YODA else sponge_bob_personality

        self.history = []
        self.model_type = model_type
        self.character = character

    def interact_single(self, message: str):
        response, self.history = self.model.interact_single(
            message, self.history[-2:], self.personality)
        self.history.append(message)
        self.history.append(response)
        return response

    def interact(self):
        self.model.interact(personality=self.personality)
