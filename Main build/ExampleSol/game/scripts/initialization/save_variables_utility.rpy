init python:

    def label_callback(label_name, jump_call_or_context):
        initialize_variables(False)
        
        return

    def disable_saving():
        store.disable_saves = True
        store._game_menu_screen = 'preferences'
        return

    def enable_saving():
        store.disable_saves = False
        store._game_menu_screen = "save"
        return

    class Save_Variable(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    def initialize_variables_utility(array, force_reinitialization = False):
        for variable_obj in array:
            variable_name = variable_obj.name
            
            try:
                eval(variable_name)
            except NameError:
                exec("store." + variable_name + " = " + variable_obj.value)
            else:
                if force_reinitialization:
                    exec("store." + variable_name + " = " + variable_obj.value)
        
        return

    config.label_callback = label_callback

label initialize_variables(force_reinitialization=False):

    $ initialize_variables(force_reinitialization = force_reinitialization)

    return