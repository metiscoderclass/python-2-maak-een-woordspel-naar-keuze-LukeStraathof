import random

woorden = ["aankleden", "fles", "bedekt", "infectie", "schrijfmachine", "grafheuvel", "zuiver", "stadion", "oorbeschermer", "vaas", "leeftijd", "appel", "ontvoeren", "januari", "blind", "miljoen", "gedicht", "granen", "senaat", "ceremonie", "wrat", "vleugel", "walvis", "linkshandige", "fan", "helikopter", "ober", "voorvader", "octopus", "wrijven"]
def woordlijststreepjes(geradenletters, woord):
  resultaat = ""

  for i in woord:
    if i in geradenletters:
      resultaat = resultaat + i
    else:
      resultaat = resultaat + "_"

  return resultaat



def naamvragen():
  print("Welkom bij")
  print("  ___    __    __    ___   ____  ____")
  print(" / __)  /--\  (  )  / __) (_  _)( ___)")
  print("( (_-. /(__)\  )(__( (_-..-_)(   )__)")
  print(" \___/(__)(__)(____)\___/\____) (____)")


def lettercheck():
  woord = random.choice(woorden)
  aantal_slecht = 0
  doorgaan = True
  geradenletters = []
  
  while doorgaan:
    letter = input("Kies een letter of kies ? om het geheime woord te raden: ").lower()
    alphabetcheck = letter.isalpha()
    if alphabetcheck == True:
      if len(letter) != 1:
        print("dit mag niet, probeer het maar opnieuw.")
      elif letter in geradenletters:
        print("Dit heb je al geraden, probeer het maar opnieuw.")
      else:
        geradenletters.append(letter)

        if letter in woord:
          print("Je hebt de volgende letters goed geraden:", woordlijststreepjes(geradenletters, woord))
        else:
          aantal_slecht += 1
          if aantal_slecht == 1:
            print("_________")
            print("|/")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|___")
          elif aantal_slecht == 2:
            print("_________")
            print("|/       |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|___")
          elif aantal_slecht == 3:
            print("_________")
            print("|/       |")
            print("|       ( )")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|___")
          elif aantal_slecht == 4:
            print("_________")
            print("|/       |")
            print("|       ( )")
            print("|       /|\ ")
            print("|")
            print("|")
            print("|")
            print("|___")
    else:
      if letter == "?":
        raad_woord = input("Raad het geheime woord: ").lower()
        if raad_woord == woord:
          print("Je hebt het goed, het woord was", woord + ".")
          if input("Wil je opnieuw spelen? ")  == "ja":
            aantal_slecht = 0
            geradenletters = []
            woord = random.choice(woorden)
          else:
            doorgaan = False
      else:
        print("dit mag niet, probeer het maar opnieuw.")
    geradenletters += letter
    if woordlijststreepjes(geradenletters, woord) == woord:
      print("Je hebt het goed, het woord was", woord + ".")
      if input("Wil je opnieuw spelen? ")  == "ja":
        aantal_slecht = 0
        geradenletters = []
        woord = random.choice(woorden)
      else:
        doorgaan = False
    if aantal_slecht == 5:
      print("_________")
      print("|/       |")
      print("|       ( )")
      print("|       /|\ ")
      print("|       / \ ")
      print("|")
      print("|")
      print("|___")
      print("Game over")
      print("Het juiste woord was:", woord)
      if input("Wil je opnieuw spelen? ")  == "ja":
        aantal_slecht = 0
        geradenletters = []
        woord = random.choice(woorden)
      else:
        doorgaan = False

naamvragen()
lettercheck()