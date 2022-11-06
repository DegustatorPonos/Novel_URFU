init python:
    config.keymap['button_select'].append('K_SPACE')
    config.keymap['focus_up'].append(['w', 'W'])
    config.keymap['focus_left'].append(['a', 'A'])
    config.keymap['focus_down'].append(['s', 'S'])
    config.keymap['focus_right'].append(['d', 'D'])
    config.keymap['screenshot'] = ['K_PRINT']
    config.keymap['rollback'].append(['q', 'Q'])
    config.keymap['rollforward'].append(['e', 'E'])
    config.keymap['toggle_fullscreen'] = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ]
    config.keymap['self_voicing'] = []