from flask import Flask,render_template, request, Response
from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import *
from selecionar_documento import *
from selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4-1106-preview"

minhas_tools = [
    {"type": "retrieval"},
    {
      "type": "function",
            "function": {
            "name": "validar_codigo_promocional",
            "description": "Valide um código promocional com base nas diretrizes de Descontos e Promoções da empresa",
            "parameters": {
                "type": "object",
                "properties": {
                    "codigo": {
                        "type": "string",
                        "description": "O código promocional, no formato, CUPOM_XX. Por exemplo: CUPOM_ECO",
                    },
                    "validade": {
                        "type": "string",
                        "description": f"A validade do cupom, caso seja válido e esteja associado as políticas. No formato DD/MM/YYYY.",
                    },
                },
                "required": ["codigo", "validade"],
            }
        }
    }
    
]