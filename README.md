
# CrewAI Tech Trends Automation 📰🤖

An AI-powered workflow built with [CrewAI](https://github.com/joaomdmoura/crewai) that automates the discovery, summarization, and formatting of the latest trends in technology — including DevOps, Kubernetes, AWS, GitOps, Terraform, System Design, AI Agents, and Drones.

## 📌 What It Does

This project uses a multi-agent architecture to:

- 🔍 **Search** for recent, relevant articles across defined tech domains
- ✍️ **Parse and summarize** key insights from each source
- 🗂️ **Organize content** into structured markdown by topic
- 🎨 **Format and style** the final result into a polished HTML newsletter

The goal is to help developers and tech-curious readers stay informed — with minimal effort and maximum signal.

---

## 🛠️ Tech Stack

- **CrewAI** — for managing the AI agents and task flow
- **OpenAI GPT-4** — for summarization and formatting
- **Serper API** — for web search
- **CrewAI Tools** — including `ScrapeWebsiteTool`, `FileWriterTool`, `FileReadTool`
- **Markdown + CSS** — for clean, shareable output

---

## 📂 Folder Structure

```
.
├── config/
│   ├── agents.yaml         # Agent roles and goals
│   ├── tasks.yaml          # Task definitions and execution context
├── styles/
│   └── newsletter.css      # Optional styling for HTML output
├── outputs/
│   ├── search_results.json
│   ├── parsed_articles.json
│   ├── summaries.json
│   ├── daily_trends.md
│   └── newsletter.html
├── src/
│   └── crew.py             # Main workflow launcher
├── README.md
```

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/YOUR_USERNAME/crewai-tech-trends-automation
   cd crewai-tech-trends-automation
   ```

2. Install dependencies  
   *(use a virtualenv or conda environment)*  
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API keys  
   ```bash
   export SERPER_API_KEY=your-serper-key
   export OPENAI_API_KEY=your-openai-key
   ```

4. Run the automation  
   ```bash
   python src/crew.py
   ```

---

## 📬 Sign Up for the Newsletter

Want to get the updates this system generates?

**Sign up here:**  
👉 [http://si3mshady.github.io/flight-club-landing/](http://si3mshady.github.io/flight-club-landing/)

---

## 📌 Coming Soon

- Email delivery
- Retry logic for failed topics
- Streamlit dashboard for visual previews
- More CrewAI-powered workflows

---

## 🤝 Contributing

Pull requests welcome! If you’ve got CrewAI ideas or want to extend this for other domains, open an issue or submit a PR.

---

## 📄 License

MIT

---

*Built with 🤖 by [Elliott Arnold]*  
```

