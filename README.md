# Telegram Group Member Scraper

A lightweight **Python 3.8+** script that uses **[Telethon](https://github.com/LonamiWebs/Telethon)** to export all members of one or more public Telegram channels / groups to a CSV file.

> **Purpose**  
> Research, analytics, backup, or moderation tasks where you need a clean list of user IDs, usernames, and basic profile info.

---

## ✨ Features
- **One‑file setup** – nothing to install beyond requirements  
- **Multiple groups** – scrape as many public groups as you like  
- **CSV output** – ready for Excel, pandas, Google Sheets, etc.  
- **2‑FA support** – works with Telegram accounts that have a password  

---

## 🛠 Prerequisites

| Requirement | Notes |
|-------------|-------|
| Python ≥ 3.8 | Check with `python --version` |
| Telegram account | Must receive the login code |
| Telegram API credentials | Obtain **API_ID** and **API_HASH** from <https://my.telegram.org> |

---

## 📦 Installation

```bash
git clone https://github.com/azorkai/telegram-group-scraper.git
cd telegram-member-scraper
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
pip install -r requirements.txt   # installs Telethon
```

> **Tip:** Keep credentials out of version control—use environment variables or a `.env` file.

---

## ⚙️ Configuration

Open `scraper.py` and fill in:

```python
API_ID   = 123456
API_HASH = "your_api_hash"
PHONE    = "+15551234567"
TWO_FA   = "your_password"   # leave "" if 2‑FA disabled
GROUPS   = ["PublicGroup1", "AnotherGroup"]
```

- `SESSION` stores your login as `<SESSION>.session`.  
- Private groups **cannot** be scraped by username alone; you must be a member and pass their invite link or entity.

---

## ▶️ Usage

```bash
python scraper.py
```

1. First run: a code is sent to your Telegram app/SMS—enter it at the prompt.  
2. If your account has a password, enter it when asked.  
3. Progress prints for each group.  
4. On success you’ll see something like:

```
✓ 13 842 done! -> members.csv
```

### CSV Columns

| group | id | username | first_name | last_name | phone | is_bot | is_verified |
|-------|----|----------|------------|-----------|-------|--------|-------------|

---

## 🤝 Contributing

1. Fork the repo  
2. Create a branch: `git checkout -b feature/awesome`  
3. Commit changes: `git commit -m "Add awesome feature"`  
4. Push: `git push origin feature/awesome`  
5. Open a Pull Request

All PRs welcome—tests, docs, refactors, new features!

---

## 📜 License

MIT – see [`LICENSE`](LICENSE) for details.

---

## ⚠️ Disclaimer

Scraping Telegram data may violate Telegram’s Terms of Service or local privacy laws **depending on how you use it**.  
This script is provided **for educational purposes only.** You assume all responsibility for compliance and ethical usage.
