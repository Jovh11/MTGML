#Declare Dependencies and create the variables that are needed to create the manabases

import numpy as np
import pandas as pd

df = pd.read_csv('names.csv', index_col=[0])
df = df.dropna()
decklist = pd.read_csv('Miirym.csv')
lands = pd.read_csv('lands.csv', index_col=[0])
lands = lands.dropna()

true_duals = ['Tundra', 'Scrubland', 'Plateau', 'Savannah', 'Underground Sea', 'Volcanic Island', 'Tropical Island', 'Badlands', 'Bayou', 'Taiga']
fetches = ['Flooded Strand', 'Marsh Flats', 'Arid Mesa', 'Windswept Heath', 'Polluted Delta', 'Scalding Tarn', 'Misty Rainforest', 'Bloodstained Mire', 'Verdant Catacombs', 'Wooded Foothills']
shocks = ['Hallowed Fountain', 'Godless Shrine', 'Sacred Foundry', 'Temple Garden', 'Watery Grave', 'Steam Vents', 'Breeding Pool', 'Blood Crypt', 'Overgrown Tomb', 'Stomping Ground']
tri_lands = ["Raffine's Tower", 'Raugrin Triome', "Spara's Headquarters", "Xander's Lounge", 'Zagoth Triome', "Ziatora's Proving Ground", 'Savai Triome', 'Indatha Triome', 'Ketria Triome', "Jetmir's Garden"]
check_lands = ['Glacial Fortress', 'Isolated Chapel', 'Clifftop Retreat', 'Sunpetal Grove', 'Drowned Catacomb', 'Sulfur Falls', 'Hinterland Harbor', 'Dragonskull Summit', 'Woodland Cemetery', 'Rootbound Crag']
temples = ['Temple of Enlightenment', 'Temple of Silence', 'Temple of Triumph', 'Temple of Plenty', 'Temple of Deceit', 'Temple of Epiphany', 'Temple of Mystery', 'Temple of Malice', 'Temple of Malady', 'Temple of Abandon']
filter_lands = ['Mystic Gate', 'Fetid Heath', 'Rugged Prairie', 'Wooded Bastion', 'Sunken Ruins', 'Cascade Bluffs', 'Flooded Grove', 'Graven Cairns', 'Twilight Mire', 'Fire-Lit Thicket']
gates = ['Azorius Guildgate', 'Orzhov Guildgate', 'Boros Guildgate', 'Selesnya Guildgate', 'Dimir Guildgate', 'Izzet Guildgate', 'Simic Guildgate', 'Rakdos Guildgate', 'Golgari Guildgate', 'Gruul Guildgate','Citadel Gate', 'Sea Gate', 'Black Dragon Gate', 'Cliffgate', 'Manor Gate', "Baldur's Gate", 'Basilisk Gate', 'Gateway Plaza', 'Gond Gate', 'Heap Gate', 'Thran Portal']
pain_lands = ['Adarkar Wastes', 'Caves of Koilos', 'Battlefield Forge', 'Brushland', 'Underground River', 'Shivan Reef', 'Yavimaya Coast', 'Sulfurous Springs', 'Llanowar Wastes', 'Karplusan Forest']
gain_lands = ['Tranquil Cove', 'Scoured Barrens', 'Wind-Scarred Crag', 'Blossoming Sands', 'Dismal Backwater', 'Swiftwater Cliffs', 'Thornwood Falls', 'Bloodfell Caves', 'Jungle Hollow', 'Rugged Highlands']
reveal_lands = ['Port Town', 'Shineshadow Snarl', 'Furycalm Snarl', 'Fortified Village', 'Choked Estuary', 'Frostboil Snarl', 'Vineglimmer Snarl', 'Foreboding Ruins', 'Necroblossom Snarl', 'Game Trail']
typed_duals = ['Idyllic Beachfront', 'Sunlit Marsh', 'Sacred Peaks', 'Radiant Grove', 'Contaminated Aquifer', 'Molten Tributary', 'Tangled Islet', 'Geothermal Bog', 'Haunted Mire', 'Wooded Ridgeline']
artifact_duals = ['Razortide Bridge', 'Goldmire Bridge', 'Rustvale Bridge', 'Thornglint Bridge', 'Mistvault Bridge', 'Silverbluff Bridge', 'Tanglepool Bridge', 'Drossforge Bridge', 'Darkmoss Bridge', 'Slagwoods Bridge']
snow_duals = ['Glacial Floodplain', 'Snowfield Sinkhole', 'Alpine Meadow', 'Arctic Treeline', 'Ice Tunnel', 'Volatile Fjord', 'Rimewood Falls', 'Sulfurous Mire', 'Woodland Chasm', 'Highland Forest']
slow_lands = ['Deserted Beach', 'Shattered Sanctum', 'Sundown Pass', 'Overgrown Farmland', 'Shipwreck Marsh', 'Stormcarved Coast', 'Dreamroot Cascade', 'Haunted Ridge', 'Deathcap Glade', 'Rockfall Vale']
fast_lands = ['Seachrome Coast', 'Concealed Courtyard', 'Inspiring Vantage', 'Razorverge Thicket', 'Darkslick Shores', 'Spirebluff Canal', 'Botanical Sanctum', 'Blackcleave Cliffs', 'Blooming Marsh', 'Copperline Gorge']
tango_lands = ['Prairie Stream', 'Sunken Hollow', 'Smoldering Marsh', 'Cinder Glade', 'Canopy Vista']
horizon_lands = ['Silent Clearing', 'Fiery Islet', 'Nurturing Peatland', 'Sunbaked Canyon', 'Waterlogged Grove', 'Horizon Canopy']

