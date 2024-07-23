import json
from src.config import QUOTES_PATH
import logging

def get_quote(item):
    logging.debug(f"Getting quote for item: {item}")
    try:
        with open(QUOTES_PATH, 'r') as file:
            quotes = json.load(file)
        quote_data = quotes.get(item, {"key_message": "No quote found for this item.", "mental_health_quote": "No mental health quote available."})
        logging.debug(f"Quote retrieved: {quote_data}")
        return quote_data
    except Exception as e:
        logging.error(f"Error reading quotes file: {e}")
        return {"key_message": "Error retrieving quote.", "mental_health_quote": "Error retrieving mental health quote."}