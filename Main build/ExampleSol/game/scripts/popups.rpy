init python:
    def play_pop_up_sound(trans, st, at):
        if store.pop_up_general_sound:
            renpy.play("audio/sounds/" + store.pop_up_general_sound)
        return None

screen pop_up_general(text_to_display, sound=None, appear_time=1.75, yalign=add_relationship_boldness_points_yalign):
    $ store.pop_up_general_sound = sound
    $ store.pop_up_general_appear_time = appear_time
    $ store.pop_up_general_total_time = appear_time + popup_delay + popup_fadein_time + popup_fadeout_time
    text text_to_display at popup_relatonship_appear(yalign = yalign)
    timer store.pop_up_general_total_time action Hide('pop_up_general')


transform popup_relatonship_appear(yalign=add_relationship_boldness_points_yalign):
    xalign 0.5
    yalign yalign
    on show:
        alpha 0.0
        linear popup_fadein_time alpha 1.0
        pause popup_delay
        function play_pop_up_sound
    on hide:

        linear popup_fadeout_time alpha 0.0