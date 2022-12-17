#В этом скрипте будет что-то типа __init__  
define boolBreak = False

define NSFWfilter = 0
define politeness = 5
define calledTasks = 0 #All tasks player faced
define CompletedTasks = 0 #All tasks player has done correctly


define audio.bassyBGM = "audio/music/BGbass.mp3"

define DefaultName = "Николай"
define NameSpace = ""
define mainChar = Character("[NameSpace]", color = "#402b2b")
image MCIdle = "MainCharIdlePlaceholder.png" #PH
image MCSad = "MainCharSadPlaceholder.png" #PH
image MCAngry = "MainCharAngryPlaceholder.png" #PH
image MCBloody = "MainCharSadBloodyPlaceholder.png" #PH

#Объявление персонажей

define polly = Character("Полина", color = "#ab274f")
image pollyIdle = "PollyIdle.png"
image pollyAngry = "PollyAngryPlaceholder.png" #PH

define EV = Character("Евгений Викторович", color = "#00ff9d")
define EVatt = 0

define Alex = Character("Александр", color = "#23019e")
define AlexAtt = 0

define Semen = Character("Семён", color = "#ff9900")
define SAtt = 0

define Galina = Character("Галина", color = "#81008d")
define GalAtt = 0

define Gennadiy = Character("Геннадий", color = "#ff0000")
define GenAtt = 0

define AttitudeVar = {'common':politeness, 'EV':EVatt, 'Alex':AlexAtt, 'Semen':SAtt, 'Galina':GalAtt, 'Gennadiy':GenAtt}
define tasksPointer = {'undone':calledTasks, 'done':CompletedTasks}

#Непривязанный к персонажам контент
define unknown = Character("Голос", color="#c9c9c9")
image bg_bbg = "blackbackground.png"
image bg_bedroom = "spal`nya ready(defolt)(1).png"
image bg_kitchen = "kitchen.png"
image bg_pollysroom = "bedroom polini 1.png"
image bg_toilet_clean = "ToiletPlaceholder.jpg" #PH
image bg_toilet_bloody = "ToiletPlaceholder.jpg" #PH
image blink = "Blink.png"


# Технический лейбл, перетекает в act1part1
label start:
    call generate_GrumblingArray
    call generate_Math_equations
    scene bg_bbg


    $NameSpace = renpy.input("Введите имя главного героя (По умолчанию '[DefaultName]')").strip()
    "В процессе игры могут присутствовать сцены насилия и жестокости. Вы готовы их видеть?"
    menu:
        "Да":
            $NSFWfilter = 0
        "Нет":
            $NSFWfilter = 1
    if len(NameSpace) < 1:
        $NameSpace = DefaultName

    jump act1part1


init python:
    import random, this

    boolBreak = False

    def SayWGrumbling(content, ammount):
        for i in range(ammount):
            EV(GrumblingArray[renpy.random.randint(0, len(GrumblingArray) - 1)])
        EV(content)

    def AttUpdate(character, ammount):
        AttitudeVar['common'] += ammount
        AttitudeVar[character] += ammount


        





