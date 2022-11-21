import csv
import json

class BaseWriter:
    def __init__(self):
        self.formats = ['csv', 'json', 'txt']

class CsvWriter(BaseWriter):
    def __init__(self):
        super().__init__()
    def write(self, data, file_path):
        with open(file_path, "w") as file:
            spamwriter = csv.writer(file, lineterminator="\n")
            for line in data:
                        spamwriter.writerow(line)
                    
class CsvReader(BaseWriter): 
    def __init__(self):
        super().__init__()
        
    def read(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            return list(csv_reader)


class JsonWriter(BaseWriter):
    def __init__(self):
        super().__init__()
        
    def write(self, data, file_path):
        with open(file_path, "w") as file:
            json.dump(data, file)

class JsonReader(BaseWriter): 
    def __init__(self):
        super().__init__()
        
    def read(self, file_path):
        with open(file_path, "r") as file:
            json_data = json.load(file)
            return json_data

class TxtWriter(BaseWriter):
    def __init__(self):
        super().__init__()
        
    def write(self, data, file_path):
        with open(file_path, "w") as file:
            file.write(data)

class TxtReader(BaseWriter): 
    def __init__(self):
        super().__init__()
        
    def read(self, file_path):
        with open(file_path, "r") as file:
            return file.read()