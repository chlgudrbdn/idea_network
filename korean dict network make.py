# from selenium import webdriver
import time
import pandas as pd
from urllib.parse import urljoin
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import pickle

# from timedelta import datetime

start_time = datetime.now()
print("start_time : ", start_time)


class Agent:
    def __init__(self, headword, description, part_of_speech):
        self.headword = headword  # 표제어
        self.description = description  # 뜻풀이
        self.part_of_speech = part_of_speech  # 품사
        self.edge_to_method = []
        self.edge_to_method_threshold = 0.0
        uniform_prob = 1 / len(self.edge_to_method)
        self.edge_to_method_weight = [uniform_prob] * len(self.edge_to_method)

        self.edge_to_attribute = []
        self.edge_to_attribute_threshold = 0.0
        uniform_prob = 1 / len(self.edge_to_attribute)
        self.edge_to_attribute_weight = [uniform_prob] * len(self.edge_to_attribute)

    def initial_weighting(self):
        uniform_prob = 1/len(self.edge_to_method)
        self.edge_to_method_weight = [uniform_prob] * len(self.edge_to_method)

        uniform_prob = 1/len(self.edge_to_attribute)
        self.edge_to_attribute_weight = [uniform_prob] * len(self.edge_to_attribute)


def make_dictionary(headwords, descriptions):
    dict = {}
    for i in len(headwords):
        dict[headwords[i]] = descriptions[i]
    return dict


file_name = 'fullversion.xlsx'
tmp_df = pd.read_excel(file_name)
as_list = tmp_df['표제어'].tolist()

# dictionary = make_dictionary(tmp_df['표제어'].tolist(), tmp_df['뜻풀이'].tolist())



print("take time : {}".format(datetime.now() - start_time))
