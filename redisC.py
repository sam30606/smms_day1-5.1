import redis
import time
from natsort import natsorted


def main():
    r = redis.Redis(host="localhost", port=6379, username="sam", password="0000", db=0, decode_responses=True)
    r.flushall()
    print(r.keys())
    qty = 200
    redisInfo = r.info()
    policy = redisInfo["maxmemory_policy"]
    usedMemory = redisInfo["used_memory"]
    maxMemory = redisInfo["maxmemory"]
    print(f"{policy=} {maxMemory=} {usedMemory=}")
    try:
        for key in range(qty):
            redisInfo = r.info()
            usedMemory = redisInfo["used_memory"]
            r.set(key, key, ex=100)
            size = r.memory_usage(key)
            print(f"{usedMemory=} {key=} {size=}")
    except Exception as err:
        print(err)

    for e in range(200):
        for i in range(50):
            r.get(i)
    print("\n Readed\n")
    try:
        for key in range(qty, qty + 50):
            redisInfo = r.info()
            usedMemory = redisInfo["used_memory"]
            r.set(key, key)
            finalKey = key
            print(f"{usedMemory=} {key=} {size=}")
    except Exception as err:
        print(err)

    redisInfo = r.info()
    usedMemory = redisInfo["used_memory"]
    keys = natsorted(r.keys())
    loss = []

    for i in range(finalKey):
        if str(i) not in keys:
            loss.append(str(i))
    print(f"{usedMemory=}")
    print(f"{keys=}")
    print(f"{loss=} {len(loss)}")


main()
