import pandas as pd
from csv import reader

world = {'X':'Empty',
         'G': 'Ground',
         'W':'Water',
         'a': 'POI a',
         'b': 'POI b'}

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

position = (9,0)
turn = 0

while True:
  turn = turn +1
  print(f'\nturn: {turn}')

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
  get_world = world.get(stage.iat[x, y])
  print(f"player {get_avatar} at {position}: {get_world} \n")
  stage.iat[x, y] = get_avatar

  print(stage)
  
  a = input('enter position: ')
  a = tuple(int(x) for x in a.split(","))

# get stage from the 'layout' layer
  layer = layers[1]
  file = open(layer, encoding='utf-8')
  ground = pd.read_csv(file)
  if ground.iat[a] == True:
    position = a
  else:
    obstacle = world.get(stage.iat[a])
    print(f'Can not walk on {a} because it is {obstacle} : {stage.iat[a]}')
    turn = turn -1

#list of lists from dataframe
#lol = stage.values.tolist()
