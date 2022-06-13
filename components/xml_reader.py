import datetime
import xml.etree.ElementTree as ET


class XmlReader:
    actual_persons = []

    def __init__(self, src):
        self.xml_src = src

    def __get__(self, instance, owner):
        return instance, owner

    def get_persons_list(self):
        return self.actual_persons

    def open_xml(self):
        tree = ET.parse(self.xml_src)
        return tree.getroot()

    def get_actual_birth(self, max_days=-12, min_days=-3):
        persons_list = self.open_xml()
        day_today = datetime.date.today()
        for item in persons_list:
            birthday_array = item.attrib['birthdate'].split('.')
            date_birthday = datetime.date(2022, int(birthday_array[1]), int(birthday_array[0]))
            date_diff = day_today - date_birthday
            if max_days < date_diff.days < min_days:
                self.actual_persons.append(item.attrib)


