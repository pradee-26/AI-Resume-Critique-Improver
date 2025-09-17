# 🧾 AI Resume Critique & Improver (Offline)

A privacy-focused AI-powered tool that helps improve resumes by:
- 🧠 Analyzing tone, formatting, and content
- ✍️ Suggesting improvements
- 🔄 Rewriting weak sections with stronger language

Built using Python, Streamlit, and Mistral 7B running locally via Ollama — no internet or API required.

---

## ✅ Features

- Upload a resume in PDF format
- Extract and preview resume content
- Receive actionable critique on formatting, keywords, tone
- Paste weak sections and get improved rewrites
- Fully offline with no data leaving your machine

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **PDF Parsing:** PyMuPDF
- **LLM:** Mistral 7B via Ollama
- **Prompt Engineering:** Custom prompt templates for critique and rewrite

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/SHAIKAFZALHAMEED/AI-Resume-Critique-Improver
cd AI-Resume-Critique-Improver.git
```

2. **(Optional) Create virtual environment:**

```bash
python -m venv venv
# Activate it:
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate       # Windows
```

3. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install Ollama & pull Mistral model:**

```bash
ollama pull mistral
```

---

## 🧪 Running the App

```bash
ollama pull mistral
streamlit run app.py
```

Then:
- Upload your resume PDF
- Click **"Analyze Resume"** to get feedback
- Paste weak text and click **"Rewrite Section"**

---

## 📂 Project Structure

```
ai-resume-critiquer/
├── app.py               # Streamlit UI
├── resume_utils.py      # PDF extraction logic
├── ollama_client.py     # Runs Mistral locally
├── prompts.py           # Prompt templates
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 📌 Future Improvements

- Add download button for improved content
- Support for DOCX files
- Resume scoring system (ATS-friendly check)
- Section tagging & highlighting

---

## 📚 References

- Ollama: https://ollama.com/docs
- Mistral 7B: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1
- Streamlit: https://docs.streamlit.io/
- PyMuPDF: https://pymupdf.readthedocs.io/en/latest/
- Python subprocess: https://docs.python.org/3/library/subprocess.html
