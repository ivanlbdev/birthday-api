from components.xml_reader import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    data = XmlReader('data_xml/Сотрудники.xml')
    data.get_actual_birth()
    print(data.get_persons_list())