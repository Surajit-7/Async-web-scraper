from bs4 import BeautifulSoup as bs
import requests as req
from typing import List

def collect_urls(url:str, base_url:str)-> List:
    response = req.get(url=url)
    
    soup = bs(response.text, "html.parser")
    a_tag_list = soup.find_all(name="a", attrs={"href":True})

    url_manager = [tag["href"] for tag in a_tag_list if (tag.has_attr("href"))]
    gibrish_data = [wasted_link for wasted_link in url_manager if ("http") not in wasted_link]

    
    gibrish_turned_data = []
    for link in gibrish_data:
        if '/' == link[0]:
            gibrish_turned_data.append(base_url+link)

    url_manager = [link for link in url_manager if ("http") in link]

    url_manager = url_manager + gibrish_turned_data

    indexed_url_manager = {}
    for idx,urls in enumerate(url_manager):
        indexed_url_manager[idx] = urls
    return indexed_url_manager
    






