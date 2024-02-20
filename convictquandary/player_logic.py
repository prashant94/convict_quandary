from abc import ABC, abstractmethod
from constants import Action, Persuasion, Belief
from typing import List

class PlayerLogic(ABC):
    
    @abstractmethod
    def get_persuasion(
        self, 
        player_actions: List[Action], 
        player_persuasions: List[Persuasion], 
        player_beliefs: List[Belief], 
        opponent_actions: List[Action], 
        opponent_persuasions: List[Persuasion]
        ) -> Persuasion:
        pass

    @abstractmethod
    def get_belief(
        self, 
        player_actions: List[Action], 
        player_persuasions: List[Persuasion], 
        player_beliefs: List[Belief], 
        opponent_actions: List[Action], 
        opponent_persuasions: List[Persuasion]
        ) -> Belief:
        pass

    @abstractmethod
    def get_action(
        self, 
        player_actions: List[Action], 
        player_persuasions: List[Persuasion], 
        player_beliefs: List[Belief], 
        opponent_actions: List[Action], 
        opponent_persuasions: List[Persuasion]
        ) -> Action:
        pass