from talanakombat.domain.kombat.kombat import Kombat


def get_kombat_result(player1: dict, player2: dict) -> dict:
    talana_kombat = Kombat(
        player_1_name="Tony",
        player_2_name="Arnold",
        player1_data=player1 if player1 else {"movimientos": [], "golpes": []},
        player2_data=player2 if player2 else {"movimientos": [], "golpes": []},
    )
    return talana_kombat.play()