no_budget = [true_duals, fetches, shocks, tri_lands, filter_lands, horizon_lands]
high_budget = [fetches, shocks, tri_lands, filter_lands, tango_lands]
medium_budget = [check_lands, temples, pain_lands, reveal_lands, slow_lands, fast_lands]
low_budget = [gain_lands, gates, typed_duals, snow_duals, artifact_duals]


#Determine the mana cost and the coverted cost for ease of seperating for both an individual card and for every card in the decklist submitted.

def return_mana(name):
    row = df.loc[df['name'] == name]
    cmc = row['cmc'].values[0]
    mana_cost = row['mana_cost'].values[0]
    return cmc, mana_cost

def all_mana(names):
    all_manacosts = []
    for name in names:
        mana = return_mana(name)
        all_manacosts.append(mana)
    return all_manacosts

def mana_spread(decklist):
    cards = decklist['Name'].values
    mana = all_mana(cards)
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thirteen = []
    fourteen = []
    fifteen = []
    for val in mana:
        cmc = val[0]
        mc = val[1]
        if cmc == 1:
            one.append(mc)
        elif cmc == 2:
            two.append(mc)
        elif cmc == 3:
            three.append(mc)
        elif cmc == 4:
            four.append(mc)
        elif cmc == 5:
            five.append(mc)
        elif cmc == 6:
            six.append(mc)
        elif cmc == 7:
            seven.append(mc)
        elif cmc == 8:
            eight.append(mc)
        elif cmc == 9:
            nine.append(mc)
        elif cmc == 10:
            ten.append(mc)
        elif cmc == 11:
            eleven.append(mc)
        elif cmc == 12:
            twelve.append(mc)
        elif cmc == 13:
            thirteen.append(mc)
        elif cmc == 14:
            fourteen.append(mc)
        elif cmc == 15:
            fifteen.append(mc)
    all_costs = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen]
    return all_costs

#breakdown a list of cards into the relative amounts of the colored symbols needed to cast them the value that matters the most 
# in determining the spread of land cards used in a manabase     

def manatyping(listofmana):
    symbols = {}
    white = []
    blue = []
    black = []
    red = []
    green = []
    wingding = []
    for val in listofmana:
        w = val.count('W')
        u = val.count('U')
        b = val.count('B')
        r = val.count('R')
        g = val.count('G')
        c = val.count('C')
        white.append(w)
        blue.append(u)
        black.append(b)
        red.append(r)
        green.append(g)
        wingding.append(c)
    # print(listofmana)
    symbols['White'] = sum(white)
    symbols['Blue'] = sum(blue)
    symbols['Black'] = sum(black)
    symbols['Red'] = sum(red)
    symbols['Green'] = sum(green)
    symbols['Colorless'] = sum(wingding)
    return symbols

#Creates a breakdown of the number of symbols per casting cost

def manas(decklist):
    spread = mana_spread(decklist)
    i = 0
    breakdown = {}
    for mana in spread:
        if mana:
            i+=1
            symbols = manatyping(mana)
            total_pips = sum(symbols.values())
            white_pct = symbols['White'] / total_pips
            blue_pct = symbols['Blue'] / total_pips
            black_pct = symbols['Black'] / total_pips
            red_pct = symbols['Red'] / total_pips
            green_pct = symbols['Green'] / total_pips
            colorless_pct = symbols['Colorless'] / total_pips
            all_pct = [white_pct, blue_pct, black_pct, red_pct, green_pct, colorless_pct]
            breakdown[i] = all_pct
    return breakdown
#defines percentages of mana needed for each color between low, medium and high casting costs which are used to 
# give weight to the stages of the game at which one needs to mana to play these spells

def mana_ranges(decklist):
    breakdown = manas(decklist)
    bounds = breakdown.keys()
    all_bounds = []
    for key in bounds:
        all_bounds.append(key)
    upper_bound = all_bounds[-1]
    low_mana = []
    mid_mana = []
    high_mana = []
    for i in range(1,4):
        if breakdown[i]:
            value = breakdown[i]
            low_mana.append(value)
    for i in range(4,7):
        if breakdown[i]:
            value = breakdown[i]
            mid_mana.append(value)
    for i in range(7,(upper_bound + 1)):
        if breakdown[i]:
            value = breakdown[i]
            high_mana.append(value)
    return low_mana, mid_mana, high_mana

