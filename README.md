# ai-code-reviewer
An automated tool that uses OpenAI's GPT-4 to review GitHub pull requests and provide feedback on code quality, potential bugs, and improvement suggestions.

### Built with
Python, OpenAI GPT-4, Github API, Docker

### Highlights
- Reviews code in pull requests using an LLM
- GitHub PR integration
- Simple REST endpoint for testing

### Installation

1. Clone the Repo
   ```sh
   git clone https://github.com/your-username/ai-code-reviewer.git
   cd ai-code-reviewer
   ```
2. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Set Environment Variables
   ```js
   OPENAI_API_KEY=your_openai_key
   GITHUB_TOKEN=your_github_token
   ```
4. Run the App
   ```sh
   uvicorn main:app --reload
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
