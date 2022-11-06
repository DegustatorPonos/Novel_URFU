init python:
    def math_minigame_choice_number_boost():
        if store.inventory.has_item(3):
            return -1
        
        return 0

    def math_minigame_generate_question_simple_operation_prompt(operands, operators):
        prompt = ""
        for i in range( 0, len(operands) ):
            operand = operands[i]
            if operand < 0 and i > 0 and operators[i - 1] == "-":
                operand = "(" + str(operand) + ")"
            
            prompt += str( operand ) + " "
            
            if i < len(operands) - 1:
                operator = operators[i]
                
                if operator == "*":
                    operator = "X"
                prompt += " " + operator + " "
        
        prompt += "?"
        
        return prompt

    def minigame_math_build_answers(right_answer, wrong_answers):
        answers = []
        answers.extend(wrong_answers)
        answers.append(right_answer)
        
        random.shuffle(answers)
        return answers

    def minigame_math_generate_question_simple_operation_answer(operands, operators):
        eval_string = ""
        
        for i in range( 0, len(operands) ):
            operand = operands[i]
            
            if i > 0 and operators[i - 1] == "/":
                operand = float(operand)
            
            if operand < 0:
                operand = "(" + str(operand) + ")"
            eval_string += str( operand ) + " "
            
            if i < len(operands) - 1:
                eval_string += " " + operators[i] + " "
        
        return eval(eval_string)

    def valid_division_addend(addend, right_answer, wrong_answers, minimum_distance = .20, restrict_very_low_decimals = False):
        wrong_answer = right_answer + addend
        
        if restrict_very_low_decimals and wrong_answer % 1 != 0 and wrong_answer % 1 < .10:
            renpy.log("Failed on restrict_very_low_decimals and wrong_answer % 1 < .10")
            renpy.log("-")
            return False
        
        if addend == 0:
            renpy.log("addend == 0")
            renpy.log("-")
            return False
        
        if wrong_answer == right_answer:
            renpy.log("Failed on wrong_answer == right_answer")
            renpy.log("-")
            return False
        
        
        if wrong_answer in wrong_answers:
            renpy.log("Failed on wrong_answer in wrong_answers")
            renpy.log("-")
            return False
        
        if any( abs( wrong_a - wrong_answer ) < minimum_distance for wrong_a in wrong_answers ):
            renpy.log("Failed on any( abs( wrong_a - wrong_answer ) < minimum_distance for wrong_a in wrong_answers )")
            renpy.log("-")
            return False
        
        
        if right_answer % 1 != 0 and abs(addend) < .20:
            renpy.log("Failed on right_answer % 1 != 0 and abs(addend) < .20")
            renpy.log("-")
            return False
        
        
        if right_answer < 1 and wrong_answer >= 1:
            renpy.log("Failed on right_answer < 1 and wrong_answer >= 1")
            renpy.log("-")
            return False
        
        
        if right_answer > 1 and wrong_answer <= 1:
            renpy.log("Failed on right_answer > 1 and wrong_answer <= 1")
            renpy.log("-")
            return False
        
        
        if right_answer < 0 and wrong_answer >= 0:
            renpy.log("Failed on right_answer < 0 and wrong_answer >= 0")
            renpy.log("-")
            return False
        
        
        if right_answer > 0 and wrong_answer <= 0:
            renpy.log("Failed on right_answer > 0 and wrong_answer <= 0")
            renpy.log("-")
            return False
        
        renpy.log("Succeeded")
        renpy.log("Adding " + str(right_answer) + " + " + str(addend) + " = " + str(wrong_answer))
        renpy.log("-")
        
        return True

    def minigame_math_generate_wrong_answers_normal( right_answer, wrong_answer_choices, num_range):
        wrong_answer_choices = []
        
        for i in range(0, len( num_range ) ):
            test_wrong_answer = right_answer + num_range[i]
            
            
            if test_wrong_answer in wrong_answer_choices:
                continue
            
            if num_range[i] == 0 or test_wrong_answer == right_answer or test_wrong_answer == 0:
                continue
            
            
            if right_answer < 0 and test_wrong_answer > 0:
                continue
            
            
            if right_answer > 0 and test_wrong_answer < 0:
                continue
            
            wrong_answer_choices.append(test_wrong_answer)
        
        return wrong_answer_choices

    def minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = .20, divide_by_100 = True, restrict_very_low_decimals = False ):
        for i in range(0, len( num_range ) ):
            test_addend = num_range[i]
            
            if divide_by_100:
                test_addend = test_addend / float(100)
            
            if valid_division_addend( test_addend, right_answer, wrong_answer_choices, minimum_distance = minimum_distance, restrict_very_low_decimals = restrict_very_low_decimals ):
                wrong_answer_choices.append( right_answer + test_addend )
        
        return wrong_answer_choices

    def minigame_math_generate_question_simple_operation_wrong_answers(right_answer, decimal_offset = False):
        wrong_answers = []
        wrong_answer_choices = []
        
        if decimal_offset:            
            if right_answer % 1 == 0:
                divide_by_100 = False
                range_min = min(-3, -(store.minigame_math_num_wrong_choices ) )
                range_max = max(4, store.minigame_math_num_wrong_choices + 1)
                
                step = 1
            else:
                divide_by_100 = True
                
                range_min = -50
                
                range_max = 50
                step = 1
            
            num_range = range(range_min, range_max, step)
            random.shuffle(num_range)
            
            wrong_answer_choices = minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = .15, divide_by_100 = divide_by_100, restrict_very_low_decimals = True )
            
            if len( wrong_answer_choices ) < minigame_math_num_wrong_choices:
                wrong_answer_choices = minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = .10, divide_by_100 = divide_by_100, restrict_very_low_decimals = True )
            
            if len( wrong_answer_choices ) < minigame_math_num_wrong_choices:
                wrong_answer_choices = minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = .5, divide_by_100 = divide_by_100, restrict_very_low_decimals = True )
            
            if len( wrong_answer_choices ) < minigame_math_num_wrong_choices:
                wrong_answer_choices = minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = 0, divide_by_100 = divide_by_100, restrict_very_low_decimals = False )
            
            renpy.log("----------")
        else:
            
            if store.math_difficulty == "hard":
                num_range = range(-50, 51, 10)
            else:
                num_range = range(-20, 20)
            
            random.shuffle(num_range)
            
            wrong_answer_choices = minigame_math_generate_wrong_answers_normal( right_answer, wrong_answer_choices, num_range)
            
            if len( wrong_answer_choices ) < minigame_math_num_wrong_choices:
                wrong_answer_choices = minigame_math_generate_wrong_answers_normal( right_answer, wrong_answer_choices, range(-50, 50))
            
            if len( wrong_answer_choices ) < minigame_math_num_wrong_choices:
                wrong_answer_choices = minigame_math_generate_division_wrong_answer_choices( right_answer, wrong_answer_choices, num_range, minimum_distance = 0, divide_by_100 = divide_by_100, restrict_very_low_decimals = False )
        
        
        random.shuffle(wrong_answer_choices)
        
        while len(wrong_answers) < store.minigame_math_num_wrong_choices:
            wrong_answer = random.choice(wrong_answer_choices)
            wrong_answer_choices.remove(wrong_answer)
            wrong_answers.append(wrong_answer)
        
        return wrong_answers

    def minigame_math_generate_question_simple_operation_answer_obj(minimum = -100, maximum = 100, operator_choices = ["+"], operand_num = 2, number_exclusions = [], decimal_offset = False, prevent_same_operand = False):
        operands = []
        operators = []
        
        while len(operands) < operand_num:
            operand = random.randint(minimum, maximum)
            if operand not in number_exclusions and (not prevent_same_operand or operand not in operands):
                operands.append( operand ) 
        
        for i in range(0, operand_num - 1):
            operators.append( random.choice(operator_choices) ) 
        
        right_answer = minigame_math_generate_question_simple_operation_answer(operands, operators)
        if right_answer % 1 != 0:
            right_answer = round(right_answer, 2)
        
        wrong_answers = minigame_math_generate_question_simple_operation_wrong_answers(right_answer, decimal_offset = decimal_offset)
        
        return {"operands": operands, "operators": operators, "right_answer": right_answer, "wrong_answers": wrong_answers}

