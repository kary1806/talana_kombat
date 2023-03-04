class Player:
    def __init__(self, name, moves, hits):
        self.name = name
        self.moves = moves
        self.hits = hits
        self.energy = 6
        self.opponent = None
        self.turn = False

    def get_move(self, player: str, move: str, hit: str) -> None:
        description_fight = ""
        if len(move) > 2 and "DSD" in move[-3:] and hit == "P" and player == "player_1":
            return "usa un Taladoken"
        elif len(move) > 1 and "SD" in move[-2:] and hit == "K" and player == "player_1":
            return "conecta un Remuyuken"
        if len(move) > 2 and "ASA" in move[-3:] and hit == "P" and player == "player_2":
            return "usa un Taladoken"
        elif len(move) > 1 and "SA" in move[-2:] and hit == "K" and player == "player_2":
            return "conecta un Remuyuken"

        if len(move) == 1 and move == "D":
            description_fight = "avanza"
        else:
            description_fight = "se mueve"
        if hit == "P":
            description_fight = (
                f"{description_fight} y da un puñetazo" if description_fight else "da un puñetazo"
            )
        elif hit == "K":
            description_fight = (
                f"{description_fight} y da una patada" if description_fight else "da una patada"
            )

        return description_fight if description_fight else "No hay movimientos"

    def attack(self, player: str, move: str, hit: str) -> None:
        if len(move) > 2 and "DSD" in move[-3:] and hit == "P" and player == "player_1":
            self.opponent.energy -= 3
        elif len(move) > 1 and "SD" in move[-2:] and hit == "K" and player == "player_1":
            self.opponent.energy -= 1
        elif len(move) > 2 and "ASA" in move[-3:] and hit == "P" and player == "player_2":
            self.opponent.energy -= 2
        elif len(move) > 1 and "SA" in move[-2:] and hit == "K" and player == "player_2":
            self.opponent.energy -= 3
        elif hit == "P":
            self.opponent.energy -= 1
        elif hit == "K":
            self.opponent.energy -= 1

    def start_turn(self):
        self.turn = True
        self.opponent.turn = False

    def end_turn(self):
        self.turn = False
        self.opponent.turn = True

    def is_alive(self):
        return self.energy > 0
