import os
import csv
import urllib.request


def write_to_file(data):
    try:
        with open('collection.csv', 'wb') as collection:
            collection.write(data)
    except Exception as e:
        raise e

def download_iris_collection():
    with urllib.request.urlopen('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv') as conn:
        write_to_file(conn.read())

def data_file_does_not_exist():
    return not os.path.exists('collection.csv')

def get_one_from_collection():
    with open("collection.csv") as csvfile:
        for row in csv.DictReader(csvfile):
            yield row