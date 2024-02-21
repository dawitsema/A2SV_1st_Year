class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        
        play_pt = train_pt = 0
        while play_pt < len(players) and train_pt < len(trainers):
            if players[play_pt] <= trainers[train_pt]:
                count += 1
                play_pt += 1
                train_pt += 1
            else:
                train_pt += 1
        
        return count
        