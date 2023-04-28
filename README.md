# Movie Genius

The idea of the Movie Genius project is to answer any question related to a plot of a movie thrown at it by the user. It is question answering system built using Langchain and Openai's models. It is a CLI based application.

Steps to use Movie Genius:

1. Clone the repo locally
2. Run the below command to install the required packages (creating a virtual env before installing it would be a better option)
```pip install -r requirements```
3. Go to the terminal and Run the below command to start the application (use python3 or python depending on your system) 
```python app.py```
4. Throw the question to the application related to your favourite movie and have fun

NOTE: Since the application uses OpenAI's api to generate a best possible answer, it will ask for your openai api key. 

You can also directly try it out in the Hugging Face Spaces @ https://huggingface.co/spaces/simplyjaga/movie_genius_openai

NOTE: In case installing packages through requirements.txt throws an error, use the below command to install the required packages manually.

```pip install duckduckgo_search wikipedia langchain faiss-cpu openai gradio tiktoken ```
