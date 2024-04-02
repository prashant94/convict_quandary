from abc import ABCMeta, abstractmethod

from .constants import Action, Belief, Persuasion


class PlayerLogic(metaclass=ABCMeta):

    def get_persuasion(
        self,
        player_actions: list[Action],
        player_persuasions: list[Persuasion],
        player_beliefs: list[Belief],
        opponent_actions: list[Action],
        opponent_persuasions: list[Persuasion],
    ) -> Persuasion:
        return Persuasion.TRUTH  # pragma: no cover

    def get_belief(
        self,
        player_actions: list[Action],
        player_persuasions: list[Persuasion],
        player_beliefs: list[Belief],
        opponent_actions: list[Action],
        opponent_persuasions: list[Persuasion],
    ) -> Belief:
        return Belief.BELIEVE  # pragma: no cover

    @abstractmethod
    def get_action(
        self,
        player_actions: list[Action],
        player_persuasions: list[Persuasion],
        player_beliefs: list[Belief],
        opponent_actions: list[Action],
        opponent_persuasions: list[Persuasion],
    ) -> Action:
        pass  # pragma: no cover
