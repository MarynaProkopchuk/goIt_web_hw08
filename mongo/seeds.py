from models import Authors, Quotes

import json
import connect


def insert_authors():
    with open("authors.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for x in data:
            author = Authors(
                fullname=x["fullname"],
                born_date=x["born_date"],
                born_location=x["born_location"],
                description=x["description"],
            )
            author.save()
        return author


def insert_quotes():
    with open("quotes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for x in data:
            author, *_ = Authors.objects(fullname=x.get("author"))
            quote = Quotes(
                tags=x["tags"],
                author=author,
                quote=x["quote"],
            )
            quote.save()
        return quote


if __name__ == "__main__":
    insert_authors()
    insert_quotes()
