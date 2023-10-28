######################################################
# ------------ Dependencias del código ---------------
######################################################

import base64
import streamlit as st
import plotly.express as px
from Nucleo import Quizbot
from PIL import Image
import json

######################################################
# ------ Código relacionado a la presentación --------
######################################################

df = px.data.iris()
Racha = 0
Map = 1
contenido = Quizbot()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: rgb(210,154,20);
background: linear-gradient(0deg, rgba(210,154,20,1) 0%, rgba(254,252,248,1) 47%, rgba(255,255,255,1) 100%);
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
justify-content: center;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
    
st.markdown(page, unsafe_allow_html=True)
st.title("#Nombre")
st.header("Mira tu que slogan mas apañao")
######################################################
# ------ Código relacionado a la interacción ---------
######################################################

# Initialize session state variables if they don't exist yet
if "current_question" not in st.session_state:
    st.session_state.answers = {}
    st.session_state.current_question = 0
    st.session_state.questions = []
    st.session_state.right_answers = 0
    st.session_state.wrong_answers = 0

placeholder = st.empty()
with placeholder.container():
    st.image(Image.open(str(st.session_state.right_answers - st.session_state.wrong_answers)+'.png'), width=300)


def Correcto():
    amount = st.session_state.right_answers - st.session_state.wrong_answers
    if amount < 0:
        amount = 0
        
    placeholder.empty()
    with placeholder.container():
        st.image(Image.open(str(amount) + '.png'), caption='¡Bien hecho!', width=300)
        
def Incorrecto():
    amount = st.session_state.right_answers - st.session_state.wrong_answers
    if amount < 0:
        amount = 0
        
    placeholder.empty()
    with placeholder.container():
        st.image(Image.open(str(amount) + '.png'), caption='Ups...', width=300)


# Adaptar
def display_question():
    # Handle first case
    if len(st.session_state.questions) == 0:
        first_question = Quizbot()
        st.session_state.questions.append(first_question)

    # Disable the submit button if the user has already answered this question
    submit_button_disabled = st.session_state.current_question in st.session_state.answers

    # Get the current question from the questions list
    question = st.session_state.questions[st.session_state.current_question]

    # Display the question prompt
    st.write(f"{st.session_state.current_question + 1}. {question['question']}")

    # Use an empty placeholder to display the radio button options
    options = st.empty()

    # Display the radio button options and wait for the user to select an answer
    user_answer = options.radio("Your answer:", question["options"], key=st.session_state.current_question)

    # Display the submit button and disable it if necessary
    submit_button = st.button("Submit", disabled=submit_button_disabled)

    # If the user has already answered this question, display their previous answer
    if st.session_state.current_question in st.session_state.answers:
        index = st.session_state.answers[st.session_state.current_question]
        options.radio(
            "Your answer:",
            question["options"],
            key=float(st.session_state.current_question),
            index=index,
        )

    # If the user clicks the submit button, check their answer and show the explanation
    if submit_button:
        # Record the user's answer in the session state
        st.session_state.answers[st.session_state.current_question] = question["options"].index(user_answer)

        # Check if the user's answer is correct and update the score
        if user_answer == question["answer"]:
            st.write("¡Muy bien!")
            st.session_state.right_answers += 1
            Correcto()
        else:
            st.write(f"¡Ups! la respuesta correcta es: {question['answer']}.")
            st.session_state.wrong_answers += 1
            Incorrecto()

    # Display the current score
    st.write(f"Respuestas correctas:   {st.session_state.right_answers}")
    st.write(f"Respuestas equivocadas: {st.session_state.wrong_answers}")


# Define a function to go to the next question
def next_question():
    # Move to the next question in the questions list
    st.session_state.current_question += 1

    # If we've reached the end of the questions list, get a new question
    if st.session_state.current_question > len(st.session_state.questions) - 1:
        next_question = Quizbot()
        st.session_state.questions.append(next_question)



# Define a function to go to the previous question
def prev_question():
    # Move to the previous question in the questions list
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1
        st.session_state.explanation = None


# Create a 3-column layout for the Ant/Sig buttons and the question display
col1, col2, col3 = st.columns([1, 6, 1])

# Add a Prev button to the left column that goes to the previous question
with col1:
    if col1.button("Ant"):
        prev_question()

# Add a Next button to the right column that goes to the next question
with col3:
    if col3.button("Sig"):
        next_question()

# Display the actual quiz question
with col2:
    display_question()


        
download_button = st.sidebar.download_button(
    "Download Quiz Data",
    data=json.dumps(st.session_state.questions, indent=4),
    file_name="quiz_session.json",
    mime="application/json",
)
