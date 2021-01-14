import asyncio

strq = 'global Done'

try:
    def decor(func):
        def new_func(*args):
            print('Start')
            print(func.__name__)
            result = func(*args)
            print('Faster')
            return result
        return new_func


    @decor
    async def good():
        global strq
        print(strq)
        strq = 'new Done'
        return print(strq)


    asyncio.run(good())
except Exception as ex:
    print(ex.__doc__ + ' oops')
