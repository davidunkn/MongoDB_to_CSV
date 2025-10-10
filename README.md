# Export MongoDB data to CSV using PyMongo

This Python script connects to a **MongoDB** collection and exports the results to a **CSV file**.  
It also includes errors (exception) and logging handling.

## Features

- Connects to MongoDB using `pymongo`
- Extracts only selected fields: `_id`, `Amount` and `Date`
- Exports results to a `.csv` file
- Includes error handling and logging (auditlog.log)

## Database structure example

```
db.transactions.insertMany([
    {
        "Date": ISODate("2024-06-20T12:10:00Z"),
        "Amount": 123.33,
        "txHash": "0x6e3a95a567595dbe3d179d8eb50b2b0a8ae4754c"
    },
    {
        "Date": ISODate("2024-06-30T12:10:00Z"),
        "Amount": 444.56,
        "txHash": "0x54cf5e20ffb32357c9fee4aaf41e5dd07abedeba"
    },
    {
        "Date": ISODate("2024-06-10T12:10:00Z"),
        "Amount": 12.12,
        "txHash": "0xebf9af135d1d0d3b1042efd9d2bbdc5199cf24ad"
    },
    {
        "Date": ISODate("2024-06-12T13:30:00Z"),
        "Amount": 88.35,
        "txHash": "0x5fe27a854b21ea64041e4dc38439c95282586c6b"
    },
    {
        "Date": ISODate("2024-06-13T14:40:00Z"),
        "Amount": 120.68,
        "txHash": "0xf174472936d4d7da3b6740a92812900164cbe9ae"
    },
    {
        "Date": ISODate("2024-06-14T15:50:00Z"),
        "Amount": 250.75,
        "txHash": "0x1d0b250229f1b6614f14e2a35b9d23035acd7a0a"
    }
]);
```

## Configuration

Inside the `extract_to_csv.py` file, change the following variables:
```
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "YOUR_DATABASE"
COLLECTION_NAME = "YOUR_COLLECTION"
```
If you want to the exported file to a different name, change the following line:
```
# From: 
export_to_csv(transactions)
# To:
export_to_csv(transactions, "your_filename.csv")
```

## Requirements

Install the dependencies using pip:

```bash
pip install pymongo pandas
