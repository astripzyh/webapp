from turtle import width
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Cybersecurity", page_icon=":globe_with_meridians:", layout="wide")
st.sidebar.markdown ("Cybersecurity Overview :woman-gesturing-ok:")

# Tab function
tab1, tab2, tab3 = st.tabs(["Pengertian Cybersecurity", "Pentingnya Cybersecurity", 
    "Jenis-Jenis Ancaman Cybersecurity"])
    
# Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Material
lottie_ask = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qqu8eybe.json")
image = Image.open('Data\cyber-security.png')

# Isi tab page
with tab1:
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.title("WHAT IS CYBERSECURITY?")
    with right_column:
        st_lottie(lottie_ask, height=200)
    st.write('---')
    st.write(
        '''
        **Beberapa tahun terakhir istilah _cybersecurity_ telah semakin terdengar. Menurut Google Trends, 
        penelusuran informasi tentang cyber security memiliki tren yang meningkat di dunia dalam lima tahun 
        terakhir. Demikian juga di Indonesia.** \n
        **Jadi, apa sebenarnya _cybersecurity_?**
        '''
    )
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image, caption='Apa itu cyber-security')
    with text_column:
        st.write(
            """
            Menurut ISO _(International Organization for Standardization)_, tepatnya ISO/IEC 27032; 
            mengutip dari sejumlah sumber; cyber security adalah preservasi dari kerahasiaan, integritas, 
            dan ketersediaan informasi di dunia maya. Cyberspace mengacu pada lingkungan yang kompleks 
            yang merupakan hasil interaksi antara orang, perangkat lunak, dan layanan internet melalui 
            penggunaan berbagai perangkat teknologi dan berbagai koneksi jaringan; lingkungan yang tidak 
            memiliki bentuk. \n
            Sementara itu, menurut Kaspersky; cyber security adalah praktik melindungi komputer, server, 
            perangkat seluler, sistem elektronik, jaringan, dan data dari serangan jahat. Demikian juga 
            Cisco yang mendefinisikan cyber security sebagai praktik melindungi berbagai sistem, jaringan, 
            dan program dari serangan digital.           
            """
        )
    st.write('')
    st.subheader('Jadi, cybersecurity dapat dikatakan sebagai tindakan untuk melindungi informasi di dunia maya dari berbagai serangan.')

with tab2:
    st.title("KENAPA CYBERSECURITY ITU SANGAT PENTING?")
    st.write('---')
    st.write(
        '''
        Dengan berkembangnya era digital yang semakin pesat, cybersecurity adalah tindakan perlindungan yang 
        sangat diperlukan bagi setiap pengguna internet. Seperti yang telah diketahui sebelumnya, istilah 
        cybersecurity kian marak di Indonesia pada saat ini. Terutama setelah adanya peristiwa global pandemi 
        yang mengakibatkan mayoritas masyarakat di seluruh dunia melakukan aktivitas via internet. Oleh karena 
        itu kesadaran terhadap keamanan cyber sangat penting dipahami setiap pengguna internet supaya terhindar 
        dari kejahatan di dunia maya atau _cyber crime_.
        '''
    )
    st.write('')
    st.subheader("Berikut ini beberapa alasan mengapa cybersecurity itu sangatlah penting")
    st.write(
        '''
        **1. Komputer dan Jaringannya Makin Banyak Digunakan**\n
        [Cybersecurity](https://infokomputer.grid.id/read/122710604/apa-itu-cyber-security-mengapa-cyber-security-kini-makin-penting?pag) 
        semakin populer berhubung makin banyaknya penggunaan komputer seperti desktop, laptop, smartphone, server, 
        dan perangkat IoT (internet of things) serta penggunaan jaringan komputer seperti internet dalam kehidupan 
        umat manusia sehari-hari.\n
        Menurut World Bank, berdasarkan data ITU (International Telecommunication Union), misalnya porsi pengguna 
        internet di dunia adalah sekitar 49% populasi pada tahun 2017. Porsi tersebut meningkat pesat dibandingkan 
        tahun 2000 yang hanya sekitar 6,7%.\n
        Serupa halnya menurut Internet World Stats yang memperkirakan porsi pengguna internet di dunia adalah sebesar 
        64,2% populasi pada kuartal pertama tahun 2021. Adapun jumlah pengguna internet yang diperkirakan itu adalah 
        sebanyak lebih dari 5 miliar. Jumlah tersebut meningkat sekitar 1.300% dibandingkan tahun 2000.\n
        **2. Jumlah Cyber Attack Kian Meningkat**\n
        Menurut Deep Instinct misalnya, jumlah cyber attack atau serangan siber menggunakan malware mengalami 
        peningkatan sebesar 358% pada tahun 2020 dibandingkan tahun 2019. Sementara, khusus ransomware, 
        peningkatannya sebanyak 435% pada tahun 2020 dibandingkan tahun sebelumnya.\n
        Khusus Indonesia, BSSN (Badan Siber dan Sandi Negara) menyatakan sepanjang bulan Januari sampai Agustus 
        tahun 2020, terdapat hampir 190 juta upaya serangan siber di Indonesia; naik lebih dari empat kali lipat 
        dibandingkan periode yang sama pada tahun 2019 yang sekitar 39 juta.\n
        Pada tahun 2021 ini sejumlah pihak menilai pula serangan siber belum akan mereda. Kaspersky misalnya 
        menyebutkan bahwa pandemi COVID-19 bisa membuat munculnya berbagai gelombang kemiskinan yang kemungkinan 
        meningkatkan kejahatan, termasuk melakukan cyber attack.
        **3. Kerugian Akibat Cyber Attack Yang Besar**\n
        Tak sekadar jumlah cyber attack yang banyak, kerugian yang dihasilkan cyber attack pun besar. Ambil contoh 
        WannaCry yang sempat menghebohkan dunia beberapa tahun lalu. Menurut Kaspersky, WannaCry mengakibatkan 
        kerugian setidaknya US$4 miliar secara global. WannaCry menginfeksi lebih dari 230.000 perangkat di 150 
        negara.\n
        Di Indonesia sendiri, mengutip Microsoft, berdasarkan studi Frost & Sullivan yang dilakukan pada tahun 2018, 
        potensi kerugian ekonomi di Indonesia yang diakibatkan oleh cyber attack yang berhasil bisa mencapai US$34,2 
        miliar. Besarnya nilai kerugian tersebut adalah lebih dari 3% PDB Indonesia pada tahun 2018.\n
        **4. Standar Cybersecurity**\n
        Menilik hal-hal di atas, tak heran bila cyber security kini makin penting, utamanya bagi organisasi. 
        Alhasil sekarang tersedia banyak standar cyber security. Tujuannya adalah untuk membantu mencegah cyber 
        attack dan membantu mitigasi cyber attack yang berhasil. Organisasi yang mengadopsi suatu standar cyber 
        security sewajarnya berharap bisa meminimalkan cyber security risk atau risiko keamanan siber; meminimalkan 
        ancaman terhadap cyber security, kerentanan sehubungan cyber security, dan dampak apabila suatu cyber attack 
        berhasil. Beberapa dari standar cyber security yang populer adalah ISO/IEC 27001, NIST Cybersecurity Framework, 
        dan PCI DSS.
        '''
    )