screen minigame_math_points:
    text str(math_current_points) + "/" + str(math_max_tries) size 60 xalign 0.99

label minigame_math(partner=None):
    call process_scene_beginning
    call math_minigame_initialize
    call math_minigame_intro

    if config.developer:
        "DEBUG/DEVELOPER MODE: Reduced amount of questions and increased time"

    show screen minigame_math_points
    $ disable_rollback()
    call math_minigame_round

    call math_minigame_end

    return

label math_minigame_intro:
    python:
        random_line = random.randint(1, 3)

    if random_line == 1:
        $ display_multiple_characters([ (n, ""), (sa, "pose leaning face neutral") ], reset = True)
        call process_character (sa, appearance="pose leaning face neutral", text="Бьюсь об заклад, ты хочешь вызов!")
    elif random_line == 2:
        $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)
        call process_character (sa, appearance="pose handsbehind face neutral", text="Хорошо, насколько трудными должны быть эти вопросы?")
    else:
        $ display_multiple_characters([ (n, ""), (sa, "pose handface face neutral") ], reset = True)
        call process_character (sa, appearance="pose handsbehind face neutral", text="Давай погрызём некоторые цифры!")

    menu:
        "Полегче со мной.":
            $ math_difficulty = "easy"
            $ math_timer = 8
            call process_character (sa, appearance="pose handsbehind face neutral", text="Попробуй ответить на вопросы по математике так быстро, как можешь!")
        "Давай я попробую посложнее. (Увеличение Смелости)":
            call process_character (sa, appearance="pose handsbehind face neutral", text="Это должно повысить твои математические навыки!")
            $ math_difficulty = "medium"
            $ math_timer = 10
        "Дайте мне всё что у тебя есть. (Увеличение Смелости)":
            call process_character (sa, appearance="pose handsbehind face neutral", text="Это тяжело, даже для меня!")
            $ math_difficulty = "hard"
            $ math_timer = 12

    if config.developer:
        $ math_timer = 999

    $ disable_saving()

    return


