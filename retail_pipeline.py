import pandas as pd
import numpy as np
import logging 

# Set up the logger 
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler
file_handler = logging.FileHandler('data_log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


# Instantiate the logger object
logger = logging.getLogger()

# Add the file handler to the logger
logger.addHandler(file_handler)

# Add the console handler to the logger
logger.addHandler(console_handler)


#EXTRACT
logger.info("Extracting data from flat file")
#function to read data
def extract_data(path=''):
    #check file extension if ends with xlsx
    if path.endswith('.xlsx'):
        df = pd.read_excel(path)
    #check file extension if ends with CSV
    elif path.endswith('.csv'):
        df = pd.read_csv(path, encoding='ISO-8859-1')

    return df

logger.info("Data successfully Extracted")
#TRANSFORM


logger.info("Transforming flat file")
#data processing layer
def data_processing(df):
    #delete unwanted rows
    df = df[['Order Channel','Quantity','Unit Price','Customer Type','Category Group','shippingStatus', 'Category','Delivery Date']]
#convert delivery date to datetime
    df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])

#remove comma from unit price then multiply with quantity
    df['Unit Price'] = df['Unit Price'].str.replace(',','')
#convert unit price to numeric
    df['Unit Price'] = df['Unit Price'].astype(float)
#replace missing dates
    df = df.replace(np.nan, 12/17/20)

    return df
logger.info("Transformation Successful")


logger.info("Loading transformed file")
#export/load data
def load_file(df):
    print('creating csv file..')
    df.to_csv(path_or_buf=f'extractedData/clean_data_2.csv', index=False)

logger.info("Loaded file Successfully")
#Load data to Data Warehouse or S3 bucket
"""Insert some code here"""

if __name__ =="__main__":
#load data
    df = extract_data('raw.xlsx')
#data processing layer
    df = data_processing(df)

#load file
    df = load_file(df)

