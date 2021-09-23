# this dictionary has the first line spoken by characters in the pilot of the office
office_d={}
theoffice = open('theofficepilot.txt', 'r')
for line in theoffice:
  person, words = line.split(':')
  office_d[person] = words
print(office_d['Dwight'])
print(office_d['Jim'])
print('Dwight' in office_d.keys())
print()

count={}
for character in office_d['Jan']:
  count.setdefault(character,0)
  count[character]=count[character]+1
print(count)

def word_count(str):
  counts = dict()
  words = str.split()
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
    return counts

# i dont know why but this only have me the first word. will have to keep looking into this <_<
print(office_d['Oscar'])
print(word_count(office_d['Oscar']))