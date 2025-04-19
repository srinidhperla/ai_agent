from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct")
)


agent.print_response("tell the difference between chaina and us in table form")