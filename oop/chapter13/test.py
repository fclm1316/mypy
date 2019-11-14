#encoding:utf-8
from time import sleep
from random import randint,random
import asyncio
all_potatos={x:randint(1,50) for x  in "abcd"}
print(all_potatos)
async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        else:
            potato = all_potatos.popitem()
            yield potato
            count += 1
            if count == num:
                break

async def buy_potatos():
    bucket = []
    async for p in take_potatos(20):
        bucket.append(p)
        print(bucket)

async def ask_for_potato():
    await asyncio.sleep(3)
    all_potatos.update({x:randint(1,20) for x  in "临兵斗者皆阵列在前"})

def main():
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([buy_potatos()])  )
    loop.close()
    print(all_potatos)

if __name__ == '__main__':
    main()