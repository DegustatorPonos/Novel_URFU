init python:
    if not getattr(persistent, 'disabled_music', False):
        persistent.disabled_music = set()

    def empty_queue_callback():
        if not music_queue_enabled:
            return
        
        if main_menu:
            return
        
        if renpy.music.is_playing():
            return
        
        if not getattr(store, 'music_is_queued', False):
            return
        
        if len(store.music_playlist) <= 0:
            if store.stats.current_location:
                store.stats.current_location.decide_and_play_daily_music_queue()
            else:
                home.decide_and_play_daily_music_queue()
        elif store.current_queued_music is None:
            pop_playlist()
        
        return

    renpy.music.set_queue_empty_callback(empty_queue_callback)

    def home_daytime_music_list():
        music_list = []
        music_list.append("audio/music/Daily_Music_03.ogg")
        music_list.append("audio/music/Groundwork.ogg")
        music_list.append("audio/music/Wallpaper.ogg")
        music_list.append("audio/music/Take it Easy 01.ogg")
        music_list.append("audio/music/Lighter 01.ogg")
        music_list.append("audio/music/Lighter 02.ogg")
        
        
        music_list.extend(custom_music_files("home/daytime"))
        
        return music_list

    def home_evening_music_list():
        music_list = []
        music_list.append("audio/music/Daily_Music_01.ogg")
        music_list.append("audio/music/Daily_Music_02.ogg")
        music_list.append("audio/music/Smooth 01.ogg")
        
        music_list.append("audio/music/Beatz 01.ogg")
        music_list.append("audio/music/Beatz 02.ogg")
        music_list.append("audio/music/Beatz 03.ogg")
        
        music_list.extend(custom_music_files("home/evening"))
        
        return music_list

    def outside_daytime_music_list():
        music_list = []
        music_list.append("audio/music/Fashion.ogg")
        music_list.append("audio/music/Funking the Streets.ogg")
        music_list.append("audio/music/Son Of A Rocket.ogg")
        
        music_list.extend(custom_music_files("outside/daytime"))
        
        return music_list

    def outside_evening_music_list():
        music_list = []
        music_list.append("audio/music/Lounging1 80.ogg")
        music_list.append("audio/music/Lounge5.ogg")
        music_list.append("audio/music/Papergirl.ogg")
        
        music_list.extend(custom_music_files("outside/evening"))
        
        return music_list

    def sound_test(filename):
        renpy.music.play(filename)
        
        return

    def audio_filename_without_extension_from_path(filename):
        split = filename.split("/")
        without_extension = split[ len(split) - 1].split(".ogg")[0]
        
        return without_extension

    def disable_audio_filenames(array):
        filename_array = []
        
        for filename in array:
            filename_array.append( { "filename_display_title": audio_filename_without_extension_from_path(filename), "path": filename} )
        
        return filename_array


    def music_valid_candidates(array):
        music_list = []
        
        for filename in array:
            without_extension = audio_filename_without_extension_from_path(filename)
            if without_extension not in persistent.disabled_music:
                music_list.append(filename)
        
        return music_list

    def play_music_queue(music_list):
        renpy.music.stop(fadeout=1)
        store.music_is_queued = True
        store.faded_out_audio = False
        
        random.shuffle(music_list)
        
        if len(music_list) > 1 and music_list[0] == store.last_queued_music:
            music_list.append(music_list.pop(0))
        
        store.music_playlist = music_list
        pop_playlist()
        
        return

    def pop_playlist():
        if len(store.music_playlist) > 0:
            new_music = store.music_playlist.pop(0)
            store.last_queued_music = new_music
            play_music(new_music, fadein = 1, considered_queue = True)
        
        return

    def play_music(name, channel='music', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False, considered_queue = False):
        if not considered_queue:
            store.music_is_queued = False
        renpy.music.play(name, channel=channel, loop=loop, fadeout=fadeout, synchro_start=synchro_start, fadein=fadein, tight=tight, if_changed=if_changed)
        return

    def stop_music(channel='music', fadeout=None):
        store.current_queued_music = None
        store.music_is_queued = False
        renpy.music.stop(channel=channel, fadeout=fadeout)
        
        return

    def fadeout_queued_music_func():
        fadeout_time = 2
        
        previous_queued_music = store.current_queued_music
        music_channel = renpy.audio.audio.get_channel('music')
        music_channel_number = music_channel.get_number()
        
        
        store.current_queued_music = renpy.audio.music.get_playing()
        
        if previous_queued_music != store.current_queued_music:
            store.faded_out_audio = False
        
        if renpy.music.is_playing() and store.music_is_queued and not store.faded_out_audio and renpy.audio.music.get_pos():
            time_left = renpy.audio.music.get_duration() - renpy.audio.music.get_pos()
            
            if time_left <= 2:
                renpy.music.stop(fadeout = fadeout_time)
                store.faded_out_audio = True
        
        return

screen fadeout_queued_music:
    timer 0.5 action Function(fadeout_queued_music_func) repeat True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
