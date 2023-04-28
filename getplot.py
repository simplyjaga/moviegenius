from duckduckgo_search import ddg 
import wikipedia

def ddg_info(query):
        """Run query through DuckDuckGo and return results."""
        
        results = ddg(query,max_results=5)
        snippets = [result["body"] for result in results] 
        return " ".join(snippets)

def wiki_info(query):
	"""Returns the movie plot from wikipedia"""
	
	#adding wiki tag to enhance the chances of getting wiki page as first result
	result = ddg(query + " Wikipedia", max_results = 1)
	
	if "wikipedia" in result[0]['title'].lower(): #if wikipage is returned
		pg_id = result[0]['title'].split('-')[0] #getting the page id from the ddg search results
		
		#ref: https://stackoverflow.com/a/70409134
		pg_content = wikipedia.page(pg_id, auto_suggest=False).content #gettig the contents of wiki page using page id
		
		return pg_content.split("==")[2]  #specifically selecting only the plot section
	else:
		print("No Wikipedia's page found, So using only DDG search results.")
		return ""

def getplot(query):
	#ddg search results
	ddg_res = ddg_info(query)
	#wiki search results
	wiki_res = wiki_info(query)
	content = wiki_res + "\n" + ddg_res
	return content












