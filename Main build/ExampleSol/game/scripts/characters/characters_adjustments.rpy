init python:
    def npc_list():
        character_list = []
        
        character_list.append( store.k )
        character_list.append( store.si )
        character_list.append( store.sa )
        character_list.append( store.julia )
        character_list.append( store.janet )
        character_list.append( store.edna )
        character_list.append( store.gloryhole_girl )
        character_list.append( store.vicky )
        
        
        
        
        return character_list



    def family_list():
        character_list = []
        character_list.append( store.n )
        character_list.append( store.k )
        character_list.append( store.si )
        character_list.append( store.sa )
        character_list.append( store.julia )
        character_list.append( store.janet )
        character_list.append( store.edna )
        
        return character_list

label retry_prompt_boldness_failure(retry_prompt_boldness_failure_char):
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned", text="(Я не знаю, готов ли я к этому)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned", text="(Может, если я буду {b}смелее{/b}...)")
    $ retry_prompt_boldness_failure_char.display_menu()
    return

label scene_limit_notice(scene_limit_char):
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="Может, я смогу сделать это завтра?")
    $ scene_limit_char.display_menu()
    return