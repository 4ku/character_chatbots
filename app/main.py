# FastAPI imports
import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from html_utils import build_html_chat


from models import ConvGPTModel
from enums import ModelType, Character

# This is a global vars
# To allow correct behaviour for multiple
# users we need to use Sessions
history = []
conv_model = None

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
    global conv_model, history
    history = []

    conv_model = ConvGPTModel(ModelType(model), Character(character))
    return RedirectResponse("/chat")


@app.post("/chat", response_class=HTMLResponse)
@app.get("/chat", response_class=HTMLResponse)
async def root(request: Request, message: Optional[str] = Form(None)):

    if conv_model is None:
        raise HTTPException(status_code=404, detail="Form data not found")

    # if the Form is not None, then get a reply from the bot
    if message is not None:
        
        history.append(message)
        # gets a response of the AI bot
        response = conv_model.interact_single(message)
        history.append(response)

        # converts the chat history into an HTML dialog
        chat_html = '\n'.join([
            build_html_chat(is_me=i %
                            2 == 0, character=conv_model.character.value, text=msg)
            for i, msg in enumerate(history)
        ])

    else:
        chat_html = ''

    message_dict = {
        "request": request,
        "chat": chat_html,
        "model": conv_model.model_type.value
    }

    # returns the final HTML
    return templates.TemplateResponse("chat.html", message_dict)

# initialises the chatbot model and starts the uvicorn app
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
