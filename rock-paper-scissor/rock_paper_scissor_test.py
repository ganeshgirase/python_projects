import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from rock_paper_scissor import Judge, Administrator, Scorer, Player, GameMove, UserMessage, UserQuitsException

class TestJudge(TestCase):

    def test_should_return_correct_winner_for_paper_rock_combination(self):
        combinations = (
            (GameMove.PAPER, GameMove.ROCK),
            (GameMove.ROCK, GameMove.SCISSOR),
            (GameMove.SCISSOR, GameMove.PAPER),
        )
        for (move1, move2) in combinations:
            player1 = Player(1, move1)
            player2 = Player(2, move2)
            winner = Judge.get_winner(player1, player2)
            err = f"Judge given incorrect result for {move1.name} - {move2.name} combination"
            assert winner == player1, err
            winner = Judge.get_winner(player2, player1)
            assert winner == player1, err

    def test_should_return_none_if_both_player_choose_same_GameMove(self):
        err = "Incorrect result! Expected draw!! "
        assert Judge.get_winner(Player(1, GameMove.ROCK), Player(1, GameMove.ROCK)) is None, err
        assert Judge.get_winner(Player(1, GameMove.SCISSOR), Player(1, GameMove.SCISSOR)) is None, err
        assert Judge.get_winner(Player(1, GameMove.PAPER), Player(1, GameMove.PAPER)) is None, err

class TestScorer(TestCase):

    @patch("rock_paper_scissor.Console")
    def test_congratulate_player(self, mock_console):
        Scorer.congratulate_player()
        mock_console.write.assert_called_once_with(UserMessage.Congratulations)

    @patch("rock_paper_scissor.Console")
    def test_condole_player(self, mock_console):
        Scorer.condole_player()
        mock_console.write.assert_called_once_with(UserMessage.Condole)

    @patch("rock_paper_scissor.Console")
    def test_declare_draw(self, mock_console):
        Scorer.declare_draw()
        mock_console.write.assert_called_once_with(UserMessage.Draw)


class TestAdministartor(TestCase):
    admin = Administrator()

    def test_check_if_user_interested_to_continue_game(self):
        errmsg = "System is behaving incorretly opposite to user ask !!"
        with patch("rock_paper_scissor.Console") as mock_console:
            mock_console.read.return_value = "y"
            assert self.admin.is_user_interested_to_play() is True, errmsg
            mock_console.read.return_value = "yes"
            assert self.admin.is_user_interested_to_play() is True, errmsg
            # Test for blank input
            mock_console.read.return_value = ""
            assert self.admin.is_user_interested_to_play() is True, errmsg

            mock_console.read.return_value = "n"
            assert self.admin.is_user_interested_to_play() is False, errmsg
            mock_console.read.return_value = "no"
            assert self.admin.is_user_interested_to_play() is False, errmsg

    def test_should_return_if_system_is_winner(self):
        assert self.admin.is_system_winner(Player(id=0)) is True, "Incorrect system user!"
        assert self.admin.is_system_winner(Player(id=1)) is False, "Incorrect system user!"

    def test_should_return_player_with_given_id(self):
        id = 2
        player = self.admin.get_player(id)
        assert player.id == id, "Incorrect Player received !!"

    def test_should_return_system_user(self):
        player = self.admin.get_system_player()
        assert player.id == 0, "Incorrect system Player received !!"

    def test_should_get_user_choice_correct(self):
        self.admin.get_user_input = MagicMock()
        errmsg = "incorrect interpretation of user input of choice"
        self.admin.get_user_input.return_value = str(GameMove.PAPER.value)
        assert self.admin.get_user_choice() == GameMove.PAPER, errmsg
        self.admin.get_user_input.return_value = str(GameMove.ROCK.value)
        assert self.admin.get_user_choice() == GameMove.ROCK, errmsg
        self.admin.get_user_input.return_value = str(GameMove.SCISSOR.value)
        assert self.admin.get_user_choice() == GameMove.SCISSOR, errmsg

        # Test for string upper case values
        self.admin.get_user_input.return_value = GameMove.PAPER.name
        assert self.admin.get_user_choice() == GameMove.PAPER, errmsg
        self.admin.get_user_input.return_value = GameMove.ROCK.name
        assert self.admin.get_user_choice() == GameMove.ROCK, errmsg
        self.admin.get_user_input.return_value = GameMove.SCISSOR.name
        assert self.admin.get_user_choice() == GameMove.SCISSOR, errmsg

        # Test for string values
        self.admin.get_user_input.return_value = "paper"
        assert self.admin.get_user_choice() == GameMove.PAPER, errmsg
        self.admin.get_user_input.return_value = "rock"
        assert self.admin.get_user_choice() == GameMove.ROCK, errmsg
        self.admin.get_user_input.return_value = "scissor"
        assert self.admin.get_user_choice() == GameMove.SCISSOR, errmsg

    def test_get_user_choice_should_inform_player_about_incorrect_choice_input(self):
        self.admin.get_user_input = MagicMock()
        with self.assertRaises(UserQuitsException) as exp, patch("rock_paper_scissor.Console") as mock_console:
            self.admin.get_user_input.return_value = "junk value"
            self.admin.get_user_choice()
            mock_console.write.assert_called_with(UserMessage.InvalidInput) 
            self.assertEqual(str(exp.exception), UserMessage.QuitGame)

    @patch("rock_paper_scissor.Judge")
    def test_check_play_method_behaving_correctly(self, mock_judge):
        player1 = self.admin.get_player(id=1)
        player2 = self.admin.get_system_player()
        self.admin.get_player_choices = MagicMock()
        with patch("rock_paper_scissor.Console") as mock_console:
            self.admin.get_player_choices.return_value = (player1, player2)            
            mock_judge.get_winner.return_value = player1
            self.admin.play(player1, player2)
            mock_console.write.assert_called_once_with(UserMessage.Congratulations)
            mock_console.write.reset_mock()

            mock_judge.get_winner.return_value = player2
            self.admin.play(player1, player2)
            mock_console.write.assert_called_once_with(UserMessage.Condole)
            mock_console.write.reset_mock()

            mock_judge.get_winner.return_value = None
            self.admin.play(player1, player2)
            mock_console.write.assert_called_once_with(UserMessage.Draw)
            mock_console.write.reset_mock()


if __name__ == "__main__":
     unittest.main()