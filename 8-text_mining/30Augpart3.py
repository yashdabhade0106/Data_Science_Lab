# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:35:24 2024

@author: yashd
"""

import bs4
from bs4 import BeautifulSoup as bs 
import requests
link = "https://www.amazon.in/Zebronics-Zeb-Jaguar-Wireless-Precision-Ambidextrous/dp/B098JYT4SY/?_encoding=UTF8&pd_rd_w=qPM3Y&content-id=amzn1.sym.211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_p=211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_r=54D6NJESB07KAXTHX78Z&pd_rd_wg=As2nO&pd_rd_r=d2c0e944-ea05-4522-83c3-9c59c3e4bc94&ref_=pd_hp_d_btf_crs_zg_bs_976392031&th=1"
page = requests.get(link)
page



