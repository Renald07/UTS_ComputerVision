# UTS Computer Vision

**Nama:** Zaky Renald Putra Permana  
**NIM:** 43050230033  
**Kelas:** 5 TIB  

---

## 🧠 Deskripsi Program
Program ini membuat karakter sederhana berbentuk **robot wajah lucu** bernama *BotRen* di atas kanvas digital menggunakan OpenCV dan NumPy.

---

## 🎨 Karakter
Karakter memiliki:
- Kepala berbentuk lingkaran merah
- Dua mata putih dengan pupil hitam
- Mulut berbentuk persegi panjang
- Antena di atas kepala dengan bola hijau
- Tulisan nama di bawah karakter

---

## 🔄 Transformasi yang Diterapkan
1. **Translasi** → Menggeser posisi karakter ke kanan bawah.  
2. **Rotasi** → Memutar karakter sebesar 45°.  
3. **Resize** → Mengubah ukuran karakter menjadi setengah.  
4. **Crop** → Memotong sebagian area wajah.

---

## ⚙️ Operasi Citra
1. **Bitwise AND** → Menggabungkan karakter dengan background polos.  
2. **Add (Brightness)** → Meningkatkan kecerahan karakter.

---

## 📂 Struktur Folder
```
UTS_ComputerVision/
│
├── karakter.py
├── img/
│   └── background.jpg (opsional)
├── output/
│   ├── karakter.png
│   ├── translate.png
│   ├── rotate.png
│   ├── resize.png
│   ├── crop.png
│   ├── bitwise.png
│   └── final.png
└── README.md
```

---
