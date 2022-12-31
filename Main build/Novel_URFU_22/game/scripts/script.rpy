#В этом скрипте будет что-то типа __init__  
define boolBreak = False

define NSFWfilter = 0
define politeness = 5 #Unused in the release version but the game crashes if we delete it =D
define calledTasks = 0 #All tasks player faced
define CompletedTasks = 0 #All tasks player has done correctly


define audio.bassyBGM = "audio/music/BGbass.mp3"

define DefaultName = "Николай"
define NameSpace = ""

#Объявление персонажей

define mainChar = Character("[NameSpace]", color = "#402b2b")
image MCIdle = "Characters/MC/MCIdle.png" 
image MCSad = "Characters/MC/MCLaughter.png" 
image MCAngry = "Characters/MC/MCAngry.png" 
image MCScream = "Characters/MC/MCScream.png" 
#image MCBloody = "Characters/MC/MCIdle.png" 

define polly = Character("Полина", color = "#ab274f")
image pollyIdle = "Characters/Polly/PollyIdle.png"
image pollyAngry = "Characters/Polly/PollyAngry.png" 

define EV = Character("Евгений Викторович", color = "#00ff9d")
define EVatt = 0
image EVcalm = "Characters/Evgeniy/EVIdle.png"
image EVAngry = "Characters/Evgeniy/EVAngry.png"
image EVSad = "Characters/Evgeniy/EVSad.png"
image EVScream = "Characters/Evgeniy/EVScream.png"
image EVSmile = "Characters/Evgeniy/EVSmile.png"

define Alex = Character("Александр", color = "#23019e")
define AlexAtt = 0
image AlexIdle = "Characters/Alex/AlexIdle.png"
image AlexSmile = "Characters/Alex/AlexSmiling.png"
image AlexSad = "Characters/Alex/AlexSad.png"
image AlexScream = "Characters/Alex/AlexScream.png"

define Semen = Character("Семён", color = "#ff9900")
define SAtt = 0
image SemIdle = "Characters/Semen/SemIdle.png"
image SemSmile = "Characters/Semen/SemHappy.png"
image SemSad = "Characters/Semen/SemSad.png"
image SemScream = "Characters/Semen/SemAngry.png"

define Galina = Character("Галина", color = "#81008d")
define GalAtt = 0
image GalIdle = "Characters/Galina/GalIdle.png"
image GalSmile = "Characters/Galina/GalHappy.png"
image GalSad = "Characters/Galina/GalAngry.png"
image GalScream = "Characters/Galina/GalScream.png"

define Gennadiy = Character("Геннадий", color = "#ff0000")
define GenAtt = 0
image GenIdle = "Characters/Gennadiy/GenIdle.png"
image GenSmile = "Characters/Gennadiy/GenLaughter.png"
image GenSad = "Characters/Gennadiy/GenAngry.png"
image GenScream = "Characters/Gennadiy/GenScream.png"

#Объявление задников

image bg_bbg = "BGs/blackbackground.png"
image blink = "BGs/Blink.png"

image bg_bedroom = "BGs/spal`nya ready(defolt)(1).png"
image bg_kitchen = "BGs/kitchen.png"
image bg_pollysroom = "BGs/bedroom polini 1.png"
image bg_toilet_clean = "BGs/bathroom1.png" 
image bg_toilet_bloody = "BGs/bathroom(bloody).png" 

image EntryBG = "BGs/Entry.jpg"
image GalBG = "BGs/GalinaBG.jpg"
image GenBG = "BGs/GenBG.jpg"
image SemG = "BGs/Semen.jpg"
image EVBG = "BGs/Evgeniy Borisovi4.jpg"
image AlexBG = "BGs/Alexander Svincov(1).jpg"
image MC_BG = "BGs/MCBG.jpg"
image HallBG = "BGs/koridor.jpg"
image ClubBG = "BGs/nightclub.jpg"

define AttitudeVar = {'common':politeness, 'EV':EVatt, 'Alex':AlexAtt, 'Semen':SAtt, 'Galina':GalAtt, 'Gennadiy':GenAtt}
define tasksPointer = {'undone':calledTasks, 'done':CompletedTasks}

#Непривязанный к персонажам контент
define unknown = Character("Голос", color="#c9c9c9")



# Технический лейбл, перетекает в act1part1
label start:
    call generate_GrumblingArray
    call generate_Math_equations
    scene bg_bbg

    $GenAtt = -1.5
    call act2_Gen_meet3

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

    #def AttUpdate(character, ammount):
    #    AttitudeVar['common'] += ammount
    #    AttitudeVar[character] += ammount


        





