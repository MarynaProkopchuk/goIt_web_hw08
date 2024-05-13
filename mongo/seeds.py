from models import Authors, Quotes

import json
import connect


def insert_authors():
    with open("authors.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            author = Authors(
                fullname=d["fullname"],
                born_date=d["born_date"],
                born_location=d["born_location"],
                description=d["description"],
            )
            author.save()
        return author


def insert_quotes():
    with open("quotes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            author, *_ = Authors.objects(fullname=d.get("author"))
            quote = Quotes(
                tags=d["tags"],
                author=author,
                quote=d["quote"],
            )
            quote.save()
        return quote


if __name__ == "__main__":
    insert_authors()
    insert_quotes()
