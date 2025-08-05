# 🤖 AI Task Agent: Gmail ➝ LLM ➝ Google Calendar

An AI-powered personal productivity agent that connects to **Gmail**, summarizes emails, detects meeting/tasks using **LLaMA3-8B (via Groq)**, and automatically schedules them on your **Google Calendar**.

---

## ✨ Features

- 🔐 OAuth2-based Gmail & Google Calendar integration
- 📬 Fetch recent emails and analyze with AI
- 🧠 Use **Groq’s `llama3-8b-8192` model** for:
  - Summarization
  - Task/meeting extraction
- 📅 Automatically schedule events in Google Calendar
- 🕓 Timezone aware (default: `Asia/Kolkata`)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/codewithbhagyashri-22/ai-task-agent.git
cd ai-task-agent
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Google OAuth Setup

### Step 1: Create OAuth credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing one).
3. Enable the following APIs:
   - **Gmail API**
   - **Google Calendar API**
4. Go to `APIs & Services → Credentials`
5. Click `+ Create Credentials` → Select **OAuth client ID**
6. Select **Desktop App** as application type.
7. Download the credentials JSON.
8. Copy it in root folder of project as `client_secret.json` (Use it in next step)

---

### Step 2: Get your `refresh_token`

Run the helper script to initiate OAuth and get your token:

```bash
python get_refresh_token.py
```

It will:
- Open a browser window for login/consent.
- Save and show your `refresh_token` in the terminal.

---

### Step 3: Create your `.env` file

Use the `.env.sample` file as reference:

```env
# Gmail & Calendar
GMAIL_CLIENT_ID=your_client_id
GMAIL_CLIENT_SECRET=your_client_secret
GMAIL_REFRESH_TOKEN=your_refresh_token
GOOGLE_CALENDAR_ID=primary

# Groq LLM Configuration
GROQ_API_KEY=your_groq_key
```

---

## 🚀 How to Run

To fetch Gmail, extract tasks/meetings using LLM, and sync to Google Calendar:

```bash
python main.py
```

This will:
- Read latest emails
- Use `llama3-8b-8192` model from Groq to extract meaningful tasks/meetings
- Create events on your Google Calendar

---

## 🧠 LLM Configuration

The app uses **Groq API** to run **Meta’s LLaMA3 8B model** with low-latency:

```
GROQ_API_BASE=https://api.groq.com/openai/v1
GROQ_MODEL=llama3-8b-8192
```

The code uses OpenAI-compatible format for prompt and completion.

---

## 📌 Example Output

Example event created from email:

```json
{
  "summary": "Client Sync Meeting",
  "start": {"dateTime": "2025-08-06T11:00:00+05:30"},
  "end":   {"dateTime": "2025-08-06T11:30:00+05:30"}
}
```

---

## 🧪 Testing Individual Modules

- Test LLM extraction alone:
  ```bash
  python agent.py
  ```

- Test only calendar event creation:
  ```bash
  python calendar_sync.py
  ```

---

## 📈 Roadmap

- [ ] Integrate with Notion for task sync
- [ ] Add recurring meeting detection
- [ ] Email thread history/context
- [ ] Deploy on Replit/Render with UI

---

## 📄 License

This project is licensed under thethe [MIT License](./LICENSE). Feel free to use, modify, and distribute with attribution.

---

## ❤️ Credits

This project is built using:

- [Groq API](https://console.groq.com/) — ultra-fast inference using Meta’s LLaMA3 models
- [Google API Client for Python](https://github.com/googleapis/google-api-python-client)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- Meta’s [LLaMA3-8B-8192](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)

Special thanks to the open-source and developer community 🌍

---

## 💬 Contact

Created by **[Bhagyashri Salgare]**  
GitHub: [github.com/codewithbhagyashri-22](https://github.com/codewithbhagyashri-22)  
LinkedIn: [linkedin.com/in/BhagyashriSalgare](https://www.linkedin.com/in/bhagyashri-salgare-485b5b146/)