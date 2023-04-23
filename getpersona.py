from langchain.prompts import PromptTemplate

def getpersona():
	prompt_template ="""
	I want you to act as a question answering assistant regrading movie storylines and plots. Use the following information about the movie to answer the following questions related to the story of the film. Don't try to make up the answers, Tell the user you don't know the answer if don't know or confused.
	
	Try to find the answer from the movie story.
	
	{context}
	
	Question: {question}
	Answer:
	"""
	
	return PromptTemplate(template=prompt_template, input_variables=["context", "question"])
