import json
import streamlit as st
import random as rd
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Da Squad', initial_sidebar_state='expanded', layout='wide')
hide_streamlit_items = """
            <style>
            /*header{visibility: hidden;}*/
            /*#MainMenu {visibility: hidden;}*/
            footer {visibility: hidden;}

            .css-6qob1r p{
                color: white !important;
                font-family: Copperplate, Fantasy;
                font-size: 30px;
            }
            </style>
            """
st.markdown(hide_streamlit_items, unsafe_allow_html=True)

#Option Menu
options = ['Home', 'Spy', 'Never Have I Ever']
with st.sidebar:
    game = option_menu(menu_title='Games 3al Lebnene', menu_icon='None' , icons=['None', 'None', 'None'], options=options)

class Games():
    def __init__(self):
        #SPY INIT
        self.player_count = [3,4,5,6,7,8]
        self.spy_count = [1,2,3]
        self.words = ['School', 'Church', 'Parking', 'Cinema', 'Bed', 'Mall', 'Hospital', 'Animal', 'Bank', 'Pool', 'Airplane', 'Gym', '']
        self.players = []

        #NEVER INIT
        self.nvr_eng = ['Never have I ever got a tattoo', 'Never have I ever done a nude streak in public', 'Never have I ever stood someone up on a date', 'Never have I ever had a speeding ticket', 'Never have I ever ghosted someone', 'Never have I ever lied to get out of going to work', 'Never have I ever given a fake name', 'Never have I ever dumped someone over text', 'Never have I ever been sick on public transport', 'Never have I ever lied to someone in this room', 'Never have I ever texted an ex out of nowhere', 'Never have I ever lied on a dating app', 'Never have I ever shoplifted', "Never have I ever kissed a friend's sibling", 'Never have I ever catfished someone', 'Never have I ever been refused entry to a club', 'Never have I ever had a holiday romance', "Never have I ever used someone else's toothbrush", 'Never have I ever peed in the shower', "Never have I ever stalked an ex's new partner on social media", 'Never have I ever been thrown out of a bar or club', 'Never have I ever gone skinny dipping', "Never have I ever gone out with a friend's ex", "Never have I ever said 'I love you' when I didn't mean it", 'Never have I ever been mugged', 'Never have I ever broken a bone', 'Never have I ever lied about leaving the club early', 'Never have I ever been sick on my friend/someone else', 'Never have I ever kissed a celebrity', 'Never have I ever eaten leftover food from another table at a restaurant', 'Never have I ever gone on a blind date', 'Never have I ever stolen anything', 'Never have I ever been cheated on', 'Never have I ever dined and dashed', 'Never have I ever trespassed', 'Never have I ever spent more than Â£200 on a night out', 'Never have I ever DMed a celebrity', 'Never have I ever paid for a gym class and not attended', 'Never have I ever caught my parents having sex', 'Never have I ever been caught by my parents having sex', 'Never have I ever been to a nudist beach', 'Never have I ever pulled an all nighter', 'Never have I ever cheated on a test or exam', 'Never have I ever pretended to be someone else', 'Never have I ever ignored someone I knew in public', 'Never have I ever ruined an item of clothing I borrowed from a friend', 'Never have I ever hitchhiked a ride', 'Never have I ever snuck into a festival or club', 'Never have I ever lied in this game', 'Never have I ever peed in public', 'Never have I ever lied about kissing someone', 'Never have I ever broken the law', 'Never have I ever fancied someone in this room', 'Never have I ever got drunkenly locked out of my house', 'Never have I ever lied to my boss', "Never have I ever slipped into someone's DMs", 'Never have I ever got a tattoo I regretted', 'Never have I ever not worn underwear on a night out', 'Never have I ever looked through my partnerâ€™s phone', 'Never have I ever edited my selfies', 'Never have I ever used someone elseâ€™s Netflix account', 'Never have I ever ghosted someone for something tiny and unimportant', 'Never have I ever told someoneâ€™s secret', "Never have I ever returned something after I'd already worn it", 'Never have I ever dropped my phone in a toilet', 'Never have I ever not eaten before a night out to get more drunk', 'Never have I ever Googled my own name', 'Never have I ever forgotten where I parked my car', "Never have I ever fancied a friend's parent", 'Never have I ever used a pick up line', 'Never have I ever cheated on anyone', 'Never have I ever re-gifted a present I didnâ€™t want', 'Never have I ever given a partner an embarrassing pet name', 'Never have I ever created a fake Instagram', 'Never have I ever fake-cried to get something', 'Never have I ever used a fake ID to get into a club', "Never have I ever recreated the I'm a Celeb eating trial", "Never have I ever forgotten a friend's birthday", 'Never have I ever skipped class', 'Never have I ever cooked drunk and burnt the food']
        self.nvr_dirty_eng = ['Never have I ever had sex in a public place', 'Never have I ever sent a dirty text to the wrong person', 'Never have I ever said the wrong name in bed', 'Never have I ever had a friend with benefits', "Never have I ever slept with someone whose name I don't know", 'Never have I ever been to a sex shop', 'Never have I ever had a threesome', "Never have I ever joined the 'mile high' club", 'Never have I ever sent a sexy selfie', 'Never have I ever had sex in the sea/a swimming pool', 'Never have I ever had a one night stand', 'Never have I ever faked an orgasm', 'Never have I ever flashed someone', 'Never have I ever given or received a lap dance', 'Never have I ever slept with a co-worker', 'Never have I ever gone back to an ex', "Never have I ever been 'walked in on' while having sex", 'Never have I ever had a sex dream about someone in this room', 'Never have I ever had a sex dream about someone the people in this room know', 'Never have I ever had a favourite sex toy', 'Never have I ever role-played in bed', 'Never have I ever eaten food off a partner', 'Never have I ever sucked my partnerâ€™s toes', 'Never have I ever done the walk of shame', 'Never have I ever had a sex dream about someone else when I was in a relationship', 'Never have I ever Googled sex positions', 'Never have I ever had a sexy nickname / given someone a sexy nickname', 'Never have I ever kissed more than one person in one day', 'Never have I ever had to hide a love bite', 'Never have I ever had a sex fantasy', 'Never have I ever played strip poker', 'Never have I ever snuck someone into the house', 'Never have I ever acted out my sex fantasy', 'Never have I ever used handcuffs or something similar', 'Never have I ever sent a nude picture or video']
        self.nvr_dirty_leb = ['Never have I ever nteket bi mahal public', 'Never have I ever ba3atet dirty text lal sha5s el 8alat', 'Never have I ever elt el esem el 8alat bel ta5et', 'Never have I ever ken 3andk friend with benefits', 'Never have I ever neket hada ma bta3rif esmo', 'Never have I ever rehet 3ala sex shop', 'Never have I ever 3melt threesome', 'Never have I ever ba3atet a sexy pic la hada', 'Never have I ever 3melt sex bel pool aw bel baher', 'Never have I ever 3melt shower sex', 'Never have I ever hdort porn enta w 3am bt nik', 'Never have I ever had a one night stand', 'Never have I ever farjet your private parts la hada in public', 'Never have I ever tolo3lak lap dance', 'Never have I ever rje3t la exak', 'Never have I ever 3melt sex ma benten/shabben ma bya3rfo baad bnafs el nhar', 'Never have I ever 5enet sahebtak/sahbik ma3 rfi2o/rfi2a', 'Never have I ever hashashet', 'Never have I ever masset asabi3 ejren', 'Never have I ever neket hada ma3ak bel she8el', 'Never have I ever helemt enak aam tnik hada', 'Never have I ever sta3malet sex toy', 'Never have I ever sta3malet talje with your foreplay', 'Never have I ever fet hada 3lek enta w aam tnik', 'Never have I ever sara2et shi mnel supermarket', 'Never have I ever l2it masare 3al ard w aratun', 'Never have I ever wa2afuk 3al hejiz', 'Never have I ever rehet 3and sahebtak bala ma yaarfo ahla', 'Never have I ever shtaret hashish', 'Never have I ever kissed aktar men sha5es bi nafs el nhar', 'Never have I ever lahwaset taht bat hada', 'Never have I ever fantaret in public', 'Never have I ever fataht telephonak edem hada toli3 porn on screen', 'Never have I ever ba3atet nudes la hada', 'Never have I ever 3melt hickey la hada', 'Never have I ever jarabet tehke hada rfi2ak ken 3am yshek 3laya', 'Never have I ever fetet 3a Google la tshuf sex positions', 'Never have I ever 3melt anal sex', 'Never have I ever 2refet waeta kent aam telhas your partner', 'Never have I ever hatet aktar men 3 fingers bi hada']

    def spy(self):
        play1, play2 = st.columns([1,1])
        with play1:
            players_count = st.selectbox('Kam Wahad Ento?', self.player_count)
        with play2:
            spies_count = st.selectbox('Kam Er Fi?', self.spy_count)

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
                er[f'Player {er_i +1 }'] = 'Enta el Er'
                for i in range(len(self.players)):
                    if i == er_i:
                        pass
                    else:
                        self.players[i][f'Player {i+1}'] = word

            elif spies_count == 2:
                ayren = rd.sample(self.players, 2)
                er_1 = self.players.index(ayren[0])
                er_2 = self.players.index(ayren[1])
                ayren[0][f'Player {er_1 + 1}'] = 'Ent Awal Er'
                ayren[1][f'Player {er_2 + 1}'] = 'Ent Tene Er'
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
                ayren[0][f'Player {er_1 + 1}'] = 'Ent Awal Er'
                ayren[1][f'Player {er_2 + 1}'] = 'Ent Tene Er'
                ayren[2][f'Player {er_3 + 1}'] = 'Ent Telit Er'
                for i in range(len(self.players)):
                    if i == er_1 or i == er_2 or i == er_3:
                        pass
                    else:
                        self.players[i][f'Player {i+1}'] = word

            with open('spy_game.json', 'w') as f:
                json.dump(self.players, f)

            st.success('Game Started!')

        st.markdown('** **')

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
                        if data[index][f'Player {index + 1}'] == 'Enta el Er' or data[index][f'Player {index + 1}'] == 'Ent Awal Er' or data[index][f'Player {index + 1}'] == 'Ent Tene Er' or data[index][f'Player {index + 1}'] == 'Ent Telit Er':
                            st.subheader(f"Player {index + 1}")
                            st.write(f"{data[index][f'Player {index + 1}']}")
                        else:
                            st.subheader(f"Player {index + 1}")
                            st.write(f"Word:  {data[index][f'Player {index + 1}']}")
                    elif data[-1] ==data[index] and (data[index][f'Player {index + 1}'] == 'Enta el Er' or data[index][f'Player {index + 1}'] == 'Ent Awal Er' or data[index][f'Player {index + 1}'] == 'Ent Tene Er' or data[index][f'Player {index + 1}'] == 'Ent Telit Er'):
                        st.subheader(f"Player {index + 1}")
                        st.write(f"{data[index][f'Player {index + 1}']}")
                        st.info('All Players Have Been Revealed!')
                    else:
                        st.subheader(f"Player {index + 1}")
                        st.write(f"Word: {data[index][f'Player {index + 1}']}")
                        st.info('All Players Have Been Revealed!')
                except IndexError:
                    st.info('All Players Have Been Revealed!')

            elif next:
                index += 1
                with open("index.txt", "w") as indexf:
                    indexf.write(str(index))

    def never(self):
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

#Main
g = Games()

if game == 'Home':
    st.header('Da Squad')

elif game == 'Spy':
    st.header('Spy Ya Maneyik')
    st.text('''
    Spy Game Rules:
    -Na2o kam sha5es ento w kam spy fi
    -Press "Play" to start the game
    -Reveal your identity then press "Next"
    and give it to the next player
    ''')
    g.spy()

elif game == 'Never Have I Ever':
    st.header("Never Have I Ever")
    st.text('''
            Game Rules:
            -Na2o hada ye2ra el jemal lal kell
            -kel wahad aando 15 lives
            -bt watto osbo3 kel marra el jemle btetaba2 3laykun
            -The Game will auto generate the "Never Have I Ever" sentences
            ''')
    g.never()


