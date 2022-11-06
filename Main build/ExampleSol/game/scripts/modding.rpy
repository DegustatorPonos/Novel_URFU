init python:
    def custom_music_files(type):
        custom_files = []
        
        files = renpy.list_files()
        files = [string for string in files if "custom_music/" + type + "/" in string and ".ogg" in string]
        
        return files