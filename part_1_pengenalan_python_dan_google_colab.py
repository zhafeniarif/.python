# -*- coding: utf-8 -*-
"""Part_1_Pengenalan_Python_dan_Google_Colab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gtxi0ReHlTapFDcM4f_FMdkVWxjSQcEd

# ALGORITMA
> "*Algoritma adalah serangkaian langkah-langkah yang digunakan untuk menyelesaikan masalah atau menyelesaikan tugas.*"

Secara sederhana, algoritma adalah metode untuk menyelesaikan masalah dengan mengatur urutan langkah-langkah yang harus dilakukan. Algoritma digunakan secara luas di berbagai bidang, seperti:
- ***Computer Science***;
- **Matematika**;
- **Riset Operasi**;
- ***Artificial Intelligence***; dan
- ***Data Science***.

Agar bisa menyelesaikan masalah dengan efektif, sebuah algoritma terdiri dari instruksi-instruksi yang terstruktur, berurutan, dan tidak ambigu, sehingga prosesnya konsisten dan menghasilkan output yang diharapkan. Instruksi-instruksi dalam algoritma idealnya memiliki karakteristik berikut:
1. **Input yang Jelas**: Setiap input yang dibutuhkan harus ditentukan dengan jelas;
2. **Tidak Ambigu**: Setiap langkah harus jelas agar tidak menimbulkan penafsiran ganda;
3. **Berakhir**: Algoritma harus selesai setelah sejumlah langkah yang terbatas;
4. **Output yang Jelas**: Algoritma harus menghasilkan output yang sudah ditentukan dengan jelas;
5. **Efektif**: Algoritma harus mampu menyelesaikan masalah sesuai yang diharapkan;
6. **Independen Bahasa**: Algoritma harus bisa diterjemahkan ke berbagai bahasa pemrograman, tanpa bergantung pada satu bahasa tertentu.

## Mengapa Algoritma Penting?
Di zaman yang serba digital ini, memahami algoritma sangat penting, baik untuk mereka yang bekerja di bidang teknologi maupun dalam kehidupan sehari-hari. Banyak aplikasi yang kita gunakan setiap hari juga bekerja dengan algoritma. Misalnya, aplikasi pemesanan makanan mengatur proses dari memilih makanan hingga mengantarnya ke rumah kita dengan langkah-langkah yang mirip dengan algoritma memasak atau belanja bulanan. Memahami Algoritma akan membantu kita membuat keputusan yang lebih baik, bekerja lebih efisien, dan memahami proses di sekitar kita dengan lebih baik.

## Algoritma Dalam Keseharian
Pada dasarnya algoritma bukanlah sesuatu yang asing, hampir setiap aspek dalam keseharian kita akan berurusan dengan algoritma. Permasalahan sehari-hari yang kita hadapi biasanya membutuhkan penanganan logis dan sistematis, maka secara natural algoritma akan selalu dapat diterapkan. Selain membantu menyederhanakan permasalahan yang kompleks, algoritma juga memungkinkan replikasi proses pemecahan masalah oleh individu lain yang menghadapi permasalahan serupa serta memastikan output yang sama akan dihasilkan, terlepas dari siapapun yang melaksanakan proses.

Resep Masakan adalah ilustrasi paling nyata dari penerapan algoritma dalam kehidupan sehari-hari. Mengkonsumsi makanan yang telah dimasak adalah salah satu cara untuk memenuhi kebutuhan energi dan melangsungkan kehidupan. Untuk memastikan bahwa makanan yang dikonsumsi memenuhi standar selera serta nutrisi berdasarkan bahan baku tertentu, maka disusunlah tata cara memasak yang dituangkan ke dalam sebuah resep. Dengan adanya resep tersebut, maka cita rasa dan nutrisi yang serupa dapat disediakan di meja setiap rumahtangga yang menggunakannya.

Tidak hanya Resep seperti dideskripsikan di atas, masih banyak hal dari keseharian kita yang sebenarnya merupakan ilustrasi penerapan dari algoritma. Untuk membantu dalam memahami bagaimana algoritma diterapkan dalam berbagai pemecahan masalah, di bawah berikut telah disusun beberapa ilustrasi lain secara lebih terperinci.

### Memasak Mie Goreng Instan
Memasak mie goreng instan adalah satu-satunya keterampilan memasak yang diperlukan bagi seorang pria Indonesia sejati untuk bisa bertahan hidup.

```
Nyalakan kompor
Isi panci dengan air bersih
Taruh panci berisi air di kompor yang menyala
Buka bungkus mie goreng
Ambil mangkuk dan tuangkan bumbu instan
Jika air di panci mendidih
    Masukkan mie ke dalam panci
    Jika waktu rebus masih di bawah 3 menit
        Biarkan mie di panci
    Matikan kompor
    Angkat panci
Pindahkan mie dari panci ke saringan
Tiriskan mie di saringan
Tuang mie yang sudah ditiriskan ke mangkuk
Aduk mie hingga bumbu merata
Sajikan mie goreng
```

**Coba pikirkan:** Apakah ada efisiensi yang dapat dilakukan terhadap algoritma di atas??

### Belanja Bulanan Keluarga

Dalam rangka memenuhi kebutuhannya, setiap awal bulan sebuah keluarga harus melakukan belanja bulanan. Sebelum berbelanja, keluarga tersebut akan membuat sebuah daftar belanja berisikan berbagai barang serta jumlah yang diperkirakan akan dibutuhkan olehnya selama sebulan ke depan. Untuk memastikan agar siapapun yang berbelanja akan membawa pulang berbagai barang yang sesuai dengan kebutuhan, maka keluarga tersebut membuat sebuah prosedur belanja bulanan seperti berikut ini:

```
Buka `Daftar Belanja`
Jika seluruh `Item` pada `Daftar Belanja` sudah tercoret
    Batalkan belanja bulanan
Ambil `Trolley`
Untuk setiap `Item` pada `Daftar Belanja`
    Cari dan kumpulkan setiap `Merek` tersedia dari `Item`
    Buat `Daftar Merek` berisi setiap `Merek` dari `Item` yang tersedia
    Jika jumlah `Merek` pada `Daftar Merek` lebih dari 1
        Untuk setiap `Merek` pada `Daftar Merek`
            Hitung `Harga per satuan` dari `Merek`
            Proses `Merek` selanjutnya
        Urutkan `Merek` pada `Daftar Merek` berdasarkan `Harga per satuan`
        Masukkan `Item` dengan `Harga per satuan` paling rendah ke `Trolley` sebanyak jumlah tertera pada `Daftar Belanja`
        Coret `Item` pada `Daftar Belanja`
    Jika `Merek` pada `Ragam Item` hanya 1
        Masukkan `Item` ke `Trolley` sebanyak jumlah tertera pada `Daftar Belanja`
        Coret `Item` pada `Daftar Belanja`
    Lanjutkan pencarian ke `Item` berikutnya
Bawa `Trolley` ke kasir dan lakukan pembayaran
Jika terdapat `Item` pada `Daftar Belanja` yang belum tercoret
    Pergi ke toko lain, ulangi proses belanja dari awal
```

**Coba pikirkan:** Adakah proses yang perlu ditambahkan/dikurangi dari algoritma di atas??

### Sensus Tumbuh Kembang Anak
Dalam rangka melakukan analisis kecukupan gizi siswa Sekolah Dasar (SD) di sebuah Kabupaten, maka setiap Kepala SD di Kabupaten tersebut diperintahkan untuk melakukan Sensus **Indikator Tumbuh Kembang** anak terhadap seluruh murid yang terdaftar di sekolahnya. Untuk memastikan agar pelaksanaan dan output dari sensus sesuai dengan seharusnya, maka pelaksana sensus menetapkan sebuah prosedur sederhana yang harus dipatuhi oleh setiap kepala sekolah seperti berikut ini:

```
Buka `Daftar Murid`, ambil data dari kolom `Nama`, `Jenis Kelamin`, dan `Tanggal Lahir`
Untuk setiap `Murid` pada `Daftar Murid`
    Panggil `Murid` menghadap ke UKS
    Untuk setiap `Indikator` pada `Indikator Tumbuh Kembang`
        Ukur dan catat `Indikator` dari `Murid`
        Lanjutkan pengukuran dan pencatatan untuk `Indikator` berikutnya
    Tandai `Murid` sudah disurvey pada `Daftar Murid`
    Lanjutkan proses ke `Murid` berikutnya
Hitung `Umur` seluruh `Murid` berdasarkan `Tanggal Lahir`
Tentukan `Kelompok Usia` setiap `Murid` berdasarkan hasil perhitungan `Umur`
Hitung statistics:
  1. Kelompokkan data berdasarkan `Kelompok Usia`
  2. Hitung `mean`, `min`, `max`, & `stdev` per `Kelompok Usia`
```

## Kesimpulan
Algoritma adalah bagian integral dari kehidupan kita, dari hal-hal sederhana seperti memasak mie hingga proses yang lebih kompleks dalam dunia teknologi. Dengan memahami dan menerapkan algoritma, kita dapat menyelesaikan masalah lebih efisien dan memastikan hasil yang konsisten.

---
# ALGORITMA DALAM DATA ANALYTICS : *SORTING*
> "*Sorting adalah proses untuk mengurutkan angka/karakter berdasarkan urutan tertentu (Descending/Ascending)*."

*Sorting* merupakan salah satu proses terkomputerisasi dasar penting yang menjadi bagian integral dari algoritma proses terkomputerisasi lanjutan lainnya. Sebagai ilustrasi, dalam setiap algoritma *search*, proses *sorting* merupakan proses pertama yang dikenakan terhadap data, sebelum pencarian dilakukan. Seperti kata pepatah "Banyak jalan menuju Roma", demikian pula halnya dengan proses melakukan *sorting*, terdapat banyak alternatif algoritma yang dapat dipilih, mulai dari yang paling sederhana hingga yang teramat kompleks. Oleh karena itu, pemahaman atas bagaimana berbagai proses *sorting* yang berbeda dilakukan, merupakan sebuah langkah awal untuk mengerti berbagai alternatif algoritma lain yang tersedia untuk menyelesaikan suatu permasalahan.

Meskipun banyak alternatif algoritma yang tersedia bagi proses *sorting*, namun mempertimbangkan sisi kemudahan pembelajaran dan keterbatasan waktu, maka pada *exercise* ini hanya akan dilakukan pembahasan terkait dua algoritma *sorting* klasik, yaitu:
1. ***Bubble Sorting***; dan
2. ***Quick Sorting***.

Pembahasan akan dimulai dengan melakukan proses *sorting* terhadap sebuah deret acak dengan menggunakan kedua algoritma tersebut, untuk membandingkan *output* dari keduanya. Selanjutnya akan ditunjukkan dampak dari pemilihan masing-masing algoritma terhadap proses *sorting* yang dilakukan--baik terhadap cara pemrosesan maupun terhadap efisiensi dari proses.

___
> Untuk dapat mengikuti dan menjalankan beberapa *exercises* di bawah berikut, silahkan unduh modul [functions](https://drive.google.com/file/d/1dXMuGyplSRowrLZ-_tvowhavE7rJ3Xw_/view?usp=sharing) terlebih dahulu, lalu unggah modul tersebut ke `session storage` sehingga berbagai fungsi yang telah dibuat di dalamnya dapat di*import* ke `notebook` ini.
___

## Membuat Deret Angka Acak

1. Dari modul `functions` panggil fungsi `generate_deret` dan `print_satu_persatu`;
2. Buat deret berisi 10 angka bulat acak, dengan range nilai 0 - 100000, simpan pada variabel `deret`;
3. Tampilkan `deret` ke layar menggunakan fungsi `print_satu_persatu`.
"""

