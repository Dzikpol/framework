import pandas as pd
from csv import reader

layout_csv = 'framework - layout (1).csv'
ground_csv = 'framework - ground (2).csv'

layers = (layout_csv, ground_csv)

avatars = ['P','█','▒','☉','░','🧙']
av_num = list(range(len(avatars)))

av_list = list(zip(av_num,avatars))
print(av_list)
a = input('choose avatar (0-5)')
a = int(a)

avatar = avatars[a]

position = (5,5)
turn = 0

while True:
  turn = turn +1
  print(f'turn: {turn}')
  player = {'position' : position, 'avatar' : avatar}

  get_position = player.get('position')
  x = get_position[0]
  y = get_position[1]

  get_avatar = player.get('avatar')

# get stage from the 'layout' layer
  layer = layers[0]
  file = open(layer, encoding='utf-8')
  stage = pd.read_csv(file)
  
# update_stage
  stage.iat[x, y] = get_avatar

# get stage at location
  print(f'player at {position}: {stage.iloc[x, y]}')
  print(stage)

  p = input('enter position: x, y ')
  p = tuple(int(x) for x in p.split(','))
  position = p

lol = stage.values.tolist()
lol
