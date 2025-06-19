# 📊 Template Method Design Pattern – Data Parser (Python)

This project demonstrates the **Template Method Design Pattern** by building a flexible data parsing framework that supports CSV, JSON, and XML formats. The pattern defines the overall algorithm structure in an abstract base class (`DataParser`), while allowing concrete subclasses to define specific steps for their file formats.

---

## 📁 Project Structure

- **abstract_data_parser.py**: Contains the abstract `DataParser` class, which defines the template method `parse()`.
- **csv_parser.py**: Implements `CSVParser` with format-specific logic for loading and extracting data.
- **json_parser.py**: Implements `JSONParser` for JSON files.
- **xml_parser.py**: Implements `XMLParser` for XML files.
- **main.py**: Demonstrates how to use the parsers.

---

## 🔧 Core Components

### 🧩 `DataParser` (Abstract Base Class)
Defines the skeleton of the parsing process:

```python
def parse(self, file):
    self.open_file(file)
    self.load_data()
    self.validate_data()
    self.extract_data()
    self.close_file()
```

**Overridable Steps**:
- `load_data()` → required (abstract)
- `extract_data()` → required (abstract)
- `validate_data()` → optional
- `open_file()` / `close_file()` → common to all

---

## 🧩 Concrete Parsers

Each parser subclass overrides only the steps it needs:

- **CSVParser**: Uses `csv.DictReader` to read records.
- **JSONParser**: Uses `json.loads()` to load structured data.
- **XMLParser**: Uses `ElementTree` to parse XML elements.

---


## ✅ Sample Output

```
Opening File... File opened
Loading Data... CSV data loaded
Validating Data... None
Extracting Data... Extracted 2 CSV records
Closing File... File closed
```

> Output varies by parser type and file content.

---

## 📦 Sample Data Files

### `data.csv`
```
name,age
Alice,30
Bob,25
```

### `data.json`
```json
[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
```

### `data.xml`
```xml
<users>
  <user><name>Alice</name><age>30</age></user>
  <user><name>Bob</name><age>25</age></user>
</users>
```

---

## 🧠 Why Template Method?

- Keeps parsing logic consistent across different formats
- Promotes code reuse and clean separation of concerns
- Easy to extend: just create a new subclass!

---

## 🚀 How to Run

Just run `main.py` to test all parser types:

```bash
python main.py
```

Make sure your sample data files (`data.csv`, `data.json`, `data.xml`) are placed in a `data/` directory or adjust the paths accordingly.

---

## 📝 Author

This project was created to practice and demonstrate the **Template Method Pattern** in Python through a practical, real-world example.
