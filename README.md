<p align="center">
  <h1 align="center">🕸️ Generic Scrapper</h1>
  <p align="center">
    <strong>Tiny Flask API that scrapes any page with Selenium and returns the matched text as a downloadable <code>.txt</code> file.</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
    <img src="https://img.shields.io/badge/Selenium-driver-43b02a?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
    <img src="https://img.shields.io/badge/Docker-ready-2496ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/github/last-commit/pratiks360/Generic-Scrapper?style=for-the-badge&label=Last+Commit" alt="Last Commit">
  </p>
</p>

---

## ✨ What Is This?

Send a URL, an XPath and a filename; **Generic Scrapper** opens the page in a headless Selenium browser, extracts the text for that XPath and streams it back as an attachment. CORS is enabled so a browser front-end can call it directly.

## 🔌 Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/scrape` | Form fields `url`, `xpath`, `scope`, `filename` → `filename.txt` attachment |
| `GET` | `/` | Health greeting |

A request missing `url`, `filename` or `scope` returns `400 Invalid request`.

## 🚀 Quick Start

```bash
git clone https://github.com/pratiks360/Generic-Scrapper.git
cd Generic-Scrapper
pip install -r requirements.txt
python app.py          # listens on http://localhost:9001
```

```bash
curl -X POST http://localhost:9001/scrape   -F url=https://example.com -F xpath="//h1" -F scope=page -F filename=out -o out.txt
```

Or with Docker: `docker build -t generic-scrapper . && docker run -p 9001:9001 generic-scrapper` (switch `app.run` to `host='0.0.0.0'` first — see the commented line in `app.py`).

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Web** | Flask, flask-cors |
| **Browser automation** | Selenium + webdriver-manager |
| **Packaging** | Dockerfile |

> Only scrape sites whose terms allow it.

---

<p align="center">
  <sub>Built with ❤️ for quick scraping jobs.</sub>
</p>
