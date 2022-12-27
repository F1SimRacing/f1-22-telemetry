"""
More info is available here:
https://answers.ea.com/t5/General-Discussion/F1-22-UDP-Specification/td-p/11551274?attachment-id=607611
"""


TEAM_IDS = {
    0: 'Mercedes',
    1: 'Ferrari',
    2: 'Red Bull Racing',
    3: 'Williams',
    4: 'Aston Martin',
    5: 'Alpine',
    6: 'Alpha Tauri',
    7: 'Haas',
    8: 'McLaren',
    9: 'Alfa Romeo',
    85: 'Mercedes 2020',
    86: 'Ferrari 2020',
    87: 'Red Bull 2020',
    88: 'Williams 2020',
    89: 'Racing Point 2020',
    90: 'Renault 2020',
    91: 'Alpha Tauri 2020',
    92: 'Haas 2020',
    93: 'McLaren 2020',
    94: 'Alfa Romeo 2020',
    95: 'Aston Martin DB11 V12',
    96: 'Aston Martin Vantage F1 Edition',
    97: 'Aston Martin Vantage Safety Car',
    98: 'Ferrari F8 Tributo',
    99: 'Ferrari Roma',
    100: 'McLaren 720S',
    101: 'McLaren Artura',
    102: 'Mercedes AMG GT Black Series Safety Car',
    103: 'Mercedes AMG GTR Pro',
    104: 'F1 Custom Team',
    106: 'Prema ‘21',
    107: 'Uni - Virtuosi ‘21',
    108: 'Carlin ‘21',
    109: 'Hitech ‘21',
    110: 'Art GP ‘21',
    111: 'MP Motorsport ‘21',
    112: 'Charouz ‘21',
    113: 'Dams ‘21',
    114: 'Campos ‘21',
    115: 'BWT ‘21',
    116: 'Trident ‘21',
    117: 'Mercedes AMG GT Black Series',
}


