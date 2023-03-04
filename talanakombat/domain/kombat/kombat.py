from typing import Tuple

from talanakombat.domain.kombat import player


class Kombat:
    def __init__(self, player_1_name, player_2_name, player1_data, player2_data):
        self.player1 = player.Player(
            player_1_name, player1_data["movimientos"], player1_data["golpes"]
        )
        self.player2 = player.Player(
            player_2_name, player2_data["movimientos"], player2_data["golpes"]
        )
        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

    def _begin_kombat(self) -> str:
        player = ""
        if len(self.player1.moves) < len(self.player2.moves):
            self.player1.start_turn()
            player = self.player1.name
        elif len(self.player2.moves) < len(self.player1.moves):
            self.player2.start_turn()
            player = self.player2.name
        elif len(self.player1.moves) == len(self.player2.moves):
            if len(self.player1.moves[-1]) < len(self.player2.moves[-1]):
                self.player1.start_turn()
                player = self.player1.name
            elif len(self.player2.moves[-1]) < len(self.player1.moves[-1]):
                self.player2.start_turn()
                player = self.player2.name
            else:
                self.player1.start_turn()
                player = self.player1.name
        return f"{player} comienza atacando \n"

    def _get_move_and_hit(self, player: player.Player) -> Tuple[str, str]:
        if not player.moves and player.hits:
            move = ""
            hit = player.hits.pop(0)
        elif player.moves and not player.hits:
            move = player.moves.pop(0)
            hit = ""
        else:
            move = player.moves.pop(0)
            hit = player.hits.pop(0)
        return move, hit

    def play(self) -> str:
        description_figth = "¡Comienza el combate! \n"
        # Determinar quién empieza
        description_figth += self._begin_kombat()

        # Jugar hasta que alguien muera
        while self.player1.is_alive() and self.player2.is_alive():
            if self.player1.turn:
                if not self.player1.moves and not self.player1.hits:
                    description_figth += "No hay movimientos \n"
                    self.player1.end_turn()
                    self.player2.start_turn()
                else:
                    move, hit = self._get_move_and_hit(player=self.player1)
                    self.player1.attack(player="player_1", move=move.upper(), hit=hit.upper())
                    move_str = self.player1.get_move(
                        player="player_1", move=move.upper(), hit=hit.upper()
                    )
                    description_figth += f"{self.player1.name} {move_str} \n"
                    self.player1.end_turn()
                    # Determinar quién empieza
                    self.player2.start_turn()
            elif self.player2.turn:
                if not self.player2.moves and not self.player2.hits:
                    description_figth += "No hay movimientos \n"
                    self.player2.end_turn()
                    self.player1.start_turn()
                    continue
                else:
                    move, hit = self._get_move_and_hit(player=self.player2)
                    self.player2.attack(player="player_2", move=move.upper(), hit=hit.upper())
                    move_str = self.player2.get_move(
                        player="player_2", move=move.upper(), hit=hit.upper()
                    )
                    description_figth += f"{self.player2.name} {move_str} \n"
                    self.player2.end_turn()
                    self.player1.start_turn()

        # Mostrar el resultado final
        if self.player1.is_alive():
            description_figth += f"¡{self.player1.name} gana la pelea con {self.player1.energy} puntos de energía restantes!"
            return description_figth
        else:
            description_figth += f"¡{self.player2.name} gana la pelea con {self.player2.energy} puntos de energía restantes!"
            return description_figth
