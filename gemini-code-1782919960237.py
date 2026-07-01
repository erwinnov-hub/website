html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erwinnov - Premium Indonesian Products</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        :root {
            --primary: #1a2a3a;
            --secondary: #b8860b;
            --accent-blue: #008b8b;
            --dark: #222222;
            --light: #f9f9f9;
            --white: #ffffff;
        }

        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        /* Navigation */
        nav {
            background-color: var(--primary);
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .logo {
            color: var(--white);
            font-size: 1.8rem;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: #dddddd;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary);
        }

        .nav-btn {
            background-color: var(--secondary);
            color: var(--white);
            padding: 0.6rem 1.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.3s;
        }

        .nav-btn:hover {
            background-color: #966f0a;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(15, 32, 39, 0.85), rgba(44, 83, 100, 0.85));
            color: var(--white);
            padding: 8rem 5% 6rem 5%;
            text-align: center;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            font-weight: 700;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2.5rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            color: #e0e0e0;
        }

        .hero-btns {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
        }

        .btn {
            padding: 0.8rem 2rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-block;
        }

        .btn-primary {
            background-color: var(--secondary);
            color: var(--white);
        }

        .btn-primary:hover {
            background-color: #966f0a;
        }

        .btn-secondary {
            background-color: var(--accent-blue);
            color: var(--white);
        }

        .btn-secondary:hover {
            background-color: #006e6e;
        }

        /* Features Section */
        .features {
            padding: 5rem 5%;
            background-color: var(--white);
            display: flex;
            justify-content: space-around;
            gap: 2rem;
            flex-wrap: wrap;
        }

        .feature-card {
            flex: 1;
            min-width: 280px;
            max-width: 350px;
            text-align: center;
            padding: 2.5rem 1.5rem;
            border-radius: 8px;
            background: var(--light);
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            margin-bottom: 1rem;
            color: var(--primary);
            font-size: 1.4rem;
        }

        /* Products Section */
        .products {
            padding: 5rem 5%;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 4rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background-color: var(--secondary);
            margin: 10px auto 0 auto;
            border-radius: 2px;
        }

        .product-grid {
            display: flex;
            flex-direction: column;
            gap: 4rem;
        }

        .product-row {
            display: flex;
            background-color: var(--white);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        }

        .product-row.reverse {
            flex-direction: row-reverse;
        }

        .product-gallery {
            flex: 1;
            background-color: #eaeaea;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 350px;
            position: relative;
        }

        /* Custom SVG placeholder graphics instead of empty boxes */
        .product-gallery svg {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .product-info {
            flex: 1;
            padding: 3.5rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .product-tag {
            align-self: flex-start;
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .tag-batik {
            background-color: #fdf5e6;
            color: var(--secondary);
        }

        .tag-vaname {
            background-color: #e0f7fa;
            color: var(--accent-blue);
        }

        .product-info h3 {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }

        .product-info p {
            color: #555555;
            margin-bottom: 1.5rem;
        }

        .product-features {
            list-style: none;
            margin-bottom: 2rem;
        }

        .product-features li {
            margin-bottom: 0.5rem;
            position: relative;
            padding-left: 1.5rem;
            color: #444;
        }

        .product-features li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #2e7d32;
            font-weight: bold;
        }

        /* About Section */
        .about {
            background-color: var(--primary);
            color: var(--white);
            padding: 5rem 5%;
            text-align: center;
        }

        .about-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .about h2 {
            font-size: 2.3rem;
            margin-bottom: 1.5rem;
            color: var(--secondary);
        }

        .about p {
            font-size: 1.15rem;
            color: #e0e0e0;
            line-height: 1.8;
        }

        /* Contact Section */
        .contact {
            padding: 5rem 5%;
            background-color: var(--white);
        }

        .contact-container {
            display: flex;
            max-width: 1000px;
            margin: 0 auto;
            gap: 4rem;
        }

        .contact-info {
            flex: 1;
        }

        .contact-info h3 {
            font-size: 1.8rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
        }

        .contact-details {
            margin-top: 2rem;
        }

        .contact-item {
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .contact-item-icon {
            font-size: 1.5rem;
            color: var(--secondary);
            width: 30px;
        }

        .contact-form {
            flex: 1.2;
            background-color: var(--light);
            padding: 2.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: var(--primary);
        }

        .form-group input, .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group input:focus, .form-group textarea:focus {
            outline: none;
            border-color: var(--secondary);
        }

        .submit-btn {
            background-color: var(--primary);
            color: var(--white);
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
            width: 100%;
        }

        .submit-btn:hover {
            background-color: #0f1a24;
        }

        /* Footer */
        footer {
            background-color: #0f1a24;
            color: #999999;
            text-align: center;
            padding: 2rem 5%;
            font-size: 0.9rem;
            border-top: 1px solid #1a2a3a;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav {
                flex-direction: column;
                gap: 1rem;
            }
            .nav-links {
                gap: 1rem;
            }
            .hero h1 {
                font-size: 2.2rem;
            }
            .hero-btns {
                flex-direction: column;
                gap: 1rem;
            }
            .product-row, .product-row.reverse {
                flex-direction: column;
            }
            .contact-container {
                flex-direction: column;
                gap: 2.5rem;
            }
            .product-info {
                padding: 2rem;
            }
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav>
        <div class="logo">Erwin<span>nov</span></div>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#produk">Produk</a></li>
            <li><a href="#tentang">Tentang Kami</a></li>
            <li><a href="#kontak">Hubungi Kami</a></li>
        </ul>
        <a href="#produk" class="nav-btn">Katalog</a>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
        <h1>Dari Warisan Budaya hingga Kekayaan Laut:<br>Terbaik dari Indonesia untuk Anda</h1>
        <p>Erwinnov menghadirkan produk-produk premium pilihan asli Indonesia. Mulai dari keanggunan mahakarya Batik tradisional hingga kesegaran komoditas ekspor Udang Vaname berkualitas global.</p>
        <div class="hero-btns">
            <a href="#batik" class="btn btn-primary">Batik Premium</a>
            <a href="#vaname" class="btn btn-secondary">Udang Vaname</a>
        </div>
    </header>

    <!-- Value Proposition -->
    <section class="features">
        <div class="feature-card">
            <div class="feature-icon">💎</div>
            <h3>Kualitas Ekspor</h3>
            <p>Semua produk melalui proses kurasi ketat untuk memenuhi standar komoditas pasar internasional.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <h3>100% Asli & Berkelanjutan</h3>
            <p>Mendukung penuh keberlanjutan lingkungan dan kesejahteraan para pengrajin serta petambak lokal.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <h3>Kemitraan Tepercaya</h3>
            <p>Pelayanan profesional berintegritas tinggi dengan jaminan pengiriman yang aman, terjaga, dan tepat waktu.</p>
        </div>
    </section>

    <!-- Products Section -->
    <section class="products" id="produk">
        <h2 class="section-title">Kategori Produk Unggulan</h2>
        
        <div class="product-grid">
            <!-- Product 1: Batik -->
            <div class="product-row" id="batik">
                <div class="product-gallery">
                    <!-- SVG Decorative Placeholder for Batik Theme -->
                    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
                        <rect width="100%" height="100%" fill="#f4ece1"/>
                        <path d="M0,0 Q100,200 200,200 T400,400 M400,0 Q300,200 200,200 T0,400" stroke="#b8860b" stroke-width="2" fill="none" opacity="0.3"/>
                        <circle cx="200" cy="200" r="80" fill="none" stroke="#b8860b" stroke-width="3" stroke-dasharray="10,5"/>
                        <text x="50%" y="52%" dominant-baseline="middle" text-anchor="middle" font-family="Georgia" font-size="24" fill="#654321" font-weight="bold">BATIK PREMIUM</text>
                    </svg>
                </div>
                <div class="product-info">
                    <span class="product-tag tag-batik">Karya Seni & Fashion</span>
                    <h3>Eksotika Batik Indonesia</h3>
                    <p>Koleksi kain dan pakaian batik tulis serta cap eksklusif dengan motif autentik nusantara yang kaya akan filosofi. Dibuat menggunakan bahan katun dan sutra premium pilihan yang memberikan kenyamanan maksimal untuk kebutuhan formal maupun gaya hidup modern.</p>
                    <ul class="product-features">
                        <li>Kain Katun & Sutra Grade A</li>
                        <li>Pewarnaan Alami, Kuat & Tahan Lama</li>
                        <li>Desain Eksklusif yang Terbatas</li>
                    </ul>
                    <a href="#kontak" class="btn btn-primary" style="align-self: flex-start;">Lihat Koleksi Kolektif</a>
                </div>
            </div>

            <!-- Product 2: Udang Vaname -->
            <div class="product-row reverse" id="vaname">
                <div class="product-gallery">
                    <!-- SVG Decorative Placeholder for Marine Theme -->
                    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
                        <rect width="100%" height="100%" fill="#e0f2f1"/>
                        <path d="M 0,200 Q 100,150 200,200 T 400,200" stroke="#008b8b" stroke-width="3" fill="none" opacity="0.4"/>
                        <path d="M 0,250 Q 100,200 200,250 T 400,250" stroke="#008b8b" stroke-width="1.5" fill="none" opacity="0.3"/>
                        <circle cx="200" cy="200" r="70" fill="none" stroke="#008b8b" stroke-width="2" stroke-dasharray="5,5"/>
                        <text x="50%" y="52%" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="22" fill="#004d40" font-weight="bold">UDANG VANAME</text>
                    </svg>
                </div>
                <div class="product-info">
                    <span class="product-tag tag-vaname">Fresh & Frozen Food</span>
                    <h3>Udang Vaname Global Grade</h3>
                    <p>Udang Vaname (Litopenaeus vannamei) hasil budidaya terbaik dari perairan pesisir Indonesia yang dikelola secara higienis dan berkelanjutan. Diproses langsung menggunakan teknologi pembekuan cepat (IQF) guna mengunci kesegaran alami, rasa manis otentik, serta tekstur daging yang padat dan juicy.</p>
                    <ul class="product-features">
                        <li>Standar Higienis & Biosekuriti Ketat</li>
                        <li>100% Bebas Antibiotik & Bahan Kimia</li>
                        <li>Kapasitas Pasokan Skala Besar (Kontainer)</li>
                    </ul>
                    <a href="#kontak" class="btn btn-secondary" style="align-self: flex-start;">Minta Penawaran Harga</a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about" id="tentang">
        <div class="about-content">
            <h2>Tentang Erwinnov</h2>
            <p>"Di Erwinnov, kami percaya bahwa potensi kekayaan Indonesia tidak memiliki batas. Kami berkomitmen untuk menjembatani karya seni terbaik dari para maestro pengrajin batik tanah air serta komoditas kelautan unggulan dari petambak lokal langsung ke hadapan Anda. Setiap kemitraan dan produk yang Anda pilih bersama kami merupakan langkah nyata dalam mendukung pertumbuhan ekonomi sirkular lokal yang berkelanjutan."</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact" id="kontak">
        <div class="contact-container">
            <div class="contact-info">
                <h3>Hubungi Erwinnov</h3>
                <p>Tertarik untuk melakukan pemesanan khusus, kemitraan pasokan, atau negosiasi volume ekspor? Hubungi tim representatif kami sekarang.</p>
                
                <div class="contact-details">
                    <div class="contact-item">
                        <div class="contact-item-icon">📍</div>
                        <div><strong>Lokasi Kantor:</strong> Indonesia</div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-item-icon">✉️</div>
                        <div><strong>Email Resmi:</strong> info@erwinnov.com</div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-item-icon">💬</div>
                        <div><strong>WhatsApp Bisnis:</strong> +62 8xx-xxxx-xxxx</div>
                    </div>
                </div>
            </div>
            
            <div class="contact-form">
                <form action="#" method="POST" onsubmit="event.preventDefault(); alert('Terima kasih! Pesan Anda telah terkirim ke Erwinnov.');">
                    <div class="form-group">
                        <label for="name">Nama Lengkap / Perusahaan</label>
                        <input type="text" id="name" required placeholder="Masukkan nama Anda">
                    </div>
                    <div class="form-group">
                        <label for="email">Alamat Email</label>
                        <input type="email" id="email" required placeholder="nama@perusahaan.com">
                    </div>
                    <div class="form-group">
                        <label for="message">Pesan atau Kebutuhan Spesifik</label>
                        <textarea id="message" rows="5" required placeholder="Tuliskan spesifikasi produk, volume, atau pertanyaan Anda..."></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Kirim Pesan</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Erwinnov. All Rights Reserved. | Penawaran Komoditas & Budaya Indonesia Berkualitas Tinggi.</p>
    </footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File index.html successfully created.")