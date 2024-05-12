from models import Authors, Quotes
import connect


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def find_by_tag(args):
    tag = args[0]
    quotes = Quotes.objects(tags__iregex=tag)
    print(quotes)
    result = [q.quote for q in quotes]
    return result


def find_by_tags(args):
    result = []
    for el in args:
        tags = el.split(",")
        for tag in tags:
            quotes = Quotes.objects(tags__iregex=tag)
            quote_by_tag = [q.quote for q in quotes]
            result.append(quote_by_tag[0])
        return result


def find_by_author(args):
    author = (" ").join(args)
    authors = Authors.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quotes.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result


def main():
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "exit":
            print("Good bye!")
            break
        elif command == "name:":
            print(find_by_author(args))
        elif command == "tag:":
            print(find_by_tag(args))
        elif command == "tags:":
            print(find_by_tags(args))


if __name__ == "__main__":
    main()
