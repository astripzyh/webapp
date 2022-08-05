import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Contoh Kasus & Case Study", page_icon=":memo:", layout="wide")

# Contoh Kasus
st.sidebar.markdown (":memo:Contoh Kasus & Case Study")

# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Contoh Kasus I', 'Contoh Kasus II', 
'Case Study I', 'Case Study II'])

# Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Material
lottie_hack1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_x1ikbkcj.json")
lottie_hack2 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zdtukd5q.json")
lottie_case1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_case2 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_fq7pwzey.json")

# Functions for each of the pages
def contoh1():
    st.title("CONTOH KASUS PERETASAN DI INDONESIA 2021")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Kasus BPJS Kesehatan (Mei 2021)")
        st.write(
            """
            **Impact :**\n
            Data milik 279 juta penduduk Indonesia diduga bocor dan dijual di forum online bernama Raid Forums. 
            Data yang dijual seharga harga 0,15 bitcoin (sekitar Rp 84,4 juta, kurs 20 Mei 2021) tersebut berisi 
            NIK, nomor ponsel, e-mail, alamat, hingga gaji.\n
            **Response :**\n
            Kominfo pun akhirnya mengajukan pemutusan akses terhadap tautan (link) untuk mengunduh data pribadi 
            tersebut, termasuk memblokir Raid Forums sebagai langkah antisipatif mencegah penyebaran data yang 
            lebih luas.
            """
            )
    with right_column:
        st.subheader("YouTube BNPB (Desember 2021)")
        st.write(
            """
            **Impact :**\n
            Akun YouTube BNPB yang semula bernama "BNPB Indonesia" berubah nama menjadi "Ethereum 2.0". Selain 
            mengubah nama, hacker juga menggunakan akun YouTube BNPB untuk melakukan siaran langsung (live streaming).\n
            **Response :**\n
            Pihak BNPB mengetahui peretasan ini dan dibantu pihak Google untuk memulihkan akun YouTube BNPB Indonesia. 
            Saat ini, akun tersebut sudah kembali seperti semula dan sudah digunakan kembali oleh BNPB Indonesia.
            """
            )
# Insert lottie animation
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st_lottie(lottie_hack1, height=200)
        with right_column:
            st_lottie(lottie_hack2, height=200)

def contoh2():
    st.title("CONTOH KASUS PERETASAN DI INDONESIA 2021")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Kasus e-HAC Kemenkes (Agustus 2021)")
        st.write(
            """
            **Impact :**\n
            Data milik 1,3 juta masyarakat Indonesia yang tersimpan di aplikasi e-HAC disebut bocor. Tidak hanya 
            mengungkap data pengguna e-HAC, tetapi juga seluruh infrastruktur terkait e-HAC, seperti data tes 
            Covid-19 yang dilakukan penumpang, data pribadi penumpang, data rumah sakit, hingga data staf e-HAC.\n
            **Response :**\n
            Pemerintah menyatakan bahwa sudah tidak menggunakan aplikasi tersebut sejak 2 Juli 2021. Setelah 2 Juli, 
            sistem aplikasi e-HAC yang digunakan masyarakat telah terintegrasi di aplikasi PeduliLindungi, yang mana 
            dari aspek infrastruktur dan servernya berbeda dari versi lama sehingga tidak terdampak insiden kebocoran 
            data. Terkait kebocoran data ini, pihak Kemenkes meminta masyarakat untuk menghapus aplikasi e-HAC versi lama.
            """
            )
    with right_column:
        st.subheader("Situs Sekretariat Kabinet RI (Juli 2021)")
        st.write(
            """
            **Impact :**\n
            Dengan metode deface, situs Setkab.go.id diretas dan tak bisa diakses. Kemudian, situs Setkab berubah 
            tampilannya menjadi hitam dengan foto yang menampilkan demonstran membawa bendera merah putih.\n
            **Response :**\n
            Polisi menduga peretasan ini dilakukan demi keuntungan ekonomi. Peretas bertujuan menjual script backdoor 
            dari website yang jadi target kepada orang yang membutuhkan. Menurut penyelidikan sementara kepolisian, 
            peretasan situs setkab.go.id terjadi akibat kelemahan pada sistem keamanan dan kelengahan operator. Lalu, 
            seminggu setelah peretasan, situs Setkab sudah kembali ke tangan pemerintah. Pihak Setkab memastikan 
            tidak ada dokumen rahasia pada situs Setkab.
            """
            )
    st.write("[Baca Selengkapnya...](https://tekno.kompas.com/read/2021/12/21/06540017/8-kasus-peretasan-yang-terjadi-di-indonesia-sepanjang-2021?page=all)")
        
