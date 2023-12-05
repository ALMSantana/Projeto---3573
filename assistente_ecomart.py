from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"
contexto = carrega("dados/ecomart.txt")

assistente = cliente.beta.assistants.create(
    name="Atendente EcoMart",
    instructions = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Além disso, adote a persona abaixo para respondero ao cliente.
            
            ## Contexto
            {contexto}

            ## Persona
            {personas["neutro"]}
            """,
    model = modelo
)

thread = cliente.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Liste os produtos"
        }
    ]
)

cliente.beta.threads.messages.create(
    thread_id=thread.id, 
    role = "user",
    content =  " da categoria moda sustentável"
)

run = cliente.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistente.id
)

while run.status !="completed":
    run = cliente.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

historico = cliente.beta.threads.messages.list(thread_id=thread.id).data

for mensagem in reversed(historico):
    print(f"role: {mensagem.role}\nConteúdo: {mensagem.content[0].text.value}")
