from .abstract_data_parser import DataParser
import xml.etree.ElementTree as ET

class XMLParser(DataParser):
    def load_data(self):
        self.tree = ET.ElementTree(ET.fromstring(self.raw_data))
        self.root = self.tree.getroot()
        return "XML data loaded"

    def extract_data(self):
        return f"Extracted {len(self.root)} XML elements"