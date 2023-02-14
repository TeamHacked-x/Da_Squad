import streamlit as st
import random as rd
import json

class Spy:
    def __init__(self):
        self.player_count = [3,4,5,6,7,8]
        self.spy_count = [1,2,3]
        self.words = ['School', 'Church', 'Parking', 'Cinema', 'Bed', 'Mall', 'Hospital', 'Animal', 'Bank', 'Pool', 'Airplane', 'Gym', '']
        self.players = []

    def game(self):
        play1, play2 = st.columns([1,1])
        with play1:
            players_count = st.selectbox('Kam Wahad Ento?', self.player_count)
        with play2:
            spies_count = st.selectbox('Kam Spy Fi?', self.spy_count)

        if st.button('Play'):
            with open('index.txt', 'w') as f:
                f.write('')
            word = rd.choice(self.words)
            for i in range(players_count + 1):
                if i == 0:
                    pass
                else:
                    self.players.append({f'Player {i}': ''})

            if spies_count == 1:
                er = rd.choice(self.players)
                er_i = self.players.index(er)
                er[f'Player {er_i +1 }'] = 'Spy'
                for i in range(len(self.players)):
                    if i == er_i:
                        pass
                    else:
                        self.players[i][f'Player {i+1}'] = word

            elif spies_count == 2:
                ayren = rd.sample(self.players, 2)
                er_1 = self.players.index(ayren[0])
                er_2 = self.players.index(ayren[1])
                ayren[0][f'Player {er_1 + 1}'] = 'Spy'
                ayren[1][f'Player {er_2 + 1}'] = 'Spy'
                for i in range(len(self.players)):
                    if i == er_1 or i == er_2:
                        pass
                    else:
                        self.players[i][f'Player {i+1}'] = word

            elif spies_count == 3:
                ayren = rd.sample(self.players, 3)
                er_1 = self.players.index(ayren[0])
                er_2 = self.players.index(ayren[1])
                er_3 = self.players.index(ayren[2])
                ayren[0][f'Player {er_1 + 1}'] = 'Spy'
                ayren[1][f'Player {er_2 + 1}'] = 'Spy'
                ayren[2][f'Player {er_3 + 1}'] = 'Spy'
                for i in range(len(self.players)):
                    if i == er_1 or i == er_2 or i == er_3:
                        pass
                    else:
                        self.players[i][f'Player {i+1}'] = word

            with open('spy_game.json', 'w') as f:
                json.dump(self.players, f)

            st.success('Game Started!')

        st.markdown('** **')
        st.write('Player 1 reveals his identity and passes the phone to the next player')

        spy1, spy2 = st.columns([0.5,1])
        with spy1:
            reveal = st.button('Reveal')
        with spy2:
            next = st.button('Next')

        with open('spy_game.json', 'r') as f:
            data = json.load(f)
            try:
                with open("index.txt", "r") as indexf:
                    index = int(indexf.read().strip())
            except:
                index = 0
            if reveal:
                try:
                    if data[-1] !=data[index]:
                        if data[index][f'Player {index + 1}'] == 'Spy':
                            st.subheader(f"Player {index + 1}")
                            st.write(f"{data[index][f'Player {index + 1}']}")
                        else:
                            st.subheader(f"Player {index + 1}")
                            st.write(f"Word:  {data[index][f'Player {index + 1}']}")
                    elif data[-1] ==data[index] and data[index][f'Player {index + 1}'] == 'Spy':
                        st.subheader(f"Player {index + 1}")
                        st.write(f"{data[index][f'Player {index + 1}']}")
                        st.info('All Players Have Been Revealed!')
                    else:
                        st.subheader(f"Player {index + 1}")
                        st.write(f"Word: {data[index][f'Player {index + 1}']}")
                        st.info('All Players Have Been Revealed!')
                except IndexError:
                    st.info('All Players Have Been Revealed, Please Restart The Game')