# Import fungsi-fungsi yang diperlukan dari modul `functions`
from functions import generate_deret, print_satu_persatu

type(generate_deret)

help(generate_deret)

type(print_satu_persatu)

help(print_satu_persatu)

type(print)

help(print)

# INPUTS:
# 1. Tentukan jumlah elemen deret
jml_elemen = 10
# 2. Tentukan batas bawah nilai elemen
bts_bawah = 0
# 3. Tentukan batas atas nilai elemen
bts_atas = 100000

# PROSES & OUTPUT:
# 1. Buat `deret`, masukkan variabel-variabel INPUTS ke fungsi `generate_deret`
deret = generate_deret(jumlah_elemen=jml_elemen, batas_bawah=bts_bawah, batas_atas=bts_atas)
# 2. Tampilkan `deret` menggunakan fungsi `print_satu_persatu`
print_satu_persatu(jdl="Deret acak yang dihasilkan:", deret=deret, margin=0)

"""## Melakukan *Sorting*

### *Bubble Sorting*
Algoritma *Bubble Sorting* menerapkan teknik ***Nested Loop***, dimana sebuah proses iterasi dilakukan di dalam sebuah iterasi lain. Sehingga algoritma ini akan dicirikan dengan terdapatnya sebuah ***inner loop*** dalam sebuah ***outer loop***. *Nested Loop* ini dilakukan untuk memastikan agar output yang dihasilkan dari proses sesuai dengan harapan.

Pada *bubble sorting* ini, ***inner loop*** akan berupa pengulangan proses **perbandingan nilai dan penukaran posisi** untuk setiap elemen pada `deret` dari elemen paling kiri hingga paling kanan. Selanjutnya, setiap `deret` hasil ***inner loop*** akan diproses ulang sebanyak jumlah elemen pada `deret` oleh sebuah ***outer loop***.

Adapun algoritma dimaksud, akan seperti dituliskan di bawah berikut:
```
Terima `deret` untuk disort
Tentukan `banyaknya_proses` berdasarkan jumlah elemen pada `deret`
Untuk setiap `urutan_proses` pada `banyaknya_proses`
    Untuk setiap `posisi_elemen` pada `deret`
        Jika elemen ke-(`posisi_elemen`) > elemen ke-(`posisi_elemen`+1)
            Tukar posisi elemen ke-(`posisi_elemen`) dengan elemen ke-(`posisi_elemen`+1)
        Lanjut ke `posisi_elemen` berikutnya
    Lanjut ke `urutan_proses` berikutnya
```
"""

