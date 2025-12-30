<div align="center">

# 🎲 Collatz DualStream PRNG

[![Python](https://img.shields.io/badge/Language-Python%203.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Experimental-orange?style=for-the-badge)](https://github.com/syhnshn/BSG-collatz-dual-stream-prng)
[![Algorithm](https://img.shields.io/badge/Algorithm-Coupled%20Collatz-7023c4?style=for-the-badge)](https://en.wikipedia.org/wiki/Collatz_conjecture)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

_A chaotic, custom Pseudo-Random Number Generator based on the **"Coupled Streams"** architecture._

---

<img src="akis_semasi.png" alt="Collatz DualStream Flowchart" width="85%" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">

<br>
<i> The Architecture of Chaos: Two streams racing and colliding to generate entropy.</i>
<br><br>

[🇹🇷 Türkçe](#-proje-hakkında-tr) • [🇬🇧 English](#-about-project-en)

</div>

---

## <a id="tr"></a>🇹🇷 Proje Hakkında

**CollatzDualStream**, standart rastgele sayı üreteçlerinden sıkılanlar için tasarlanmış, **Coupled Streams** (Çift Akış) mimarisini kullanan deneysel ve estetik bir algoritmadır.

Bu sistem, meşhur **Collatz Sanısı** (3n+1 Problemi)'nın kaotik doğasını kullanarak tahmin edilemezlik üretir. Ancak tek bir sayı dizisi yerine, **birbirine dolanmış iki farklı sayı akışını** yarıştırır.

### ✨ Öne Çıkan Özellikler

- **⚡ Çift Motorlu Yapı:** `Stream A` ve `Stream B` adında iki bağımsız motor aynı anda çalışır.
- **🔗 Dinamik Çaprazlama (The Twist):** Akışlar izole değildir! Her adımda `Stream A`, `Stream B` ile **XOR** işlemine girerek kirlenir. Bu, lineer analizi imkansızlaştırır.
- **🏁 Yarış Mantığı:** Çıktı biti, "Hangi sayı daha büyük?" sorusunun cevabına göre (`1` veya `0`) belirlenir.

### � Kurulum ve Çalıştırma

1.  **Projeyi İndirin:**

    ```bash
    git clone https://github.com/syhnshn/BSG-collatz-dual-stream-prng.git
    cd BSG-collatz-dual-stream-prng
    ```

2.  **Çalıştırın:**

    ```bash
    python collatz_dual_stream.py
    ```

3.  **Sonucu İzleyin:**
    Sizden bir sayı (tohum) girmeniz istenecek. Ardından, algoritmanın **ilk 5 adımını görselleştiren** özel bir demo ekranı ve 32-bitlik çıktı sizi karşılayacak.

### 📊 Örnek Görünüm

```text
=== Collatz DualStream Architecture Demo ===
Step   | Stream A             | Stream B             | Coupling (A^B)  | Bit
--------------------------------------------------------------------------------
#1     | 12345   -> 37036     | 8337277144 -> ...    | 8337248372      | 0
...
[OUTPUT] 32-Bit Generated Sequence:
> 00010101111010101111111111000101
```

---

## <a id="en"></a>🇬🇧 About Project

**CollatzDualStream** is a unique Pseudo-Random Number Generator (PRNG) that utilizes a **"Coupled Streams"** architecture based on the chaotic nature of the Collatz Conjecture.

Instead of a single evolving state, it runs two numbers simultaneously and forces them to interact via **XOR operations**, generating entropy from their relative behavior ("The Race").

### 🧠 Core Logic

1.  **Dual Motors:** Initialized from a split seed.
2.  **Collatz Rule:** Applied to both streams (3n+1 or n/2).
3.  **Coupling:** `stream_a = stream_a ^ stream_b` (Non-linear mixing).
4.  **Bit Generation:** `1` if `stream_a > stream_b`, else `0`.

---

<div align="center">

**Developed with ❤️ by [Seyhan](https://github.com/syhnshn)**

</div>
