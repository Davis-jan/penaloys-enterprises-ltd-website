from pathlib import Path
import shutil, zipfile, textwrap
from flask import Flask, render_template

base = Path("/mnt/data/Penaloys_Website")
assets = base / "assets"
assets.mkdir(parents=True, exist_ok=True)

# Copy the logo extracted from the supplied company profile.
shutil.copy("C:\\Users\\Admin\\Downloads\\penaloys-logo-bold-small.png", assets / "penaloys-logo.png")

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Penaloys Enterprises Limited | General Supplies and Construction">
  <title>Penaloys Enterprises Limited</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header" id="top">
    <div class="container nav-wrap">
      <a class="brand" href="#home" aria-label="Penaloys Enterprises Limited home">
        <img src="assets/penaloys-logo.png" alt="Penaloys Enterprises Limited logo">
      </a>

      <button class="menu-toggle" aria-label="Open navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>

      <nav class="nav" aria-label="Main navigation">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#values">Values</a>
        <a href="#why-us">Why Us</a>
        <a href="#contact" class="nav-cta">Contact Us</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero" id="home">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <p class="eyebrow">GENERAL SUPPLIES AND CONSTRUCTION</p>
        <h1>Reliable Solutions,<br><span>Lasting Value.</span></h1>
        <p class="hero-text">
          Dependable solutions for public and private sector clients,
          delivered with quality, integrity, reliability and professionalism.
        </p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="#services">Explore Our Services</a>
          <a class="btn btn-outline" href="#contact">Get In Touch</a>
        </div>
      </div>
    </section>

    <section class="intro section" id="about">
      <div class="container two-col">
        <div>
          <p class="section-label">01 / ABOUT THE COMPANY</p>
          <h2>Building a strong and reputable enterprise through dependable service.</h2>
        </div>
        <div class="copy">
          <p>
            PENALOYS ENTERPRISES LIMITED was established to pursue business opportunities
            in general supplies, construction, and related services across the public and
            private sectors.
          </p>
          <p>
            The company seeks to respond to the growing demand for reliable suppliers
            and service providers while creating sustainable business opportunities
            for its stakeholders.
          </p>
          <p>
            We aim to develop lasting relationships with clients and partners while
            continuously expanding our capacity to meet diverse market needs.
          </p>
        </div>
      </div>

      <div class="container vision-grid">
        <article class="feature-card">
          <span class="number">01</span>
          <h3>Our Vision</h3>
          <p>To be a trusted leader in quality and reliable service delivery.</p>
        </article>
        <article class="feature-card">
          <span class="number">02</span>
          <h3>Our Mission</h3>
          <p>To provide dependable solutions through quality service, integrity, and commitment to our clients.</p>
        </article>
        <article class="feature-card">
          <span class="number">03</span>
          <h3>Primary Business</h3>
          <p>General supplies and construction.</p>
        </article>
      </div>
    </section>

    <section class="services section dark" id="services">
      <div class="container">
        <div class="section-heading light">
          <p class="section-label">02 / OUR SERVICES</p>
          <h2>Solutions tailored to different specifications and project requirements.</h2>
          <p>
            Our approach is flexible, allowing us to respond to different scopes of work
            and requirements across public and private sector assignments.
          </p>
        </div>

        <div class="service-grid">
          <article class="service-card">
            <div class="service-icon">01</div>
            <h3>General Supplies</h3>
            <p>Dependable supply of goods to meet the requirements of public and private sector clients.</p>
          </article>
          <article class="service-card">
            <div class="service-icon">02</div>
            <h3>Construction</h3>
            <p>Construction works delivered according to specification, scope of work and project requirements.</p>
          </article>
          <article class="service-card">
            <div class="service-icon">03</div>
            <h3>Related Services</h3>
            <p>Supporting services that complement our supply and construction work, tailored to each assignment.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="values section" id="values">
      <div class="container">
        <div class="section-heading">
          <p class="section-label">03 / CORE VALUES</p>
          <h2>Principles that guide how we work.</h2>
        </div>

        <div class="value-grid">
          <article><span>01</span><h3>Integrity</h3><p>Honest and transparent dealings in everything we do.</p></article>
          <article><span>02</span><h3>Quality</h3><p>Dependable standards in every assignment we deliver.</p></article>
          <article><span>03</span><h3>Reliability</h3><p>Doing what we promise, when we promise it.</p></article>
          <article><span>04</span><h3>Professionalism</h3><p>Serving every client with skill, courtesy and respect.</p></article>
          <article><span>05</span><h3>Customer Focus</h3><p>Putting the needs of our clients first.</p></article>
          <article><span>06</span><h3>Accountability</h3><p>Taking full responsibility for our work and results.</p></article>
        </div>
      </div>
    </section>

    <section class="why section" id="why-us">
      <div class="container two-col">
        <div>
          <p class="section-label">04 / WHY CHOOSE US</p>
          <h2>Quality, reliability and professional service.</h2>
          <p class="lead">
            We are committed to delivering quality, reliable, and professional services
            at competitive rates while prioritising client needs, integrity, accountability
            and timely delivery.
          </p>
        </div>

        <div class="check-list">
          <div><span>✓</span> Quality, reliable and professional services</div>
          <div><span>✓</span> Competitive rates</div>
          <div><span>✓</span> Client needs come first</div>
          <div><span>✓</span> Integrity and accountability</div>
          <div><span>✓</span> Timely delivery</div>
          <div><span>✓</span> Flexible solutions that create lasting value</div>
        </div>
      </div>
    </section>

    <section class="objectives section">
      <div class="container">
        <div class="section-heading">
          <p class="section-label">05 / COMPANY OBJECTIVES</p>
          <h2>Focused on sustainable business growth and dependable service.</h2>
        </div>
        <div class="objective-list">
          <div><b>01</b><span>To deliver quality and reliable services.</span></div>
          <div><b>02</b><span>To meet client needs efficiently and professionally.</span></div>
          <div><b>03</b><span>To build lasting relationships with clients and partners.</span></div>
          <div><b>04</b><span>To provide competitive and value-driven solutions.</span></div>
          <div><b>05</b><span>To achieve sustainable business growth and development.</span></div>
        </div>
      </div>
    </section>

    <section class="contact section dark" id="contact">
      <div class="container contact-grid">
        <div>
          <p class="section-label light-label">06 / CONTACT US</p>
          <h2>Let's discuss your next assignment.</h2>
          <p>
            Contact PENALOYS ENTERPRISES LIMITED for general supplies,
            construction and related services.
          </p>
        </div>

        <div class="contact-details">
          <a href="tel:+254797490032">
            <small>TELEPHONE</small>
            <strong>+254 797 490 032</strong>
          </a>
          <a href="mailto:penaloys@gmail.com">
            <small>EMAIL</small>
            <strong>penaloys@gmail.com</strong>
          </a>
          <div>
            <small>POSTAL ADDRESS</small>
            <strong>P.O. Box 181-40222, Oyugis</strong>
          </div>
          <div>
            <small>PHYSICAL LOCATION</small>
            <strong>Ringa, Along Kisii-Kisumu Road, Homa Bay County, Kenya</strong>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container footer-wrap">
      <img src="assets/penaloys-logo.png" alt="Penaloys Enterprises Limited logo">
      <p>© 2026 PENALOYS ENTERPRISES LIMITED. All rights reserved.</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
