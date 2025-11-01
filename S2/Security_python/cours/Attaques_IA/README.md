# AI-Powered Attacks with Python (Free Tools Edition)

This course demonstrates how AI (LLMs) can be used in offensive security scenarios, including prompt injection, phishing, and recon, using only free, local tools.

## Structure:
1. Prompt Injection
2. Phishing Email Generation
3. Recon with LLM

All exercises use `llama-cpp-python` to run LLMs locally without internet access or API tokens.

---

## ✅ LLaMA Environment Setup (Offline, Free)

### 🧠 What You’ll Get:
- Offline-capable LLM (e.g. TinyLlama, Mistral)
- Usable in Python (Jupyter, scripts)
- No API keys, no cloud access needed

---

### 🧰 1. System Requirements

- **OS**: Windows 10/11, macOS, Linux
- **RAM**: 8GB+ recommended
- **Python**: 3.9–3.11 (best with 3.10)
- Optional: CUDA for GPU acceleration (Linux/Windows)

---

### 🛠️ 2. Set up Python Environment

Use `venv` or `conda`.

=====
# Create and activate virtual environment
python -m venv llama-env
# python3 -m venv llama-env
source llama-env/bin/activate  # Linux/macOS
# llama-env\Scripts\activate   # Windows

# Upgrade pip
pip install --upgrade pip
=====

---

### 📦 3. Install Required Packages

=====
pip install llama-cpp-python==0.2.60 jupyter notebook numpy beautifulsoup4
=====

For GPU support (optional, only on supported NVIDIA cards with CUDA):
=====
pip install llama-cpp-python[cuda]
=====

---

### 🧠 4. Download a GGUF LLM Model

Use a small, open-source model like **TinyLlama** or **Mistral** from [HuggingFace](https://huggingface.co/TheBloke).

Example (Mistral, 7B):

- URL: https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF/resolve/main/openhermes-2.5-mistral-7b.Q4_K_M.gguf

- File: `openhermes-2.5-mistral-7b.Q4_K_M.gguf` (choose `q4_K_M` quantized version)

Save it to:

=====
AI_Attack_Course/
├── models/
│   └── mistral7b.gguf
=====

---

### 🧪 5. Test Model Load in Python

======
from llama_cpp import Llama

llm = Llama(model_path="models/mistral7b.gguf", n_ctx=512)
output = llm("USER: How can I protect my password?\nASSISTANT:", max_tokens=100)
print(output["choices"][0]["text"].strip())
=====

If it prints a response, you're good to go!

---

### 📚 6. Run the Labs

Start Jupyter:

=====
jupyter notebook
=====

Open the `.ipynb` lab notebooks and run cells. Make sure the model path matches where you placed the GGUF file.

---

### 📁 Recommended Folder Structure

=====
AI_Attack_Course/
├── models/
│   └── mistral7b.gguf
├── data/
│   └── github_sample.html
├── 1_prompt_injection.ipynb
├── 2_phishing_email_generator.ipynb
├── 3_recon_with_llm.ipynb
=====

---

Would you like me to bundle this setup into a printable README or include an installation script (`setup.sh` or `install.bat`) for students?


