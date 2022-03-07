# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def climbingLeaderboard(ranked, player):
    ranked.sort(reverse=True)
    answer = []
    ranking = [1]

    for i in range(1, len(ranked)):
        if ranked[i] == ranked[i-1]:
            ranking.append(ranking[-1])
        else:
            ranking.append(ranking[-1] + 1)

    start = len(ranked)-1
    for p in player:
        while p > ranked[start]:
            start -= 1
            if start < 0:
                break
        if p < ranked[start]:
            rank = ranking[start] + 1
        elif p == ranked[start]:
            rank = ranking[start]
        else:
            rank = 1

        answer.append(rank)

    return answer
