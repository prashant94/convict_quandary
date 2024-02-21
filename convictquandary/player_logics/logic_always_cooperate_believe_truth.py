from player_logic import PlayerLogic
from constants import Action, Persuasion, Belief
from typing import List

class LogicAlwaysCooperateBelieveTruth(PlayerLogic):

    def get_persuasion(
            self, 
            player_actions: List[Action], 
            player_persuasions: List[Persuasion], 
            player_beliefs: List[Belief], 
            opponent_actions: List[Action], 
            opponent_persuasions: List[Persuasion]
            ) -> Persuasion:
        return Persuasion.TRUTH
    
    def get_belief(
            self, 
            player_actions: List[Action], 
            player_persuasions: List[Persuasion], 
            player_beliefs: List[Belief], 
            opponent_actions: List[Action], 
            opponent_persuasions: List[Persuasion]
            ) -> Belief:
        return Belief.BELIEVE
    
    def get_action(
            self, 
            player_actions: List[Action], 
            player_persuasions: List[Persuasion], 
            player_beliefs: List[Belief], 
            opponent_actions: List[Action], 
            opponent_persuasions: List[Persuasion]
            ) -> Action:
        return Action.COOPERATE