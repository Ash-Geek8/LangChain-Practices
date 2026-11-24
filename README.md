# LangChain Practices

A hands-on Python repository for learning and experimenting with **LangChain and Generative AI**.

This repository explores model integration, prompt engineering, LangChain Expression Language (LCEL), multimodal inputs, image generation, and external tools.

## Learning Objectives

- Integrate Google Gemini with LangChain.
- Build reusable prompts using PromptTemplate.
- Understand LCEL and chain composition.
- Experiment with multimodal image understanding.
- Explore image-generation APIs.
- Integrate external search tools.
- Build a foundation for RAG and agentic AI applications.

## Tech Stack

- Python 3.10+
- LangChain
- LangChain Core
- LangChain Google GenAI
- LangChain Community
- Google Gemini API
- OpenAI API
- python-dotenv

## Repository Structure

```text
LangChain-Practices/
│
├── LCEL.py
├── prompts_langchain.py
├── check.py
├── img-und.py
├── img_gen.py
├── test.py
├── tool_trial.py
├── module-try.py
├── test.jpg
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Ash-Geek8/LangChain-Practices.git
cd LangChain-Practices
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

If execution policy blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**Windows CMD**

```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

API credentials:

- [Google AI Studio](https://aistudio.google.com/apikey)
- [OpenAI API](https://platform.openai.com/api-keys)

Never commit API keys or upload your `.env` file to GitHub.

## Running the Experiments

| File                   | Concept                          |
| ---------------------- | -------------------------------- |
| `check.py`             | Gemini model integration         |
| `prompts_langchain.py` | PromptTemplate                   |
| `LCEL.py`              | LangChain Expression Language    |
| `img-und.py`           | Image understanding using Gemini |
| `img_gen.py`           | DALL·E image generation          |
| `test.py`              | OpenAI image-generation API      |
| `tool_trial.py`        | DuckDuckGo search integration    |
| `module-try.py`        | LangChain version verification   |

Run individual experiments:

```bash
python check.py
python prompts_langchain.py
python LCEL.py
python img-und.py
python img_gen.py
python test.py
python tool_trial.py
```

Some experiments require separate provider API credentials and account access.

## Understanding LCEL

The `LCEL.py` experiment demonstrates how individual LangChain components can be connected using the pipe operator.

```text
Input
  |
  v
PromptTemplate
  |
  v
ChatGoogleGenerativeAI
  |
  v
StrOutputParser
  |
  v
Final Response
```

Example:

```python
chain = prompt | llm | output_parser

result = chain.invoke({
    "topic": "programming"
})

print(result)
```

## Learning Roadmap

- [ ] Gemini model integration
- [ ] Prompt templates
- [ ] LCEL fundamentals
- [ ] Image understanding
- [ ] Image-generation experiments
- [ ] Search tool integration
- [ ] Conversation history
- [ ] Structured outputs
- [ ] Runnable sequences and parallel execution
- [ ] Document loaders and text splitters
- [ ] Embeddings and vector databases
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Tool calling and agents
- [ ] LangGraph workflows

## Useful Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [LangChain API Reference](https://reference.langchain.com/python)
- [Google AI Studio](https://aistudio.google.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## Author

**Ashfaq Ahamed**

GitHub: [@Ash-Geek8](https://github.com/Ash-Geek8)

Repository: [LangChain-Practices](https://github.com/Ash-Geek8/LangChain-Practices)

---

A practical learning repository documenting my journey into LangChain, LLM applications, RAG, and Agentic AI.
