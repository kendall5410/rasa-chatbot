from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from rasa.core.agent import Agent
from rasa.core.http_interpreter import RasaNLUHttpInterpreter
import openai 

app = FastAPI()

# interpreter = RasaNLUHttpInterpreter("models/nlu")
# agent = Agent.load(domain='models', http_interpreter=interpreter)

interpreter = RasaNLUHttpInterpreter()
model_path = "models"  # Provide the correct path to the trained model directory
agent = Agent.load(model_path, http_interpreter=interpreter)

@app.post("/chat")
async def chat(message: str):
    print (message)
    responses = await agent.handle_text(message)
    bot_response = responses[0]['text']
    return JSONResponse(content={"response": bot_response})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)