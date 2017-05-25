# The script of the game goes in this file.

init -10 python:
    from dpj_script import *
    import collections
    
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Джек", color="#000000")
define p = Character("Пиратка")


# The game starts here.

label start:

    python:
        player_ship = Ship('Стриж')
        
    call fight

    scene bg promenade

    player "Старпом, ко мне. "

    show girl with moveinright
    
    p "Ахой!"
    p "Корабль готов к отплытию, капитан."
    
    hide girl with dissolve
    
    return

label fight:
        
    python:
        pass
    
    show bg sail with dissolve
    
    "Мы вышли на охоту."
        
    'Состояние "Стрижа" [player_ship.condition], скорость [] узлов, сила залпа [], абордажная сила [].'
    
    return
