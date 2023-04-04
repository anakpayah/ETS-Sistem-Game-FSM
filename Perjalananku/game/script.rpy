# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define C_ADMIN = Character("Admin")

define C_Komandan = Character("Pak Sutarno")
define C_IbuKantin = Character("Ibu Kantin")
define C_ROWAN = Character("Rowan")
define C_AFIFAN = Character("Afifan")
define C_RYAN = Character("Ryan")
define C_IMAM = Character("Pak Imam")
define C_FITRAH = Character("Fitrah")
define C_MANSUR = Character("Mansur")
define C_DWI = Character("Pak Dwi")
define C_RULLI = Character("Pak Rulli")

image bg BG_MeetingRoom = "bg/MeetingRoom.jpg"
image bg BG_LandPark = "bg/LandPark.JPG"
image bg BG_PintuDepan = "bg/BG2.JPG"
image bg BG_Entrance = "bg/Entrance.JPG"
image bg BG_Stair1 = "bg/UpStair2.JPG"
image bg BG_Lantai2 = "bg/HMTCCorner.JPG"
image bg BG_KantinL1 = "bg/KantinL1Area.JPG"
image bg BG_Stair2 = "bg/UpStair3.JPG"
image bg BG_RuangDosen = "bg/DosenRoom.JPG"
image bg BG_Wudhu = "bg/WudhuArea.JPG"
image bg BG_AJK = "bg/LabAJK.JPG"
image bg BG_MCI = "bg/LabMCI.JPG"
image bg BG_LP2 = "bg/LabP2.JPG"
image bg BG_ALPRO = "bg/LapAlpro.JPG"
image bg BG_GIGA = "bg/LabGIGA.JPG"
image bg BG_KBJ = "bg/LabKBJ.JPG"
image fsm = im.Scale("FSM.jpg",720,720)



# The game starts here.

label start:

    $ PETUNJUK_FLASHDRIVE = False

    $ PETUNJUK_IBU_KANTIN = False

    $ PETUNJUK_KACAMATA = False

    $ BLUE_GLASSES_STATE = "unhave"

    $ ALLOW_TO_ARREST = False

    # These display lines of dialogue.

    "DISCLAIMER!"

    "Credit:\nRyan Garnet Andrianto (05111940000063)\nAfifan Syafaqi Yahya (5111940000234)"

    "Music By:\nPhat Phrog Studio"

    "Enjoy!"

    "..."

    scene bg BG_MeetingRoom:
        zoom 1.3
    with dissolve

    play music "audio/3RPGMusic.wav"

    C_ADMIN "Selamat datang di 'Perjalananku'."

    C_ADMIN "Di dalam gim ini, kamu akan menjadi seorang mahasiswa Teknik Informatika di ITS."

    C_ADMIN "Kamu adalah seorang polisi yang sedang menyamar dan hendak menangkap tersangka di sana."

    C_ADMIN "Sebelum itu, gim ini dipersembahkan oleh Ryan dan Afifan"

    show fsm
    with dissolve

    C_ADMIN "Gambar berikut merupakan FSM yang telah dibuat untuk menjelaskan alur dari gim ini"

    C_ADMIN "Tekan tombol 'H' Untuk menyembunyikan dialog bar"

    C_ADMIN "Pada FSM tersebut ada garis dan kata berwarna kemerah-merahan yang mennujukan alur 'investigasi' pada tempat yang sama"

    C_ADMIN "Investigasi bisa dilakukan berulang-ulang kali, hanya sekedar itu saja"

    C_ADMIN "selain itu, hitam, sekedar perpindahan antar label saja."

    hide fsm

    scene black

    menu:
        "Apakah kamu sudah siap?"

        "Ya":
            jump SudahSiap

        "Tidak":
            jump BelumSiap

    return

label BelumSiap:
    "Kamu dikirim kembali ke kantor dan dinonaktifkan dari kepolisian."
    return

