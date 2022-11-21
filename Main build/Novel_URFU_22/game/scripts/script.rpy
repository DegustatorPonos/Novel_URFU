#В этом скрипте будет что-то типа __init__

define NSFWfilter = 0
define politeness = 5

define audio.bassyBGM = "audio/music/BGbass.mp3"

define DefaultName = "Николай"
define NameSpace = ""
define mainChar = Character("[NameSpace]", color = "#402b2b")
image MCIdle = "MainCharIdlePlaceholder.png" #PH
image MCSad = "MainCharSadPlaceholder.png" #PH
image MCAngry = "MainCharAngryPlaceholder.png" #PH
image MCBloody = "MainCharSadBloodyPlaceholder.png" #PH

define polly = Character("Полина", color = "#ab274f")
image pollyIdle = "PollyIdle.png"
image pollyAngry = "PollyAngryPlaceholder.png" #PH

define EV = Character("Евгений Викторович", color = "#262672")

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
    scene bg_bbg
    
    $TestF("test")
    #$EVsay("Test", 5)

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

label EVSpeech(toSay = "Error"):
    EV "[toSay]."

#define EVSpeechl = _EVSpeech

init python:
    import random

    
    def TestF(content):
        EV('Test')

    def EVsay(content, ammount):
        global EVSpeechl
        #renpy.call(EVSpeechl(content)) 
        #renpy.text start character
        #msg character "message"
        #text end
        for i in range(ammount):
            _EVSpeech(GrumblingArray[randrange(len(GrumblingArray))])




