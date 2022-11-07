# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
#define e = Character('Эйлин', color="#c8ffc8")


define testVar = 0
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#В лейбле start будет что-то типа __init__
define NameSpace = "" #ToChange
define mainChar = Character("[NameSpace]", color = "#402b2b")
define polly = Character("Полина", color = "#ab274f")
define unknown = Character("Голос", color="#c9c9c9")
image bg_bbg = "blackbackground.png"

# Игра начинается здесь:
label start:

    scene bg_bbg
    $NameSpace = renpy.input("Введите имя главного героя (По умолчанию 'Николай')").strip()
    if NameSpace == "":
        $NameSpace= "Николай"
    #mainChar "TestSpeech"
    
    jump act1part1


