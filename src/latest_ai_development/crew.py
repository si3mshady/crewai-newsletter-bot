import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool, FileReadTool

# Ensure API keys are set for OpenAI and Serper before running
# os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"
os.environ["SERPER_API_KEY"] = ""

llm = LLM(
    model="gpt-4-1106-preview",
    max_tokens=4000,
    temperature=0.2
)

@CrewBase
class TechTrendsCrew():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def trends_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['trends_agent'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                FileWriterTool()
            ],
            verbose=True,
            llm=llm
        )

    @agent
    def newsletter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['newsletter_agent'],
            tools=[
                FileWriterTool(),
               
            ],
            verbose=True,
            llm=llm
        )

    @task
    def search_trends(self) -> Task:
        return Task(
            config=self.tasks_config['search_trends'],
            agent=self.trends_agent()
        )

    @task
    def parse_content(self) -> Task:
        return Task(
            config=self.tasks_config['parse_content'],
            agent=self.trends_agent()
        )

    @task
    def summarize_content(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_content'],
            agent=self.trends_agent()
        )

    @task
    def categorize_content(self) -> Task:
        return Task(
            config=self.tasks_config['categorize_content'],
            agent=self.trends_agent()
        )

    @task
    def save_results(self) -> Task:
        return Task(
            config=self.tasks_config['save_results'],
            agent=self.trends_agent()
        )

    @task
    def create_newsletter(self) -> Task:
        return Task(
            config=self.tasks_config['create_newsletter'],
            agent=self.newsletter_agent(),
            tools=[ FileReadTool(file_path="parsed_articles.json"),
                FileReadTool(file_path="newsletter.css")]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

if __name__ == "__main__":
    crew_instance = TechTrendsCrew()
    result = crew_instance.crew().kickoff()
    print("✅ Daily tech trends report and newsletter generated.")
    # Optional: Email the report (functionality to be enabled later)
    # send_report_via_email("daily_trends.md", recipient="you@example.com")