# Import fungsi-fungsi yang diperlukan dari `functions`
from functions import bubble_sort

type(bubble_sort)

help(bubble_sort)

# 1. Urut `deret` dengan fungsi `bubble_sort`, simpan pada variabel `deret_bubble_sort`
deret_bubble_sort = bubble_sort(deret)
# 2. Tampilkan Hasil sorting menggunakan fungsi `print_satu_persatu`
print_satu_persatu(jdl="Hasil Bubble Sort:", deret=deret_bubble_sort, margin=0)

"""#### *Quick Sorting*
Algoritma *Quick Sorting* menerapkan teknik ***Function Recursion***, dimana suatu fungsi akan memanggil dirinya sendiri untuk memproses *output*nya. Sehingga algoritma ini akan dicirikan dengan terdapatnya pemanggilan dirinya sendiri untuk memproses output yang dihasilkannya. Hal penting yang perlu ditentukan pada teknis *recursive* adalah untuk menghindari terjadinya pemrosesan tanpa akhir (*infinite*). Oleh karena itu pada algoritma ini akan diperlukan penetapan kondisi dimana proses *recursive* harus dihentikan.

Proses *recursive* yang dilakukan pada saat menerapkan algoritma *quick sorting* melibatkan tiga proses berikut ini:
1. Pemilihan sebuah elemen dari `deret` untuk bertindak sebagai **pivot**, biasanya dipilih dari elemen paling tengah, paling awal, atau paling ujung pada `deret`;
2. Proses **partisi** yang memisahkan elemen deret menjadi tiga kelompok `deret`, yaitu `deret kiri`, `deret tengah`, dan `deret kanan`, dengan cara membandingkan nilai setiap elemen dengan nilai **pivot**; dan
3. Memanggil dirinya sendiri untuk memproses setiap kelompok `deret kiri` dan `deret kanan` yang dihasilkan.

Agar proses *recursive* di atas tidak berlangsung selamanya, maka perlu ditentukan sebuah kondisi penghentian proses, yaitu ketika jumlah elemen pada `deret` yang diproses lebih kecil atau sama dengan satu.

Adapun algoritma dimaksud, akan seperti dituliskan di bawah berikut:
```
Terima `deret` untuk disort
Jika jumlah elemen pada `deret`<=1
    maka `deret` tidak perlu diproses
Set nilai `pivot` = elemen `deret` paling tengah
Pisah elemen `deret` bernilai < `pivot` ke deret `kiri`
Pisah elemen `deret` bernilai == `pivot` ke deret `tengah`
Pisah elemen `deret` bernilai > `pivot` ke deret `kanan`
Lakukan langkah 1 - 7 terhadap `kiri`
Lakukan langkah 1 - 7 terhadap `kanan`
Gabungkan hasil langkah ke-8 dengan `tengah` dan hasil langkah ke-9
```
"""

