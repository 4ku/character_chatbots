# FastAPI imports
import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from html_utils import build_html_chat

# GPT model imports
from gpt_models.conv_ai import ConvAIArgs, ConvAIModel
from dataset.yoda.personality import yoda_personality
from dataset.sponge_bob.personality import sponge_bob_personality

MODELS_FOLDER = 'gpt_models/models'

# This is a global vars
# To allow correct behaviour for multiple
# users we need to use Sessions
history = []
model_character = ''
model_type = ''

app = FastAPI()
# mounts the static folder that contains the css file
app.mount("/static", StaticFiles(directory="static"), name="static")

# locates the template files that will be modified at run time
# with the dialog form the user and bot
templates = Jinja2Templates(directory="templates")


# Combine this 2 functions
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def process_form(request: Request, character: str = Form(...), model: str = Form(...)):
    global model_character, model_type, history
    history = []
    model_character = character
    model_type = model
    return RedirectResponse("/chat")


@app.post("/chat", response_class=HTMLResponse)
@app.get("/chat", response_class=HTMLResponse)
async def root(request: Request, message: Optional[str] = Form(None)):
    global model_character, model_type, history

    if model_character is None or model_type is None:
        raise HTTPException(status_code=404, detail="Form data not found")

    model_personality = ''
    if model_character == 'yoda':
        model_personality = yoda_personality
    elif model_character == 'sponge_bob':
        model_personality = sponge_bob_personality

    if model_type != 'TF-IDF':
        model_args = ConvAIArgs()
        model_args.max_history = 2
        model_args.max_length = 30
        model_args.num_candidates = 1
        model_args.reprocess_input_data = True

        model = ConvAIModel(
            model_type=f'{model_type}',
            model_name=f'{MODELS_FOLDER}/{model_type}-persona-{model_character}',
            use_cuda=True,
            args=model_args
        )

    # if the Form is not None, then get a reply from the bot
    if message is not None:

        # gets a response of the AI bot
        _, history = model.interact_single(message, history, model_personality)

        # converts the chat history into an HTML dialog
        chat_html = '\n'.join([
            build_html_chat(is_me=i %
                            2 == 0, character=model_character, text=msg)
            for i, msg in enumerate(history)
        ])

    else:
        chat_html = ''

    message_dict = {
        "request": request,
        "chat": chat_html,
        "model": model_type
    }

    # returns the final HTML
    return templates.TemplateResponse("chat.html", message_dict)

# initialises the chatbot model and starts the uvicorn app
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8001)
