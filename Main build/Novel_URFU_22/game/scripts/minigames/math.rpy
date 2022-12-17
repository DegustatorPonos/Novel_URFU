init python:

    import asyncio #просто оставлю, может как памятник полуторанедельным страданиям.
    import datetime
    import random


    
    async def timer(secs, statusBool):
        import time
        await asyncio.sleep(secs)
        statusBool = True


    def MathMG():
        deadlineTime = (datetime.datetime.now() + datetime.timedelta(seconds=10)).time()#datetime.timedelta(minutes=2, seconds=30)).time()
        while datetime.datetime.now().time() < deadlineTime:
            tasksPointer['undone'] += 1
            actual_question = renpy.random.choice(Math_equations)
            if renpy.input(actual_question[0]).strip() == actual_question[1]:
                tasksPointer['done'] += 1
        
        

label tempLabel:
    $MathMG()