DRIVER_IDS = {
    0: 'Carlos Sainz',
    1: 'Daniil Kvyat',
    2: 'Daniel Ricciardo',
    3: 'Fernando Alonso',
    4: 'Felipe Massa',
    6: 'Kimi Räikkönen',
    7: 'Lewis Hamilton',
    9: 'Max Verstappen',
    10: 'Nico Hulkenburg',
    11: 'Kevin Magnussen',
    12: 'Romain Grosjean',
    13: 'Sebastian Vettel',
    14: 'Sergio Perez',
    15: 'Valtteri Bottas',
    17: 'Esteban Ocon',
    19: 'Lance Stroll',
    20: 'Arron Barnes',
    21: 'Martin Giles',
    22: 'Alex Murray',
    23: 'Lucas Roth',
    24: 'Igor Correia',
    25: 'Sophie Levasseur',
    26: 'Jonas Schiffer',
    27: 'Alain Forest',
    28: 'Jay Letourneau',
    29: 'Esto Saari',
    30: 'Yasar Atiyeh',
    31: 'Callisto Calabresi',
    32: 'Naota Izum',
    33: 'Howard Clarke',
    34: 'Wilheim Kaufmann',
    35: 'Marie Laursen',
    36: 'Flavio Nieves',
    37: 'Peter Belousov',
    38: 'Klimek Michalski',
    39: 'Santiago Moreno',
    40: 'Benjamin Coppens',
    41: 'Noah Visser',
    42: 'Gert Waldmuller',
    43: 'Julian Quesada',
    44: 'Daniel Jones',
    45: 'Artem Markelov',
    46: 'Tadasuke Makino',
    47: 'Sean Gelael',
    48: 'Nyck De Vries',
    49: 'Jack Aitken',
    50: 'George Russell',
    51: 'Maximilian Günther',
    52: 'Nirei Fukuzumi',
    53: 'Luca Ghiotto',
    54: 'Lando Norris',
    55: 'Sérgio Sette Câmara',
    56: 'Louis Delétraz',
    57: 'Antonio Fuoco',
    58: 'Charles Leclerc',
    59: 'Pierre Gasly',
    62: 'Alexander Albon',
    63: 'Nicholas Latifi',
    64: 'Dorian Boccolacci',
    65: 'Niko Kari',
    66: 'Roberto Merhi',
    67: 'Arjun Maini',
    68: 'Alessio Lorandi',
    69: 'Ruben Meijer',
    70: 'Rashid Nair',
    71: 'Jack Tremblay',
    72: 'Devon Butler',
    73: 'Lukas Weber',
    74: 'Antonio Giovinazzi',
    75: 'Robert Kubica',
    76: 'Alain Prost',
    77: 'Ayrton Senna',
    78: 'Nobuharu Matsushita',
    79: 'Nikita Mazepin',
    80: 'Guanya Zhou',
    81: 'Mick Schumacher',
    82: 'Callum Ilott',
    83: 'Juan Manuel Correa',
    84: 'Jordan King',
    85: 'Mahaveer Raghunathan',
    86: 'Tatiana Calderon',
    87: 'Anthoine Hubert',
    88: 'Guiliano Alesi',
    89: 'Ralph Boschung',
    90: 'Michael Schumacher',
    91: 'Dan Ticktum',
    92: 'Marcus Armstrong',
    93: 'Christian Lundgaard',
    94: 'Yuki Tsunoda',
    95: 'Jehan Daruvala',
    96: 'Gulherme Samaia',
    97: 'Pedro Piquet',
    98: 'Felipe Drugovich',
    99: 'Robert Schwartzman',
    100: 'Roy Nissany',
    101: 'Marino Sato',
    102: 'Aidan Jackson',
    103: 'Casper Akkerman',
    109: 'Jenson Button',
    110: 'David Coulthard',
    111: 'Nico Rosberg',
    112: "Oscar Piastri",
    113: "Liam Lawson",
    114: "Juri Vips",
    115: "Theo Pourchaire",
    116: "Richard Verschoor",
    117: "Lirim Zendeli",
    118: "David Beckmann",
    121: "Alessio Deledda",
    122: "Bent Viscaal",
    123: "Enzo Fittipaldi",
    125: "Mark Webber",
    126: "Jacques Villenneuve",
    127: "Jake Hughes",
    128: "Frederik Vesti",
    129: "Olli Caldwell",
    130: "Logan Sargeant",
    131: "Cem Bölükbasi",
    132: "Ayumu Iwasa",
    133: "Clément Novalak",
    134: "Dennis Hauger",
    135: "Calan Williams",
    136: "Jack Doohan",
    137: "Amaury Cordeel",
}


TRACK_IDS = {
    0: 'Melbourne',
    1: 'Paul Ricard',
    2: 'Shanghai',
    3: 'Sakhir (Bahrain)',
    4: 'Catalunya',
    5: 'Monaco',
    6: 'Montreal',
    7: 'Silverstone',
    8: 'Hockenheim',
    9: 'Hungaroring',
    10: 'Spa',
    11: 'Monza',
    12: 'Singapore',
    13: 'Suzuka',
    14: 'Abu Dhabi',
    15: 'Texas',
    16: 'Brazil',
    17: 'Austria',
    18: 'Sochi',
    19: 'Mexico',
    20: 'Baku (Azerbaijan)',
    21: 'Sakhir Short',
    22: 'Silverstone Short',
    23: 'Texas Short',
    24: 'Suzuka Short',
    25: 'Hanoi',
    26: 'Zandvoort',
    27: 'Imola',
    28: 'Portimão',
    29: 'Jeddah',
    30: 'Miami',
}


