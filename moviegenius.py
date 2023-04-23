from getplot import getplot
from contentloader import ContentLoader
from getpersona import getpersona

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.callbacks import get_openai_callback


def mgchat(user_que):
	#get the plot info
	content  = getplot(user_que) #[wiki_plot, ddg_res]

	#convert the list of plot info into kind of document
	loader = ContentLoader(content, "wiki_ddg")
	document = loader.load()

	#chunk the document
	text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
	texts = text_splitter.split_documents(document)

	#build the vector store
	embeddings = OpenAIEmbeddings()
	docsearch = FAISS.from_documents(texts, embeddings)

	#build the answering system
	llm = OpenAI()
	
	prompt = getpersona()
	chain_type_kwargs = {"prompt": prompt}
		
	# ref: https://github.com/hwchase17/langchain/issues/2255
	retriever = docsearch.as_retriever(search_kwargs={"k": 1})
	
	qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever,chain_type_kwargs=chain_type_kwargs)

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
	
	
	
	
	
	
	
	
	

