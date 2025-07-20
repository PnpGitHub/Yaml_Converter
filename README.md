# 🔧 GitLab CI → GitHub Actions YAML Converter

A smart, offline tool that converts your `.gitlab-ci.yml` into a clean, deployable `GitHub Actions` workflow.  
Built for DevOps engineers migrating CI/CD pipelines — no OpenAI key required!

![Tool Screenshot](./screenshot.png) <!-- optional: add your own -->

---

## 🚀 Features

- 🧾 Paste your `.gitlab-ci.yml`, get GitHub Actions YAML
- 💡 Smart logic to map job, script, and image (Python)
- 🔐 Fully offline fallback (no API needed)
- 🤖 Optional AI Mode (ChatGPT) for advanced use cases *(WIP)*
- 🖼️ Streamlit GUI — super clean and interactive

---

## ⚙️ Tech Stack

- `Python 3.9+`
- `Streamlit` for UI
- `ruamel.yaml` for precise YAML formatting
- *(Optional)* `OpenAI API` for AI-based conversion (if quota available)

---

## 🧑‍💻 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/yaml-convert
cd yaml-convert

# Create virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run the app
streamlit run app.py
