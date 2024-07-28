import json
from src.config import QUOTES_PATH
import logging
import random

def get_quote(item):
    logging.debug(f"Getting quote for item: {item}")
    try:
        with open(QUOTES_PATH, 'r') as file:
            quotes = json.load(file)
        quote_data = quotes.get(item, {
            "key_message": "No quote found for this item.",
            "question": "No question available.",
            "answers": [],
            "correct_answer": ""
        })
        # Randomize the order of the answers
        quote_data["answers"] = random.sample(quote_data["answers"], len(quote_data["answers"]))
        logging.debug(f"Quote retrieved: {quote_data}")
        return quote_data
    except Exception as e:
        logging.error(f"Error reading quotes file: {e}")
        return {
            "key_message": "Error retrieving quote.",
            "question": "Error retrieving question.",
            "answers": [],
            "correct_answer": ""
        }