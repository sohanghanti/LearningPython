from MogodbScripts.script3 import parse_jsonRequest


class script2:
    def __init__(self):
        self.jsonPath = '..\\db\\db_templates\\'

    def insert_record(self, count):
        list_data1 = []

        collection = 'incidents'
        if collection == 'incidents':
            self.jsonPath = self.jsonPath + 'insert_incident.json'

        print(self.jsonPath)
        for i in range(0, count):
            rec = parse_jsonRequest(self.jsonPath)
            list_data1.append(rec)
        print(list_data1)



script2().insert_record(5)
