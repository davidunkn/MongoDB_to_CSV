import logging
from dataclasses import dataclass
from datetime import datetime
from pymongo import MongoClient
import pandas as pd
import sys

# Class model with constructor
# Following https://docs.python.org/3/library/dataclasses.html examples
@dataclass
class Transaction:
    _id: str
    Amount: float
    Date: datetime

# MongoDB connection handler & data fetching
def fetch_transactions(uri: str, db_name: str, collection_name: str):
    """Connect to MongoDB and fetch transactions."""
    try:
        logging.info("Connecting to the database...")
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]
        logging.info("Connection established successfully.")

        # Fetch only required fields (_id, Amount, Date and txHash)
        fetchResult = collection.find({}, {"_id": 1, "Amount": 1, "Date": 1})
        transactions = []

        for item in fetchResult:
            try:
                #Instantiate a Transaction class object
                transaction = Transaction(_id=str(item.get("_id")), Amount=float(item.get("Amount", 0)), Date=pd.to_datetime(item.get("Date"))))
                # Append it to the array
                transactions.append(transaction)
            except Exception as e:
                logging.warning(f"Error parsing item {item.get('_id')}: {e}")

        logging.info(f"Fetched {len(transactions)} transactions from the database.")
        return transactions

    except Exception as e:
        logging.error(f"Failed to fetch transactions: {e}")
        return []

# Convert to DataFrame & Export
def export_to_csv(transactions, filename="transactions.csv"):
    """Convert list of Transaction objects to CSV."""
    try:
        df = pd.DataFrame([t.__dict__ for t in transactions])
        df.to_csv(filename, index=False)
        logging.info(f"Exported {len(df)} records to {filename}.")
    except Exception as e:
        logging.error(f"Error exporting data to CSV: {e}")

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("auditlog.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

# Main Execution
if __name__ == "__main__":
    # Replace with your actual MongoDB connection details
    MONGO_URI = "mongodb://localhost:27017"
    DB_NAME = "YOUR_DATABASE"
    COLLECTION_NAME = "YOUR_COLLECTION"

    transactions = fetch_transactions(MONGO_URI, DB_NAME, COLLECTION_NAME)

    if transactions:
        export_to_csv(transactions)
    else:
        logging.warning("No transactions found to export.")
