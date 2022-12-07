init python:

    

    import asyncio

    async def timer(secs, statusBool):
        import time
        await asyncio.sleep(secs)
        statusBool = True
 

    def MathMG():
        isDone = False
        timerTask = asyncio.create_task(timer(10, isDone))
        asyncio.run(timerTask)
        while True:
            Gennadiy("123")
            if isDone:
                return
        

label tempLabel:
    $MathMG()
    "TempEnd"
