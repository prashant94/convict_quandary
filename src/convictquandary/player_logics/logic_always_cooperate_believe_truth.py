from ..constants import Action, Belief, Persuasion
from ..player_logic import PlayerLogic


class LogicAlwaysCooperateBelieveTruth(PlayerLogic):

    def get_action(
        self,
        player_actions: list[Action],
        player_persuasions: list[Persuasion],
        player_beliefs: list[Belief],
        opponent_actions: list[Action],
        opponent_persuasions: list[Persuasion],
    ) -> Action:
        return Action.COOPERATE
