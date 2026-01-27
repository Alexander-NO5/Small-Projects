class City:
  def __init__(self, name, country, population, landmarks, founding_year, football_team, fun_fact):
    self.name = name
    self.country = country
    self.population = round(population, -3)
    self.landmarks = list(landmarks)
    self.founding_year = founding_year
    self.football_team = football_team
    self.fun_fact = fun_fact

hometown = City('Ploiesti', 'Romania', 180539, ['Ploiesti Shopping City', 'Hipodrom', 'Gara de sud', 'Shaorma\'s Alley'], 1503, 'Petrolul Ploiesti', 'This city was a republic for 15h in 1870')

print(vars(hometown))