# Import fungsi-fungsi yang diperlukan dari `functions`
from functions import quick_sort

type(quick_sort)

help(quick_sort)

# 1. Urut deret dengan `quick_sort`, simpan pada variabel `deret_quick_sort`
deret_quick_sort = quick_sort(deret)
# 2. Tampilkan `deret_quick_sort` menggunakan print_satu_persatu
print_satu_persatu("Hasil Quick sort:", deret_quick_sort, 0)

deret_bubble_sort==deret_quick_sort

"""### Kesimpulan
Penerapan algoritma baik `Bubble` maupun `Quick` *sorting* terhadap sebuah deret yang acak, akan menghasilkan output berupa deret terurut yang serupa!!

## Bubble Vs Quick Sorting

### Langkah Pemrosesan
Perbedaan paling mendasar dari kedua algoritma *sorting* tersebut terletak pada berbagai langkah yang dilakukan untuk melakukan proses *sorting*. Bagian berikut di bawah ini akan mencoba untuk menunjukkan perbedaan antara kedua algoritma yang disebutkan, dari segi cara pemrosesan secara visual sederhana.

#### Bubble Sorting
Agar dapat memvisualisasikan langkah-langkah yang dilakukan ketika menjalankan algoritma *Bubble Sorting*, maka fungsi `bubble_sort` yang sudah kita pergunakan sebelumnya di atas telah dimodifikasi dan disimpan dalam fungsi baru bernama `bubble_sort_show`.
"""

