import asyncio

def printFirst():
    print("First")

def printSecond():
    print("second")

def printThird():
    print("third")


class Foo:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.fc = False
        self.sc = False


    async def first(self, printFirst):
        await self.lock.acquire()
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.fc = True
        
        self.lock.release()


    async def second(self, printSecond):
        x = True
        while x:
            await self.lock.acquire()
            if self.fc:
                # printSecond() outputs "second". Do not change or remove this line.
                printSecond()
                self.sc = True
                x = False
            self.lock.release()


    async def third(self, printThird):
        x = True
        while x:
            await self.lock.acquire()
            if self.sc:
                # printThird() outputs "third". Do not change or remove this line.
                printThird()
                x = False
            self.lock.release()
        
async def main():
    s = Foo()
    await s.first(printFirst)
    await s.second(printSecond)
    await s.third(printThird)

asyncio.run(main())