label SudahSiap:
    "Ponsel kamu berdering."

    C_Komandan "(Melalui SMS) Cari pelaku yang mencuri data rahasia BIN tahun 2048 lalu dan tangkap pelakunya paling lambat 7 hari lagi."

    jump DiHalamanDepan

label DiHalamanDepan:
    scene bg BG_Entrance:
        zoom 1.3

    "Kamu berada di Halaman Depan."

    menu:
        "Kemana kamu akan pergi?"

        "→ Ke Parkiran":
            jump DiParkiran

        "↑ Ke Pintu Masuk":
            jump DiPintuMasuk

        "↓ Ke Kantor Polisi":
            jump office

    return

label office:
    scene bg BG_MeetingRoom:
        zoom 1.3
    "Kamu berada di kantor polisi."

    menu:
        "Istirahat":
            "Kamu beristirahat."
            jump office
        "Identifikasi tersangka":
            jump arrest
        "Back to Informatika ITS":
            jump DiHalamanDepan

label arrest:
    "............................................................\nSISTEM INFORMASI KEPOLISIAN\n............................................................"
    menu:
        "Masukkan jenis kelamin:"
        "Pria":
            $ ARREST_GENDER = "Male"
            "Pria dipilih."
        "Wanita":
            $ ARREST_GENDER = "Female"
            "Wanita dipilih."

    menu:
        "Aksesoris yang dapat diidentifikasi:"

        "Kalung":
            $ ARREST_AKSESORIS = "Kalung"
        "Kacamata":
            $ ARREST_AKSESORIS = "Kacamata"
        "Gelang":
            $ ARREST_AKSESORIS = "Gelang"

    menu:
        "Barang bukti (jika ada)"


        "Flask Drive bergambar Ikan Kakap" if PETUNJUK_FLASHDRIVE == True:
            "(Computer) Menganalisis flash drive bergambar ikan kakap..."
            "(Computer) Mendekripsi file dengan algoritma greedy..."
            "(Computer) Satu file dengan hash data yang dicuri dari BIN ditemukan cocok 100 persen."
            "(Computer) Terdapat foto pemandangan di dalam flash drive."
            "(Computer) Memindai exif foto pemandangan..."
            
            if ARREST_AKSESORIS == "Kacamata" and ARREST_GENDER == "Male":
                "Suspect: Mansyur Firmansyah, mahasiswa Informatika angkatan 2046"
                C_Komandan "Kita sudah dapatkan pelakunya, sekarang tangkap dia."

                $ ALLOW_TO_ARREST = True

                jump office
            else:
                "Ditemukan 65 hasil. Pencarian gagal karena kurang spesifik."
                jump office

        "Tidak ada barang bukti":
            "Mencari orang di database.."
            "Ditemukan 102,293,233 hasil. Pencarian gagal karena kurang spesifik."
            jump office
    return

label DiParkiran:
    scene bg BG_LandPark:
        zoom 1.3

    "Kamu berada di Parkiran."

    menu:
        "Investigasi" if PETUNJUK_FLASHDRIVE == False:
            $ PETUNJUK_FLASHDRIVE = True
            "Kamu menemukan sebuah Flash Drive bergambar Ikan Kakap."
            "New inventory: Flash Drive bergambar Ikan Kakap"
            jump DiParkiran
        "Investigasi" if PETUNJUK_FLASHDRIVE == True:
            "Tidak ditemukan apapun."
            jump DiParkiran

        "↑ Ke Kantin":
            jump DiKantinL1

        "← Ke Halaman Depan":
            jump DiHalamanDepan

    return

