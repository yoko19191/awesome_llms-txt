# Awesome LLMs.txt

## ABOUT

An llms.txt file is a proposed web standard designed to make website content more accessible and understandable to large language models (LLMs). It is a markdown-formatted text file placed at a website’s root path (e.g., example.com/llms.txt) that provides a structured, concise overview of the site’s key information, tailored for AI processing.

## `llms.txt` vs. `llms-full.txt`

there are two types of `llms.txt` and `llms-full.txt`  availabel.

`llms.txt` acts as a concise index or summary, guiding LLMs to key information and resources on a website.
it contains a brief overview (e.g., project name, purpose in a blockquote) and links to important pages (e.g., documentation, APIs) with short descriptions. It prioritizes brevity and structure.

`llms-full.txt` provides a comprehensive, detailed representation of the website’s content, including full text or in-depth descriptions. it includes extensive information, such as complete documentation, detailed explanations, or aggregated content from multiple pages. It’s less about linking and more about embedding the actual content.

| Feature       | llms.txt                        | llm-full.txt                     |
| ------------- | ------------------------------- | -------------------------------- |
| Purpose       | Concise index with links        | Comprehensive content dump       |
| Content Depth | Summaries and pointers          | Detailed, full-text content      |
| Size          | Small, fits LLM context windows | Large, may exceed context limits |
| Processing    | Quick and lightweight           | Requires more processing power   |
| Use Case      | Guide LLMs to resources         | Provide all content directly     |

## Content

token* comsumption estimated by tiktokenizer o200k_base.

| website              | files                                                                  | tokens  | source  | create_date |
| -------------------- | ---------------------------------------------------------------------- | ------- | ------- | ----------- |
| [modelcontextprotocol](https://modelcontextprotocol.io/llms.txt) | [llms.txt](./content/modelcontextprotocol/llms.txt)                      | 1,693   | website | 20250422    |
| [modelcontextprotocol](https://modelcontextprotocol.io/llms-full.txt) | [llms-full.txt](./content/modelcontextprotocol/)            | 103,827 | website | 20250422    |
| [LangGraph Python](https://langchain-ai.github.io/langgraph/llms-full.txt)     | [llms.txt](./content/langgraph_python/llms.txt)                                                              | 9808    | website | 20250422    |
| [LangGraph Python](https://langchain-ai.github.io/langgraph/llms-full.txt)     | [llms-full.txt](./content/langgraph_python/llms-full.txt)   | 274,937 | website | 20250422    |
| [LangGraph JS](https://langchain-ai.github.io/langgraphjs/llms.txt)        | [llms.txt](./content/langgraph_js/llms.txt)           | 5,081   | website | 20250422    |
| [LangGraph JS](https://langchain-ai.github.io/langgraphjs/llms-full.txt)         | [llms-full.txt](./content/langgraph_js/llms-full.txt) | 235,019 | website | 20250422    |
| [LangChain Python](https://python.langchain.com/llms.txt)     | [llms.txt](./content/langchain_python/llms.txt)                         | 24,800  | website | 20250422    |
| [LangChain JS](https://js.langchain.com/llms.txt)         | [llms-full.txt](./content/langchain_js/llms.txt)                        | 23,879  | website | 20250422    |
