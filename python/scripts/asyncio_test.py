import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'https://www.baidu.com',
        'https://www.sina.com',
        'https://cn.bing.com',
    ]
    start_time = time.perf_counter()

    asyncio.run(download_all(sites))

    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()


# import asyncio
# from asyncio.tasks import gather
#
#
# async def say():
#     print("在吗?")
#     await asyncio.sleep(2)
#     await say_in_heart("-----2秒后")
#     print("人呢？")
#
#
# async def say_in_heart(strs="------即时响应"):
#     print("心里：不会是放我鸽子了吧"+strs)
#
#
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(gather(say()))
