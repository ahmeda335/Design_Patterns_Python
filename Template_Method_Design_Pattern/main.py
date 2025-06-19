from Data_Parser import CSVParser, XMLParser, JSONParser
import os

DATA_PATH = "Template_Method_Design_Pattern\DATA"

parser = CSVParser()
parser.parse(os.path.join(DATA_PATH, "data.csv"))
print('-' * 50)

parser = JSONParser()
parser.parse(os.path.join(DATA_PATH, "data.json"))
print('-' * 50)

parser = XMLParser()
parser.parse(os.path.join(DATA_PATH, "data.xml"))
print('-' * 50)