# Insert lottie animation
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st_lottie(lottie_hack1, height=200)
        with right_column:
            st_lottie(lottie_hack2, height=200)

def case1():
    st.title(":book: STUDI KASUS :book:")
    st.write("---")
    st.subheader("Case Study 1")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **Scenario :**\n
            CEO perusahaan kontraktor pemerintah menerima notifikasi bahwa terdapat pelelangan di dark web yang 
            menjual akses ke data bisnis perusahaan mereka, yang mencakup akses ke database klien militer mereka. 
            CEO dengan cepat menetapkan bahwa data yang 'dijual' sudah usang, dan tidak terkait dengan klien lembaga 
            pemerintah mana pun. Bagaimana itu terjadi? Perusahaan mengidentifikasi bahwa seorang karyawan senior 
            telah mengunduh lampiran email berbahaya, mengira itu dari sumber tepercaya.\n
            **Attack :**\n
            Terjadi akibat serangan phishing di mana malware berada dalam lampiran email.\n
            **Response :**\n
            Manajemen IT perusahaan segera mematikan komunikasi ke server yang terpengaruh dan membuat sistem offline 
            untuk menjalankan cybersecurity scans untuk mengidentifikasi ada tidaknya pelanggaran tambahan. Pimpinan 
            perusahaan menyewa firma forensik cybersecurity yang bereputasi baik. Setiap instansi pemerintah yang 
            berpotensi terkena dampak diberitahu. Dinas Rahasia A.S. membantu dalam penyelidikan forensik.\n
            **Impact :**\n
            Dampak operasional dan finansial dari pelanggaran tersebut sangat luas – menelan biaya lebih dari $1 juta. 
            Perusahaan mengalami offline selama beberapa hari sehingga mengganggu bisnis selain itu lisensi perangkat 
            lunak keamanan dan server harus diatur kembali.\n
            """
            )
    with right_column:
        st.write(
            """
            **Lesson Learned :**\n
            - Serangan siber bisa terjadi pada siapa saja.
            - Ajari staf tentang bahaya mengklik tautan dan lampiran email yang tidak diminta dan tekankan 
              perlunya tetap waspada terhadap tanda-tanda peringatan email palsu.
            - Instal dan perbarui anti-virus, firewall jaringan, dan alat enkripsi informasi secara teratur 
              untuk memindai dan melawan virus dan program berbahaya.
            - Melakukan pengujian kerentanan dan penilaian risiko yang berkelanjutan pada jaringan komputer.
            """
            )   
        st_lottie(lottie_case1, height=400)

def case2():
    st.title(":book: STUDI KASUS :book:")
    st.write("---")
    st.subheader("Case Study 2")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **Scenario :**\n
            CEO sebuah Boutique Hotel menyadari bisnisnya telah menjadi korban dari wire fraud ketika orang dari 
            bagian pembukuan mulai menerima pemberitahuan dana tagihan yang tidak mencukupi. Sebelumnya diketahui 
            CEO telah mengklik tautan di email yang dia pikir berasal dari IRS (Internal Revenue Service). Tetapi 
            itu bukan. Ketika Ia mengklik tautan dan memasukkan kredensial, para cyber criminals menangkap informasi 
            login CEO, memberi mereka akses penuh ke detail bisnis dan pribadi.\n
            **Attack :**\n
            Serangan yang terjadi berupa Social engineering, phishing attack\n
            **Response :**\n
            Cadangan uang tunai hotel habis. Transfer palsu tersebut diperkirakan mencapai jumlah lebih dari $1 juta. 
            Hotel juga menghubungi perusahaan keamanan siber untuk membantu mereka mengurangi risiko serangan berulang.\n
            **Impact :**\n
            Bisnis mengalami kerugian $1 juta dan dana tidak kembali.\n
            """
            )
    with right_column:
        st.write(
            """
            **Lesson Learned :**\n
            - Diadakan pelatihan mengenai bahaya mengklik tautan dan lampiran email yang tidak diminta, 
              dan perlunya tetap waspada terhadap tanda-tanda peringatan email palsu.
            - Terapkan protokol wire transfer yang ketat dan sertakan bentuk validasi sekunder.
            - Siapkan rencana respons akan insiden cyber untuk mengantisipasi kejadian serupa.
            """
            )
        st_lottie(lottie_case2, height=400)  
    st.write("[More Case Study...](https://www.nist.gov/itl/smallbusinesscyber/cybersecurity-basics/case-study-series)")

# Navigation options
if options == 'Contoh Kasus I':
    contoh1()
elif options == 'Contoh Kasus II':
    contoh2()
elif options == 'Case Study I':
    case1()
elif options == 'Case Study II':
    case2()