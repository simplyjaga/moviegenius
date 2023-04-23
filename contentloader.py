# ref:https://github.com/hwchase17/langchain/blob/master/langchain/document_loaders/text.py

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader

class ContentLoader(BaseLoader):
    def __init__(self, contents, source="wiki-ddg"):
        self.contents = contents
        self.source = source

    def load(self):
        text = ''
        for content in self.contents:
          text = f"{text}\n{content}"          
        metadata = {"source": self.source}
        return [Document(page_content=text, metadata=metadata)]
        
