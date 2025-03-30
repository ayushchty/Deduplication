import pandas as pd
import json


class FileChecker:
    def __init__(self, file_path):
        # self.file_path = file_path.lower()
        self.df = pd.read_csv(file_path)  

    def get_dataframe(self):
        return self.df
    def get_extension(self):
        return self.file_path.split('.')[-1]

    def read_file(self):
        extension = self.get_extension()
        if extension == 'xlsx':
            return pd.read_excel(self.file_path)
        elif extension == 'csv':
            return pd.read_csv(self.file_path)
        elif extension == 'txt':
            with open(self.file_path, 'r') as file:
                return file.read()
        elif extension == 'json':
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            raise ValueError("Unsupported file format!")
