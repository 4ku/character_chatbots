# FastAPI imports
import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from html_utils import build_html_chat

# GPT model imports
from gpt_models.conv_ai import ConvAIArgs, ConvAIModel
from dataset.yoda.personality import yoda_personality
from dataset.sponge_bob.personality import sponge_bob_personality

MODELS_FOLDER = 'gpt_models/models'
history = []

app = FastAPI()


# mounts the static folder that contains the css file
app.mount("/static", StaticFiles(directory="static"), name="static")

# locates the template files that will be modified at run time
# with the dialog form the user and bot
templates = Jinja2Templates(directory="templates")


@app.post("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request, message: Optional[str] = Form(None)):
    global history
    # if the Form is not None, then get a reply from the bot
    if message is not None:

        # gets a response of the AI bot
        _, history = model.interact_single(message, history, yoda_personality)

        # converts the chat history into an HTML dialog
        chat_html = '\n'.join([
            build_html_chat(is_me=i %
                            2 == 0, text=msg)
            for i, msg in enumerate(history)
        ])

    else:
        chat_html = ''

    message_dict = {
        "request": request,
        "chat": chat_html
    }

    # returns the final HTML
    return templates.TemplateResponse("index.html", message_dict)

# initialises the chatbot model and starts the uvicorn app
if __name__ == "__main__":
    model_args = ConvAIArgs()
    model_args.max_history = 2
    model_args.max_length = 30
    model_args.num_candidates = 1
    model_args.reprocess_input_data = True

    model = ConvAIModel(
        model_type='gpt2',
        model_name=f'{MODELS_FOLDER}/gpt2-persona-yoda',
        use_cuda=True,
        args=model_args
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
