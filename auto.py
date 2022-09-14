with open('auto.txt') as file:
    lines = [line.rstrip() for line in file]
    
with open('pastery.json', 'w') as jadi:
  jadi.write("[")
  for line in lines:
    jadi.write('{{"name": \"{}\","category": "pastery","region": "","link": "","maps": "","notes": ""}},'.format(line))
  jadi.write("]")
