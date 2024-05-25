from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="ADP-Agency", page_icon="✌", layout="wide")
##def load_lottieurl(url):
    ##r = requests.get(url)
    ##if r.status_code != 200:
       ##return None
    ##return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
##lottie_coding = load_lottieurl("https://lottiefiles.com/animations/coding-e604h4O6xY?from=search")
##img_contact_form = Image.open("images/yt_contact_form.png")
##img_lottie_animation = Image.open("images/yt_lottie_animation.png")
with st.container():
    st.subheader("Hello 🖐")
    st.title(" We are smm agency ")
    st.write("We are engaged in digital marketing smm Google ADS Seo")
    st.write("[Ask come questions >](mailto:adpagency1@gmail.com)")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our mission is simple yet powerful: to propel businesses like yours to the forefront of the digital landscape through strategic social media marketing, SEO mastery,targeted advertising on platforms like Facebook and Google Ads.")
        st.write("[Telegram >](https://t.me/ADPAgency)")
    ##with right_column:
        ##st_lottie(lottie_coding, height= 300, key="coding")
with st.container():
    st.write("---")
    st.header("Why us?")
    st.write("- Qualified employees with more than 4 years of experience")
    st.write("- Specialists from all over the world")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    ##with image_column:
        ##st.image(img_lottie_animation)
with st.container():
    st. write("---")
    st.header("Gen In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/adpagency1@gmail.com" method="POST">
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