import json
import time

import requests
import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie


# ---- LOAD ASSETS ----
img_contact_form = Image.open(r"C:\Users\DELL\Downloads\webpage\images\Golf Game.png")
img_snake_form = Image.open(r"C:\Users\DELL\Downloads\webpage\images\Game.png")
img_chess_form = Image.open(r"C:\Users\DELL\Downloads\webpage\images\Chess.png")

def login():
    names = ['Play Games','Gamers','Anurag']
    usernames = ['amazon','walmart','vpkbiet']
    passwords = ['amazonpay','phonepe','vpkbietpe']
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login('Login', 'main')
        
    if st.session_state["authentication_status"]:
        test=authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        # ---- HEADER SECTION ----
        with st.container():
            st.subheader("Student from VPKBIET")
            st.title("Hello!! Gamers :game_die:")
            st.write(
                "I'm a Gamer. Not because I don't have a life. But because I choose to have many."
            )
        # ---- WHAT I DO ----
        with st.container():
            st.write("----")
            left_column, right_column = st.columns(2)
        with left_column:
            st.header("")
            st.write("##")
            st.write(
                """
                efhshfihewihfhe \n
                fehaosihfioehwoif \n 
                isafhuifhuih
            
                """)
        with right_column:
            with open(r'C:\Users\DELL\Downloads\webpage\gaming.json') as source:
                gaming=json.load(source)
            st_lottie(gaming, height=300)
            
        
        # ---- PROJECTS ----
        with st.container():
            st.write("---")
            st.header("Our Games...!! ")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_snake_form)
        with text_column:
            st.subheader("Alien-Dimension")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Play Game...](https://pmp-p.github.io/pygame-alien-dimension-wasm/)")


        with st.container():
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)    
        with text_column:
            st.subheader("Golf Game")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Download Game...](https://mega.nz/file/TtMX1RoA#0zM4OOvFqsZ_3qj_LZJj4cz0hm0a3yqsvbiYPN4XoJc)")
            
            
        with st.container():
            image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_chess_form)
        with text_column:
            st.subheader("Chess Game")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Play Game...](https://pmp-p.github.io/pygame-pychess-wasm/index.html)")
            
        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header("Get In Touch With Us!")
            st.write("##")

            # Documention: https://formsubmit.co/ 
            contact_form = """
            <form action="https://formsubmit.co/shreyashkhuspe@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()
                
                                    
    
       
        
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')
        
def main():
    login()
    # Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Gaming-Website", page_icon=":bulb:", layout="wide")


# Animation Assets
def load_lottiefile(lottie_streamlit: str):
    with open(lottie_streamlit, "r") as f:
        return json.load(f)



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(r"C:\Users\DELL\Downloads\webpage\style\style.css")

if __name__ == "__main__":
    main()