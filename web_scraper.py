import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from bs4 import BeautifulSoup
import requests
import re
from flask import Flask, request, jsonify

def get_data():

    """
        Refactored code for extracting the data from ncdc website in a dictionary format (key-value pair)
    """
    PAGE_URL = "https://covid19.ncdc.gov.ng/"
    
    # Response Data
    response_data = requests.get(PAGE_URL).text

    # Initializing the BeautifulSoup package and the specifying the parser
    soup = BeautifulSoup(response_data, 'lxml')
    content_table = soup.find("table", id="custom1")

    # Extracting the Table header names 
    table_headers = content_table.thead.findAll("tr")
    for k in range(len(table_headers)):
        data = table_headers[k].find_all("th")
        column_names = [j.string.strip() for j in data]

    # Extracting the data in the Table's body (values)
    table_data = content_table.tbody.findAll('tr')
    values = []
    keys = []
    data_dict = {}
    for k in range(len(table_data)):
        key = table_data[k].find_all("td")[0].string.strip()
        value = [j.string.strip() for j in table_data[k].find_all("td")]
        keys.append(key)
        values.append(value)
        data_dict[key] = value
    
    return data_dict
    


print(get_data())

