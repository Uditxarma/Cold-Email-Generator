# ✉️ Cold Email Generator

Generate personalized cold emails from job postings — powered by AI and LLMs.

## 🚀 Overview
The Cold Email Generator is a Streamlit web app that helps you craft tailored cold emails for job applications. By leveraging large language models (LLMs) and vector search, it analyzes job postings and your portfolio to generate highly relevant emails, saving you time and increasing your chances of landing interviews.

## 🛠️ Features
- **Paste a Job Posting URL:** Enter any job posting link to analyze its content.
- **Automatic Data Extraction:** The app scrapes and cleans job descriptions for you.
- **Portfolio Integration:** Matches your skills and portfolio links to the job requirements.
- **AI-Powered Email Writing:** Uses LLMs to generate personalized cold emails.
- **Modern UI:** Clean, responsive interface built with Streamlit.

## 📦 Project Structure
```
├── main.py                # Streamlit app entry point
├── chains.py              # LLM and email generation logic
├── portfolio.py           # Portfolio management and querying
├── utils.py               # Utility functions (e.g., text cleaning)
├── requirements.txt       # Python dependencies
├── sample_portfolio.csv   # Example portfolio data
├── DockerFile             # Docker container setup
├── .dockerignore          # Docker build context exclusions
├── .gitignore             # Git exclusions
├── vectorstore2/          # Vector database (auto-generated)
└── Cold Email Generator.png # App result screenshot
```

## ⚡ Quick Start
### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Cold-Email-Generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run main.py
```

### 4. Open in Browser
Go to [http://localhost:8501](http://localhost:8501) to use the app.

## 🐳 Docker Usage
Build and run the app in a container:
```bash
docker build -t cold-email-generator .
docker run -p 8001:8001 cold-email-generator
```

## 📝 How It Works
1. **Input:** Paste a job posting URL.
2. **Processing:** The app scrapes and cleans the job description.
3. **Portfolio Matching:** Your portfolio is loaded and matched to job skills.
4. **Email Generation:** An LLM writes a personalized cold email.
5. **Output:** The generated email is displayed for you to copy and use.

## 📁 Customization
- **Portfolio:** Replace `sample_portfolio.csv` with your own data for better results.
- **LLM & Chains:** Modify `chains.py` to use different models or prompt templates.

## 🤝 Contributing
Pull requests and suggestions are welcome! Please open an issue to discuss changes.

## 📄 License
MIT License. See `LICENSE` for details.

---

> Made with ❤️ using Streamlit, LangChain, and Python.
