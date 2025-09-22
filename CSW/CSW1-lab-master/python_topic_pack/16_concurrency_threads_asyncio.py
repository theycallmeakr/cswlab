"""
Topic 16 — Concurrency: threads vs asyncio (tiny taste)
"""

import time, threading, asyncio

def work(i):
    time.sleep(0.2)
    print(f"thread {i} done")

threads = [threading.Thread(target=work, args=(i,)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()

async def async_work(i):
    await asyncio.sleep(0.2)
    print(f"task {i} done")

async def main():
    await asyncio.gather(*(async_work(i) for i in range(3)))

if __name__ == "__main__":
    asyncio.run(main())