'''

css = r''':root {
  --navy: #071735;
  --navy-2: #0d2148;
  --gold: #d9a62e;
  --gold-light: #e9c15d;
  --white: #ffffff;
  --cream: #f7f6f1;
  --text: #182238;
  --muted: #687287;
  --line: #e5e6e9;
  --shadow: 0 20px 60px rgba(7, 23, 53, .10);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--text);
  background: var(--white);
  line-height: 1.65;
}
a { color: inherit; text-decoration: none; }
.container { width: min(1120px, calc(100% - 40px)); margin: 0 auto; }
.section { padding: 100px 0; }

.site-header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(7, 23, 53, .97);
  border-bottom: 1px solid rgba(255,255,255,.10);
}
.nav-wrap { min-height: 78px; display: flex; align-items: center; justify-content: space-between; gap: 30px; }
.brand img { width: 205px; display: block; }
.nav { display: flex; align-items: center; gap: 28px; color: #fff; font-size: 14px; font-weight: 600; }
.nav a { opacity: .88; transition: .2s ease; }
.nav a:hover { color: var(--gold-light); opacity: 1; }
.nav-cta { border: 1px solid var(--gold); color: #fff !important; padding: 10px 18px; border-radius: 4px; }
.menu-toggle { display: none; background: none; border: 0; cursor: pointer; }
.menu-toggle span { display: block; width: 25px; height: 2px; background: #fff; margin: 5px; }

.hero {
  min-height: 700px; display: flex; align-items: center; position: relative;
  background:
    radial-gradient(circle at 75% 30%, rgba(217,166,46,.18), transparent 28%),
    linear-gradient(115deg, var(--navy) 0%, #0b2149 65%, #112c5d 100%);
  overflow: hidden;
}
.hero::after {
  content: ""; position: absolute; width: 480px; height: 480px;
  border: 1px solid rgba(217,166,46,.22); border-radius: 50%;
  right: -160px; bottom: -220px;
}
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(90deg, rgba(7,23,53,.15), transparent); }
.hero-content { position: relative; z-index: 2; color: #fff; max-width: 760px; padding: 80px 0; }
.eyebrow, .section-label { color: var(--gold); font-size: 12px; font-weight: 800; letter-spacing: .20em; text-transform: uppercase; }
.hero h1 { font-size: clamp(48px, 7vw, 82px); line-height: 1.02; margin: 18px 0 25px; letter-spacing: -.045em; }
.hero h1 span { color: var(--gold-light); }
.hero-text { max-width: 650px; font-size: 19px; color: rgba(255,255,255,.78); }
.hero-actions { display: flex; gap: 14px; margin-top: 35px; flex-wrap: wrap; }
.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 50px; padding: 0 23px; border-radius: 4px; font-weight: 700; font-size: 14px; }
.btn-gold { background: var(--gold); color: var(--navy); }
.btn-outline { border: 1px solid rgba(255,255,255,.4); color: #fff; }

.two-col { display: grid; grid-template-columns: .9fr 1.1fr; gap: 90px; align-items: start; }
h2 { font-size: clamp(34px, 4vw, 50px); line-height: 1.12; letter-spacing: -.035em; margin-top: 14px; }
.copy { color: var(--muted); font-size: 16px; }
.copy p + p { margin-top: 18px; }
.vision-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 70px; }
.feature-card { border-top: 3px solid var(--gold); background: var(--cream); padding: 30px; min-height: 210px; }
.feature-card .number { color: var(--gold); font-weight: 800; font-size: 13px; }
.feature-card h3 { margin: 18px 0 8px; font-size: 21px; }
.feature-card p { color: var(--muted); }

.dark { background: var(--navy); color: #fff; }
.light { color: #fff; }
.light h2 { max-width: 780px; }
.section-heading > p:last-child { max-width: 700px; color: rgba(255,255,255,.68); margin-top: 18px; }
.service-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 55px; }
.service-card { padding: 35px; border: 1px solid rgba(255,255,255,.12); min-height: 280px; background: rgba(255,255,255,.025); transition: .25s ease; }
.service-card:hover { transform: translateY(-5px); border-color: rgba(217,166,46,.7); }
.service-icon { color: var(--gold); font-size: 13px; font-weight: 800; }
.service-card h3 { font-size: 25px; margin: 45px 0 12px; }
.service-card p { color: rgba(255,255,255,.65); }

.values { background: var(--cream); }
.value-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--line); margin-top: 50px; border: 1px solid var(--line); }
.value-grid article { background: #fff; padding: 30px; min-height: 185px; }
.value-grid span { color: var(--gold); font-weight: 800; font-size: 12px; }
.value-grid h3 { margin: 18px 0 7px; font-size: 20px; }
.value-grid p { color: var(--muted); font-size: 14px; }

.why { background: #fff; }
.lead { margin-top: 25px; color: var(--muted); max-width: 570px; }
.check-list { display: grid; gap: 14px; }
.check-list div { display: flex; gap: 14px; align-items: center; padding: 17px 20px; border: 1px solid var(--line); font-weight: 600; background: #fff; }
.check-list span { color: var(--gold); font-weight: 900; }

.objective-list { margin-top: 50px; border-top: 1px solid var(--line); }
.objective-list div { display: grid; grid-template-columns: 80px 1fr; gap: 25px; padding: 22px 0; border-bottom: 1px solid var(--line); }
.objective-list b { color: var(--gold); }
.objective-list span { font-weight: 600; }

.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 100px; }
.contact h2 { max-width: 600px; }
.contact > .container > div:first-child > p:last-child { color: rgba(255,255,255,.65); margin-top: 22px; max-width: 500px; }
.light-label { color: var(--gold-light); }
.contact-details { display: grid; gap: 25px; }
.contact-details a, .contact-details div { padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,.13); }
.contact-details small { display: block; color: var(--gold); font-size: 10px; font-weight: 800; letter-spacing: .18em; margin-bottom: 5px; }
.contact-details strong { display: block; color: #fff; font-size: 17px; font-weight: 600; }

footer { background: #050f25; color: rgba(255,255,255,.55); padding: 25px 0; }
.footer-wrap { display: flex; justify-content: space-between; align-items: center; gap: 20px; font-size: 12px; }
.footer-wrap img { width: 160px; }

@media (max-width: 850px) {
  .menu-toggle { display: block; }
  .nav { display: none; position: absolute; top: 78px; left: 0; right: 0; padding: 20px; background: var(--navy); flex-direction: column; align-items: stretch; }
  .nav.open { display: flex; }
  .nav a { padding: 8px 0; }
  .nav-cta { text-align: center; }
  .two-col, .contact-grid { grid-template-columns: 1fr; gap: 45px; }
  .vision-grid, .service-grid, .value-grid { grid-template-columns: 1fr; }
  .hero { min-height: 650px; }
  .section { padding: 75px 0; }
  .footer-wrap { flex-direction: column; align-items: flex-start; }
}
'''

js = r'''const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");

toggle.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});

document.querySelectorAll(".nav a").forEach(link => {
  link.addEventListener("click", () => nav.classList.remove("open"));
});
'''



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
#readme = r'''# PENALOYS ENTERPRISES LIMITED WEBSITE

# This is the first responsive website version for PENALOYS ENTERPRISES LIMITED.

# ## Files

# - `index.html` - website structure and content
# - `styles.css` - layout, branding and responsive design
# - `script.js` - mobile navigation
# - `assets/penaloys-logo.png` - logo extracted from the supplied company profile

# ## Run locally

# 1. Open this folder in VS Code.
# 2. Open `index.html` directly in a browser, or use the VS Code Live Server extension.
# 3. No Python, Node.js or database is required for this first static version.

# ## Content source

# The company information is based on the supplied PENALOYS ENTERPRISES LIMITED company profile.

# ## Next development stage

# Possible additions include:
# - quotation/request form
# - WhatsApp contact button
# - projects/portfolio section
# - downloadable company profile
# - Google Maps location
# - CMS or admin panel
# - backend/database if the company later needs an operational management system
# '''

# #(base / "index.html").write_text(html, encoding="utf-8")
# #(base / "styles.css").write_text(css, encoding="utf-8")
# #(base / "script.js").write_text(js, encoding="utf-8")
# #(base / "README.txt").write_text(readme, encoding="utf-8")

# #zip_path = Path("/mnt/data/Penaloys_Website.zip")
# #with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
# #    for path in base.rglob("*"):
# #        if path.is_file():
# #            z.write(path, path.relative_to(base.parent))

# #print(f"Created: {zip_path}")
# #print(f"Website folder: {base}")
