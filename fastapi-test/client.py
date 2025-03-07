import requests
import asyncio
import time

#get
#res = requests.get("http://127.0.0.1:8000")
#print(res.status_code)
#print(res.text)

#post
#res = requests.post("http://127.0.0.1:8000/items/",
#                    json={"name":"Tシャツ","price":200,"description":"白いシャツです"})

# async,await
async def sleep_time(sec):
    loop = asyncio.get_running_loop()
    res = await loop.run_in_executor(
        None, requests.get, f"http://127.0.0.1:8000/sleep_time/?sec={sec}"
    )
    return res.text


async def main():
    print(f"main開始 {time.strftime('%X')}")
    results = await asyncio.gather(sleep_time(1), sleep_time(2))
    print(results)
    print(f"main終了 {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())

