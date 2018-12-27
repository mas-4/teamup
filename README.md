# Team Up

This script programmatically comes up with the best teams based on a yaml file
of players and skill levels. It was originally developed to come up with teams
for Christmas Trivia. It is adaptable to nearly anything.

## Yaml format

The format of the yaml file must be a list of dictionaries:

    - name: <name>
      skill: <int>
    - name: <name>
      skill: <int>
    - name: <name>
      skill: <int>

I have been rating based on 1-10 but the solution should work based on any skill
rating system, so long as it is an integer.

## Command line arguments

There are three required arguments:

    -p --players    Path to the players yaml file
    -k --numteams   The number of teams to process the players into
    -n --teamsize   The size of each team to process the players into

Please note, the number of players must be evenly divisable by `k` and `n`. I
will eventually code a robuster solution.

## Output

The program creates new team assignments based on the pool of combinations
generator style. Each assignment is tested for variance. Variance is defined as
the difference between the maximum team aggregate skill level and the minimum
team aggregate skill level. The program will output each new best case as it
finds smaller levels of variance.

## Notes

From my own anecdotal and thoroughly unscientific observations, it seems like
there is a very high correlation between the size of the groups and the optimal
team up variance. This seems obvious. But I don't know enough math to prove it.
I simply recommend less, and bigger, teams.

My observation was that, on the same 20 players, I could get (with `variance =
v`, and `(k, n)`:

- `v = 8` with `(10, 2)` after ten or so minutes
- `v = 5` with `(5, 4)`
- `v = 1` with `(4, 5)` quickly
- `v = 0` with `(2, 10)` almost immediately. In fact, the program quit, which
  doesn't make sense to me.

### Acknowledgements

This solution is arrived at based on the following resources:

- [Get list of combinations for K groups of N members and L groups of M
  members](https://cmsdk.com/python/get-list-of-combinations-for-k-groups-of-n-members-and-l-groups-of-m-members.html),
  a documented question on CMSDK I found through googling.
- [All combinations of set of dictionaries into K N-sized
  groups](https://stackoverflow.com/questions/53916276/all-combinations-of-set-of-dictionaries-into-k-n-sized-groups),
  a question I asked on StackOverflow.
- The actual solution is developed from [this answer by
  @blhsing](https://stackoverflow.com/a/53918184/9691276) to my question.
- [This answer by @nicholishen](https://stackoverflow.com/a/53917051/9691276) to
  my question is also very good, but ultimately not efficient or adaptable
  enough. It produces too many combinations to sort through to get to a single
  first valid solution for my case.
