init:
    screen _exception_actions(traceback_fn, tt, *args):

        textbutton _("Open Traceback"):
            action _EditFile(traceback_fn)
            hovered tt.action(_("Открыть traceback.txt в текстовом редакторе."))

        textbutton _("Копировать в буфер"):
            action _CopyFile(traceback_fn)
            hovered tt.action(_("Скопировать traceback.txt в буфер обмена."))

        vbox:
            textbutton _("Advance Time"):
                action Jump("day_advance_time")
                hovered tt.action(_("Попробовать исправить игру, опережая время. Непредвиденные побочные эффекты могут произойти."))

            textbutton _("Новая Игра+"):
                action Jump("new_game_plus_label")
                hovered tt.action(_("Начать новую игру, сохраняя награды от мини-игр. Любой другой прогресс не будет перенесен."))