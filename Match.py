import FRCTeam
from enum import Enum


class Victor(Enum):
    BlueWins = 1
    RedWins = 2
    Tie = 3
class Match:
    #Teams should be an array
    def __init__(self, MatchNum,BlueTeams,RedTeams):
        self.MatchNum = MatchNum
        self.BlueTeams = BlueTeams
        self.RedTeams = RedTeams


    


    def Update(self,NewTeam,ReplacedTeam):
        for i in Teams:
            if Teams[i] == ReplacedTeam:
                Teams[i] = NewTeam


    def Result(self):
        BlueScore = 0
        RedScore = 0
        for Playing in BlueTeams:
            BlueScore += BlueTeams[Playing].FindAverage()
        for Playing in RedTeams:
            RedScore += RedTeams[Playing].FindAverage()
        if BlueScore > RedScore:
            return Victor.BlueWins
        if BlueScore < RedScore:
            return Victor.RedWins
        if BlueScore == RedScore:
            return Victor.Tie