import logging
import pandas as pd

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("SUCCES")
    except FileNotFoundError:
        logging.error("ERROR")