#В этом скрипте будет что-то типа __init__
define politeness = 5

define DefaultName = "Николай"
define NameSpace = ""
define mainChar = Character("[NameSpace]", color = "#402b2b")
image MCIdle = "MainCharIdlePlaceholder.png"
image MCSad = "MainCharSadPlaceholder.png"
image MCAngry = "MainCharAngryPlaceholder.png"
image MCBloody = "MainCharSadBloodyPlaceholder.png"

define polly = Character("Полина", color = "#ab274f")
image pollyIdle = "PollyIdlePlaceholder.png"
image pollyAngry = "PollyAngryPlaceholder.png"

#Непривязанный к персонажам контент
define unknown = Character("Голос", color="#c9c9c9")
image bg_bbg = "blackbackground.png"
image bg_bedroom = "spal`nya ready(defolt)(1).png"
image bg_kitchen = "kuhnya_melvill.webp"
image bg_pollysroom = "spal`nya ready(defolt).png"
image bg_toilet_clean = "ToiletPlaceholder.jpg"
image bg_toilet_bloody = "ToiletPlaceholder.jpg"
image blink = "Blink.png"
# Технический лейбл, перетекает в act1part1
label start:

    scene bg_bbg
    $NameSpace = renpy.input("Введите имя главного героя (По умолчанию '[DefaultName]')").strip()
    if len(NameSpace) < 1:
        $NameSpace = DefaultName
    
    jump act1part1