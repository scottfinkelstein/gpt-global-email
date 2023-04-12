import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

template = """
    Below is an email that may be poorly worded. Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you about.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.

    Here are some examples of words in different dialects:
    - American English: French Fries, cotton candy, apartment, garbage, cookie
    - British English: chips, candyfloss, flat, rubbish

    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR RESPONSE:
"""



# prompt = PromptTemplate(
#     input_variables=['tone', 'dialect', 'email'],
#     template=template
# )

# def load_LLM():
#     llm = OpenAI(temperature=0.5)
#     return llm

# llm = load_LLM()

st.set_page_config(page_title='Globalize Email', page_icon=':robot:')
st.header('Globalize Text')

col1, col2 = st.columns(2)

with col1:
    st.markdown("Often professionals would like to improve their emails, but don't know how. Globalize Email will help you improve your email skills by converting your emails.")

with col2:
    st.image('firefly.jpg', width=500, caption="abstract")

st.markdown('## Enter Your Email to Convert')

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        'Which tone would you like your email to have?',
        ('Formal', 'Informal')
    )
with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American English', 'British English')
    )

def get_text():
    input_text = st.text_area(label='', placeholder='Your Email...', key='email_input')
    return input_text


email_input = get_text()

st.markdown('## Your Converted Email:')

if email_input:
    chat = ChatOpenAI(temperature=0)

    human_message_prompt = HumanMessagePromptTemplate.from_template(template)
    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    formatted_email = chain.run(tone=option_tone, dialect=option_dialect, email=email_input)
   
    st.write(formatted_email)