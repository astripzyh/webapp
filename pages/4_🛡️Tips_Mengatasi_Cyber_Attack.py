import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Tips Menghindari Cyber Attack", page_icon=":pushpin:", layout="wide")
st.sidebar.markdown (":pushpin: Hal-Hal Yang Perlu Dilakukan Untuk Menghindari Cyber Attack")

# Tab function
tab1, tab2, tab3 = st.tabs(["Pemerintah", "Pelaku Usaha Bisnis", "Masyarakat & Individu"])

# Isi tab page
with tab1:
    st.title('Peran Pemerintah Dalam Mencegah Cyber Attack')
    st.write('---')
    st.write(
        '''
        Menurut riset, Indonesia adalah 
        [negara terbesar keempat dengan angka pertumbuhan pengguna internet yang besar sedunia](https://datareportal.com/reports/digital-2019-global-digital-overview). 
        Perkembangan ini tentu merupakan sebuah kabar baik. Artinya, masyarakat Indonesia sudah melek dengan 
        kemajuan teknologi. Namun, perkembangan teknologi juga berjalan bersamaan dengan munculnya bahaya 
        cyber crime.\n
        Pada 2021, Badan Siber dan Sandi Negara mengumumkan laporan tahunan yang menyatakan ada lebih dari 
        [1,6 miliar serangan siber](https://tekno.kompas.com/read/2022/04/08/06020007/indonesia-hadapi-1-6-miliar-serangan-siber-dalam-setahun-ini-malware-terbanyak?page=all) 
        yang terjadi di wilayah Indonesia. Melihat potensi ancaman kejahatan siber yang begitu besar, 
        pemerintah harus bisa segera mengambil tindakan. \n
        '''
        )
    st.subheader('Bagaimanakah cara mengatasi cyber crime yang bisa dilakukan oleh pemerintah?')
    st.write(
        '''
        Di bawah ini adalah beberapa langkah yang dapat dilakukan oleh pemerintah untuk mengatasi cyber crime
        yang telah dirangkum oleh [theconversation](https://theconversation.com/mewujudkan-keamanan-siber-bagi-indonesia-apa-yang-harus-dilakukan-116813) 
        dan [digitaltransformation](https://digitaltransformation.co.id/cara-mengatasi-cyber-crime-apa-yang-harus-dilakukan-pemerintah/)
        '''
        )
    st.write(
        '''
        **1. Memetakan Ancaman**\n
        Kasus cyber crime terbesar yang terjadi di Indonesia kebanyakan berhubungan dengan peretasan yang 
        menargetkan situs website pemerintahan. Selama bertahun-tahun, kita sudah sering mendengar bahwa 
        website resmi pemerintahan sering diretas. Dengan mengetahui dan mendeteksi ancaman kejahatan, maka 
        pemerintah bisa mengutamakan fokus dan memperbaiki keamanan situs pemerintah.\n
        **2. Membuat Kebijakan Yang Kuat**\n
        Saat ini, Indonesia hanya memiliki payung kebijakan dalam bentuk Undang-undang tentang Informasi dan 
        Transaksi Elektronik Tahun 2016. Peraturan ini belum cukup untuk mengatur banyak hal yang mencakup 
        kejahatan siber. Apalagi seiring perkembangan zaman, ancaman kejahatan siber pun juga semakin 
        berkembang. Pemerintah harus terus melakukan evaluasi terhadap peraturan yang dimiliki dan terus 
        memperkuatnya.\n
        **3. Menjalin Koordinasi Yang Baik antar Lembaga**\n
        Memerangi kejahatan siber tidak akan bisa dilakukan oleh satu lembaga saja. Karenanya, pihak 
        kepolisian akan membutuhkan bantuan dari lembaga lain untuk membentuk koordinasi yang baik. 
        Saat ini, Indonesia sudah menerapkan hal tersebut. Selain kepolisian, ada pihak lain yang bergerak 
        untuk mengamankan pemerintah dari kejahatan dunia maya.\n
        Diantaranya Badan Siber dan Sandi Negara (BSSN) dibentuk untuk memimpin koordinasi pelaksanaan 
        keamanan siber, TNI untuk membentuk unit siber dan melakukan operasi pertahanan siber, lalu 
        Kementerian Luar Negeri untuk terus melakukan diplomasi siber, kemudian Kementerian Komunikasi dan 
        Informasi sebagai tim tanggap demi memastikan keamanan internet di Indonesia.\n
        **4. Meningkatkan Keterampilan dan Infrastuktur Digital**\n
        Cara mengatasi cyber crime lainnya adalah dengan meningkatkan keterampilan sumber daya manusia 
        di Indonesia. Indonesia perlu bekerja sama dengan pihak atau negara lain untuk meningkatkan kemampuan 
        menangani cyber crime.\n
        Selain meningkatkan keterampilan, pemerintah juga perlu membangun sistem infrastruktur digital yang 
        aman. Dengan sistem keamanan siber yang kuat dan solid, maka kejahatan siber bisa dicegah. 
        Pengembangan sistem ini harus dimulai dengan pemutakhiran teknologi untuk mengakomodasi ancaman siber 
        yang baru.\n
        **5. Membentuk Pusat Data Nasional**\n
        BSSN mengatakan bahwa membentuk pusat data nasional yang terpusat akan lebih aman daripada menyimpan 
        data secara lokal. Indonesia kini memiliki lebih dari 100 data center dan masing-masing menyimpan 
        data sensitif. Hal ini bisa menjadi ladang yang bagus untuk penyalahgunaan data.\n
        **6. Mengembangkan Industri Cybersecurity**\n
        Terakhir, pemerintah harus mengembangkan industri keamanan siber lokal. Industri keamanan siber 
        Indonesia masih baru berkembang. Pasarnya masih didominasi oleh produk perangkat keras dan perangkat 
        lunak asing. Hanya industri jasa konsultasi lokal yang tumbuh dengan baik, menyediakan layanan 
        seperti forensik dan keamanan digital.
        '''
        )