label DiPintuMasuk:
    scene bg BG_PintuDepan:
        zoom 1.3

    "Kamu berada di Pintu Masuk."

    menu:
        "Investigasi":
            menu:
                "Bicara Mahasiswa Asing" if PETUNJUK_IBU_KANTIN == True:
                    "Hello?"
                    C_ROWAN "Yes? Who are you?"
                    "Can I ask you few question?"
                    C_ROWAN "Okay."
                    "Do you happen to know this Flash Drive?"
                    C_ROWAN "It was with me. I was.. told to deliver it by person with очки glasses. I don't know them."
                    $ PETUNJUK_KACAMATA = True
                    jump DiPintuMasuk

                "Bicara dengan Mahasiswa Asing" if PETUNJUK_IBU_KANTIN == False:
                    "Hello?"
                    "Mahasiswa tersebut terlihat sibuk, lebih baik jangan diganggu."
                    jump DiPintuMasuk
                "Leave":
                    jump DiPintuMasuk

        "→ Ke Kantin":
            jump DiKantinL1

        "↗ Naik Tangga":
            jump DiTanggaLantai1

        "← Ke Halaman Depan":
            jump DiHalamanDepan

    return

label DiTanggaLantai1:
    scene bg BG_Stair1:
        zoom 1.3

    "Kamu berada di Tangga Lantai 1."

    menu:
        "Investigasi":
            "Terlihat secarik kertas."
            menu:
                "Baca":
                    "\"Sometimes the best help that you can do is not helping at all.\" \n ~R"
                    jump DiTanggaLantai1
                "Leave":
                    jump DiTanggaLantai1
        "↗ Naik":
            jump DiLantai2
        "↘ Turun":
            jump DiPintuMasuk

    return

label DiLantai2:
    scene bg BG_Lantai2:
        zoom 1.3

    "Kamu berada di HMTC Corner di Lantai 2."

    menu:
        "Investigasi":
            "Tidak ditemukan apapun."
            jump DiLantai2
        "↘ Turun Ke Lantai 1":
            jump DiTanggaLantai1
        "↗ Naik Ke Lantai 3":
            jump DiTanggaLantai2
        "→ Ke Ruang Dosen":
            jump DiRuangDosen
    return

label DiKantinL1:
    scene bg BG_KantinL1:
        zoom 1.3
    menu:
        "Investigasi":
            menu:
                "Tanya Ibu Kantin":
                    C_IbuKantin "Mau beli apa?"
                    menu:
                        "Tanya Flash Drive Ikan Kakap" if PETUNJUK_FLASHDRIVE:
                            C_IbuKantin "Oh itu, waktu itu saya lihat anak jalan bawa itu. Rambutnya pirang."
                            $ PETUNJUK_IBU_KANTIN = True
                            jump DiKantinL1
                        "Leave":
                            jump DiKantinL1

                "Tanya Mahasiswa yang lagi makan":
                    jump FAQ
                "Leave":
                    jump DiKantinL1

        "← Ke Tempat Wudhu":
            jump DiTempatWudhu
        "↑ Ke Parkiran":
            jump DiParkiran
        "→ Ke Pintu Masuk":
            jump DiPintuMasuk

    return

label FAQ:
    C_RYAN "Mau tanya apa?"
    menu:
        "Siapa pembuat game ini?":
            C_RYAN "Game ini dibuat oleh Ryan Garnet Andrianto dan Afifan sebagai tugas Evaluasi Tengah Semester di matakuliah Sistem Game."
            jump FAQ
        "Bagaimana cara memenangkan game ini?":
            C_RYAN "Cari tau siapa pelakunya dan tangkap dia. Cari petunjuk yang relevan. Hati-hati dengan petunjuk redundan."
            jump FAQ
        "Leave":
            jump DiKantinL1

