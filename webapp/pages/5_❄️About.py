import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Thank You", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style\style.css")
local_css("style/style1.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("C:\Streamlit\stenv\sunrise.png")
img_lottie_animation = Image.open("C:\Streamlit\stenv\sunrise.png")

# ---- HEADER SECTION ----
with st.container():
    st.header("Halo kami dari kelompok 7 :wave:")
    st.title("Peserta Pelatihan Women in Tech: Cybersecurity and Python Kelas D")
    st.subheader('Terima kasih kepada teman-teman yang telah mengunjungi website kami:smile:')

# Referensi
st.write('---')
st.header('Referensi Materi dan Koding')
st.write(
    '''
    **materi cybersecurity**\n
    https://connect.comptia.org/blog/cyber-security-stats-facts\n
    https://digitaltransformation.co.id/cara-mengatasi-cyber-crime-apa-yang-harus-dilakukan-pemerintah/\n
    https://financesonline.com/cybersecurity-statistics/\n
    https://indihome.co.id/blog/12-cara-mengatasi-cyber-crime-yang-efektif-untuk-melindungi-data-penting\n
    https://infokomputer.grid.id/read/122710604/apa-itu-cyber-security-mengapa-cyber-security-kini-makin-penting?pag\n
    https://tekno.kompas.com/read/2021/12/21/06540017/8-kasus-peretasan-yang-terjadi-di-indonesia-sepanjang-2021?page=all\n
    https://theconversation.com/mewujudkan-keamanan-siber-bagi-indonesia-apa-yang-harus-dilakukan-116813\n
    https://www.entrepreneur.com/article/347385\n
    https://www.kompas.com/edu/read/2022/05/22/163700171/mahasiswa-waspadai-7-jenis-ancaman-cyber-security?page=all\n
    https://www.logique.co.id/blog/2021/02/01/cara-mencegah-cyber-crime/\n
    https://www.nist.gov/itl/smallbusinesscyber/cybersecurity-basics/case-study-series\n
    https://www.varonis.com/blog/cybersecurity-statistics#attack\n    
    **coding**\n
    https://docs.streamlit.io/library/api-reference\n
    https://github.com/andymcdgeo/streamlit_tutorial_series\n
    https://github.com/Sven-Bo/personal-website-streamlit\n
    **animasi**\n
    https://lottiefiles.com/\n
    https://pixabay.com/\n
    https://www.istockphoto.com/en\n
    https://www.webfx.com/tools/emoji-cheat-sheet/\n
    '''
)
st.write('**Tutorial Video**')
image_column1, image_column2, image_column3 = st.columns((3))
with image_column1:
    st.image('website.png')
    st.write('[Watch Video...](https://www.youtube.com/watch?v=VqgUkExPvLY)')
with image_column2:
    st.image('snowflake.png')
    st.write('[Watch Video...](https://www.youtube.com/watch?v=8SLiFCnFOEo)')
with image_column3:
    st.image('contact.png')
    st.write('[Watch Video...](https://www.youtube.com/watch?v=FOULV9Xij_8&t=57s)')


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/astripaoziyahs@gmail.com" method="POST">
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