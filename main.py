from constraint import Problem


def coloring_map():

  p = Problem()

  p.addVariable("WA", ["R","G","B"])
  p.addVariable("NT", ["R","G","B"])
  p.addVariable("SA", ["R","G","B"])
  p.addVariable("Q", ["R","G","B"])
  p.addVariable("NSW", ["R","G","B"])
  p.addVariable("V", ["R","G","B"])
  p.addVariable("T", ["R","G","B"])

  s1 = p.getSolution()
  print(s1)
     
  p.addConstraint(lambda a,b: a!=b,("WA","NT"))
  p.addConstraint(lambda a,b: a!=b,("WA","SA"))
  p.addConstraint(lambda a,b: a!=b,("SA","NT"))
  p.addConstraint(lambda a,b: a!=b,("SA","Q"))
  p.addConstraint(lambda a,b: a!=b,("SA","NSW"))
  p.addConstraint(lambda a,b: a!=b,("SA","V"))
  p.addConstraint(lambda a,b: a!=b,("NSW","NT"))
  p.addConstraint(lambda a,b: a!=b,("NSW","V"))
  
  s2 = p.getSolution()
  print(s2)

def scheduling_problem():
   
# On your own, figure out this scheduling problem.

# You are trying to schedule workers for the coming week. Some workers can only work on certain days. 
# Also, some workers do not get along with each other, so they cannot work on the same day. 
# Also, you have a husband and wife who need to work together on the same day. 
# You also have a new trainee who needs to work with one of two trainers.
  p = Problem()
  p.addVariable("Alice",["M","W","F"])
  p.addVariable("Bob",["M","T"])
  p.addVariable("Charlie",["T","W","TR","F"])
  p.addVariable("Danielle",["M","W","F"])
  p.addVariable("Edwin",["M","TR","F"])

  p.addConstraint(lambda a,b: a == b, ("Bob","Alice"))
  p.addConstraint(lambda a,b: a != b, ("Bob","Charlie"))
  p.addConstraint(lambda a,b: a != b, ("Danielle","Charlie"))
  p.addConstraint(lambda a,b: a != b, ("Danielle","Edwin"))
  p.addConstraint(lambda a,b: a != b, ("Danielle","Alice"))
  p.addConstraint(lambda a,b,c: a == b or a == c, ("Edwin","Charlie","Bob"))

  s1 = p.getSolution()
  print(s1)
# Here are your domains:
# * Alice can work Mon, Wed, and Fri
# * Bob can work Mon and Tue
# * Charlie can work Tue, Wed, Thu, and Fri
# * Danielle can work Mon, Wed, and Fri
# * Edwin can work Wed, Thu, and Fri

# Here are your constraints:
# * Bob has to work on the same day as Alice
# * Danielle cannot work with Charlie
# * Bob cannot work with Charlie
# * Danielle cannot work with Edwin
# * Danielle cannot work with Alice
# * Edwin needs to work with either Bob or Charlie




def main():
  coloring_map()
  scheduling_problem()
  

if __name__ == "__main__":
  main()