import os
from dataset.yoda_personality import yoda_personality 
from conv_ai import ConvAIModel, ConvAIArgs
import sys


model_args = ConvAIArgs()
model_args.max_history = 2
model_args.max_length = 30
model_args.num_candidates = 1
model_args.reprocess_input_data = True

MODELS_FOLDER = 'models'

# Get the command line arguments
args = sys.argv
if len(args) == 1:
    print("A model type should be specified. gpt or gpt2")
    exit()

if args[1] not in ['gpt', 'gpt2']:
    print("There are only to model types available. gpt or gpt2")
    exit()

model = ConvAIModel(
    args[1],
    os.path.join(MODELS_FOLDER, "trained_models", args[1]),
    use_cuda=True,
    args=model_args
)

model.interact(
    personality=yoda_personality
)