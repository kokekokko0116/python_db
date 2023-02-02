import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

connection_config ={
  'user': 'postgre',
  'password': '0116',
  'host': 'localhost',
  'port': '5432',
  'database': 'postgress'
}

def VioletScraping():
  res = requests.get("https://yuyu-tei.jp/game_poc/buy/buy_price.php?ver=sv01v")
  soup = BeautifulSoup(res.content, "html.parser")
  # print(soup)
  # name = soup.find("p", class_="name").get_text()
  name = soup.find_all(class_="name").get_text()
  print(name)


VioletScraping()