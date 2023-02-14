import streamlit as st
import random as rd

class Would:
    def __init__(self):
        pass

    def game(self):
        lang = ['English - Normal', 'English - Dirty', 'Lebnene - Dirty']

        nvr_lang = st.selectbox('Select a Language', lang)
        gen = st.button('Generate')
        if nvr_lang == 'English - Normal':
            if gen:
                st.subheader(rd.choice(self.nvr_eng))
        elif nvr_lang == 'English - Dirty':
            if gen:
                st.subheader(rd.choice(self.nvr_dirty_eng))
        elif nvr_lang == 'Lebnene - Dirty':
            if gen:
                st.subheader(rd.choice(self.nvr_dirty_leb))