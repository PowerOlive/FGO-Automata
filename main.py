from core.Automata import Automata
# init
shiki = Automata("assets/checkpoint.png", "assets/qp.png", (248, 0))
# start
shiki.select_checkpoint()
shiki.select_support()
shiki.start_battle()
# battle 1
shiki.select_servant_skill(4)
shiki.select_servant_skill(5)
shiki.select_cards([7])
# battle 2
shiki.select_servant_skill(9)
shiki.select_cards([8])
# battle 3
shiki.show_master_skill()
shiki.select_master_skill(2, 1)
shiki.select_servant_skill(1)
shiki.select_servant_skill(2)
shiki.select_cards([6])
# finish
shiki.finish_battle()
