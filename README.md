# Machine-Learning-Sales
Machine Learning to improve business sales

Program ini dibuat menggunakan python, untuk menggunakan machine learning menggunakan metode regresi linear.

TUTORIAL 
1. Buka file python itu dan ubah direktori file penjualan.csv kalian
Contoh:
data_file = "C:\\Python\\Machine Learning\\Data Penjualan Paskal\\data_penjualan.csv"


2. Ubah CSV dengan data penjualan kalian dengan format (Tanggal,SalesHarian)
Contoh:
01/20/2023,20000000

3. Terakhir, tinggal liat kodingan paling bawah python dan ubah "fture date" menjadi tanggal sales yg ingin di cari
Contoh:
future_date = pd.to_datetime("2023-05-12", format="%Y-%m-%d")
akan menampilkan prediksi penjualan pada "2023-05-12" di console log

Perhatian!
Catatan :
- Pastikan data yang anda punya 6 bulan terakhir.
- Versi ini masih tahap awal akan ada pengembangan lanjutan nantinya