NATIONALITY_IDS = {
    1: 'American',
    2: 'Argentinean',
    3: 'Australian',
    4: 'Austrian',
    5: 'Azerbaijani',
    6: 'Bahraini',
    7: 'Belgian',
    8: 'Bolivian',
    9: 'Brazilian',
    10: 'British',
    11: 'Bulgarian',
    12: 'Cameroonian',
    13: 'Canadian',
    14: 'Chilean',
    15: 'Chinese',
    16: 'Colombian',
    17: 'Costa Rican',
    18: 'Croatian',
    19: 'Cypriot',
    20: 'Czech',
    21: 'Danish',
    22: 'Dutch',
    23: 'Ecuadorian',
    24: 'English',
    25: 'Emirian',
    26: 'Estonian',
    27: 'Finnish',
    28: 'French',
    29: 'German',
    30: 'Ghanaian',
    31: 'Greek',
    32: 'Guatemalan',
    33: 'Honduran',
    34: 'Hong Konger',
    35: 'Hungarian',
    36: 'Icelander',
    37: 'Indian',
    38: 'Indonesian',
    39: 'Irish',
    40: 'Israeli',
    41: 'Italian',
    42: 'Jamaican',
    43: 'Japanese',
    44: 'Jordanian',
    45: 'Kuwaiti',
    46: 'Latvian',
    47: 'Lebanese',
    48: 'Lithuanian',
    49: 'Luxembourger',
    50: 'Malaysian',
    51: 'Maltese',
    52: 'Mexican',
    53: 'Monegasque',
    54: 'New Zealander',
    55: 'Nicaraguan',
    56: 'Northern Irish',
    57: 'Norwegian',
    58: 'Omani',
    59: 'Pakistani',
    60: 'Panamanian',
    61: 'Paraguayan',
    62: 'Peruvian',
    63: 'Polish',
    64: 'Portuguese',
    65: 'Qatari',
    66: 'Romanian',
    67: 'Russian',
    68: 'Salvadoran',
    69: 'Saudi',
    70: 'Scottish',
    71: 'Serbian',
    72: 'Singaporean',
    73: 'Slovakian',
    74: 'Slovenian',
    75: 'South Korean',
    76: 'South African',
    77: 'Spanish',
    78: 'Swedish',
    79: 'Swiss',
    80: 'Thai',
    81: 'Turkish',
    82: 'Uruguayan',
    83: 'Ukrainian',
    84: 'Venezuelan',
    85: 'Barbadian',
    86: 'Welsh',
    87: 'Vietnamese',
}


GAME_MODE = {
    0: 'Event Mode',
    3: 'Grand Prix',
    5: 'Time Trial',
    6: 'Splitscreen',
    7: 'Online Custom',
    8: 'Online League',
    11: 'Career Invitational',
    12: 'Championship Invitational',
    13: 'Championship',
    14: 'Online Championship',
    15: 'Online Weekly Event',
    19: 'Career ‘22',
    20: 'Career ’22 Online',
    127: 'Benchmark',
}


RULESET_IDS = {
    0: 'Practice & Qualifying',
    1: 'Race',
    2: 'Time Trial',
    4: 'Time Attack',
    6: 'Checkpoint Challenge',
    8: 'Autocross',
    9: 'Drift',
    10: 'Average Speed Zone',
    11: 'Rival Duel',
}


SURFACE_TYPES = {
    0: 'Tarmac',
    1: 'Rumble strip',
    2: 'Concrete',
    3: 'Rock',
    4: 'Gravel',
    5: 'Mud',
    6: 'Sand',
    7: 'Grass',
    8: 'Water',
    9: 'Cobblestone',
    10: 'Metal',
    11: 'Ridge',
}


PENALTY_TYPES = {
    0: 'Drive through',
    1: 'Stop Go',
    2: 'Grid penalty',
    3: 'Penalty reminder',
    4: 'Time penalty',
    5: 'Warning',
    6: 'Disqualified',
    7: 'Removed from formation lap',
    8: 'Parked too long timer',
    9: 'Tyre regulations',
    10: 'This lap invalidated',
    11: 'This and next lap invalidated',
    12: 'This lap invalidated without reason',
    13: 'This and next lap invalidated without reason',
    14: 'This and previous lap invalidated',
    15: 'This and previous lap invalidated without reason',
    16: 'Retired',
    17: 'Black flag timer',
}


