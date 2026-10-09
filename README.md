# Identitas Pembuat
* **Nama:** Anisa Julianti
* **NPM:** G1A023052
* **Program Studi:** Informatika, Universitas Bengkulu

---

# Studi Kasus: Simulasi Evakuasi Bencana Berbasis HPC (*Agent-Based Modeling for Disaster Evacuation*)

Studi kasus dan implementasi kode ini dikembangkan berdasarkan materi **Informatics Practitioner Lecture Series** dengan narasumber **Asst. Prof. Dr. Warawan Diaz Carbalo** (Thammasat University, Thailand) dengan tema **"Bridging Global Infrastructure to Address Local Challenge with HPC"**.

---

## 1. Latar Belakang & Konteks Studi Kasus
* **Isu Lokal:** Bencana alam (seperti banjir bandang atau evakuasi darurat di kawasan perkotaan/kampus) sering kali memakan korban jiwa akibat buruknya perencanaan jalur evakuasi dan tingginya kepadatan mobilitas warga.
* **Peranan HPC (*High Performance Computing*):** Seperti yang dijelaskan oleh pemateri, simulasi fenomena dunia nyata (seperti simulasi evakuasi kota atau pergerakan massa kerumunan) membutuhkan daya komputasi tinggi untuk menghitung ribuan hingga jutaan agen/individu secara simultan dan paralel (*Agent-Based Simulation*).
* **Tujuan Proyek:** Membangun purwarupa simulasi berbasis Python untuk memodelkan evakuasi kerumunan (*crowd evacuation*) dari zona rawan menuju titik kumpul aman, serta mengukur performa waktu komputasi evakuasi.

---

## 2. Alur Kerja "Integrator" (Konsep Materi)
Dr. Warawan menekankan pentingnya peran mahasiswa informatika sebagai **Integrator**-yaitu seseorang yang mampu menjembatani antara kebutuhan riil di tingkat lokal, kolaborasi dengan pakar domain, dan pemanfaatan infrastruktur komputasi global:
1. **Definisi Masalah Lokal:** Memetakan wilayah simulasi (koordinat area, posisi zona bahaya, dan titik kumpul aman/*assembly point*).
2. **Pemodelan Agen (*Agent-Based Modeling*):** Setiap individu/agen memiliki parameter fisik seperti posisi koordinat $(x, y)$, variasi kecepatan gerak, dan faktor kepanikan lingkungan (*stochastic noise*).
3. **Eksekusi Komputasi (Simulasi Iteratif):** Menjalankan pembaruan posisi seluruh agen secara bertahap (*timestep*) hingga seluruh populasi berhasil dievakuasi.
4. **Analisis Kinerja:** Mencatat riwayat log evakuasi menggunakan struktur data `Pandas DataFrame` untuk mengevaluasi efisiensi waktu evakuasi.

---

## 3. Implementasi Kode Studi Kasus

Skrip Python ini mengimplementasikan arsitektur berorientasi objek (*Object-Oriented Programming*) untuk memodelkan lingkungan dan kerumunan agen:

```python
# 1. Inisialisasi Kelas Lingkungan (EvacuationEnvironment) & Sistem Agen (CrowdAgentSystem)
# 2. Pengaturan Parameter Simulasi (1000 Agen Kerumunan, Batas 300 Timestep)
# 3. Eksekusi Iterasi Pergerakan Agen Menuju Titik Kumpul Aman Terdekat
# 4. Pencatatan Log Analitik & Pengukuran Waktu Eksekusi Komputasi (Execution Duration)
