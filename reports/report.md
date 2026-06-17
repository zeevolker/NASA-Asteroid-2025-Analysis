# NASA Near-Earth Asteroid Analysis 2025

## Executive Summary

Proyek ini menganalisis data Near-Earth Objects (NEO) dari NASA NeoWs API selama tahun 2025. Tujuan utama analisis adalah memahami karakteristik asteroid yang mendekati Bumi, mengidentifikasi asteroid berpotensi berbahaya, serta mengevaluasi faktor-faktor yang memengaruhi tingkat risiko suatu asteroid.

Dataset yang digunakan berisi 1.655 observasi asteroid dengan 22 variabel yang mencakup ukuran asteroid, kecepatan, jarak pendekatan ke Bumi, kategori ukuran, serta skor risiko yang dihitung dari kombinasi beberapa parameter utama.

---

## Dataset Overview

Jumlah observasi asteroid: 1.655

Jumlah asteroid berbahaya: 172

Jumlah asteroid tidak berbahaya: 1.483

Rata-rata diameter asteroid: 176,78 meter

Diameter asteroid terbesar: 49.435,62 meter

Kecepatan rata-rata: 48.823 km/jam

Kecepatan maksimum: 186.135 km/jam

Jarak pendekatan terdekat ke Bumi: 136.610 km

---

## Key Findings

### 1. Mayoritas Asteroid Berukuran Kecil hingga Menengah

Sebagian besar asteroid berada pada kategori Small dan Medium. Hanya sebagian kecil asteroid yang masuk kategori Huge.

Distribusi ukuran:

* Small: 695 asteroid
* Medium: 727 asteroid
* Large: 208 asteroid
* Huge: 25 asteroid

Temuan ini menunjukkan bahwa asteroid berukuran sangat besar relatif jarang ditemukan dalam pendekatan ke Bumi.

### 2. Asteroid Berbahaya Merupakan Minoritas

Dari total 1.655 observasi, hanya 172 asteroid yang diklasifikasikan sebagai hazardous.

Persentase asteroid berbahaya sekitar 10%.

Hal ini menunjukkan bahwa sebagian besar asteroid yang mendekati Bumi tidak dianggap memiliki potensi ancaman signifikan menurut kriteria NASA.

### 3. Kecepatan Asteroid Sangat Bervariasi

Kecepatan rata-rata asteroid mencapai hampir 49.000 km/jam.

Beberapa asteroid bergerak jauh lebih cepat dengan kecepatan maksimum lebih dari 186.000 km/jam.

Variasi kecepatan ini menjadi salah satu faktor penting dalam evaluasi risiko asteroid.

### 4. Kedekatan Tidak Selalu Berarti Bahaya

Meskipun terdapat asteroid yang mendekati Bumi hingga sekitar 136 ribu kilometer, tidak semua asteroid dekat diklasifikasikan sebagai hazardous.

Ukuran asteroid dan karakteristik orbit juga berperan dalam menentukan tingkat ancaman.

### 5. Risiko Dipengaruhi oleh Banyak Faktor

Perhitungan Risk Score menunjukkan bahwa asteroid dengan risiko tertinggi bukan selalu asteroid terbesar.

Risk Score dipengaruhi oleh:

* Diameter asteroid
* Kecepatan asteroid
* Jarak pendekatan ke Bumi

Pendekatan multidimensi memberikan gambaran risiko yang lebih realistis dibanding hanya melihat ukuran asteroid.

---

## Top 5 Highest Risk Asteroids

1. 66008 (1998 QH2)
2. 887 Alinda (A918 AA)
3. 465402 (2008 HW1)
4. 154276 (2002 SY50)
5. (2009 SG18)

Asteroid-asteroid ini memiliki kombinasi ukuran besar, kecepatan tinggi, dan jarak pendekatan relatif dekat sehingga memperoleh skor risiko tertinggi dalam analisis.

---

## Conclusion

Analisis menunjukkan bahwa sebagian besar asteroid yang mendekati Bumi pada tahun 2025 berukuran kecil hingga menengah dan tidak tergolong berbahaya. Namun demikian, terdapat sejumlah asteroid dengan kombinasi karakteristik yang meningkatkan tingkat risiko potensial.

Penggunaan Risk Score membantu mengidentifikasi asteroid yang layak mendapatkan perhatian lebih lanjut. Pendekatan ini dapat menjadi dasar untuk pengembangan model machine learning yang bertujuan memprediksi status hazardous asteroid berdasarkan ukuran, kecepatan, dan jarak pendekatan.

Secara keseluruhan, data NASA NeoWs memberikan wawasan penting mengenai aktivitas Near-Earth Objects dan dapat digunakan untuk mendukung penelitian, pendidikan, maupun pengembangan sistem peringatan dini berbasis data.
