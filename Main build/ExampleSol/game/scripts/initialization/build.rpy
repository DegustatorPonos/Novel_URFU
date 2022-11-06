init python:
    config.developer = False


    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("video", "all")
    build.archive("database", "all")
    build.archive("settings_override", "all")


    build.classify("game/scripts/initialization/settings_override.rpyc", "settings_override")
    build.classify("game/**.rpyc", "scripts")


    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")


    build.classify("game/audio/**.mp3", "audio")
    build.classify("game/audio/**.ogg", "audio")
    build.classify("game/audio/**.wav", "audio")


    build.classify("game/**.webm", "video")


    build.classify("game/custom_music/**.ogg", None)
    build.classify("game/custom_music/**.mp3", None)
    build.classify("game/custom_music/**.wav", None)


    build.classify("game/**.rpy", None)
    build.classify("**.gitignore", None)
    build.classify("**.md", None)
    build.classify("**.git", None)
    build.classify("**.save", None)
    build.classify("persistent", None)