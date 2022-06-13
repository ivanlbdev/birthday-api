from components.xml_reader import *
from flask import Flask, jsonify

data = XmlReader('data_xml/Сотрудники.xml')
data.get_actual_birth()

domen = 'http://127.0.0.1:5000'

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/birthdays/")
def get_persons():
    serialaze_dict = {}
    for index,value in enumerate(data.get_persons_list()):
        serialaze_dict[index] = value
    print(serialaze_dict)
    return serialaze_dict

@app.route("/links/")
def get_links():
    links_dict = {}
    for index, value in enumerate(data.get_persons_list()):
        alias = value['id'][1:-1]
        links_dict[index] = domen + '/links/' + alias
    return links_dict

@app.route("/birthdays/<id>")
def hello_world3(id):
    return f"<p>Hello, World!{id}</p>"


# if __name__ == '__main__':
#     data = XmlReader('data_xml/Сотрудники.xml')
#     data.get_actual_birth()
#     print(data.get_persons_list())