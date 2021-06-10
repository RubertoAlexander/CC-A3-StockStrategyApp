from app.models import yf_autocomplete
from flask import render_template, request, redirect, make_response, jsonify

from app import app

@app.route("/search/<query>")
def search(query: str):
    result = yf_autocomplete.search(query)

    quotes = []
    if result:
        for quote in result["quotes"]:
            if quote["exchange"] == "ASX":
                quotes.append({
                    "symbol": quote["symbol"],
                    "name": quote["shortname"]
                })

        search_dict = jsonify(
            quotes=quotes
        )
        return search_dict