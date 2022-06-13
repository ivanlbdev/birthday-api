from components.xml_reader import *


if __name__ == '__main__':
    data = XmlReader('data_xml/Сотрудники.xml')
    data.get_actual_birth()
    print(data.get_persons_list())