# 0. Import fungsi `bubble_sort_show` dari functions
from functions import bubble_sort_show

type(bubble_sort_show)

help(bubble_sort_show)

# 1. Setting margin Tampilan
margin = 100
# 2. Cetak garis Pembatas awal
print(f"{' DERET AWAL ':=<{margin}}")
# 3. Cetak Deret awal yang akan di sort
print_satu_persatu("", deret, margin)
# 4. Cetak Garis Pembatas
print(f"\n{'':=^{margin}}")
# 5. Visualisasikan proses Sorting dan simpan hasilnya pada `new_deret`
new_deret = bubble_sort_show(deret, margin)
# 6. Cetak Garis Pembatas
print(f"{' DERET AKHIR ':=>{margin}}")
# 7. Cetak hasil sorting
print_satu_persatu("", new_deret, margin)
# 8. Cetak garis pembatas akhir
print(f"\n{'':=^{margin}}")

"""#### Quick Sorting
Serupa dengan sebelumnya, untuk memvisualisasikan proses yang terjadi di dalam sebuah algoritma *quick sorting*, maka telah dilakukan modifikasi terhadap fungsi `quick_sort` menjadi fungsi lain bernama `quick_sort_show`.
"""

# 0. Import fungsi `quick_sort` dari `functions`
from functions import quick_sort_show

type(quick_sort_show)

help(quick_sort_show)

