label act2_Gal_meet5:
    if !GalBlueRoot:
        call act2_Gal_meet5_Orange
        return

label act2_Gal_meet5_Orange:
    "Вы заходите в кабинет к Галине Петровне, и застаете ее болтающей по телефону."
    scene GalBG
    show MCIdle at left
    show GalSmile:
        xalign 1.0
        xzoom -1.0
    show MCIdle at left
    return