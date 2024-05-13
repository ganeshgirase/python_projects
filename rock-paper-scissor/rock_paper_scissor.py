import logging
import random
from dataclasses import dataclass
from enum import Enum


class GAMEMOVE(Enum):
    PAPER = 1
    ROCK = 2
    SCISSOR = 3


@dataclass
class Player:
    id: str
    move: GAMEMOVE = GAMEMOVE.PAPER


class Judge:
    @staticmethod
    def get_winner(player: Player, opponent: Player) -> Player | None:
        logging.debug("Player Moves:- ", player.move, opponent.move)
        if player.move == opponent.move:
            return None
        if player.move == GAMEMOVE.PAPER and opponent.move == GAMEMOVE.ROCK:
            return player
        if player.move == GAMEMOVE.ROCK and opponent.move == GAMEMOVE.SCISSOR:
            return player
        if player.move == GAMEMOVE.SCISSOR and opponent.move == GAMEMOVE.PAPER:
            return player
        return opponent


class InvalidInputException(Exception):
    pass

class UserQuitsException(Exception):
    pass


class USERMESSAGE:
    Welcome = "! Welcome to the rock-paper-scissor game !!!\n\n"
    InvalidInput = "Sorry, we cannot understand your input !!"
    Congratulations = "****  Hooray! You are winner! ****"
    Condole = "Sorry! Better luck next time! "
    Draw = "Hey, It's draw, you can try again!"
    GoodBye = "It was nice to play with you!!"
    QuitGame = "User quits games !"


class Scorer:

    @staticmethod
    def congratulate_player():
        Console.write(USERMESSAGE.Congratulations)

    @staticmethod
    def condole_player():
        Console.write(USERMESSAGE.Condole)

    @staticmethod
    def declare_draw():
        Console.write(USERMESSAGE.Draw)


class Console:
    TABS = "\t" * 4

    @staticmethod
    def read(message="") -> str:
        return input(Console.TABS + message)

    @staticmethod
    def write(message):
        print(Console.TABS + message)


class Administrator:
    def __get_system_user_choice(self) -> GAMEMOVE:
        choice = random.choice(list(GAMEMOVE))
        logging.debug(f"System choice:- {choice}")
        return choice

    def is_user_interested_to_play(self) -> bool:
        ask = Console.read("Do you still want to play game?[y/yes]:").strip().upper()
        if ask in ("", "Y", "YES"):
            return True
        return False

    def get_user_input(self) -> str:
        Console.write("Enter your choice of move from below")
        for move in list(GAMEMOVE):
            Console.write(f" => {move.name} | {move.value}")
        return Console.read("What do you want to choose?: ").strip()

    def get_user_choice(self) -> GAMEMOVE:
        choice = self.get_user_input().upper()
        logging.debug(f"User provided choice with :- {choice}")
        if choice in ("1", "PAPER"):
            return GAMEMOVE.PAPER
        if choice in ("2", "ROCK"):
            return GAMEMOVE.ROCK
        if choice in ("3", "SCISSOR"):
            return GAMEMOVE.SCISSOR
        Console.write(USERMESSAGE.InvalidInput)
        if self.is_user_interested_to_play():
            return self.get_user_choice()
        raise UserQuitsException(USERMESSAGE.QuitGame)

    def is_system_winner(self, player: Player) -> bool:
        return player.id == 0

    def get_player(self, id: int = 1) -> Player:
        return Player(id=id)

    def get_system_player(self) -> Player:
        return Player(id=0)

    def get_player_choices(
        self, player: Player, system_player: Player
    ) -> tuple[Player, Player]:
        player.move = self.get_user_choice()
        system_player.move = self.__get_system_user_choice()
        Console.write(
            f"You choose {player.move.name}!. System chooses.... {system_player.move.name}"
        )
        return (player, system_player)

    def play(self, player: Player, opponent: Player) -> None:
        (player, opponent) = self.get_player_choices(player, opponent)
        winner = Judge.get_winner(player, opponent)
        if winner is None:
            Scorer.declare_draw()
        elif self.is_system_winner(winner):
            Scorer.condole_player()
        else:
            Scorer.congratulate_player()

    def play_game(self) -> None:
        Console.write(USERMESSAGE.Welcome)
        player = self.get_player()
        system_player = self.get_system_player()
        run = True
        while run is True:
            try:
                self.play(player=player, opponent=system_player)
                run = self.is_user_interested_to_play()
            except UserQuitsException:
                run = False
        Console.write(USERMESSAGE.GoodBye)


if __name__ == "__main__":
    Administrator().play_game()
