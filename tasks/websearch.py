# tasks/websearch.py
import pywhatkit

def search_web(query):
    pywhatkit.search(query)
    return f"Searching for {query} on the web."