with tab2:
    st.title('Peran Pengusaha Dalam Mencegah Cyber Attack')
    st.write('---')
    st.write(
        '''
        Beberapa industri UMKM menganggap cybersecurity merupakan masalah yang cukup sulit untuk ditangani
        dikarenakan biaya pengeluarannya yang cukup besar. Sayangnya, industri UMKM inilah yang paling 
        mungkin menjadi sasaran kejahatan dunia maya. Faktanya, 43% serangan siber menargetkan bisnis kecil. 
        Para penjahat siber mengetahui bahwa perusahaan besar memiliki sistem keamanan yang kuat, tetapi 
        bisnis kecil seperti UMKM sering membiarkan diri mereka rentan. Jika Anda menjalankan UMKM dan 
        keamanan siber belum menjadi prioritas, saatnya untuk mengubahnya.
        '''
        )
    st.subheader('Hal-hal yang dapat dilakukan untuk melindungi usaha bisnis')
    st.write(
        '''
        **1. Melaksanakan Pelatihan Karyawan**\n
        Karyawan yang tidak terlatih atau tidak memiliki cybersecurity awareness yang baik dapat menjadi salah 
        satu kerentanan di perusahaan. Oleh karena itulah, penting bagi pelaku usaha bisnis untuk melatih 
        karyawan mereka agar lebih aware dengan tanda-tanda serangan cyber. Selain itu, mereka juga harus 
        mengetahui bagaimana cara mencegah cyber crime agar tidak terjadi di perusahaannya.\n
        Memberi pelatihan karyawan tentang ancaman keamanan tidak boleh dilakukan sekali saja. Pelatihan 
        keamanan siber harus dilakukan secara teratur untuk mengikuti teknologi terbaru dan memastikan 
        karyawan baru tidak menciptakan kerentanan keamanan.\n
        **2. Membuat System Security Plan**\n
        System Security Plan (SSP) adalah dokumen formal yang memberikan gambaran umum tentang persyaratan 
        keamanan untuk sistem informasi serta berisi penjelasan mengenai pengendalian keamanan yang perlu 
        direncanakan untuk memenuhi persyaratan tersebut. Dokumen tersebut akan mencakup rincian tentang cara 
        membatasi akses untuk pengguna resmi, memastikan karyawan untuk melakukan praktik-praktik keamanan, 
        serta menjelaskan bagaimana karyawan harus merespons ketika terjadi pelanggaran keamanan.\n
        **3. Selalu Memperbaharui Software**\n
        Pengembang software, biasanya akan melakukan pembaruan versi pada sistem yang mereka kembangkan untuk 
        peningkatan kualitas software baik dari sisi performa atau sistem keamanan di dalamnya. Jika hacker 
        melihat Anda masih menggunakan software lama yang memiliki cacat kode di dalamnya, maka mereka dapat 
        mengeksploitasi kerentanan tersebut untuk masuk dan mengakses data-data penting di dalamnya. 
        Akibatnya, kasus kebocoran data dapat terjadi sehingga merugikan perusahaan dan pelanggan.\n
        **4. Menggunakan Kata Sandi Yang Kuat**\n
        Kata sandi tidak boleh didaur ulang, dan harus diperbarui terus-menerus. Jangan membuat kata sandi 
        sederhana karena mudah diretas oleh hacker. Pada tahun 2012, seorang ahli peretas kata sandi 
        mengungkapkan sebuah program yang dapat mengatasi kata sandi delapan karakter. Inilah sebabnya mengapa 
        semua kata sandi harus lebih dari delapan karakter, semakin rumit kata sandi maka akan semakin baik.\n
        **5. Gunakan Security Software**\n
        Salah satu bentuk cyber crime yang banyak menyerang perusahaan adalah infeksi malware baik itu dalam 
        bentuk serangan ransomware, worm, trojan, atau yang lain. Malware atau malicious software ini sengaja 
        dirancang untuk  merusak perangkat Anda, mencuri data-data sensitif, dan berbagai tujuan jahat 
        lainnya.\n
        Jadi, untuk menghindari hal tersebut terjadi, tidak ada salahnya jika Anda menggunakan security 
        software pada perangkat Anda, seperti anti ransomware atau anti virus.
        '''
        )

