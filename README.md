Aulia Fitri Hanifah_F55123068_TI B


Analisis Best Case dari Naive dan Qonquer

1. Naive (Naive sort)
  Best Case: Terjadi ketika array sudah terurut atau sangat sedikit yang perlu dipindahkan. Pada kasus terbaik, setiap elemen hanya dibandingkan sekali dan tidak perlu ada pertukaran. Waktu yang dibutuhkan tetap O(n²) karen terdapat dua loop yang membandingkan setiap elemen satu per satu meskipun tidak ada pertukaran yang dilakukan. Sehingga Naive Sort sangat tidak efisien, bahkan dalam kasus terbaik.
2. Qonquer (Merge sort)
  Best Case: Merge Sort selalu membagi array menjadi dua bagian hingga bagian tersebut hanya memiliki satu elemen lalu menggabungkannya kembali. Walaupun kondisi array sudah terurut, proses ini tetap dilakukan, namun tidak ada perbandingan yang "membutuhkan pertukaran" karena penggabungan dilakukan lebih efisien karena elemen sudah terurut. Kompleksitas Waktunya adalah O(n log n) dalam kasus terbaik, terburuk, maupun rata-rata karena algoritma ini selalu membagi array dan menggabungkannya kembali dalam urutan yang lebih efisien.