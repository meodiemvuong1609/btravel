import json
from pathlib import Path
class Subdivision():

    def __readdir(self, filename):
        return "{}/location/jsondata/{}.json".format(Path(__file__).resolve().parent.parent, filename)
    
    def __readfile(self, filename):
        json_data = None
        with open(self.__readdir(filename)) as file_open:
            json_data = json.loads(file_open.read())
        return json_data
    
    @property
    def json_province(self):
        return self.__readfile("province")
    
    @property
    def json_district(self):
        return self.__readfile("district")
    
    @property
    def json_ward(self):
        return self.__readfile("ward")
    
    def __map__(self, subdivision):
        subdivision = getattr(self, subdivision)
        return [subdivision[key] for key in subdivision]
    
    @property
    def provinces(self):
        return self.__map__("json_province")
    
    @property
    def districts(self):
        return self.__map__("json_district")
    
    @property
    def wards(self):
        return self.__map__("json_ward")
    
    def __get__(self, subdivisions, parent_id):
        parent_id = int(parent_id)
        subdivisions = getattr(self, subdivisions)
        return [
            subdivision 
            for subdivision in subdivisions 
            if int(subdivision["parent_code"]) == parent_id
        ]
    
    def district(self, province_id = None):
        return self.__get__(parent_id=province_id, subdivisions="districts")
    
    def ward(self, district_id = None):
        return self.__get__(parent_id=district_id, subdivisions="wards")
    
subdivision = Subdivision()
