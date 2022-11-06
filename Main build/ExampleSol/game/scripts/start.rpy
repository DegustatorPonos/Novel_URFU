label start:
    $ config.rollback_enabled = True
    $ stop_music(fadeout=2)
    call initialize_variables (force_reinitialization=True)
    $ renpy.show_screen("fadeout_queued_music", _layer = 'scripts')
    if config.developer:
        call debug_menu
    else:
        call intro_0

    return