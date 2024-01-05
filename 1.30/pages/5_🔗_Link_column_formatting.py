import requests
import pandas as pd
import streamlit as st
from datetime import datetime

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Link column formatting", "🔗", layout="wide")

icon("🔗")
st.title("Link column formatting", anchor=False)

st.divider()

@st.cache_data
def get_github_repo_data(repo_name):
    """Fetch various data for a given GitHub repository."""
    api_url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return {
            "stars": data['stargazers_count'],
            "forks": data['forks_count'],
        }
    else:
        return None

# List of frameworks and their GitHub repos
framework_repos = {
    "LLM Examples": "streamlit/llm-examples",
    "MemoryBot": "leo-usa/MemoryBot",
    "LangChain Quickstart": "dataprofessor/langchain-quickstart",
    "Knowledge GPT": "mmz-001/knowledge_gpt",
    "SEO Chatbot": "cefege/seo-chat-bot",
    "LlamaIndex Chat with Streamlit Docs": "carolinedlu/llamaindex-chat-with-streamlit-docs"
}

# Fetch and build the dataset
framework_data = {name: get_github_repo_data(repo) for name, repo in framework_repos.items()}

# Add GitHub URL to the dataset
for name, repo in framework_repos.items():
    framework_data[name]["GitHub URL"] = f"https://github.com/{repo}"

# Create a DataFrame
df = pd.DataFrame.from_dict(framework_data, orient='index')
df.reset_index(inplace=True)
df.columns = ['Framework', 'Stars', 'Forks', 'GitHub URL']

# Display in Streamlit
st.info('Real-time GitHub data for a few LLM repos in the [Streamlit Gallery](https://streamlit.io/gallery?category=llms)', icon="⭐️")

new, old = st.columns(2)

# New link formatting
with new:
    st.header("Updated Link URL")
    with st.expander("Show code"):
        st.code(
            """
            @st.cache_data
            def get_github_repo_data(repo_name):
                "Fetch various data for a given GitHub repository."
                api_url = f"https://api.github.com/repos/{repo_name}"
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    return {
                        "stars": data['stargazers_count'],
                        "forks": data['forks_count'],
                    }
                else:
                    return None

            # List of frameworks and their GitHub repos
            framework_repos = {
                "LLM Examples": "streamlit/llm-examples",
                "MemoryBot": "leo-usa/MemoryBot",
                "LangChain Quickstart": "dataprofessor/langchain-quickstart",
                "Knowledge GPT": "mmz-001/knowledge_gpt",
                "SEO Chatbot": "cefege/seo-chat-bot",
                "LlamaIndex Chat with Streamlit Docs": "carolinedlu/llamaindex-chat-with-streamlit-docs"
            }

            # Fetch and build the dataset
            framework_data = {name: get_github_repo_data(repo) for name, repo in framework_repos.items()}

            # Add GitHub URL to the dataset
            for name, repo in framework_repos.items():
                framework_data[name]["GitHub URL"] = f"https://github.com/{repo}"

            # Create a DataFrame
            df = pd.DataFrame.from_dict(framework_data, orient='index')
            df.reset_index(inplace=True)
            df.columns = ['Framework', 'Stars', 'Forks', 'GitHub URL']

            st.data_editor(
                df,
                column_config={
                    "GitHub URL": st.column_config.LinkColumn(
                        "Hyperlink Text",
                        display_text="Open GitHub",
                    ),
                }
            )
            """)

    st.data_editor(
        df,
        column_config={
            "GitHub URL": st.column_config.LinkColumn(
                "Hyperlink Text",
                display_text="Open GitHub",
            ),
        }
    )

# Raw links
with old:
    st.header("Raw URL")
    with st.expander("Show code"):
        st.code(
            """
            @st.cache_data
            def get_github_repo_data(repo_name):
                "Fetch various data for a given GitHub repository."
                api_url = f"https://api.github.com/repos/{repo_name}"
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    return {
                        "stars": data['stargazers_count'],
                        "forks": data['forks_count'],
                        "created_at": parse_iso8601_date(data['created_at'])
                    }
                else:
                    return None

            # List of frameworks and their GitHub repos
            framework_repos = {
                "LLM Examples": "streamlit/llm-examples",
                "MemoryBot": "leo-usa/MemoryBot",
                "LangChain Quickstart": "dataprofessor/langchain-quickstart",
                "Knowledge GPT": "mmz-001/knowledge_gpt",
                "SEO Chatbot": "cefege/seo-chat-bot",
                "LlamaIndex Chat with Streamlit Docs": "carolinedlu/llamaindex-chat-with-streamlit-docs"
            }

            # Fetch and build the dataset
            framework_data = {name: get_github_repo_data(repo) for name, repo in framework_repos.items()}

            # Add GitHub URL to the dataset
            for name, repo in framework_repos.items():
                framework_data[name]["GitHub URL"] = f"https://github.com/{repo}"

            # Create a DataFrame
            df = pd.DataFrame.from_dict(framework_data, orient='index')
            df.reset_index(inplace=True)
            df.columns = ['Framework', 'Stars', 'Forks', 'GitHub URL']

            st.data_editor(
                df,
                key="old",
                column_config={
                    "GitHub URL": st.column_config.LinkColumn(
                        "Raw URL",
                    ),
                }
            )
            """)
    
    st.data_editor(
        df,
        key="old",
        column_config={
            "GitHub URL": st.column_config.LinkColumn(
                "Raw URL",
            ),
        }
    )
