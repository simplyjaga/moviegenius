from getplot import getplot

from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.callbacks import get_openai_callback


def mgchat(user_que):
	#get the plot info
	content  = getplot(user_que)

	#chunk the content and then convert it into document kind 
	text_splitter = TokenTextSplitter(chunk_size=500, chunk_overlap=100)
	texts = text_splitter.split_text(content)
	documents = text_splitter.create_documents(texts)

	#build the vector store
	embeddings = OpenAIEmbeddings()
	docsearch = FAISS.from_documents(documents, embeddings)

	#build the answer retrievel system
	llm = OpenAI()
		
	# ref: https://github.com/hwchase17/langchain/issues/2255
	retriever = docsearch.as_retriever(search_kwargs={"k": 1})
	
	qa = RetrievalQA.from_chain_type(llm=llm, chain_type="refine", retriever=retriever)

	#getting the answer
	with get_openai_callback() as cb:
		ans = qa.run(user_que)
		print("*" * 30)
		print(f"Total Tokens: {cb.total_tokens}")
		print(f"Prompt Tokens: {cb.prompt_tokens}")
		print(f"Completion Tokens: {cb.completion_tokens}")
		print(f"Total Cost (USD): ${cb.total_cost}")
		print("*" * 30)
	
	return ans
	
	
	
	
	
	
	
	
	

