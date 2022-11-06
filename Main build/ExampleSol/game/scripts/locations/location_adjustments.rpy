init -90 python:

    def location_list():
        place_list = []
        place_list.append(nate_room)
        place_list.append(kira_room)
        place_list.append(sam_room)
        place_list.append(simone_room)
        place_list.append(kitchen)
        place_list.append(backyard)
        place_list.append(living_room)
        place_list.append(hallway)
        place_list.append(bathroom)
        
        place_list.append(video_game_store)
        place_list.append(fortune_teller)
        place_list.append(park)
        place_list.append(vicky_apartment)
        place_list.append(janet_house)
        place_list.append(edna_house)
        
        place_list.append(school_library)
        place_list.append(school_bathroom)
        place_list.append(school_homeroom)
        
        return place_list


    class Nate_Room(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Моя комната"
        
        def empty_action(self):
            renpy.call("nate_room_empty")
            return
        
        def internal_name(self):
            return "nate_room"

    class Kira_Room(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return  "Комната " + store.k.say_name
        
        def internal_name(self):
            return "kira_room"

    class Sam_Room(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Комната " + store.sa.say_name
        
        def internal_name(self):
            return "sam_room"

    class Simone_Room(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Комната Мамы"
        
        def internal_name(self):
            return "simone_room"

    class Bathroom(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Ванная"
        
        def internal_name(self):
            return "bathroom"
        
        def empty_action(self):
            renpy.call("bathroom_empty")
            return

    class Kitchen(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Кухня"
        
        def internal_name(self):
            return "kitchen"

    class Backyard(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Задний двор"
        
        def internal_name(self):
            return "backyard"

    class Hallway(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Прихожая"
        
        def internal_name(self):
            return "hallway"

    class Living_Room(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Гостиная"
        
        def internal_name(self):
            return "living_room"

    class School_Start_Activation(Location):
        def __init__(self):
            Location.__init__(self)
        
        def name(self):
            return "Пойти в школу"
        
        def internal_name(self):
            return "living_room"
        
        def should_appear(self):
            return False
        
        def is_enabled(self):
            return not store.started_school and Location.is_enabled(self)
        
        def start(self, **properties):
            renpy.call("school_activate_start")
            
            return
        
        def unavailable_focused_text(self):
            if store.week.days_of_school_passed > 0:
                return "Школа началась"
            else:
                if store.week.day != 5 and week.day != 6:
                    return "School will start tomorrow"
                else:
                    return "School will start next week"


    class Outside_Location(Location):
        def internal_name(self):
            return "living_room"
        
        def zone(self):
            return store.outside
        
        def day_music_list(self):
            return outside_daytime_music_list()
        
        def night_music_list(self):
            return outside_evening_music_list()
        
        def background_full_path(self):
            return "images/bg/outside/" + self.background() + ".png"

    class Beach(Outside_Location):
        def name(self):
            return "Скоро"

    class Sex_Shop(Outside_Location):
        def name(self):
            return "Секс-шоп"

    class Video_Game_Store(Outside_Location):
        def name(self):
            return "Магазин Видеоигр"

    class Fortune_Teller(Outside_Location):
        def name(self):
            return "Гадалка"

    class Park(Outside_Location):
        def name(self):
            return "Парк"
        
        def internal_name(self):
            return "park"

    class Vicky_Apartment(Outside_Location):
        def name(self):
            return "Квартира Вики"
        
        def internal_name(self):
            return "apartment_hallway"

    class Janet_House(Outside_Location):
        def name(self):
            return "Дом [janet.say_name]"
        
        def internal_name(self):
            return "janet_house"

    class Edna_House(Outside_Location):
        def name(self):
            return "Дом Бабушки"
        
        def internal_name(self):
            return "edna_house"


    class School_Location(Location):
        def internal_name(self):
            return "living_room"
        
        def zone(self):
            return store.school

    class Library(School_Location):
        def name(self):
            return "Библиотека"

    class School_Library(School_Location):
        def name(self):
            return "Библиотека"

    class School_Bathroom(School_Location):
        def name(self):
            return "Туалет"

    class School_Homeroom(School_Location):
        def name(self):
            return "Классная комната"

    class School_Leave_Door(School_Location):
        def name(self):
            return "Пойти домой"
        
        def is_enabled(self):
            return store.is_school_time and School_Location.is_enabled(self)
        
        def unavailable_focused_text(self):
            return "Сегодня Вы были в школе"
        
        def start(self, **properties):
            renpy.call("school_leave")
            
            return


    class Grandma_Location(Location):
        def internal_name(self):
            return "living_room"
        
        def zone(self):
            return store.grandma_house

    class Grandma_House_Guest_Room(Grandma_Location):
        def empty_action(self):
            renpy.call("nate_room_empty")
            return
        
        def internal_name(self):
            return "kira_room"
        
        def name(self):
            return "Гостевая"

    class Grandma_House_Bathroom(Grandma_Location):
        def internal_name(self):
            return "bathroom"
        
        def name(self):
            return "Ванная"