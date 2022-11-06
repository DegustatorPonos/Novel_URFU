init -90 python:
    class IA_Stats(Stats):
        def stat_screen_array(self):
            array = []
            
            self.add_days_passed_stat(array)
            
            self.add_school_stat(array)
            
            self.add_weeks_passed_stat(array)
            
            self.add_dreams_had_stat(array)
            
            self.add_minigame_stats(array)
            
            self.add_scenes_completed_stat(array)
            
            
            self.add_character_scenes_stats(array)
            
            
            self.add_misc_stats(array)
            
            return array
        
        def boldness_xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            elif level == 2:
                return 5
            elif level == 3:
                return 10
            elif level == 4:
                return 15
            elif level == 5:
                return 20
            elif level == 6:
                return 25
            elif level == 7:
                return 30
            elif level == 8:
                return 35
            elif level == 9:
                return 40
            
            return 999999999
        
        def add_misc_stats(self, array):
            array = self.add_stat_screen_object(array, 'times_fapped', "Раз я мастурбировал" )
            array = self.add_stat_screen_object(array, 'times_ejaculated', "Раз я кончал" )
            array = self.add_stat_screen_object(array, 'times_received_blowjob', "Раз я получил минет" )
            array = self.add_stat_screen_object(array, 'times_given_facial', "Раз я кончал на лицо" )
            array = self.add_stat_screen_object(array, 'times_had_vaginal_sex', "Раз я трахал киску" )
            array = self.add_stat_screen_object(array, 'times_given_anal_sex', "Раз я трахал в задницу" )
            array = self.add_stat_screen_object(array, 'times_had_group_sex', "Раз у меня был групповой секс" )
            
            return array
        
        def add_school_stat(self, array):
            if store.week.days_of_school_passed > 0:
                array.append( Stat_Screen_Display_Object( "Прошло школьных дней", str( store.week.days_of_school_passed )  ) )
            
            return array
        
        def boldness_level_cap(self):
            return 8