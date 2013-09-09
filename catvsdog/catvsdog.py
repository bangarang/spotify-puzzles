__author__ = "Alex Rock"
__email__ = "hi@lxrck.com"
__date__ = "2013-9-9"

import sys
# Obtained from: http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
from bipartite_match import bipartiteMatch

class CatVsDog:
    def resolve(self):
        bipartiteByCat = {}
        catLovers = []
        dogLover = {}
        dogHater = {}
        count = 0

        for vote in votes:
            vote = "%s %d" % (vote, count)
            count += 1
            if vote[0] == 'D':
                voteParts = vote.split()

                if voteParts[0] in dogLover:
                    dogLover[voteParts[0]].add(vote)
                else:
                    dogLover[voteParts[0]] = set([vote])
                if voteParts[1] in dogHater:
                    dogHater[voteParts[1]].add(vote)
                else:
                    dogHater[voteParts[1]] = set([vote])
            else:
                catLovers.append(vote)

        for catVote in catLovers:
            catVoteParts = catVote.split()
            bipartiteByCat[catVote] = dogLover.get(catVoteParts[1], set()) | dogHater.get(catVoteParts[0], set())

        maxMatching, pred, unlayered = bipartiteMatch(bipartiteByCat)

        return len(votes) - len(maxMatching)

    def __init__(self, inVotes):
        votes = inVotes


if __name__ == "__main__":

    lines = sys.stdin.readlines()
    problems = int(lines[0])
    j = 1

    for problem in xrange(0, problems):
        problem_info = map(int, lines[j].split())
        votes = []
        j += 1
        for problem_line in xrange(0, problem_info[2]):
            votes.append(lines[j])
            j += 1

        print CatVsDog(votes).resolve()