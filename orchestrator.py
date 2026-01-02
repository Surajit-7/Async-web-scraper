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

url = "https://www.ibm.com/quantum/qiskit"
base_url = "https://www.ibm.com"

list_from_url_manager = (collect_urls(url=url, base_url=base_url))

limiter = 3

print(asyncio.run(orchestrator(url_list=list_from_url_manager, semaphore=limiter)))


"""output

fetching started for url id:0
fetching started for url id:1
fetching started for url id:2
fetching completed for url id: 0
fetching started for url id:3
fetching completed for url id: 2
fetching started for url id:4
fetching completed for url id: 1
fetching started for url id:5
fetching completed for url id: 3
fetching started for url id:6
fetching completed for url id: 5
fetching started for url id:7
fetching completed for url id: 4
fetching started for url id:8
fetching completed for url id: 6
fetching started for url id:9
fetching completed for url id: 8
fetching started for url id:10
fetching completed for url id: 7
fetching started for url id:11
fetching completed for url id: 9
fetching started for url id:12
fetching completed for url id: 10
fetching started for url id:13
fetching completed for url id: 11
fetching started for url id:14
fetching completed for url id: 12
fetching started for url id:15
fetching completed for url id: 13
fetching started for url id:16
fetching completed for url id: 14
fetching started for url id:17
fetching completed for url id: 15
fetching started for url id:18
fetching completed for url id: 16
fetching started for url id:19
fetching completed for url id: 17
fetching started for url id:20
fetching completed for url id: 18
fetching started for url id:21
fetching completed for url id: 19
fetching started for url id:22
fetching completed for url id: 20
fetching started for url id:23
fetching completed for url id: 22
fetching started for url id:24
fetching completed for url id: 21
fetching started for url id:25
fetching completed for url id: 23
fetching started for url id:26
fetching completed for url id: 26
fetching started for url id:27
fetching completed for url id: 25
fetching started for url id:28
fetching completed for url id: 24
fetching started for url id:29
fetching completed for url id: 28
fetching started for url id:30
fetching completed for url id: 27
fetching started for url id:31
fetching completed for url id: 29
fetching started for url id:32
fetching completed for url id: 30
fetching started for url id:33
fetching completed for url id: 32
fetching started for url id:34
fetching completed for url id: 31
fetching started for url id:35
fetching completed for url id: 34
fetching completed for url id: 33
fetching started for url id:36
fetching started for url id:37
fetching completed for url id: 35
fetching started for url id:38
fetching completed for url id: 36
fetching started for url id:39
fetching completed for url id: 37
fetching started for url id:40
fetching completed for url id: 38
fetching started for url id:41
fetching completed for url id: 39
fetching started for url id:42
fetching completed for url id: 40
fetching started for url id:43
fetching completed for url id: 41
fetching started for url id:44
fetching completed for url id: 42
fetching started for url id:45
fetching completed for url id: 43
fetching started for url id:46
fetching completed for url id: 44
fetching started for url id:47
fetching completed for url id: 45
fetching started for url id:48
fetching completed for url id: 46
fetching started for url id:49
fetching completed for url id: 47
fetching started for url id:50
fetching completed for url id: 48
fetching started for url id:51
fetching completed for url id: 49
fetching started for url id:52
fetching completed for url id: 50
fetching started for url id:53
fetching completed for url id: 51
fetching started for url id:54
fetching completed for url id: 52
fetching started for url id:55
fetching completed for url id: 53
fetching started for url id:56
fetching completed for url id: 54
fetching started for url id:57
fetching completed for url id: 55
fetching started for url id:58
fetching completed for url id: 56
fetching started for url id:59
fetching completed for url id: 57
fetching started for url id:60
fetching completed for url id: 58
fetching started for url id:61
fetching completed for url id: 59
fetching started for url id:62
fetching completed for url id: 60
fetching started for url id:63
fetching completed for url id: 61
fetching started for url id:64
fetching completed for url id: 62
fetching completed for url id: 63
fetching completed for url id: 64
['status code for url id:0 -> 303', 'status code for url id:1 -> 308', 'status code for url id:2 -> 307', 'status code for url id:3 -> 200', 'status code for url id:4 -> 200', 'status code for url id:5 -> 307', 'status code for url id:6 -> 200', 'status code for url id:7 -> 200', 'status code for url id:8 -> 307', 'status code for url id:9 -> 200', 'status code for url id:10 -> 200', 'status code for url id:11 -> 200', 'status code for url id:12 -> 200', 'status code for url id:13 -> 200', 'status code for url id:14 -> 307', 'status code for url id:15 -> 307', 'status code for url id:16 -> 200', 'status code for url id:17 -> 307', 'status code for url id:18 -> 307', 'status code for url id:19 -> 307', 'status code for url id:20 -> 200', 'status code for url id:21 -> 200', 'status code for url id:22 -> 200', 'status code for url id:23 -> 307', 'status code for url id:24 -> 200', 'status code for url id:25 -> 200', 'status code for url id:26 -> 200', 'status code for url id:27 -> 200', 'status code for url id:28 -> 308', 'status code for url id:29 -> 307', 'status code for url id:30 -> 200', 'status code for url id:31 -> 200', 'status code for url id:32 -> 302', 'status code for url id:33 -> 302', 'status code for url id:34 -> 301', 'status code for url id:35 -> 200', 'status code for url id:36 -> 301', 'status code for url id:37 -> 200', 'status code for url id:38 -> 200', 'status code for url id:39 -> 200', 'status code for url id:40 -> 200', 'status code for url id:41 -> 200', 'status code for url id:42 -> 200', 'status code for url id:43 -> 200', 'status code for url id:44 -> 200', 'status code for url id:45 -> 200', 'status code for url id:46 -> 200', 'status code for url id:47 -> 200', 'status code for url id:48 -> 200', 'status code for url id:49 -> 200', 'status code for url id:50 -> 200', 'status code for url id:51 -> 200', 'status code for url id:52 -> 200', 'status code for url id:53 -> 200', 'status code for url id:54 -> 200', 'status code for url id:55 -> 200', 'status code for url id:56 -> 200', 'status code for url id:57 -> 200', 'status code for url id:58 -> 200', 'status code for url id:59 -> 200', 'status code for url id:60 -> 200', 'status code for url id:61 -> 200', 'status code for url id:62 -> 200', 'status code for url id:63 -> 200', 'status code for url id:64 -> 200']"""