# 1. Cetak garis Pembatas awal
print(f"{' DERET AWAL ':=<{margin}}")
# 2. Cetak Deret awal yang akan di sort
print_satu_persatu("", deret, margin)
# 3. Beri Jeda Pemrosesan
input()
# 4. Lakukan Sorting dan simpan hasilnya pada `new_deret`
new_deret = quick_sort_show(deret, margin)
# 5. Cetak Garis Pembatas
print(f"{' DERET AKHIR ':=>{margin}}")
# 6. Cetak hasil sorting
print_satu_persatu("", new_deret, margin)
# 7. Cetak garis pembatas akhir
print(f"\n{'':=^{margin}}")

"""#### `Elapsed Time`
Penerapan algoritma berbeda, seperti dijelaskan sebelumnya, akan berdampat terhadap *Elapsed Time* (waktu pemrosesan) yang dipergunakan untuk menghasilkan output. Di bawah berikut telah disediakan sebuah pemrosesan yang ditujukan untuk melakukan pencatatan `elapsed_time` dari kedua algoritma *sorting* berdasarkan inputan jumlah elemen pada `deret` yang disorting.
"""

# Import fungsi yang diperlukan
from functions import elapsed_time, visual_sebaran

type(elapsed_time)

help(elapsed_time)

type(visual_sebaran)

help(visual_sebaran)

# INPUTS:
# 1. Mintakan jumlah elemen pada deret dari User
print(f"{'Jumlah elemen pada deret': <35}", end="")
jml = input(" = ")
# 3. Mintakan jumlah sampel pemrosesan yang akan dikumpulkan
print(f"{'Jumlah Simulasi dilakukan': <35}", end="")
sim = input(" = ")

# PRE-PROCESSING:
# Cast `jml` dan `sims` menjadi angka bulat
jml_elemen = int(jml) if jml else None
sims = int(sim) if sim else None

# PROCESSING & OUTPUT:
# 1. Generate `deret` berisi angka bulat acak
deret = generate_deret(jml_elemen, 0, 100000)
# 2. Proses Simulasi untuk kedua fungsi, catat data pada `dict_output`
dict_output = {fungsi.__name__:[elapsed_time(fungsi, deret) for _ in range(sims)] for fungsi in [bubble_sort, quick_sort]}
# Untuk setiap `key` pada `dict_output`
for key in dict_output.keys():
  # Rata-ratakan seluruh `value` pada list
  average_et=sum(value for value in iter(dict_output[key]))/sims
  # Buat Text `pesan`
  pesan = f"Average Elapsed Time %s" % (key.title().replace("_"," "))
  # Tampilkan Pesan ke layar
  print(f"{pesan: <35} ={average_et: >9,.6f} detik/proses")
# Buat Visualisasi dari data yang dihasilkan dan tampilkan ke layar
visual_sebaran(dict_output, f"Sebaran Elapsed Time Sorting {jml_elemen:,.0f} Elemen {sims:,.0f} Kali Simulasi")

dict_output

"""### Simulasi *Time Complexity*"""

# Import berbagai fungsi yang diperlukan
from functions import generate_time_complexity as gtc, buat_visualisasi

type(gtc)

help(gtc)

# 1. Tentukan Jumlah elemen maksimum pada deret
jml_elemen = 500
# 2. Tentukan Jumlah Simulasi
simulasi = 10
# 3. Lakukan sampling time complexity yang diulang sebanyak `simulasi`
df_raw, df_aggregate = gtc(quick_sort, bubble_sort, range(1, jml_elemen+1, 1), simulasi)
# 4. Buat Visualisasi hasil pengolahan
buat_visualisasi(df_aggregate, "Time_Complexity.png")

type(df_raw)

help(df_raw)

# Cek raw data hasil simulasi
df_raw

# Menampilkan hasil seluruh simulasi untuk N=1
df_raw.loc[(1, slice(None)), :]

# Cek hasil simulasi ke-1 untuk seluruh N
df_raw.loc[(slice(None), 1), :]

df_raw.info()

df_raw.describe()

df_raw.loc[(500, slice(None)), :].describe()

type(df_aggregate)

help(df_aggregate)

# Cek olahan hasil simulasi
df_aggregate

from google.colab import drive
drive.mount('/content/drive')

"""---"""