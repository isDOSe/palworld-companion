#!/usr/bin/env python3
"""Build tech-tree.json from the raw wiki scrape data."""
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

raw = """0|Primitive Workbench|0|regular
0|Stone Axe|0|regular
0|Stone Pickaxe|0|regular
0|Hand-held Torch|0|regular
0|Wooden Club|0|regular
1|Palbox|1|regular
1|Pal Sphere|1|regular
1|Campfire|1|regular
1|Wooden Chest|1|regular
1|Repair Bench|1|regular
1|Wooden Structure Set|2|regular
1|Pal Dressing Facility|1|regular
1|Old Bow|1|regular
1|Arrow|1|regular
1|Stone Spear|2|regular
1|Shoddy Bed|1|regular
1|Straw Pal Bed|2|regular
1|Global Palbox|1|regular
2|Common Shield|2|regular
2|Cloth Outfit|2|regular
2|Cloth|1|regular
2|Feed Box|2|regular
2|Berry Plantation|2|regular
2|Ranch|2|regular
2|Normal Parachute|2|regular
2|Wooden Living Room Furniture Set|1|regular
2|Wooden Tavern Furniture Set|1|regular
2|Wooden Tavern Cabinet Furniture Set|1|regular
2|Pal Gear Workbench|2|regular
2|Fire Arrow|1|regular
2|Mounted Torch|2|regular
2|Sign|1|regular
2|Wall-Mounted Sign|2|regular
2|Rushoar Saddle|1|regular
2|Foxparks Harness|1|regular
2|Houseplant Set|1|regular
2|Monitoring Stand|2|regular
2|Bat|1|regular
2|Logging Site|2|regular
2|Stone Pit|2|regular
2|Sandbag|2|regular
2|Alarm Bell|1|regular
2|Melpaca Saddle|1|regular
2|Wall-Mounted Houseplant Set|1|regular
2|Crusher|2|regular
2|Wooden Defensive Wall|1|regular
2|Wooden Gate|2|regular
2|Hanging Trap|1|regular
2|Fireplace Set|1|regular
2|Statue of Power|2|regular
2|Small Feed Bag|1|regular
3|Tropical Outfit|3|regular
3|Tundra Outfit|3|regular
3|Hot Spring|2|regular
3|Direhowl Saddled Harness|1|regular
3|Carpet Set|1|regular
3|Primitive Furnace|3|regular
3|Three Shot Bow|2|regular
3|Feathered Hair Band|2|regular
3|Nail|1|regular
3|Ladder|1|regular
3|Bear Trap Small|1|regular
3|Antique Storage Set|1|regular
3|Egg Incubator|1|ancient
3|Metal Axe|2|regular
3|Metal Pickaxe|2|regular
3|High Quality Workbench|3|regular
3|Rayne Syndicate Flag Set|1|regular
3|Chillet Saddle|2|regular
3|Lifmunk Submachine Gun|1|regular
3|Antique Chair Set|1|regular
3|Pelt Armor|2|regular
3|Meat Cleaver|2|regular
3|Medieval Medicine Workbench|2|regular
3|Tanzee Assault Rifle|1|regular
3|Eikthyrdeer Saddle|2|regular
3|Faux Greenery Set|1|regular
3|Tidy Table Set|1|regular
3|Grappling Gun|1|ancient
3|Crossbow|2|regular
3|Metal Spear|2|regular
3|Metal Chest|2|regular
3|Cooler Box|2|regular
3|Training Dummy|2|regular
3|Tanzee Ignis Assault Rifle|2|regular
3|Antique Storage Cabinet Set|1|regular
3|Mega Sphere|2|regular
3|Sphere Workbench|3|regular
3|Average Feed Bag|2|regular
3|Wall Torch|2|regular
3|Univolt Saddle|1|regular
3|Faux Crimson Foliage Set|1|regular
3|Antique Desk Set|1|regular
3|Pal Essence Condenser|2|ancient
3|Beginner Fishing Set|2|regular
3|Wheat Plantation|2|regular
3|Mill|2|regular
3|Wooden Board|1|regular
3|Viewing Cage|2|regular
3|Arsox Saddle|1|regular
3|Nitewing Saddle|2|regular
3|Hip Lantern|2|ancient
3|Mega Shield|2|regular
3|Heat Resistant Pelt Armor|3|regular
3|Surfent Saddle|1|regular
3|Faux Golden Foliage Set|1|regular
3|Antique Bath Set|1|regular
3|Antique Mirror Set|1|regular
3|Lockpicking Tool v1|1|ancient
3|Primitive Sword|2|regular
3|Cooking Pot|2|regular
3|Heater|2|regular
3|Tombstone|1|regular
3|Pengullet Rocket Launcher|2|regular
3|Piano Furniture Set|1|regular
3|Metal Shelf Set|1|regular
3|Mega Grappling Gun|2|ancient
3|Mega Glider|2|regular
3|Cold Resistant Pelt Armor|3|regular
3|Cooler|2|regular
3|Tocotoco Gloves|2|regular
3|Pengullet Lux Rocket Launcher|2|regular
3|Bathroom Set|1|regular
3|Antique High Quality Furniture Set|1|regular
3|Ring of Mercy|2|ancient
3|Pal Labor Research Laboratory|2|regular
3|Heavy Weight Module|1|regular
3|Cement|1|regular
3|Stone Structure Set|3|regular
3|Defensive Wall|2|regular
3|Stone Gate|2|regular
3|Grintale Saddle|1|regular
3|Breeding Farm|2|ancient
3|Giga Sphere|3|regular
3|Weapon Workbench|3|regular
3|Large Toolbox|2|regular
3|Free Pal Alliance Flag Set|1|regular
3|Elphidran Saddle|2|regular
3|Tarantriss Saddle|3|regular
3|Sweepa Saddle|1|regular
3|Antique Couch Set|1|regular
3|Dimensional Pal Storage|2|ancient
3|Musket|3|regular
3|Gunpowder|2|regular
3|Coarse Ammo|1|regular
3|Tomato Plantation|2|regular
3|Flame Cauldron|2|regular
3|Bear Trap Large|2|regular
3|Bear Trap Small|1|regular"""

# Parse
tech_tree = {}
for line in raw.strip().split('\n'):
    parts = line.split('|')
    lvl = int(parts[0])
    name = parts[1]
    cost = int(parts[2])
    ttype = parts[3]
    key = str(lvl)
    if key not in tech_tree:
        tech_tree[key] = {'level': lvl, 'regular': [], 'ancient': []}
    tech_tree[key][ttype].append({'name': name, 'cost': cost})

tech_list = sorted(tech_tree.values(), key=lambda x: x['level'])

with open(os.path.join(DATA_DIR, 'tech-tree.json'), 'w', encoding='utf-8') as f:
    json.dump({'version': '1.0', 'technologies': tech_list}, f, indent=2, ensure_ascii=False)

total = sum(len(v['regular'])+len(v['ancient']) for v in tech_tree.values())
print(f'tech-tree.json: {total} technologies across {len(tech_list)} levels')