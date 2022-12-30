label act2_Gal_meet4:
    "Вы входите в кабинет Галины Петровны, и застаете ее плачущей за своим столом"
    scene GalBG
    show MCIdle at left
    show GalSad:
        xalign 1.0
        xzoom -1.0
    menu:
        "Поздороваться":
            mainChar "Добрый день, а... боже мой, что случилось?"
        "Поинтересоваться":
            mainChar "Здравствуйте, а... э-эм, чего ревете?"
        "Уйти":
            $GalAtt -= 2
            "Вы решаете просто уйти"
            hide GalSad
            hide MCIdle
            scene bg_bbg
