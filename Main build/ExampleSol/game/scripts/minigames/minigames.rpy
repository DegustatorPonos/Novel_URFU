init python:



    def countdown(st, at):
        length = store.countdown_length
        time_passed_ratio = st/length
        red_text_color = "#f00" if store.countdown_red_text else "#fff"
        
        remaining = length - st
        store.countdown_remaining = remaining
        
        store.countdown_elapsed = length - remaining
        
        remaining_adjusted = remaining + store.countdown_addend
        
        if store.countdown_show_decimal:
            text = "%.1f" % remaining_adjusted
        else:
            text = str(int(remaining_adjusted))
        
        if time_passed_ratio < 0.5:
            return Text(text, color="#fff", size=72, outlines = [(2, "#000000", 0, 0)]), .1
        elif remaining > 0.0:
            return Text(text, color = red_text_color, size=72, outlines = [(2, "#000000", 0, 0)]), .1
        else:
            return renpy.display.anim.Blink(Text("0.0", color = red_text_color, size=72, outlines = [(2, "#000000", 0, 0)])), None

    def stopwatch(st, at):
        if not stopwatch_stop:
            return Text("%.1f" % st, color="#fff", size=72, outlines = [(2, "#000000", 0, 0)]), .1
        elif not store.stopwatch_stop_time:
            store.stopwatch_stop_time = st
        
        if store.stopwatch_stop_time:
            return Text("%.1f" % store.stopwatch_stop_time, color="#fff", size=72, outlines = [(2, "#000000", 0, 0)]), .1

init:
    image countdown = DynamicDisplayable(countdown)
    image stopwatch = DynamicDisplayable(stopwatch)

screen hard_block_screen:
    null width 0 height 0

screen keymaps:
    key "a" action Return("a")
    key "A" action Return("a")

    key "b" action Return("b")
    key "B" action Return("b")

    key "c" action Return("c")
    key "C" action Return("c")

    key "d" action Return("d")
    key "D" action Return("d")

    key "e" action Return("e")
    key "E" action Return("e")

    key "f" action Return("f")
    key "F" action Return("f")

    key "g" action Return("g")
    key "G" action Return("g")

    key "h" action Return("h")
    key "H" action Return("h")

    key "i" action Return("i")
    key "I" action Return("i")

    key "j" action Return("j")
    key "J" action Return("j")

    key "k" action Return("k")
    key "K" action Return("k")

    key "l" action Return("l")
    key "L" action Return("l")

    key "m" action Return("m")
    key "M" action Return("m")

    key "n" action Return("n")
    key "N" action Return("n")

    key "o" action Return("o")
    key "O" action Return("o")

    key "p" action Return("p")
    key "P" action Return("p")

    key "q" action Return("q")
    key "Q" action Return("q")

    key "r" action Return("r")
    key "R" action Return("r")

    key "s" action Return("s")
    key "S" action Return("s")

    key "t" action Return("t")
    key "T" action Return("t")

    key "u" action Return("u")
    key "U" action Return("u")

    key "v" action Return("v")
    key "V" action Return("v")

    key "w" action Return("w")
    key "W" action Return("w")

    key "x" action Return("x")
    key "X" action Return("x")

    key "y" action Return("y")
    key "Y" action Return("y")

    key "z" action Return("z")
    key "Z" action Return("z")

label minigame_stopwatch_start(xalign=.99, yalign=.01):
    python:
        stopwatch_stop = False
        stopwatch_stop_time = None

    show stopwatch at Position(xalign = xalign, yalign = yalign)

    return

label minigame_stopwatch_stop:
    python:
        stopwatch_stop = True

    return

label minigame_countdown(duration, end_label, xalign=.99, yalign=.01, show_decimal=True, call_instead_of_show=False, addend=0, red_text=True):
    python:
        countdown_length = duration
        countdown_show_decimal = show_decimal
        countdown_addend = addend
        countdown_red_text = red_text

    show countdown at Position(xalign = xalign, yalign = yalign)

    if call_instead_of_show:
        call screen minigame_countdown(duration, end_label)
    else:
        show screen minigame_countdown(duration, end_label)
    return

label hide_minigame_countdown:
    hide countdown
    hide screen minigame_countdown

    return

label process_end_of_minigame(minigame_name):
    hide screen pop_up_general
    $ minigames_done += 1
    $ minigames_tried.add(minigame_name)

    if is_school_time:
        jump school_leave

    if started_main_game:
        call day_advance_time
        return

    call debug_menu

    return

screen minigame_countdown(duration, end_label):
    timer duration action Jump(end_label)