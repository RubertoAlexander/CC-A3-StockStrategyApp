from app.models import yf_autocomplete
from flask import jsonify

from app import app

@app.route("/search/<query>")
def search(query: str):
    result = yf_autocomplete.search(query)

    quotes = []
    if result:
        for quote in result["quotes"]:
            if quote["exchange"] == "ASX":
                name = ""
                if "shortname" in quote:
                    name = quote["shortname"]
                elif "longname" in quote:
                    name = quote["longname"]
                quotes.append({
                    "symbol": quote["symbol"],
                    "name": name
                })

        search_dict = jsonify(
            quotes=quotes
        )
        return search_dict