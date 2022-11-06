python early:

    @renpy.atl_warper
    def linear_adjustable(t):
        
        unadjusted_time_difference = t - store.old_unadjusted_t
        
        store.old_unadjusted_t = t
        
        store.old_adjusted_t = store.old_adjusted_t + ( unadjusted_time_difference * store.test_speed_multiplier )
        
        if store.old_adjusted_t > 1.0:
            return None
        
        return store.old_adjusted_t
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
