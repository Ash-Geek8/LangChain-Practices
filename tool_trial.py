import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

result = search.invoke("Latest AI news")
print(result)