label DiTempatWudhu:
    scene bg BG_Wudhu:
        zoom 1.3

    menu: 
        "Investigasi" if PETUNJUK_KACAMATA == False:
            "Tidak ditemukan apapun."
            jump DiTempatWudhu
        "Investigasi" if PETUNJUK_KACAMATA == True and BLUE_GLASSES_STATE == "unhave":
            "Terlihat kacamata biru."
            C_DWI "Mas kaca mata kok ditinggal? njupuk iku"
            "Injih pak"
            "New inventory: Blue glasses"
            $ BLUE_GLASSES_STATE = "have"
            jump DiTempatWudhu
        "Investigasi" if PETUNJUK_KACAMATA == True and (BLUE_GLASSES_STATE == "have" or BLUE_GLASSES_STATE == "stored_in_ajk"):
            "Tidak ditemukan apapun."
            jump DiTempatWudhu
        "→ Ke Kantin":
            jump DiKantinL1

    return

label DiTanggaLantai2:

    scene bg BG_Stair2:
        zoom 1.3

    menu:
        "Investigasi":
            "Terlihat secarik kertas"
            "Kertas: Cara menanam ubi kayu yang baik dan benar. Sebelum bibit ubi kayu ditanam, renam dengan pupuk hayati SOT HCS yang dicampur dengan air.."
            menu:
                "Leave":
                    pass
            jump DiTanggaLantai2
        "↗ Naik":
            jump DiLantai3
        "↘ Turun":
            jump DiLantai2

    return

label DiLantai3:

    scene bg BG_MCI:
        zoom 1.3

    "Kamu berada di Lab MCI di lantai 3."

    menu:
        "Investigasi":
            "Ini adalah Laboratorium Manajemen Cerdas Informasi."
            menu:
                "Masuk":
                    "Pintu lab terkunci."
                    jump DiLantai3
                "Informasi":
                    "Laboratorium MCI menekankan pada analisis, sintesa, dan evaluasi proses bisnis dan sistem informasi pada sistem Enterprise. Kepala laboratorium MCI adalah Prof. Drs. Ec. Ir. Riyanarto Sarno, M.Sc Ph.D."
                    jump DiLantai3
                "Leave":
                    jump DiLantai3
        "↘ Ke Tangga Turun":
            jump DiTanggaLantai2
        "← Ke GIGa":
            jump DiGIGa
        "→ Ke LP2":
            jump DiLP2
    return

label DiGIGa:
    scene bg BG_GIGA:
        zoom 1.3
    menu:
        "Investigasi":
            "Ini adalah Laboratorium Grafika, Interaksi, dan Game."
            menu:
                "Masuk":
                    "Pintu lab terkunci."
                    jump DiGIGa
                "Informasi":
                    "Laboratorium GIGa menekankan pada desain, perkembangan dan dokumentasi proses pembuatan game sesuai dengan standar. Kepala laboratorium GIGa adalah Imam Kuswardayan, S.Kom., MT."
                    jump DiGIGa
                "Leave":
                    jump DiGIGa
        "→ Ke Lab MCI":
            jump DiLantai3
        "← Ke Lab AJK":
            jump DiAJK
    return

