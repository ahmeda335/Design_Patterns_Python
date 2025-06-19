from .abstract_data_parser import DataParser
import io
import csv

class CSVParser(DataParser):
    def load_data(self):
        f = io.StringIO(self.raw_data)
        reader = csv.DictReader(f)
        self.data = list(reader)
        return "CSV data loaded"
    
    def extract_data(self):
        return f"Extracted {len(self.data)} CSV records"