with tab3:
    st.title('Peran Masyarakat Dalam Mencegah Cyber Attack')
    st.write('---')
    st.write(
        '''
        Kecanggihan teknologi membawa banyak kemudahan bagi kehidupan masyarakat modern. Banyak hal yang bisa 
        dilakukan dengan memanfaatkan internet, yaitu berkomunikasi, menikmati sarana hiburan, hingga 
        melakukan berbagai jenis transaksi. Di sisi lain, kecanggihan tersebut juga menimbulkan masalah 
        baru yang dikenal dengan istilah cyber crime. Karena satu dan lain hal, pengguna internet kerap 
        mengindahkan faktor keamanan ketika berinteraksi di dunia maya. Hal itu menjadikan pengguna internet 
        rentan menjadi korban cyber attack.
        '''
        )
    st.subheader('Berikut ini hal-hal yang dapat Anda lakukan untuk mencehgah terjadinya cyber attack')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.write('')
        st.image('Data\protect-data.png')
        st.write('')
        st.image('Data\hack.jpg')
        st.write('')
        st.image('Data\data-protect.jpg')
        st.write('')
        st.image('Data\secure.jpg')
        st.write('')
    with text_column:
        st.write(
            '''
            **1. Menggunakan Gadget untuk Kepentingan Pribadi**\n
            Penggunaan gadget yang dilakukan untuk kepentingan bersama akan rentan terkena Cyber Attack karena 
            dapat disalahgunakan. Akan lebih baik menggunakan gadget untuk keperluan pribadi dan melindunginya 
            dengan penggunaan username serta password.\n
            **2. Memprioritaskan Penggunaan Software Asli**\n
            Software bajakan akan lebih rentan terkontaminasi malware atau jenis virus lainnya, maka penggunaan 
            software asli lebih disarankan. Dengan penggunaan software asli, kita juga mendapatkan update otomatis 
            secara resmi.\n
            **3. Melakukan Update Software secara Rutin**\n
            Melakukan update software secara rutin merupakan salah satu cara pencegahan Cyber Attack karena 
            dengan adanya software versi terbaru biasanya sudah dilengkapi proteksi keamanan yang lebih baik.\n
            **4. Menggunakan Password yang Unik**\n
            Password yang unik adalah salah satu cara mengatasi cyber attack. Kombinasi huruf besar, huruf kecil, 
            angka, dan karakter pada password akan membuatnya lebih sulit diretas daripada password yang hanya 
            terdiri dari huruf. Jadi, sebaiknya kita menggunakan password unik yang mudah diingat secara pribadi. 
            Usahakan untuk tidak menulis password dan memberitahukannya kepada siapa pun supaya kerahasiaannya 
            tetap terjaga.\n
            **5. Mengganti Password secara Rutin**\n
            Membuat password yang unik saja belum cukup untuk mengamankan data. Jadi, sebaiknya kita juga 
            mengganti password secara rutin untuk menghindari risiko peretasan. Kita mesti memilih password yang 
            unik dan tidak mudah diketahui orang lain. Hindari penggunaan password yang mudah diretas, contohnya 
            tanggal lahir Anda, 12345, ABC123, dan lainnya.\n
            **6. Melakukan Backup Data secara Berkala**\n
            Salah satu kebiasaan baik yang termasuk cara mengatasi cyber attack adalah melakukan backup data 
            secara berkala. Sebaiknya kita menyimpan duplikat data di beberapa tempat, misalnya HDD eksternal, 
            flash disk, dan cloud. Backup data akan mengurangi risiko kerugian saat kita menjadi korban cyber 
            attack. Pastikan kalau data-data yang sudah dicadangkan mudah diakses supaya aktivitas digital kita 
            tidak terhambat.\n
            **7. Mengabaikan Email atau Notifikasi Lainnya yang Mencurigakan**\n
            Cara mengatasi cyber attack adalah dengan mengabaikan email atau notifikasi yang mencurigakan. 
            Kiriman email atau notifikasi tersebut biasanya menjadi jebakan untuk peretasan.\n
            **8. Berhati-hati Dalam Bermedia Sosial**\n
            Agar terhindar dari cyber attack di sosial media ada baiknya untuk selalu menjaga pengaturan privasi akun, 
            selain jangan secara bebas memberi informasi pribadi apalagi terhadap orang tak dikenal. Apabila mempunyai 
            akun media sosial yang sudah tak terpakai ada baikya untuk menutup akun tersebut, menghindari supaya
            tidak disallahgunakan.
            '''
        )