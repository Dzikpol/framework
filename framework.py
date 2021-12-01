import pandas as pd
from csv import reader

def goto(line) :
  global lineNumber
  line = lineNumber

layout_csv = 'framework - layout (1).csv'
ground_csv = 'framework - ground (2).csv'

layers = (layout_csv, ground_csv)

avatars = ['P','█','▒','☉','░','🧙']
avatar = avatars[1]

position = (5,5)

while True:
  player = {'position' : position, 'avatar' : avatar}

  get_position = player.get('position')
  x = get_position[0]
  y = get_position[1]

  get_avatar = player.get('avatar')

# get stage from the 'layout' layer
  layer = layers[0]
  file = open(layer, encoding='utf-8')
  stage = pd.read_csv(file)
  pd.set_option('display.max_columns', 10)
  
# update_stage
  stage.iat[x, y] = get_avatar

# get stage at location
  print(f"player at {position}: {stage.iloc[x, y]}")
  print(stage)

  a = input('enter position: x, y ')
  a = tuple(int(x) for x in a.split(","))
  position = a

lol = stage.values.tolist()