label DiAJK:
    scene bg BG_AJK:
        zoom 2.3
        xalign 0.5
    menu:
        "Investigasi":
            "Ini adalah Laboratorium Arsitektur dan Jaringan Komputer."
            if BLUE_GLASSES_STATE == "have":
                "Kamu melihat seorang mahasiswa di dalam laboratorium Arsitektur dan Jaringan Komputer." 
            menu:
                "Tangkap Mansur" if ALLOW_TO_ARREST == True:
                    C_MANSUR "!!!"
                    "Kamu dengan sigap mengejar Mansur."
                    C_MANSUR "(Lari dengan sangat kencang)"
                    "Kamu mengambil tazer dan menembak Mansur."
                    C_MANSUR "AAAAAAA!!"
                    "Akhirnya cak Masur tertangkap pula, hahaha..."
                    "..."
                    jump end
                "Bicara ke mahasiswa di dalam" if BLUE_GLASSES_STATE == "have":
                    C_MANSUR "(Menatap)"
                    C_MANSUR "Siapa lo?"
                    menu:
                        "Tanya soal kacamata":
                            C_MANSUR "Taruh aja di atas meja biar diambil sama yang punya."
                            "Kamu menaruh kacamata di atas meja."
                            $ BLUE_GLASSES_STATE = "stored_in_ajk"
                            C_RYAN "Kamu harus tau siapa yang mengambil kacamata itu"
                            jump DiAJK
                "Bicara ke mahasiswa di dalam" if BLUE_GLASSES_STATE == "stored_in_ajk":
                    C_MANSUR "... Minta apa lagi? Tinggal aja kacamatanya, bawel"
                    "Tidak ramah.. bintang.. ah sudahlah"
                    jump DiAJK
                "Informasi":
                    "Laboratorium AJK menekankan pada pembangunan macam arsitektur jaringan sesuai standar teknologi terkini dan penerapan keamanan jaringan. Kepala laboratorium AJK adalah Dr. Wahyu Suadi, S.Kom, M.Kom.."
                    jump DiAJK
                "Leave":
                    jump DiAJK
        "← Ke Lab KBJ":
            jump DiKBJ
        "→ Ke Lab GIGa":
            jump DiGIGa

label DiKBJ:
    scene bg BG_KBJ:
        zoom 1.3
    menu:
        "Investigasi":
            "Ini adalah Laboratorium Komputasi Berbasis Jaringan."
            menu:
                "Informasi":
                    "Laboratorium KBJ menekankan pembangunan infrastruktur jaringan yang aman, sistem grid, aplikasi jaringan sesuai standar dan aplikasi multimedia berbasis jaringan. Kepala laboratorium KBJ adalah Prof. Tohari Ahmad, S.Kom,MIT, Ph.D."
                    jump DiKBJ
                "Leave":
                    jump DiKBJ
        "→ Ke Lab AJK":
            jump DiAJK

label DiLP2:
    scene bg BG_LP2:
        zoom 1.3
    menu:
        "Investigasi":
            "Tidak ditemukan apapun."
            jump DiLP2
        "→ Ke Lab Alpro":
            jump DiAlpro
        "← Ke Lab MCI":
            jump DiLantai3

label DiAlpro:
    scene bg BG_ALPRO:
        zoom 1.3
    menu:
        "Investigasi":
            "Tidak ditemukan apapun."
            jump DiAlpro
        "← Ke Lab LP2":
            jump DiLP2

label DiRuangDosen:
    scene bg BG_RuangDosen:
        zoom 1.3
    menu:
        "Investigasi":
            "Ini adalah Ruang Dosen sekaligus Ruang Sekretariat Tata Usaha."
            jump DiRuangDosen
        "Bicara Ke Pak Imam":
            "Pak"
            C_IMAM "Mau apa?"
            menu:
                "Siapa dalang dari semua ini?":
                    C_IMAM "Dalang apa? mau ribut?"
                "Siapa pembuat game ini?":
                    C_IMAM "Kelompok Afifan & Ryan Garnet. Sudah ya saya mau solat dulu."
                    "Pak Imam pergi berwudhu."
            jump DiRuangDosen

        "Bicara Ke Pak Rulli":
            "Lebih baik membuat janji melalui e-mail dulu."
            jump DiLantai2
        "← Ke HTMC Corner":
            jump DiLantai2

    return

label end:
    scene black
    with dissolve

    "Terima kasih sduah bermain gim 'Perjalananku'!"

    "Gim ini dipersembahkan untuk pemenuan tugas Evaluasi Tengah Semester dari Sistem Game yang di Ampu oleh dosen kami yaitu Pak Imam"

    "Semoga ilmu yang kita dapat dapat bermanfaat dan menjadi lebih baik lagi ke depannya"

    "Mohon maaf bila ada salah atau hal yang menyinggung dari proses pembuatan ataupun hasil akhir yang tidak berkenan"

    "Sekian dan terima kasih!"

    "..."
