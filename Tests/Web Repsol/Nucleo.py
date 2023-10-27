'''
    Nucleo.py -> contiene el enlace a GPT para hacer prompting.
    Contiene la robustez y condiciones necesarias según el caso de uso, y
    medidas generales para evitar problemas de divergencia (alucinaciones, 
    desvíos del tópico...).
    
    DEPENDENCIAS: clave.json (clave de acceso a GPT)
'''

# ---------------------------- Código para el uso de GPT ----------------------------
import openai
import os
import json

def get_completion(prompt, model="gpt-3.5-turbo"):
    '''
    Función encargada de pasar el prompt a GPT.
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

api_key = os.getenv('OPENAI_API_KEY')
with open('clave.json') as f:
    data = json.load(f)
    api_key = data['key']
openai.api_key = api_key



# ---------------------------- Robustez dada al modelo ----------------------------
contexto = """Eres una IA divulgadora sobre transición energética.
    Tu trabajo es mostrar información al usuario relativa a la transición energética y tienes prohibido
    hablar de otros temas, ya que eres una divulgadora sobre éste tema solamente. Dispones de la siguiente información a divulgar: """
with open('info_mia.txt', 'r', encoding="utf-8") as file:
    contexto += '\n' + file.read()


def Chatbot(prompt):
    '''
    Esta función está pensada para el uso en Chatbots de Repsol.
    '''
    mensaje = contexto + '\n El comentario del usuario es: ' + prompt
    
    return get_completion(mensaje)
        
    
    