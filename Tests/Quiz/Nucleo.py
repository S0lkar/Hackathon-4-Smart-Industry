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
import random

def get_completion(prompt, model="gpt-3.5-turbo"):
    '''
    Función encargada de pasar el prompt a GPT.
    '''
    messages = [{"role": "assistant", "content": prompt}]
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
contexto_chatbot = """Eres una IA divulgadora sobre transición energética.
    Tu trabajo es mostrar información al usuario relativa a la transición energética y tienes prohibido hablar de cualquier
    tema distinto a la transición energética. Devolverás una respuesta resumida en torno a 25 palabras. Dispones de la siguiente información para divulgar:"""

contexto_quiz = """Dispones de la siguiente información para divulgar:"""


with open('info_tockens.txt', 'r', encoding="utf-8") as file:
   contexto_chatbot += '\n' + file.read()
   contexto_quiz += '\n' + file.read()


def Chatbot(prompt):
    '''
    Esta función está pensada para el uso en Chatbots de Repsol.
    '''
    if prompt != '':
        mensaje = contexto_chatbot + '\n El comentario del usuario es: ' + prompt
        return get_completion(mensaje)
    else:
        return ""

bateriaPreguntas = []
def Quizbot():
    global bateriaPreguntas, contexto_quiz
    
    contexto = "Eres una IA encargada de plantear UNA SOLA pregunta fácil sobre transición energética en Repsol. Sabes que " + contexto_quiz + 'No repetir preguntas como '
    for i in bateriaPreguntas:
        contexto += i + ' '
        
    pregunta = get_completion(contexto)
    bateriaPreguntas.append(pregunta)
    
    contexto_v = "Eres una IA encargada de responder una pregunta fácil sobre transición energética en Repsol. Sabes que " + contexto_quiz + ".\n Debes responder correctamente y con menos de 6 palabras. La pregunta es: " + pregunta
    respuesta_v = get_completion(contexto_v)
    contexto_f = contexto = "Eres una IA encargada de responder una pregunta fácil sobre transición energética en Repsol. Sabes que " + contexto_quiz + ".\n Debes responder incorrectamente y con menos de 6 palabras. La pregunta es: " + pregunta
    respuesta_f1 = get_completion(contexto_f)
    
    seguridad = 0
    respuesta_f2 = respuesta_f1
    
    while respuesta_f2 == respuesta_f1 and seguridad < 4:
        contexto_f = contexto = "Eres una IA encargada de responder una pregunta fácil sobre transición energética en Repsol. No puedes responder " + respuesta_f1 + '. Sabes que ' + contexto_quiz + ".\n Debes responder incorrectamente y con menos de 9 palabras. La pregunta es: " + pregunta
        respuesta_f2 = get_completion(contexto_f)
        seguridad += 1
    
    opc = random.shuffle([respuesta_v, respuesta_f1, respuesta_f2])
    return {'question': pregunta, 'options': opc, 'answer': respuesta_v}
    
