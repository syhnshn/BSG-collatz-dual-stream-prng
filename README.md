# BSG Collatz Dual Stream PRNG

![Akış Şeması](akis_semasi.png)

## 🇹🇷 Proje Hakkında

**CollatzDualStream**, standart rastgele sayı üreteçlerinden farklı olarak, **Coupled Streams** (Çift Akış) mimarisini kullanan deneysel bir Sözde Rastgele Sayı Üreteci (PRNG) algoritmasıdır.

Bu algoritma, meşhur **Collatz Sanısı** (3n+1 Problemi) üzerine kurulmuştur ancak iki bağımsız sayı akışını birbirine "bağlayarak" (coupling) kaotik ve tahmin edilemez bir yapı oluşturmayı hedefler.

### 🚀 Nasıl Çalışır?

1.  **Çift Motor (Dual Motors):** Sistem, `stream_a` ve `stream_b` olmak üzere iki ayrı sayı ile başlar. Bu sayılar, kullanıcının girdiği "tohum" (seed) değerinden türetilir.
2.  **Collatz Döngüsü:** Her adımda, her iki akışa da Collatz kuralı uygulanır:
    - Sayı çift ise: `n / 2`
    - Sayı tek ise: `3n + 1`
3.  **Çaprazlama (Coupling - The Twist):** Burası algoritmanın kalbidir. Akışlar birbirinden bağımsız ilerlemez. Her adımdan sonra `stream_a`, `stream_b` ile XOR işlemine tabi tutulur:
    ```python
    stream_a = stream_a ^ stream_b
    ```
    Bu işlem, iki akışın birbirini sürekli "kirletmesini" ve yörüngelerinin kaotik bir şekilde değişmesini sağlar.
4.  **Bit Üretimi:** Üretilen rastgele bit (0 veya 1), iki akışın o anki büyüklük ilişkisine göre belirlenir:
    - Eğer `stream_a > stream_b` ise -> **1**
    - Aksi halde -> **0**

---

### 🛠️ Kurulum ve Kullanım

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/syhnshn/BSG-collatz-dual-stream-prng.git
cd BSG-collatz-dual-stream-prng
```

Algoritmayı çalıştırmak için:

```bash
python collatz_dual_stream.py
```

Sizden bir **Integer Seed** (Tamsayı Tohum) değeri girmeniz istenecektir. Algoritma bu değeri kullanarak 32-bit uzunluğunda rastgele bir dizi üretecektir.

### 📊 Örnek Çıktı

```text
Enter an integer seed to start the generator: 12345

Initialized with seed: 12345

=== Collatz DualStream Architecture Demo ===
Step   | Stream A             | Stream B             | Coupling (A^B)  | Bit
--------------------------------------------------------------------------------
#1     | 12345   -> 37036     | 2779092381 -> ...    | 8337248372      | 0
...

[OUTPUT] 32-Bit Generated Sequence:
> 00010101111010101111111111000101
```

## 🇬🇧 About Project

**CollatzDualStream** is a unique Pseudo-Random Number Generator (PRNG) that utilizes a **"Coupled Streams"** architecture based on the chaotic nature of the Collatz Conjecture. Instead of a single state, it evolves two numbers simultaneously and forces them to interact via XOR operations, generating entropy from their relative behavior.
