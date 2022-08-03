import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Cybersecurity Stats & Page", page_icon=":bar_chart:", layout="wide")

# Add a title and intro text
st.title('Cybersecurity Statistics And Trends')
st.text('Berikut adalah beberapa statistik dan trend populer menengenai cybersecurity')
st.write('---')

# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Data Breaches', 'Cybercrime Stats', 
'Security Cost', 'COVID19 Cybersecurity', 'Cybersecurity Job', 'Popular Security Software'])

# Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load material
lottie_secure = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_pCsReX.json")
image = Image.open('chart.JPEG')

# Functions for each of the pages
def Data_Breaches():
    st.subheader('Largest Data Breaches and Hacking Statistics')
    st.write(
      """
      Beberapa tahun terakhir merupakan tahun yang sibuk bagi para peretas, cyber criminal, dan pakar 
      cybersecurity. Berikut ini kami tampilkan lima cybersecurity breaches teratas pada tahun 2021.
      - Cybersecurity analytics firm, Cognyte, tercatat mengalami database breach sebesar 5 miliar pada Mei 2021
      - Tercatat 700 juta data breaches di LinkedIn dalam rentang waktu Juni – Agustus 2021
      - Media social raksasa seperti Facebook juga mengalami data breach lebih dari 533 juta akun yang terungkap pada Maret 2021
      - Bykea, the Pakistani ride-hailing app, mengalami data breach sebesar 400 juta pada November.
      - Brazilian Ministry of Health mengalami kehilangan 223 juta catatan pada Januari 2021.

      """
      )
    st.write('')
    st.write(
      '''
      _Data Breach merupakan suatu pelanggaran keamanan dimana data atau informasi dicuri atau 
      diambil paksa dari suatu sistem tanpa sepengetahuan dan otorasi pemilik sistem._
      '''
      )

def Cybercrime_Stats():
    st.subheader('Cybercrime Statistics by Attack Type')
    st.write(
      """
      **Ransomware & Malware attack statistics**
      - Serangan malware meningkat sebesar 358% dan serangan Ransomware naik 435% pada tahun 2020. [(Help Net Security)](https://www.helpnetsecurity.com/2021/02/17/malware-2020/)
      - 94% malware dikirimkan melalui email. [(Verizon)](https://www.verizon.com/business/resources/reports/2021-data-breach-investigations-report.pdfx?mkt_tok=MTU3LUlQVy04NDYAAAGCnSPdCJOSdAFifG0IdzWmsj1YFMrI9u449EmWg6pDFzPUawGJJkkn4EnsBYJoFvo8obB_XHL38FdaW63sVeeNrIUdRgo1gwfy-8CxnG-l7GhU4kqs)
      - Rata-rata, sebuah perusahaan menjadi korban serangan ransomware setiap 11 detik. [(Cybersecurity Ventures)](https://cybersecurityventures.com/cybercrime-damages-6-trillion-by-2021/)

      **Phishing attack**  
      - 6.95 juta kasus pishing dan scam pages telah terjadi, menjadikannya serangan paling umum pada tahun 2020, menurut FBI.
      - Setidaknya 3 dari 4 perusahaan mengalami phishing attack di tahun 2020.
      - 57% organisasi mengalami phishing attemps pada setiap harinya. [(GreatHorn)](https://info.greathorn.com/hubfs/Reports/2021-Business-Email-Compromise-Report-GreatHorn.pdf)

      **Other attacks**
      - Pada tahun 2023, jumlah total serangan DDoS di seluruh dunia diperkirakan akan menjadi 15,4 juta. [(Cisco)](https://www.cisco.com/c/en/us/solutions/collateral/executive-perspectives/annual-internet-report/white-paper-c11-741490.html)
      - 30% dari Data Breach melibatkan orang internal. [(Verizon)](https://www.verizon.com/business/resources/reports/2020-data-breach-investigations-report.pdf)
      - 25.6% website traffic diperkirakan tercipta dari bad bot traffic. [(Imperva)](https://www.imperva.com/blog/bad-bot-report-2021-the-pandemic-of-the-internet/)
      """
      )    

def Security_Cost():
    st.subheader('Security Spending and Cost Statistics')
    st.write(
      """
      - Menurut [IBM](https://www.entrepreneur.com/article/367141), anggaran cybersecurity harus terdiri dari 
        9-14% dari keseluruhan anggaran IT.
      - [Statista](https://www.statista.com/statistics/1198893/worldwide-cybersecurity-trends-coronavirus/) 
        melaporkan pengeluaran keamanan TI sebesar $40,8 miliar pada tahun 2019.
      - Cisco menunjukkan bahwa 50% perusahaan besar menghabiskan $1 juta per tahun untuk keamanan.

      """
      )
    st.subheader('Cost of Cybercrime')
    st.write(
      """
      - Biaya yang dikeluarkan untuk cyber crime telah meningkat 10% di beberapa tahun terakhir.
      - Rata-rata pengeluaran untuk mengangani data breach di 2021 sebesar 4.24 Million, menurut IBM data.
      - Cybersecurity Ventures memperkirakan bahwa cybercrime akan menelan biaya sebesar $10,5 triliun 
        per tahun di tahun 2025.

        """
      )

def COVID19_Cybersecurity():
    st.subheader('COVID-19 Cibersecurity Statistics')
    st.write(
      """
      Peristiwa COVID-19 sangat berdampak pada setiap industri di seluruh dunia, tidak terkecuali dunia maya. 
      Pandemi global membuka jalan baru bagi cyber criminal untuk menargetkan korban melalui layanan kesehatan, 
      para pencari kerja, para pekerja remote, dan lainnya. Kasus cybercrime pun meningkat selama pandemi 
      dengan phishing menjadi serangan paling umum.
      - Laporan dari PurpleSec menunjukkan bahwa insiden cyber naik 600% selama pandemi.
      - Statista melaporkan bahwa 64% organisasi di seluruh dunia kemungkinan besar mengalami data breach akibat COVID-19.
      - 30% menyatakan mereka mengalami peningkatan serangan pada sistem IT mereka selama pandemi.
      """
      )            

def Cybersecurity_Job():
    st.subheader('Cybersecurity Job Statistics')
    st.write(
      """
      Pertumbuhan insiden cybersecurity telah menyebabkan meningkatnya kebutuhan akan profesional 
      cybersecurity yang terampil.
      - Diperkirakan akan ada 3,5 juta pekerjaan dibidang cybersecurity pada akhir tahun 2025.
      - Pasar kerja diperkirakan akan tumbuh 33% antara 2020 dan 2030, menurut the Bureau of Labor Statistics
      """
      )
    st.image(image, caption='source: PwC 2021')

def Popular_Software():
    left_column, right_column = st.columns(2)
    with left_column:
      st.subheader('Most Popular IT Security Software')
      st.write(
        """
        - Norton Security
        - Cloudfare
        - Avira Antivirus Server
        - Malwarebytes
        - Kaspersky Lab
        """
        )
    with right_column:
      st_lottie(lottie_secure, height=300)
      
# Navigation options
if options == 'Data Breaches':
    Data_Breaches()
elif options == 'Cybercrime Stats':
    Cybercrime_Stats()
elif options == 'Security Cost':
    Security_Cost()
elif options == 'COVID19 Cybersecurity':
    COVID19_Cybersecurity()
elif options == 'Cybersecurity Job':
    Cybersecurity_Job()
elif options == 'Popular Security Software':
    Popular_Software()