INFRINGEMENT_TYPES = {
    0: 'Blocking by slow driving',
    1: 'Blocking by wrong way driving',
    2: 'Reversing off the start line',
    3: 'Big Collision',
    4: 'Small Collision',
    5: 'Collision failed to hand back position single',
    6: 'Collision failed to hand back position multiple',
    7: 'Corner cutting gained time',
    8: 'Corner cutting overtake single',
    9: 'Corner cutting overtake multiple',
    10: 'Crossed pit exit lane',
    11: 'Ignoring blue flags',
    12: 'Ignoring yellow flags',
    13: 'Ignoring drive through',
    14: 'Too many drive throughs',
    15: 'Drive through reminder serve within n laps',
    16: 'Drive through reminder serve this lap',
    17: 'Pit lane speeding',
    18: 'Parked for too long',
    19: 'Ignoring tyre regulations',
    20: 'Too many penalties',
    21: 'Multiple warnings',
    22: 'Approaching disqualification',
    23: 'Tyre regulations select single',
    24: 'Tyre regulations select multiple',
    25: 'Lap invalidated corner cutting',
    26: 'Lap invalidated running wide',
    27: 'Corner cutting ran wide gained time minor',
    28: 'Corner cutting ran wide gained time significant',
    29: 'Corner cutting ran wide gained time extreme',
    30: 'Lap invalidated wall riding',
    31: 'Lap invalidated flashback used',
    32: 'Lap invalidated reset to track',
    33: 'Blocking the pitlane',
    34: 'Jump start',
    35: 'Safety car to car collision',
    36: 'Safety car illegal overtake',
    37: 'Safety car exceeding allowed pace',
    38: 'Virtual safety car exceeding allowed pace',
    39: 'Formation lap below allowed speed',
    40: 'Formation lap parking',
    41: 'Retired mechanical failure',
    42: 'Retired terminally damaged',
    43: 'Safety car falling too far back',
    44: 'Black flag timer',
    45: 'Unserved stop go penalty',
    46: 'Unserved drive through penalty',
    47: 'Engine component change',
    48: 'Gearbox change',
    49: 'Parc Fermé change',
    50: 'League grid penalty',
    51: 'Retry penalty',
    52: 'Illegal time gain',
    53: 'Mandatory pitstop',
    54: 'Attribute assignee',
}

ACTUAL_TYRE_COMPOUND = {
    16: 'C5',  # super soft
    17: 'C4',
    18: 'C3',
    19: 'C2',
    20: 'C1',  # hard
    7: 'intermediates',
    8: 'wet',
    # F1 Classic
    9: 'dry',
    10: 'wet',
    # F2
    11: 'super soft',
    12: 'soft',
    13: 'medium',
    14: 'hard',
    15: 'wet',
}

# 3 compounds are chosen each weekend so they might not be a one to one match.
VISUAL_TYRE_COMPOUND = {
    16: 'soft',
    17: 'medium',
    18: 'hard',
    7: 'intermediates',
    8: 'wet',
    # F1 Classic
    9: 'dry',
    10: 'wet',
    # F2
    15: 'wet',
    19: 'super soft',
    20: 'soft',
    21: 'medium',
    22: 'hard',
}


WEATHER = {
    0: 'clear',
    1: 'light_cloud',
    2: 'overcast',
    3: 'light_rain',
    4: 'heavy_rain',
    5: 'storm',
}


DRIVER_STATUS = {
    0: 'in_garage',
    1: 'flying_lap',
    2: 'in_lap',
    3: 'out_lap',
    4: 'on_track',
}


SESSION_TYPE = {
    0: 'unknown',
    1: 'practice_1',
    2: 'practice_2',
    3: 'practice_3',
    4: 'short_practice',
    5: 'qualifying_1',
    6: 'qualifying_2',
    7: 'qualifying_3',
    8: 'short_qualifying',
    9: 'osq',
    10: 'race',
    11: 'race_2',
    12: 'race_3',
    13: 'time_trial',
}
