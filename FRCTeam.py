class FrcTeam:
    def __init__(self,scores,average,matches):
        self.scores = scores
        self.average = average
        self.matches = matches

    def FindAverage(self):
        total = 0
        for i in scores:
            total += scores[i]
            self.average = total/len(scores)