# 📄 AI-Powered CV Parser

An intelligent CV parsing system that extracts structured information from PDF resumes using advanced AI models. The project consists of a FastAPI backend powered by Qwen-4B LLM and a beautiful Streamlit frontend .

## ✨ Features

- 🤖 **AI-Powered Extraction**: Uses Qwen/Qwen3-4B language model for intelligent parsing
- 📊 **Structured Output**: Extracts key information in JSON format
- 🌐 **REST API**: FastAPI backend with ngrok for public access
- 🎨 **Modern UI**: Streamlit frontend with sleek red theme
- 🔒 **Secure**: API key authentication
- 📱 **Responsive**: Clean, centered layout with skill chips

## 📋 Extracted Information

The parser extracts the following fields from CVs:

- **Full Name** - Candidate's complete name
- **Email** - Contact email address
- **Education** - Degrees, institutions, and graduation years
- **Skills** - Technical and soft skills (displayed as interactive chips)
- **Experience** - Work history with roles, companies, and duration

## 🏗️ Project Structure

```
cv-parser/
├── cv_parser.ipynb   # Backend notebook with AI model and API
├── parser.py             # Streamlit frontend application
└── README.md            # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- GPU recommended (for faster model inference)
- ngrok account and auth token

## 🛠️ Technical Details

### Backend Stack

- **FastAPI**: Modern, fast web framework
- **LangChain**: Framework for LLM applications
- **Transformers**: Hugging Face library for AI models
- **PyPDFLoader**: PDF text extraction
- **ngrok**: Public URL tunneling

### AI Model

- **Model**: Qwen/Qwen3-4B
- **Type**: Causal Language Model
- **Precision**: FP16 (float16)
- **Device**: Auto-mapped (GPU if available)

### Frontend Stack

- **Streamlit**: Python web app framework
- **Requests**: HTTP library for API calls
- **Custom CSS**: Red-themed modern design

## 📝 Example Output

```
============================================================
           CV PARSING RESULTS
============================================================

📝 FULL NAME:
   John Doe

📧 EMAIL:
   john.doe@example.com

🎓 EDUCATION:
   • Bachelor of Science in Computer Science, MIT, 2020
   • Master of Science in AI, Stanford, 2022

💼 SKILLS:
   • Python
   • Machine Learning
   • FastAPI
   • React
   • Docker

🏢 EXPERIENCE:
   • Software Engineer at Tech Corp (2020-2023)
   • Senior ML Engineer at AI Startup (2023-Present)

============================================================
```

---

**Made with ❤️ using AI and Python**
