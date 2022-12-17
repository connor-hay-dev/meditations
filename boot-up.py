import json

from meditations_text import meditations

import os 

from return_the_book_and_chapter import return_book_and_chapter
from return_book_selection import return_book
from search_by_keyword import return_with_space_between_each_output 



def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')              
    print(""" \
        
GGGGGGGGGGGGGGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
GGGGGGGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
GGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPY?7777?Y5PYYYYY5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5J7777??J7^:^::::^^^^^^^^~!7?7!!!7?J5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPP5YJ?!~^::^^~^^~^^^:::^::::^^^~~~!~^^^^^^:^7YPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPP5YJ7!~~!~~~^^^^^^~~~^^~~^^^:^::::^~~!~~~^^~::^:~?55PP55PP5PPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPP5Y7!^^^~~!?~~~~~~^^^:^~~~:^::^^^~^::^^::.::^^~~::^:^!!?5PPP55555555555PPPPPPPPP
PPPPPPPPPPPPPPPPPPPP57!J?:^J7!~!^^~^!!7!^~!!!~~~:^::~^^^~!?J?~::::~~^^^^^~^^!?JY5555555555555555PPPP
PPPPPPPPPPPPPPPPP5J??!^7!^^~^^~:^^:!~!7~~!!!~^:~^^:~!~7JYJ?!?7~~^^^~!!^^::^!7!!!J5555555555555555555
PPPPPPPPPPPPPP5JJYYY??!7~!!!~!77!^^~~:!7~^!!!^:.^^:^~!7777?!^^^^^!7~~~:..:~!!~^~!JP55555555555555555
PPPPPPPPP555P5?!?~!JJ77YYY!~~!~7~^~~~^^7!^^~!!7!~~^:^~^:^?J5Y^::!5J7!!!!!!^?J7!!^~???J55555555555555
PPPPP5555555P7~Y?77~^~~?YG57!~^:~~~^!!!~777~!!!!!~^!^^!JYYJJ5?~!J5YJJY5Y7!~!J!~^::^^^~Y5555555555555
PPPP55555555PJ!YGG77JJ77?5PJ!J7~~!!!YP5Y5PPYJJJYJYYJJ?JBGGGG555P5J?7!??!~7J7!^:^!^~~!!Y5555555555555
55555555555Y7!!7Y5J7?J?5G55PJ7Y555PGGB##B###BPJJ7?YP5J55Y5GB#BGGGPYJYGY??PJ?7^::~777!7?Y555555555555
55555555555?7~~~?!7!~!~~??JPBGPGGGBBGPPP5Y5PPPGGPYYYPP5YYYJYPB####BBPYJJYJJP557^^~~!!!!!J55555555555
55555555555YJ7JJJ7???!!~~!YGBBBBBBPJ!~~^^^^~!7??JJYJJ?~^^^:^~7YGBBBPYYYYYJGP!!77?7~7?!~^~Y5555555555
5555555555555YJJJ5?7JY??JY5GB##BPJ!~^^^^::::.........  ....:::^~7JYPP5YJJYJ!^^?YP55J!!!^~!J5YY555555
5555555555PBG??JPGBPY5PGGGGPPP5J7!~~~~~~^^^::::::::::::.::::::^^^~!?5GGBGY7?J5GGGBBGPG5J7?YYYYYYYY55
55555555YJ??JYY5GB##BBBBGPYJJJ?7!!!~~~~^^^^^^^^^^::::::::::::^^^^~!!7J5PGGBBB##BBG5?YYY???77YYYYYYYY
55555555YJ??J5Y5GPGB#&#BPYJ??777!!!~~^^^:::::::::::::...:::::^^^^~~!77?JYGBB#BGPYJJJ?!!!55?7YYYYYYYY
55555555GG5PGB5JYPPGGGGPYJJ?77!!~~~~~^^^^^:::::::.......:::::::^^^^~~!7JJ5PPPPGGP5YJ??YYP5?JYYYYYYYY
5555555Y5######BGGGGGPPPP5J?7!!~~!!!!!!!~~~~^^^^::::^^^^^^^^^^^^^:::^~7JYYPBGGGGGGGPPP55J?JYYYYYYYYY
555555YYPPPGB######BBBBBG5J??????JY555YYJJ?7!~~~~^~!777??JJJJJ?77!!~^~7JY5PGBBBBGPPPYYPPYJYYYYYYYYYY
5555YYYY5YYYPBGBBBBBBBGGP555PP555YJJJYPPPPP5J!!~~~7J5555PPP5YYYYJJ??777?Y5PGBBBGGGP5PGPPPYJYYYYYYYYY
55YYYYYYY5YYY5Y5PGPBBBG5Y5PGGGP5?!!~~!?YPGPPPJ!~~7JYPPPPPY?!~~!7J555YJ??J55G#####BGBBBGP5YJJJJJYYYYY
YYYYYYYYYPBG5PGYJPY5PG5JJYPGGGGP5YJ????Y5PGGPJ~::~7Y5PP5J?7777???JPPPYJ??YYPBBBBBGPP5Y5YJJJJJJJJJJJY
YYYYYYYYYYPG5Y5P5Y5PPP5YJJYYY55PPYJ??7!!7JYYJ7:..^!7???77!777?77??JYJ?7777?5GB#BBGGGBPY?JJJJJJJJJJJJ
YYYYYYYYYYYYYJ5Y5GGP5PP5YJ?777?Y55YYJ?7!!!!!7!:..:~~~~~!!7?JJJJJ?!~~~!~~~!75GG5PP5G#GGPYJJJJJJJJJJJJ
YYYYYYYYYYJJJJJYYG##YJP5YJ?7!!!!7????7!!!~~!!~:..:^~~~~~~!7?JJJ?7~^^^^^~~!7YY??JJPP55YJJJJJJJJJJJJJJ
YYYYYYYYJJJJJJJJJJB#Y?5P5YJ?77!!~~~~~~~!!7777~:.:::^~!!~~~~~~~!!!!~~~~~~!!!77YYYYJ?????????JJJJJJJJJ
YYYYYYJJJJJJJJJJJ?5#PJYPP5YJ??7!!~~~~~~!7J?77~:.:::^^~!!~~~~~!!!7777777777!^^?!7??????????????JJJJJJ
YYYYYJJJJJJJJJJJJ?JGGJJ5PP55YJ?7!~!!~!!7J?~!!~^:::::.^77!~~~~~!!77????777!~~~777?????????????????JJJ
YYYYJJJJJJJJJJJ????YJ7?YY5555YJ7!!!!!!!!?YYYJ??77777!~!77!!!~~~!77??JJ??7!^!7777????????????????????
YYJJJJJJJJJJJJ?????YPJ7JJJJJYJ??77777!!!7PBBBGPPP5PP5Y7!!!!!!!!!!!7????7!^~~!!77777?????????????????
YJJJJJJJJJJ????????YP5PPPY?7?J??7777!~~~!J5GBP5PP5Y?7!^:^~~!!!!!777777!~~!??7~77777777??????????????
JJJJJJJJJJ??????????YP55555Y?????77!!~!!777Y555BPY?!~:::::::^~!!!!!!~~~~7J5YY?777777777777??????????
JJJJJJJJ?????????777?GGYJYY5YJ?77!77?!JJJYY5YYYBGY?7!!~~~^^:^^~~!~~!77!!!~!7777777777777777?????????
JJJJJJJ????????777777YPGG5YYJ????77?J?5PGP5P5PP5PGP555YYY777~~~~~~~!!77JJ?7!!!777777777777777???????
JJJJJJ????????777777?5PGGPP55P5YY5YJ5Y5GGGPP5555555YY55GGYYJ!~~!7777?J55P5YY?!!!!77777777777777?????
JJJJ?????????77777777J5PGBP5GG5555P5YY5PPPPP5YYYYYJJJYY5GG55YYJ7777!!??JP5J?!!!!!!!7777777777777????
JJJ????????777777777!!7PGB5JPG5YY55YJJJJJYJJYJJ????JJJ??JY55YYY??7????77Y7!!!!!!!!!!7777777777777???
JJJ???????777777777!!!!!5GGY5GP5YYJJ7~!!!!!!!!77!7!!~~^^~~!!!!!!7JJJJ7!??~!!!!!!!!!!77777777777777??
JJ???????777777777!!!!!!!7YBGGPP5?7???7777!7!~~!!~~~~~~^~^^^~~~~777?JY5J~!!!!!!!!!!!!77777777777777?
J????????77777777!!!!!!!!~?##BP55?!77Y?7??77?7!777777!7!777!~!!!!7JY5557~!!!!!!!!!!!!77777777777777?
J????????7777777!!!!!!!!!~!YGBG5Y?77!?J77J7?JJ??J??!7!!777??7!?JJJY5P57~!!!!!!!!!!!!!7777777777777??
????????77777777!!!!!!!!!!~~~5BY55JJY5Y?J7!!!JYYYJ??7777~~!?JJ?J5YJYY7~!!!!!!!!!!!!!!777777777777???
????????77777777!!!!!!!!!!!~~?BBGBBGPPJYYJ????JYYJJJ??J?7?JJY5?!?YP5?~!!!!!!!!!!!!!!!777777777777???
????????77777777!!!!!!!!!!!~~~7YPG#BG5Y5PYJJJJJ5JJJJ5YJJJ5Y?7??77YY?!~!!!!!!!!!!!!!!!777777777777???
????????777777777!!!!!!!!!!!!~~~JB#BP5PYYYJJ5?YGY5?7YJ???JP5YJ?Y?!~~~!!!!!!!!!!!!!!!!7777777777777??
?????????7777777777!!!!!!!!!!!!!~?P##GGGY5J777JGP5J!~~~7??JPPYJ7!~!!!!!!!!!!!!!!!!!77777777777777???
??????????7777777777!!!!!!!!!!!!!~!7?7?5P55YJJJGPY5J?77????55J7~!!!!!!!!!!!!!!!!!777777777777777????
???????????777777777!!!!!!!!!!!!!!!~~~~~!!7???7!~?G5Y????777!!!!!!!!!!!!!!!!!!!!!!77777777777???????
??????????????77?YYYYYYYYYYYYYYYYYJJJJJJJJJJJJJJJ5GY55JJ?JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?777????????
J??????????????J5PPGGGGGGGGGGGGGGGGGGGGGGGGGGGPPPGGY??7!~5PPPPPGGGGGPPPPPPPPPPPPPPP555555Y??????????
JJJ???????????J55555PPPPPPPPPPPPPPPPPPPPPPPPPPGGPBGY?7!~~Y5555555555555555YYYYYYYYYYYYYYYYYJ????????""")
    print("\n")
    print("\t***********************************************************************************")
    print("\t************************ Greetings Fellow Philosphers!  ***************************")
    print("\t***********************************************************************************")
    print("\t***********************************************************************************")
    print("\n")
    print("""\t\"Everything suits me that suits your designs, O my universe. Nothing is too early 
        or too late for me that is in your own good time. All is fruit for me that your 
        seasons bring, O nature. All proceeds from you, all subsists in you, and to you all 
        things return.\"""")
    print("\t- Marcus Aurelius Meditations 4.23")
    print("\n")

def welcome():
    display_title_bar
    ready_to_play = input("Are you ready to have fun? (and learn a little, of course!) (Y/N) : ")
    if ready_to_play == "N":
        print("No worries! See you next time!")
    elif ready_to_play == "Y":
        return select_mode()

def select_mode():
    print("Please select your mode: \n1. Book Search. \n2. Quiz Game")



