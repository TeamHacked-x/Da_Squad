import json
import streamlit as st
import random as rd
from streamlit_option_menu import option_menu

#HTML/CSS
import html_design as ht

#-------------------------------------Games Classes
from database import Login
from spy import Spy
from never import Never
from would import Would
#---------------------------------Construct Objects
lg = Login()
spy = Spy()
nvr = Never()
wld = Would()


#------------------------------------------------------------------------------------------------Page Config
st.set_page_config(page_title='Da Squad', initial_sidebar_state='expanded', layout='wide')
# st.markdown(ht.hide_streamlit_items, unsafe_allow_html=True)


#-------------------------------------------------------------------------------------------------------Main
options = ['Spy', 'Never Have I Ever', 'Would You Rather']
st.sidebar.markdown(ht.sidebar_title, unsafe_allow_html=True)
login_user = st.sidebar.text_input('Username')
login_pass = st.sidebar.text_input('Password', type='password')

if st.sidebar.checkbox('Login'):
    if lg.login_user(login_user, login_pass):
        st.sidebar.success(f'Logged in as @{login_user}')
        with st.sidebar:

            game = option_menu(menu_title=False, menu_icon='None' , icons=['None', 'None', 'None'], options=options)

        if game == 'Spy':
            st.header('Spy')
            st.text('''
            Spy Game Rules:
            -Na2o kam sha5es ento w kam spy fi
            -Press "Play" to start the game
            -Reveal your identity then press "Next"
            and give it to the next player
            ''')
            spy.game()

        elif game == 'Never Have I Ever':
            st.header("Never Have I Ever")
            st.text('''
                    Game Rules:
                    -Choose a player to read the statements
                    -Each players get 10 lives (10 Fingers)
                    -Players who have done the action described in the statement puts their finger down
                    -The Game will end until one of the players loses the 10 fingers
                    ''')
            nvr.game()

        elif game == 'Would You Rather':
            st.header("Would You Rather")
            st.text('''
                    Game Rules:
                    -Choose a player to read the statements
                    -The players will have to choose one of the 2 options in each statement and explain why
                    -Each players get 5 lives (5 Fingers)
                    -Players who don't respond with any of the options, puts their finger down
                    -The Game will end until one of the players loses the 5 fingers
                    ''')
            wld.game()

    else:
        st.sidebar.error('Incorrect Username or Password')