def count_calc(pct_lists):
    white_count = 0
    blue_count = 0
    black_count = 0
    red_count = 0
    green_count = 0
    colorless_count = 0
    for list in pct_lists:
        white = list[0]
        blue = list[1]
        black = list[2]
        red = list[3]
        green = list[4]
        colorless = list[5]
        if white > 0:
            white_count += 1
        if blue > 0:
            blue_count += 1
        if black > 0:
            black_count += 1
        if red > 0:
            red_count += 1
        if green > 0:
            green_count += 1
        if colorless > 0:
            colorless_count += 1
    overall_count = [white_count, blue_count, black_count, red_count, green_count, colorless_count]
    return overall_count

def mana_breakdown(manalists):
    white = 0
    blue = 0
    black = 0
    red = 0 
    green = 0
    colorless = 0
    for list in manalists:
        white += list[0]
        blue += list[1]
        black += list[2]
        red += list[3]
        green += list[4]
        colorless += list[5]
    overall_pips = [white, blue, black, red, green, colorless]
    return overall_pips

#Take the overall pct of the mana that appears for each color and then noramlize against the number of instances that it appears in its range (i.e. If there is green at 1,2,3 you would take
# the sum of the percentages and divide by 3 to get the true pct.) Then for each approximate value of the mana a scaling factor based on importance (1.5, 1 or 0.5) is multiplied to its value
# Finally each of these percentages are added for each range in each color and normalized against each other to show the true weighted value of each color.

def mana_pct(decklist):
    low_mana, mid_mana, high_mana = mana_ranges(decklist)
    low_divisors = count_calc(low_mana)
    mid_divisors = count_calc(mid_mana)
    high_divisors = count_calc(high_mana)
    low_pct = mana_breakdown(low_mana)
    mid_pct = mana_breakdown(mid_mana)
    high_pct = mana_breakdown(high_mana)
    true_pct = []
    for i in range(0,6):
        if low_divisors[i]:
            low = (low_pct[i]/low_divisors[i]) * 1.5
        else:
            low=0
        if mid_divisors[i]:
            mid = (mid_pct[i]/mid_divisors[i])
        else:
            mid = 0
        if high_divisors[i]:
            high = (high_pct[i]/high_divisors[i]) * 0.5
        else:
            high = 0 
        true = (low + mid + high) / 3
        true_pct.append(true)
    return true_pct

# Next each card in the deck the color values of the spells are now being determined for searching out the non-basic lands that we will be using.

def color_identity(decklist):
    names = decklist['Name'].values
    identities = []
    for name in names:
        searched = lands.loc[lands['name'] == name]
        identity = searched['color_identity'].values[0]
        if identity not in identities:
            identities.append(identity)
    return identities

def identity_search(land_list):
    target_ids = color_identity(decklist)
    non_basics = {}
    for lists in land_list:
        for land in lists:
            specific_land = lands.loc[lands['name'] == land]
            identity = specific_land['color_identity'].values[0]
            if identity in target_ids:
                non_basics[land] = identity
    return non_basics

# Next (and this will be changed in time) we determine which types of non-basic lands are being used. I broke down the (sometimes overwhelimg cost of a mana base into four tiers of
# expense and these were then used to determine which non-basics you want as it is likely at least for commander you want some number of basic lands)

def land_budget():
    budget = input('Is your budget low, medium, high, or unlimited?')
    land_list = []
    if budget.lower() == 'low':
        land_list = low_budget
    elif budget.lower() == 'medium':
        land_list = medium_budget
    elif budget.lower() == 'high':
        land_list = high_budget
    else:
        land_list = no_budget
    return land_list

# Finally with all of this information readily available the deck is taken in and these functions are all run together to determine which and how many non-basics should be chosen
# and then the number of basics was determined by the number of empty deck slots that are available. Subtracted by the number of non-basics that have been added.

def reccomendation(decklist, land_count=100-len(decklist['Name'])):
    true_pct = mana_pct(decklist)
    budget = land_budget()
    non_basics = identity_search(budget)
    land_count = land_count - len(non_basics)
    true_count = [value * land_count for value in true_pct]
    white_sources = round(true_count[0])
    blue_sources = round(true_count[1])
    black_sources = round(true_count[2])
    red_sources = round(true_count[3])
    green_sources = round(true_count[4])
    colorless_sources = round(true_count[5])
    color_count = [white_sources, blue_sources, black_sources, red_sources, green_sources, colorless_sources]
    colors = ['Plains', 'Islands', 'Swamps', 'Mountains', 'Forests', 'Wastes']
    colors_present = {}
    i = 0
    while i < len(color_count):
        if color_count[i] > 0:
            colors_present[colors[i]] = color_count[i]
            i+=1
        else:
            i+=1
    print('I suggest that you run')
    for basic in list(colors_present.keys()):
        print(f'{colors_present[basic]} {basic}')
    list_nonbasics = list(non_basics.keys())
    for card in list_nonbasics:
        print(card)

reccomendation(decklist)