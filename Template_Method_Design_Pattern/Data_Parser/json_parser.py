from .abstract_data_parser import DataParser
import json

class JSONParser(DataParser):
    def load_data(self):
        self.data = json.loads(self.raw_data)
        return "JSON data loaded"

    def extract_data(self):
        if isinstance(self.data, list):
            return f"Extracted {len(self.data)} JSON records"
        return "Extracted 1 JSON record"