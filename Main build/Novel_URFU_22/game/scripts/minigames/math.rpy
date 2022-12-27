init python:

    import asyncio #просто оставлю, может как памятник полуторанедельным страданиям.
    import datetime
    import random


    
    async def timer(secs, statusBool):
        import time
        await asyncio.sleep(secs)
        statusBool = True

    def TypingMG(arrayToParse):
        globalDeadlineTime = (datetime.datetime.now() + datetime.timedelta(minutes=2)).time()
        while datetime.datetime.now().time() < deadlineTime:
            local deadlineTime = (datetime.datetime.now() + datetime.timedelta(minutes=2)).time()
            


    def InputMG(arrayToParse):
        deadlineTime = (datetime.datetime.now() + datetime.timedelta(minutes=2)).time()
        while datetime.datetime.now().time() < deadlineTime:
            tasksPointer['undone'] += 1
            actual_question = renpy.random.choice(arrayToParse)
            if renpy.input(actual_question[0]).strip() == actual_question[1]:
                tasksPointer['done'] += 1
        
label DoMathMG:
    "Вы садитесь за рабоче место."
    "Вам предстоит провести небольшой математический анализ."
    $InputMG(Math_equations)

label DoBinarMG:
    "Вы садитесь за рабоче место."
    "Вам предстоит разобраться с системами исчисления в файлах."
    $InputMG(Different_systems)

