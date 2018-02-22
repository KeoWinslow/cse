test_map = {
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': 'You are north of the house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'WEST': 'WESTHOUSE'
         }
    },
    'EASTHOUSE': {
        'NAME': 'East of House',
        'DESCRIPTION': 'You are east of the house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'WEST': 'WESTHOUSE',
         }
    },
    'WESTHOUSE': {
        'NAME': 'West of House',
        'DESCRIPTION': 'You are west of the house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'WEST': 'WESTHOUSE'
        },
    },
}
desert_map = {
    'NORTHHOSPITAL': {
        'NAME': 'North of Hospital',
        'DESCRIPTION': 'You are north of the hospital.',
        'PATHS': {
            'NORTHEAST': 'WESTKIN',
            'NORTHWEST': 'EASTYALE'
        }
    },

    'WESTKIN': {
        'NAME': 'West of Kin',
        'DESCRIPTION': 'You are west of the Kin.',
        'PATHS': {
            'SOUTH': 'EASTHAYFIELDS',
            'SOUTHWEST': 'WESTBUNKER',
        }
    },
    'EASTVERNAL': {
        'NAME': 'East of Vernal',
        'DESCRIPTION': 'You are east of the Vernal.',
        'PATHS': {
            'EAST': 'NORTHGARAGE',
            'NORTHWEST': 'EASTRADIOTOWER'
        },
    },
    'NORTHGARAGE': {
        'NAME': 'North of Garage',
        'DESCRIPTION': 'You are north of Garage.',
        'PATHS': {
            'NORTHWEST': 'NORTHGARAGE',
            'SOUTHEAST': 'WESTHARK',

        },
    },
    'SOUTHEASTTRINITY': {
        'NAME': 'Southeast of Trinity',
        'DESCRIPTION': 'You are southeast of Trinity.',
        'PATHS': {
            'SOUTHEAST': 'SOUTHEASTCEMETERY',
            'SOUTHWEST': 'WESTKIN',
        },
    },
    'SOUTHEASTCEMETERY': {
        'NAME': 'Southeast of Cemetery',
        'DESCRIPTION': 'You are southeast of Cemetery.',
        'PATHS': {
            'NORTHWEST': 'SOUTHEASTTRINITY',
            'NORTH': 'SOUTHWESTDOCKS',
        },
    },
    'NORTHPRISON': {
        'NAME': 'North of Prison',
        'DESCRIPTION': 'You are north of Prison.',
        'PATHS': {
            'SOUTH': 'WESTKORRI',
            'EAST': 'WESTFACTORY'
        }
    },
    'WESTBUNKER': {
        'NAME': 'West of Bunker',
        'DESCRIPTION': 'You are west of Bunker.',
        'PATHS': {
            'EAST': 'EASTHAYFIELDS',
        },
    },
    'EASTHAYFIELDS': {
        'NAME': 'East of Hayfields',
        'DESCRIPTION': 'You are east of Hayfields.',
        'PATHS': {
            'EAST': 'NORTHPRISON',
        },
    },
    'SOUTHMANSION': {
        'NAME': 'South of Mansion',
        'DESCRIPTION': 'You are south of Mansion',
        'PATHS': {
            'SOUTHEAST': 'WESTBUNKER',
        }
    },
    'EASTRADIOTOWER': {
        'NAME': 'East of Radio Tower',
        'DESCRIPTION': 'You are east of Radio Tower.',
        'PATHS': {
            'EAST': 'EASTRADIOTOWER',
            'SOUTH': 'SOUTHRADIOTOWER',
        },
    },
    'WESTKORRI': {
        'NAME': 'West of Korri',
        'DESCRIPTION': 'You are west of Korri.',
        'PATHS': {
            'SOUTHWEST': 'EASTBASE',
        },
    },
    'EASTYALE': {
        'NAME': 'East of Yale',
        'DESCRIPTION': 'You are east of Yale.',
        'PATHS': {
            'NORTH': 'SOUTHTOWER',
            'NORTHEAST': 'SOUTHMANSION',
        },
    },
    'WESTHARK': {
        'NAME': 'West of Hark',
        'DESCRIPTION': 'You are west of Hark.',
        'PATHS': {
            'EAST': 'EASTBASE',
            'SOUTHEAST': 'SOUTHEASTHAYFIELD',
        },
    },
    'EASTBASE': {
        'NAME': 'East of Base',
        'DESCRIPTION': 'You are east of Military Base.',
        'PATHS': {
            'EAST': 'WESTKORRI',
        },
    },
    'SOUTHTOWER': {
        'NAME': 'South of Tower',
        'DESCRIPTION': 'You are south of Radio Tower.',
        'PATHS': {
            'EAST': 'WESTKIN',
        },
    },
    'SOUTHWESTDOCKS': {
        'NAME': 'Southwest of Docks',
        'DESCRIPTION': 'You are southwest of Docks.',
        'PATHS': {
            'SOUTHWEST': 'SOUTHWESTDOCKS',
            'WEST': 'WESTDOCKS'
        }
    },
    'WESTFACTORY': {
        'NAME': 'West of Factory',
        'DESCRIPTION': 'You are west of Factory.',
        'PATHS': {
            'NORTH': 'SOUTHEASTCEMETERY',
        },
    },
}
current_node = desert_map['NORTHHOSPITAL']
directions = ['NORTH', 'NORTHEAST', 'NORTHWEST', 'WEST', 'SOUTH', 'SOUTHEAST', 'SOUTHWEST', 'EAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        name_of_node = current_node['PATHS'][command]
        current_node = desert_map[name_of_node]
    else:
        print("This command can't be recognized...Error, try again.")
