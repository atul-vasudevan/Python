import sys


class Poker:

    def __init__(self, file):
        self.hands_won = [0,0]
        self.play_poker(file)
        return


    def play_poker(self, file):
        # with open(file) as f:
        #     for hands in f:
        #         hands = hands.split()
        #         p1 = hands[:5]
        #         p2 = hands[5:]
        #         self.compare_hands(p1, p2)
        if len(sys.argv) < 10:
            print("Insufficient arguements!")
        p1 = sys.argv[1:6]
        p2 = sys.argv[6:]
        self.compare_hands(p1, p2)
        print("Player 1: {} hands".format(self.hands_won[0]))
        print("Player 2: {} hands".format(self.hands_won[1]))

        return


    def compare_hands(self, p1, p2):
        p1 = self.rank_hands(p1)
        p2 = self.rank_hands(p2)

        for i in range(len(p1)):
            if p1[i] > p2[i]:
                self.hands_won[0] += 1
                return
            elif p1[i] < p2[i]:
                self.hands_won[1] += 1
                return

        return


    def rank_hands(self, player):
        p_flush = 11 * (len(set(x[1] for x in player)) == 1)
        p_values = self.sort_input(player)
        p_rank = self.rank_values(p_values)
        
        if p_rank[0] == 10 or p_rank[0] == 0:
            p_rank[0] += p_flush
        else:
            p_rank[0] = max(p_rank[0], p_flush)

        return p_rank


    def sort_input(self, player):
        card_value_dict = {str(i): i for i in range(2,10)}
        card_value_dict["T"] = 10
        card_value_dict["J"] = 11
        card_value_dict["Q"] = 12
        card_value_dict["K"] = 13
        card_value_dict["A"] = 14

        p_values = [x[0] for x in player]
        p_values = sorted(((p_values.count(x), card_value_dict[x]) for x in p_values), reverse=True)
        
        return p_values

    
    def rank_values(self, p_values):        
        p_rank = self.check_rank(p_values) + [x[1] for x in p_values]
        return p_rank


    def check_rank(self, values):
        straight = any(values[i][1]-values[0][1]+i for i in range(len(values)))
        if not straight:
            return [10]
        else:
            val = sum(values[i][0] for i in range(len(values)) if values[i][0] != 1)
            return [val]

        return


if __name__ == "__main__":
    Game = Poker(sys.argv[1])