with tab3:
    st.title('JENIS-JENIS ANCAMAN CYBERSECURITY')
    st.write('---')
    st.write(
        '''
        Di zaman serba digital saat ini, kejahatan tidak hanya dilakukan secara konvensional. Namun di dunia maya 
        juga sering terjadi kejahatan yang merugikan masyarakat. Kejahatan di dunia maya ini menyerang bisnis dan 
        sistem pribadi setiap harinya. Jumlah dan jenis cybersecurity threat atau ancaman keamanan siber terus 
        bertambah setiap harinya. Untuk mencegah menjadi korban kejahatan di dunia maya, masyarakat perlu berhati-hati 
        dalam melakukan kegiatan secara online dan untuk selalu menjaga sandi-sandi penting yang digunakan.
        '''
    )
    st.write('')
    st.subheader("Berikut ini beberapa jenis ancaman cybersecurity yang perlu diketahui")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('malware_types.png')
    with text_column:
        st.write('')
        st.write(
            '''
            **1. Malware**\n 
            Malware merupakan software berbahaya termasuk virus, worm, ransomeware dan spyware. Malware 
            diaktifkan ketika pengguna mengklik tautan atau lampiran dari sumber yang tidak jelas keamanannya.\n
            **2. Emotet**\n
            Cybersecurity and Infrastructure Security Agency (CISA) menjelaskan Emotet sebagai bentuk Trojan perbankan 
            modular canggih yang bekerja sebagai pengunduh atau penetes Trojan perbankan lainnya. Emotet terus menjadi 
            salah satu malware yang paling mahal dan merusak saat ini.\n
            '''
        )
    st.write(
        '''
        **3. DoS (Denial of Service)**\n
        Denial of service (DoS) adalah jenis serangan cyber yang menyerang komputer atau jaringan sehingga tidak 
        dapat menanggapi permintaan.\n
        **4. Man in the Middle (MITM)**\n
        MITM terjadi ketika peretas sudah memasukkan diri ke dalam transaksi dua pihak. Setelah mengganggu lalu 
        lintas, mereka bisa menyaring dan mencuri data. Serangan jenis ini sering terjadi ketika pengguna internet 
        sedang terhubung ke internet dengan jaringan WiFi publik yang tidak aman. Hacker akan memanfaatkan situasi 
        ini dengan ‘menyisipkan diri’ di antara para pengguna dan jaringan. Mereka kemudian menggunakan malware untuk 
        menginstal perangkat lunak dan menggunakan data secara ilegal.
        **5. Phishing**\n
        Phishing merupakan salah satu serangan cyber yang sudah lama ada. Tekniknya adalah dengan menggunakan 
        komunikasi palsu seperti email dan telepon untuk mengelabui penerimanya agar membuka dan menjalankan 
        instruksi yang mereka berikan. Salah satunya adalah dengan memberikan nomor kartu kredit. Jika data sudah 
        mereka dapatkan, data perbankan pengguna bisa digunakan secara tidak sah dan ini tentu sangat merugikan.\n
        **6. Injeksi SQL**\n
        Injeksi Structured Query Language (SQL) merupakan jenis serangan cyber yang dilakukan dengan memasukkan 
        kode berbahaya ke dalam server yang menggunakan SQL. Saat terinfeksi, server akan merilis informasi yang 
        bisa disalahgunakan oleh peretas.\n
        **7. Serangan Kata Sandi**\n
        Dengan memasukkan kata sandi yang tepat, penyerang cyber bisa memiliki akses ke banyak informasi. Rekayasa 
        sosial adalah jenis serangan kata sandi yang oleh Data Insider disebut sebagai strategi cyber security 
        attack yang memanfaatkan interaksi manusia untuk melanggar praktik keamanan standar. Serangan kata sandi 
        lainnya juga bisa dilakukan dengan mengakses basis data kata sandi atau dengan menebak-nebak kata sandi orang.
 
        '''
    )