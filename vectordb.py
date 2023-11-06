import chromadb
import csv
import logging

client = chromadb.Client()

collection = client.create_collection("norton-symbols")

def symbols_to_docs(csv_file):
    """Initialize the in memory database"""
    docs = []

    with open(csv_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        store = set()
        for row in csv_reader:
            if row[0] == 'symbols':
                continue
            symbols = row[0].split(',')
            for symbol in symbols:
                store.add(symbol.strip().lower())

        for symbol in store:
            docs.append(symbol)

    logging.info(len(docs))
    return docs

output_docs = symbols_to_docs('assets/brain.csv')
ids = list(range(0, len(output_docs)))

collection.add(documents=output_docs, ids=[str(i) for i in ids])

results = collection.query(
    query_texts=["ice cream"],
    n_results=2,
)

print(results)