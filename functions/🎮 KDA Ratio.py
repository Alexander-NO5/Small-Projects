#In some online multiplayer games, there's a KDA ratio to evaluate a player's in-game performance:

def kda(k, d, a):
  kda = (k + a) / d
  return kda

print(kda(20, 10, 15))
