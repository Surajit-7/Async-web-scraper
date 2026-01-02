from typing import  Dict
# import requests_async
#what lib to use the fetch asyncronously -> httx.async_client mostly
import asyncio # this has semaphore function in-built
from url_manager import collect_urls
import httpx

## function for fectching with semaphore embedded

async def fetcher_with_sem(client, url_index,url, semaphore):
    async with semaphore:
        print(f"fetching started for url id:{url_index}")
        await asyncio.sleep(3)

        response = await client.get(url)
        print(f"fetching completed for url id: {url_index}")
        return(f'status code for url id:{url_index} -> {response.status_code}')
        

async def orchestrator(url_list:str, semaphore:int):
    limiter = asyncio.Semaphore(semaphore)
    async with httpx.AsyncClient() as client:
        tasks = [fetcher_with_sem(client=client,url_index=url, url=url_list[url],semaphore=limiter) for url in url_list]
        get_response = await asyncio.gather(*tasks) 
        """Key rule of asyncio.gather:
        gather returns results in the same order as the task list,
        not in completion order."""

        return get_response

url = ## paste the url of the webpage; for example-www.xyz.com/abc/def
base_url = ## paste the base url; for example- www.xyz.com

list_from_url_manager = (collect_urls(url=url, base_url=base_url))

limiter = 3

asyncio.run(orchestrator(url_list=list_from_url_manager, semaphore=limiter))