label math_minigame_initialize:
    $ no_bust_art = False

    python:
        math_timer = 5
        math_current_points = 0
        math_current_tries = 0
        math_max_tries = 4

        if config.developer:
            math_max_tries = 2

        math_won = False
        math_difficulty = "easy"



        minigame_math_num_choices = 4 + math_minigame_choice_number_boost()
        minigame_math_num_wrong_choices = minigame_math_num_choices - 1

    return

label math_minigame_generate_question:
    python:
        math_current_tries += 1

    if math_difficulty == "easy":
        call math_minigame_generate_question_easy
    elif math_difficulty == "medium":
        call math_minigame_generate_question_medium
    else:
        call math_minigame_generate_question_hard

    call math_minigame_round

    return

label math_minigame_generate_question_easy:
    python:

        math_question_type_id = random.randint(1, 3)

    if math_question_type_id == 1:
        call math_minigame_generate_question_simple_operation (minimum=11, maximum=100, operator_choices=["+"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 2:
        call math_minigame_generate_question_simple_operation (minimum=11, maximum=50, operator_choices=["-"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 3:
        call math_minigame_generate_question_simple_operation (minimum=2, maximum=12, operator_choices=["*"], operand_num=2, number_exclusions=[0, 1])
    elif math_question_type_id == 4:
        call math_minigame_generate_question_simple_operation (minimum=2, maximum=10, operator_choices=["/"], operand_num=2, number_exclusions=[0, 1, 10], decimal_offset=True, prevent_same_operand=True)

    return

label math_minigame_generate_question_medium:
    python:

        math_question_type_id = random.randint(1, 3)

    if math_question_type_id == 1:
        call math_minigame_generate_question_simple_operation (minimum=-100, maximum=100, operator_choices=["+"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 2:
        call math_minigame_generate_question_simple_operation (minimum=-50, maximum=100, operator_choices=["-"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 3:
        call math_minigame_generate_question_simple_operation (minimum=-7, maximum=7, operator_choices=["*"], operand_num=2, number_exclusions=[0, 1])
    elif math_question_type_id == 4:
        call math_minigame_generate_question_simple_operation (minimum=3, maximum=20, operator_choices=["/"], operand_num=2, number_exclusions=[0, 1, 10], decimal_offset=True, prevent_same_operand=True)

    return

label math_minigame_generate_question_hard:
    python:

        math_question_type_id = random.randint(1, 3)

    if math_question_type_id == 1:
        call math_minigame_generate_question_simple_operation (minimum=-150, maximum=150, operator_choices=["+"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 2:
        call math_minigame_generate_question_simple_operation (minimum=-100, maximum=150, operator_choices=["-"], operand_num=2, number_exclusions=[0])
    elif math_question_type_id == 3:
        call math_minigame_generate_question_simple_operation (minimum=-9, maximum=12, operator_choices=["*"], operand_num=2, number_exclusions=[0, 1])
    elif math_question_type_id == 4:
        call math_minigame_generate_question_simple_operation (minimum=-5, maximum=50, operator_choices=["/"], operand_num=2, number_exclusions=[0, 1, 10], decimal_offset=True, prevent_same_operand=True)

    return

label math_minigame_round:
    if math_current_tries < math_max_tries:
        call math_minigame_generate_question

    return

label math_minigame_right_answer_response:
    python:
        response_type_id = random.randint(1, 3)

    if response_type_id == 1:
        call process_character (sa, appearance="pose leaning face neutral", text="Круто!")
    if response_type_id == 2:
        call process_character (sa, appearance="pose handface face neutral", text="Хорошая работа!")
    if response_type_id == 3:
        call process_character (sa, appearance="pose handsbehind face neutral", text="У тебя получилось!")

    $ math_current_points += 1

    return

label math_minigame_wrong_answer_response:
    python:
        response_type_id = random.randint(1, 3)

    if response_type_id == 1:
        call process_character (sa, appearance="pose handface face concerned", text="Не совсем.")
    if response_type_id == 2:
        call process_character (sa, appearance="pose handsbehind face concerned", text="Не угадал на этот раз.")
    if response_type_id == 3:
        call process_character (sa, appearance="pose handface face concerned", text="Извини [n.say_name], это неправильно.")

    return

label minigame_math_too_slow:
    hide countdown
    hide screen minigame_countdown
    call process_character (sa, appearance="pose handface face concerned", text="Попробуй отвечать быстрее.")

    return

label minigame_math_generate_question_special_division(dividend_min=0, dividend_max=0, multiple_max=0):
    return

label math_minigame_generate_question_simple_operation(minimum=-100, maximum=100, operator_choices=["+"], operand_num=2, number_exclusions=[], decimal_offset=False, prevent_same_operand=False):
    python:
        answer_obj = minigame_math_generate_question_simple_operation_answer_obj(minimum = minimum, maximum = maximum, operator_choices = operator_choices, operand_num = operand_num, number_exclusions = number_exclusions, decimal_offset = decimal_offset, prevent_same_operand = prevent_same_operand)
        math_right_answer = answer_obj.get("right_answer")
        math_operands = answer_obj.get("operands")
        math_operators = answer_obj.get("operators")

        math_answers = minigame_math_build_answers(math_right_answer , answer_obj.get("wrong_answers") )

        math_prompt = math_minigame_generate_question_simple_operation_prompt(math_operands, math_operators)

    call math_minigame_show_choose_choices (math_right_answer, math_answers, math_prompt)

    return

label math_minigame_show_choose_choices(right_answer, answers, prompt, prefix=""):
    call process_character (sa, appearance="pose handface face neutral")
    call minigame_countdown (math_timer, "minigame_math_too_slow", xalign=0.01)

    if minigame_math_num_choices == 3:
        menu:
            "[prompt]"
            "[prefix][answers[0]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[0]
            "[prefix][answers[1]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[1]
            "[prefix][answers[2]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[2]
    elif minigame_math_num_choices == 4:
        menu:
            "[prompt]"
            "[prefix][answers[0]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[0]
            "[prefix][answers[1]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[1]
            "[prefix][answers[2]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[2]
            "[prefix][answers[3]]":
                hide screen math_minigame_countdown
                $ chosen_answer = answers[3]

    hide countdown
    hide screen minigame_countdown
    if chosen_answer == right_answer:
        call math_minigame_right_answer_response
    else:
        call math_minigame_wrong_answer_response

    return


label math_minigame_end:
    $ enable_saving()

    if math_difficulty == "easy":
        if math_current_points >= math_max_tries:
            $ sa.add_points(2, minigame = True)

            show screen hud
            python hide:
                win_money = 4
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(1, minigame = True)

            show screen hud
            python hide:
                win_money = 2
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")

    elif math_difficulty == "medium":
        if math_current_points >= math_max_tries:
            call add_points_and_boldness (sa, 3, 1, minigame=True)

            show screen hud
            python hide:
                win_money = 6
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(2)

            show screen hud
            python hide:
                win_money = 4
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")
    elif math_difficulty == "hard":
        if math_current_points >= math_max_tries:
            call add_points_and_boldness (sa, 4, 1, minigame=True)

            show screen hud
            python hide:
                win_money = 8
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")

        elif math_current_points >= math_max_tries - 2:
            $ sa.add_points(3, minigame = True)

            show screen hud
            python hide:
                win_money = 6
                inventory.add_money(win_money, minigame = True)
                narrator("Получите $" + str(win_money) + " за победу.")

    if math_current_points >= math_max_tries:
        call process_character (sa, appearance="pose leaning face happy", text="Ух ты! Ты легко с этим справился!")
    elif math_current_points >= math_max_tries - 2:
        call process_character (sa, appearance="pose leaning face neutral", text="Очень хорошо, [n.say_name]!")
    else:
        call process_character (sa, appearance="pose handface face concerned", text="Может, как-нибудь попробуем еще раз.")

    $ renpy.block_rollback()
    $ enable_rollback()
    hide screen minigame_math_points
    call process_end_of_minigame ("minigame_math")

    return