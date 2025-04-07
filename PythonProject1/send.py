from jinja2 import Environment, FileSystemLoader
import db

def getMessage(data):
    environment = Environment(loader=FileSystemLoader("./"))
    template = environment.get_template("template.txt")
    res = []
    for student in data:
        filename = f"content/message_{str(student['id']) .lower()}.txt"
        content = template.render(
            student
        )
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")
        res.append(filename)
    return res


if __name__ == '__main__':
    getMessage(db.getUsers())