init python:
    def click_to_continue_animation(st, at):
        frame = int(st / .03)
        
        if frame >= 60:
            frame = 0
        
        return Image("ctc_" + str(frame) + ".png"), 0.03

init:
    image ctc:
        "images/animations/ctc/Animated Arrow0000.png"
        pause .03
        "images/animations/ctc/Animated Arrow0001.png"
        pause .03
        "images/animations/ctc/Animated Arrow0002.png"
        pause .03
        "images/animations/ctc/Animated Arrow0003.png"
        pause .03
        "images/animations/ctc/Animated Arrow0004.png"
        pause .03
        "images/animations/ctc/Animated Arrow0005.png"
        pause .03
        "images/animations/ctc/Animated Arrow0006.png"
        pause .03
        "images/animations/ctc/Animated Arrow0007.png"
        pause .03
        "images/animations/ctc/Animated Arrow0008.png"
        pause .03
        "images/animations/ctc/Animated Arrow0009.png"
        pause .03
        "images/animations/ctc/Animated Arrow0010.png"
        pause .03
        "images/animations/ctc/Animated Arrow0011.png"
        pause .03
        "images/animations/ctc/Animated Arrow0012.png"
        pause .03
        "images/animations/ctc/Animated Arrow0013.png"
        pause .03
        "images/animations/ctc/Animated Arrow0014.png"
        pause .03
        "images/animations/ctc/Animated Arrow0015.png"
        pause .03
        "images/animations/ctc/Animated Arrow0016.png"
        pause .03
        "images/animations/ctc/Animated Arrow0017.png"
        pause .03
        "images/animations/ctc/Animated Arrow0018.png"
        pause .03
        "images/animations/ctc/Animated Arrow0019.png"
        pause .03
        "images/animations/ctc/Animated Arrow0020.png"
        pause .03
        "images/animations/ctc/Animated Arrow0021.png"
        pause .03
        "images/animations/ctc/Animated Arrow0022.png"
        pause .03
        "images/animations/ctc/Animated Arrow0023.png"
        pause .03
        "images/animations/ctc/Animated Arrow0024.png"
        pause .03
        "images/animations/ctc/Animated Arrow0025.png"
        pause .03
        "images/animations/ctc/Animated Arrow0026.png"
        pause .03
        "images/animations/ctc/Animated Arrow0027.png"
        pause .03
        "images/animations/ctc/Animated Arrow0028.png"
        pause .03
        "images/animations/ctc/Animated Arrow0029.png"
        pause .03
        "images/animations/ctc/Animated Arrow0030.png"
        pause .03
        "images/animations/ctc/Animated Arrow0031.png"
        pause .03
        "images/animations/ctc/Animated Arrow0032.png"
        pause .03
        "images/animations/ctc/Animated Arrow0033.png"
        pause .03
        "images/animations/ctc/Animated Arrow0034.png"
        pause .03
        "images/animations/ctc/Animated Arrow0035.png"
        pause .03
        "images/animations/ctc/Animated Arrow0036.png"
        pause .03
        "images/animations/ctc/Animated Arrow0037.png"
        pause .03
        "images/animations/ctc/Animated Arrow0038.png"
        pause .03
        "images/animations/ctc/Animated Arrow0039.png"
        pause .03
        "images/animations/ctc/Animated Arrow0040.png"
        pause .03
        "images/animations/ctc/Animated Arrow0041.png"
        pause .03
        "images/animations/ctc/Animated Arrow0042.png"
        pause .03
        "images/animations/ctc/Animated Arrow0043.png"
        pause .03
        "images/animations/ctc/Animated Arrow0044.png"
        pause .03
        "images/animations/ctc/Animated Arrow0045.png"
        pause .03
        "images/animations/ctc/Animated Arrow0046.png"
        pause .03
        "images/animations/ctc/Animated Arrow0047.png"
        pause .03
        "images/animations/ctc/Animated Arrow0048.png"
        pause .03
        "images/animations/ctc/Animated Arrow0049.png"
        pause .03
        "images/animations/ctc/Animated Arrow0050.png"
        pause .03
        "images/animations/ctc/Animated Arrow0051.png"
        pause .03
        "images/animations/ctc/Animated Arrow0052.png"
        pause .03
        "images/animations/ctc/Animated Arrow0053.png"
        pause .03
        "images/animations/ctc/Animated Arrow0054.png"
        pause .03
        "images/animations/ctc/Animated Arrow0055.png"
        pause .03
        "images/animations/ctc/Animated Arrow0056.png"
        pause .03
        "images/animations/ctc/Animated Arrow0057.png"
        pause .03
        "images/animations/ctc/Animated Arrow0058.png"
        pause .03
        "images/animations/ctc/Animated Arrow0059.png"
        pause .03
        repeat

screen ctc:
    add "ctc" at ctc_appear


transform ctc_appear:
    xalign 0.75
    yalign .94

    alpha 0.0
    pause 2.0
    linear 0.5 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
