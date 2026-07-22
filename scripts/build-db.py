#!/usr/bin/env python3
"""Build all JSON databases from raw data."""
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# ─── PALS ───
with open(os.path.join(DATA_DIR, 'palpedia-raw.txt'), 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

WORK_KEYS = ['kindling','watering','planting','electricity','handiwork',
             'gathering','lumbering','mining','medicine','cooling','transporting','farming']

ROLES_MAP = {
    'kindling': ['Jormuntide Ignis','Blazamut Ryu','Blazamut','Faleris','Suzaku','Ragnahawk',
                 'Reptyro','Bushi','Foxparks','Rooby','Arsox','Wixen','Incineram','Pyrin',
                 'Kitsun','Blazehowl','Chillet Ignis','Gobfin Ignis','Kelpsea Ignis',
                 'Leezpunk Ignis','Tanzee Ignis','Vanwyrm','Flambelle'],
    'watering': ['Jormuntide','Azurobe','Faleris Aqua','Suzaku Aqua','Broncherry Aqua',
                 'Surfent','Elphidran Aqua','Penking','Gobfin','Celaray','Teafant','Fuack',
                 'Kelpsea','Pengullet','Croajiro'],
    'planting': ['Lyleen','Lyleen Noct','Broncherry','Petallia','Vaelet','Elizabee','Braloha',
                 'Mossanda','Dinossom','Wumpo Botan','Lullu','Caprity','Lifmunk','Tanzee',
                 'Flopie','Bristla','Robinquill','Beegarde'],
    'electricity': ['Orserk','Azurmane','Grizzbolt','Beakon','Relaxaurus Lux','Univolt',
                    'Rayhound','Dazzi','Mossanda Lux','Helzephyr Lux','Sparkit','Jolthog'],
    'handiwork': ['Anubis','Selyne','Splatterina','Lunaris','Sekhmet','Wixen Noct','Verdash',
                  'Lyleen','Katress','Gorirat','Penking','Tombat','Loupmoon','Incineram Noct',
                  'Wixen','Bushi Noct','Robinquill','Leezpunk','Depresso'],
    'gathering': ['Frostallion Noct','Verdash','Knocklem','Lullu','Petallia','Elizabee',
                  'Robinquill','Vaelet','Beegarde','Palumba','Flopie','Tombat','Lifmunk',
                  'Cattiva','Tanzee','Chikipi','Vixy','Mau','Ribbuny','Killamari'],
    'lumbering': ['Celesdir','Prixter','Wumpo','Wumpo Botan','Bushi','Gorirat','Mossanda',
                  'Dinossom','Eikthyrdeer','Reindrix','Foxcicle','Fenglope','Mammorest',
                  'Arsox','Robinquill','Elphidran','Univolt','Surfent Terra','Cryolinx'],
    'mining': ['Astegon','Blazamut','Blazamut Ryu','Knocklem','Digtoise','Anubis','Reptyro',
               'Menasting','Warsect','Xenogard','Omascul','Silvegis','Bastigor','Celesdir',
               'Dualith','Gildane','Paladius','Necromus','Bushi Noct','Mammorest Cryst',
               'Penking','Tombat','Dumud','Rushoar','Cattiva','Fuddler','Kikit','Jolthog Cryst'],
    'medicine': ['Bellanoir','Bellanoir Libero','Lyleen','Lyleen Noct','Splatterina','Vaelet',
                 'Petallia','Felbat','Sibelyx','Lovander','Katress','Wixen Noct','Cinnamoth',
                 'Flambelle','Nitemary','Prunelia','Shroomer Noct','Depresso','Hoocrates',
                 'Bristla','Cawgnito'],
    'cooling': ['Frostallion','Bastigor','Vanwyrm Cryst','Kingpaca Cryst','Sibelyx','Cryolinx',
                'Foxcicle','Hangyu Cryst','Jolthog Cryst','Swee','Mau Cryst','Pengullet',
                'Penking','Chillet','Reindrix','Wumpo','Frostplume','Muffly'],
    'transporting': ['Knocklem','Wumpo','Wumpo Botan','Helzephyr','Ragnahawk','Vanwyrm',
                     'Beakon','Mossanda','Mossanda Lux','Quivern','Jormuntide Ignis',
                     'Faleris','Faleris Aqua','Menasting','Relaxaurus','Relaxaurus Lux',
                     'Gorirat','Cryolinx','Dumud Gild','Killamari','Hangyu','Galeclaw',
                     'Nitewing','Direhowl','Surfent','Suzaku','Leifang','Kitsun'],
    'farming': ['Mozzarina','Vixy','Chikipi','Mau','Caprity','Caprity Noct','Beegarde',
                'Lamball','Cremis','Sibelyx','Woolipop','Melpaca','Flambelle'],
}

pals = []
for line in lines:
    parts = line.split('|')
    if len(parts) < 17:
        continue
    name, num, elements, hp, atk, def_, *works = parts
    work_suits = {}
    for i, key in enumerate(WORK_KEYS):
        val = int(works[i]) if i < len(works) and works[i] != '0' else 0
        work_suits[key] = val
    # Determine roles
    roles = []
    for role, pal_list in ROLES_MAP.items():
        if name in pal_list:
            roles.append(role)
    pal = {
        'id': num,
        'name': name,
        'elements': [e.strip() for e in elements.split('/')],
        'stats': {'hp': int(hp), 'attack': int(atk), 'defense': int(def_)},
        'work': work_suits,
        'roles': roles
    }
    pals.append(pal)

with open(os.path.join(DATA_DIR, 'pals.json'), 'w', encoding='utf-8') as f:
    json.dump({'version': '1.0', 'count': len(pals), 'pals': pals}, f, indent=2, ensure_ascii=False)
print(f'pals.json: {len(pals)} Pals')

# ─── PROGRESSION ───
phases = [
    {
        "phase": 1, "name": "Setup inicial", "range": "Lv 1-15",
        "focus": "Primera base, ranchs tempranos, recursos basicos",
        "tasks": [
            {"level": 1, "task": "Primera base cerca de oro (Golden Hill, Desolate Church)", "priority": "critical"},
            {"level": 5, "task": "Ranch con Vixy (cava spheres), Kelpie (Pal Fluid), Cibilic (cloth)", "priority": "high"},
            {"level": 7, "task": "Logging Site para madera (se usa hasta Lv43+)", "priority": "high"},
            {"level": 12, "task": "Capturar Merchant en small village y traerlo a base", "priority": "medium"},
            {"level": 14, "task": "Mega Sphere para capturar Pals mas fuertes", "priority": "medium"}
        ],
        "key_pals": ["Vixy", "Kelpie", "Cibilic", "Lamball", "Cattiva", "Foxparks"],
        "key_tech": ["Palbox", "Pal Sphere", "Campfire", "Ranch", "Logging Site", "Stone Pit", "Mega Sphere"]
    },
    {
        "phase": 2, "name": "Breeding & Salad", "range": "Lv 15-30",
        "focus": "Breeding Farm, salad, medicina, research lab",
        "tasks": [
            {"level": 19, "task": "Breeding Farm + Green Thunder (Grintale) + Vegetable Cake (x4 huevos)", "priority": "critical"},
            {"level": 21, "task": "Tomato Plantation", "priority": "high"},
            {"level": 24, "task": "Clinic + Medicine Rack + Pal con Medicine Production", "priority": "high"},
            {"level": 25, "task": "Lettuce Plantation → Salad Farm (+work speed 10min)", "priority": "high"},
            {"level": 19, "task": "Pal Research Lab (usa ancient pal manuscripts)", "priority": "medium"},
            {"level": 20, "task": "Dimensional Storage (300 slots de Pals)", "priority": "high"},
            {"level": 24, "task": "Mining Site (ya puedes salir de bases solo-mineria)", "priority": "medium"}
        ],
        "key_pals": ["Grintale", "Broncherry Aqua", "Braloha", "Lifmunk", "Tanzee", "Penking"],
        "key_tech": ["Breeding Farm", "Tomato Plantation", "Lettuce Plantation", "Pal Research Lab", 
                     "Dimensional Pal Storage", "Egg Incubator", "Mining Site"]
    },
    {
        "phase": 3, "name": "Electricidad & Guild Chest", "range": "Lv 30-45",
        "focus": "Base electrica, coal+sulfur+quartz, Guild Chest, Logging Site Lv2",
        "tasks": [
            {"level": 30, "task": "Primera base electrica con Grisbolt", "priority": "high"},
            {"level": 33, "task": "Spot Coal+Sulfur: (-238, -382) - 6 coal, 3 sulfur", "priority": "high"},
            {"level": 35, "task": "Spot Quartz: Mt. Obsidian (-212, 245) - 9-10 nodos", "priority": "medium"},
            {"level": 37, "task": "Coal Quarry (elimina necesidad de buscar coal)", "priority": "critical"},
            {"level": 39, "task": "Ore Mining Site Lv2", "priority": "high"},
            {"level": 41, "task": "Guild Chest (compartir inventario entre bases)", "priority": "critical"},
            {"level": 43, "task": "Logging Site Lv2 (hardwood)", "priority": "high"},
            {"level": 45, "task": "Subir base a nivel maximo para +trabajadores y 3a base", "priority": "high"}
        ],
        "key_pals": ["Grisbolt", "Orserk", "Anubis", "Sekhmet", "Digtoise", "Tombat", "Wixen"],
        "key_tech": ["Coal Mine", "Ore Mining Site II", "Guild Chest", "Logging Site II",
                     "Power Generator", "Weapon Workbench", "Giga Sphere", "Hyper Sphere",
                     "Sulfur Mine"]
    },
    {
        "phase": 4, "name": "Crude Oil & Plasteel", "range": "Lv 46-58",
        "focus": "Oil Extractor, Plasteel, Plasma Multicutter, Pure Quartz Quarry",
        "tasks": [
            {"level": 46, "task": "Sulfur Quarry + Electric Furnace → Plasteel = crude oil + ore", "priority": "critical"},
            {"level": 50, "task": "Oil Extractor en Sunlit Island (6 nodos de oil)", "priority": "critical"},
            {"level": 50, "task": "Large Power Generator (eficiencia para extractores)", "priority": "high"},
            {"level": 51, "task": "Oil Extractor automatico (menos eficiente, mas caro energia)", "priority": "low"},
            {"level": 52, "task": "Pure Quartz Quarry (desmantela bases de quartz puro)", "priority": "high"},
            {"level": 54, "task": "Plasma Multicutter (herramienta de farm definitiva)", "priority": "critical"},
            {"level": 56, "task": "Cryogenic Crusher → transforma spheres viejas en Paldium", "priority": "medium"},
            {"level": 58, "task": "Metal Detector + preparar ruta de Chromite", "priority": "high"}
        ],
        "key_pals": ["Orserk", "Jormuntide Ignis", "Blazamut", "Astegon", "Anubis", "Faleris", "Beakon"],
        "key_tech": ["Electric Furnace", "Crude Oil Extractor", "Large Power Generator", "Pure Quartz Quarry",
                     "Plasma Multicutter", "Plasteel", "Plasteel Armor", "Laser Rifle", "Ultra Sphere",
                     "Legendary Sphere"]
    },
    {
        "phase": 5, "name": "Chromite & Coralum", "range": "Lv 58-65",
        "focus": "Hexolite, Chromite con Metal Detector, Coralum con breeding",
        "tasks": [
            {"level": 58, "task": "Hexolite en playas de Feybreak (NO en isla volcanica)", "priority": "high"},
            {"level": 58, "task": "Metal Detector + Smokie (+100% yield chromite, hasta +200% condensado)", "priority": "critical"},
            {"level": 58, "task": "RUTA A chromite: Feybreak o arena de Sylva (3 nodos boss)", "priority": "high"},
            {"level": 58, "task": "RUTA B chromite: Breeding Silvegis + Pal Disassembler (~9 chromite/Pal)", "priority": "medium"},
            {"level": 60, "task": "Coralum: Breeding Wassign en isla de Neptilius (~50 coral/run)", "priority": "critical"},
            {"level": 62, "task": "Coralum schematic → Hexolite Quartz Mine automatico", "priority": "high"},
            {"level": 60, "task": "Rapirus + Rapirus Cryst → -100% peso de todos los ores", "priority": "medium"}
        ],
        "key_pals": ["Smokie", "Silvegis", "Wassign", "Rapirus", "Rapirus Cryst", "Neptilius",
                     "Blazehowl Noct", "Knocklem", "Xenogard", "Menasting"],
        "key_tech": ["Metal Detector", "Hexolite", "Gigantic Furnace", "Smokie Harness", "Coralum Ingot",
                     "Hexolite Quartz Mine", "Advanced Workshop", "Pal Disassembly Conveyor"]
    },
    {
        "phase": 6, "name": "Soralite (True Endgame)", "range": "Lv 66-73",
        "focus": "Soralite, Ancient Civilization Cores, Thermal Cores, Ancient Technologies",
        "tasks": [
            {"level": 60, "task": "Soralite Ingot schematic en Sunbreak Isles", "priority": "critical"},
            {"level": 60, "task": "Mejor base soralita: (-411, -490) borde acantilado, ~8 nodos", "priority": "high"},
            {"level": 66, "task": "Ancient Civilization Cores (expediciones)", "priority": "critical"},
            {"level": 65, "task": "Aquatic Construction Kit (construir sobre agua)", "priority": "medium"},
            {"level": 70, "task": "Thermal Cores: sacrificar Jetragon (regulares, NO alpha)", "priority": "high"},
            {"level": 70, "task": "Ancient Technologies (2 work suitabilities a la vez)", "priority": "high"},
            {"level": 72, "task": "Soralite Quarry (desbloquea mineria automatica)", "priority": "critical"}
        ],
        "key_pals": ["Jetragon", "Renoir", "Frostallion", "Frostallion Noct", "Paladius", "Necromus",
                     "Xenolord", "Bastigor", "Azurmane", "Selyne"],
        "key_tech": ["Soralite Ingot", "Soralite Quarry", "Aquatic Construction Kit", "Ancient Furnace",
                     "Ancient Workbench", "Ancient Armor", "Ancient Helm", "Ancient Shield",
                     "Ancient Kitchen", "Ancient Farm", "Ancient Clinic", "Ancient Sphere",
                     "Ancient Power Generator", "Ancient Hot Spring"]
    },
    {
        "phase": 7, "name": "World Tree / Paldium", "range": "Lv 74-80",
        "focus": "World Tree map, Paldium/Palite, Holy Water farm, Ancient Material Synthesizer",
        "tasks": [
            {"level": 74, "task": "Progresar main story → World Tree map", "priority": "critical"},
            {"level": 74, "task": "World Tree buff: Holy Water o Pal con aura ultra instinct", "priority": "critical"},
            {"level": 78, "task": "Ancient Material Synthesizer (fabrica TODO en base)", "priority": "critical"},
            {"level": 76, "task": "Holy Water farm: Selyne/Soluna + Kattress (+80%+80% drop)", "priority": "high"},
            {"level": 76, "task": "Subterranean City Ruins (cada hora, artifacts/gems/spheres)", "priority": "high"},
            {"level": 80, "task": "ENDGAME alcanzado - optimizar runs, builds, raids", "priority": "critical"}
        ],
        "key_pals": ["Selyne", "Soluna", "Kattress", "Blazamut Ryu", "Bellanoir Libero",
                     "Jormuntide Ignis", "Knocklem Ignis", "Lyleen", "Omascul", "Yakumo"],
        "key_tech": ["Ancient Material Synthesizer", "Ancient Hatchery", "Wing Pack", "Plasma Rifle",
                     "Laser Sword", "Beam Launcher", "Ancient Sphere", "Drone Launcher"]
    }
]

with open(os.path.join(DATA_DIR, 'progression.json'), 'w', encoding='utf-8') as f:
    json.dump({'version': '1.0', 'phases': phases}, f, indent=2, ensure_ascii=False)
print(f'progression.json: {len(phases)} phases')

# ─── LOCATIONS ───
locations = [
    {"name": "Golden Hill", "coords": None, "type": "base", "phase": 1, "notes": "Base inicial favorita, 8-9 nodos de ore, cerca de misiones iniciales"},
    {"name": "Desolate Church", "coords": None, "type": "base", "phase": 1, "notes": "Alternativa a Golden Hill, 8-9 nodos de ore"},
    {"name": "Small Village", "coords": None, "type": "npc", "phase": 1, "notes": "Merchant Lv12 para capturar, vende horns/pal organs/seeds/ladders"},
    {"name": "Coal+Sulfur spot", "coords": "(-238, -382)", "type": "resource", "phase": 3, "notes": "6 coal, 3 sulfur, apartado en colina (Khraze)"},
    {"name": "Quartz+Sulfur early", "coords": None, "type": "resource", "phase": 3, "notes": "6 quartz + 9 sulfur, zona amplia, algo dificil de defender"},
    {"name": "Mt. Obsidian quartz", "coords": "(-212, 245)", "type": "resource", "phase": 3, "notes": "9-10 nodos de quartz puro, inexpugnable arriba de roca"},
    {"name": "Sunlit Island", "coords": None, "type": "base", "phase": 4, "notes": "Mejor spot para Oil Extractor Lv50, 6 nodos de oil, cerca de spawn"},
    {"name": "Feybreak beaches", "coords": None, "type": "resource", "phase": 5, "notes": "Hexolite facil en playas, tambien en dungeons"},
    {"name": "Sylva boss arena", "coords": None, "type": "resource", "phase": 5, "notes": "3 nodos de chromite en su arena (ruta A con Metal Detector)"},
    {"name": "Neptilius Island", "coords": None, "type": "breeding", "phase": 5, "notes": "Wassign breeding farm para coralum"},
    {"name": "Sunbreak Isles base", "coords": "(-411, -490)", "type": "base", "phase": 6, "notes": "Borde de acantilado, ~8 nodos soralita, faciles de defender"},
    {"name": "Sunbreak Isles", "coords": None, "type": "region", "phase": 6, "notes": "Soralite Ingot schematic (Lv60), Jetragon spawn Lv70+"},
    {"name": "Desert oasis fishing", "coords": None, "type": "farming", "phase": 2, "notes": "Pescar Doom Tide Guild (sombra grande): ~50k gold, alpha ~100k"},
    {"name": "Terraria Island fishing", "coords": None, "type": "farming", "phase": 2, "notes": "Pescar Turturial Terra (medusas): decenas de miles, mas comun"},
    {"name": "World Tree map", "coords": None, "type": "region", "phase": 7, "notes": "Desbloqueado via main story, Paldium/Palite + World Tree Bark"},
    {"name": "Subterranean City Ruins", "coords": None, "type": "dungeon", "phase": 7, "notes": "World Tree, 1hr duracion, artifacts/radiant gems/ancient spheres"},
]

with open(os.path.join(DATA_DIR, 'locations.json'), 'w', encoding='utf-8') as f:
    json.dump({'version': '1.0', 'locations': locations}, f, indent=2, ensure_ascii=False)
print(f'locations.json: {len(locations)} locations')

# ─── FARMS ───
farms = [
    {
        "name": "Dog Coins", "category": "currency",
        "method": "Matar Mammorest Lv40+ con Blazehowl Noct (+drop)",
        "yield": "50-75 dog coins (hasta 200 en zonas altas)",
        "requirements": ["Blazehowl Noct", "Mammorest Lv40+"],
        "phase": 3,
        "notes": "En 1.0 los items son mas baratos. Starter Accessory Box = 50 dog coins. Merchant en iglesias con Statue of Power."
    },
    {
        "name": "Oro masivo (pesca)", "category": "gold",
        "method": "Pescar Doom Tide Guild (sombra grande) o Turturial Terra (medusas)",
        "yield": "Doom Tide: ~50K (alpha ~100K). Turturial: decenas de miles, mas comun",
        "requirements": ["Beginner Fishing Set", "Desert oasis o Terraria island"],
        "phase": 2,
        "notes": "Asustar peces con disparos resetea el spot de pesca."
    },
    {
        "name": "Leveling Pals Lv1→80", "category": "leveling",
        "method": "Omascul carry (80% exp boost) vs Selyne & Selyne normal 3 veces",
        "yield": "Lv1→80 en ~3 minutos",
        "requirements": ["Omascul con Circle Bind + Sand Twister + Apocalypse", "Seafood Salad", "Growth Acceleration Bell"],
        "phase": 6,
        "notes": "Sin usar balas del player."
    },
    {
        "name": "Legendary Schematics", "category": "materials",
        "method": "Hatch Alpha eggs + desmantelar en Pal Disassembler",
        "yield": "Schematics de charge rifle y mas",
        "requirements": ["Alpha eggs (Neptilius etc.)", "Pal Disassembly Conveyor"],
        "phase": 5,
        "notes": "Mantener transportadores fuera para no perder loot."
    },
    {
        "name": "Plasteel", "category": "materials",
        "method": "Electric Furnace: crude oil + ore",
        "yield": "Plasteel para armaduras y armas avanzadas",
        "requirements": ["Electric Furnace (Lv46)", "Oil Extractor (Lv50)", "Large Power Generator (Lv50)"],
        "phase": 4,
        "notes": "Los extractores consumen mucha energia."
    },
    {
        "name": "Chromite (Ruta A)", "category": "materials",
        "method": "Metal Detector + Smokie en Feybreak o arena de Sylva",
        "yield": "Chromite con +100% yield (Smokie), +200% condensado",
        "requirements": ["Metal Detector (Lv58)", "Smokie con harness"],
        "phase": 5,
        "notes": "Ruta preferida. 3 nodos en boss arena de Sylva."
    },
    {
        "name": "Chromite (Ruta B)", "category": "materials",
        "method": "Breeding Silvegis + Pal Disassembler",
        "yield": "~9 chromite por Silvegis",
        "requirements": ["Breeding Farm", "Silvegis padres con Lush Hospitality + Philanthropist", "Pal Disassembly Conveyor"],
        "phase": 5,
        "notes": "Semi-auto, ~150% drop + 100% breeding speed."
    },
    {
        "name": "Coralum", "category": "materials",
        "method": "Breeding Wassign en isla de Neptilius",
        "yield": "~50 coral por run",
        "requirements": ["Breeding Farm", "Wassign con Lush Hospitality + Service Minded + Philanthropist"],
        "phase": 5,
        "notes": "Usar Green Thunder + Vegetable Cake (x4 huevos)."
    },
    {
        "name": "Holy Water (World Tree)", "category": "materials",
        "method": "Selyne/Soluna + Kattress (+80%+80% drop rate)",
        "yield": "Dropea de cualquier criatura viva del mapa World Tree",
        "requirements": ["Selyne o Soluna (neutral+darkness)", "Kattress (Ember/Elechild)"],
        "phase": 7,
        "notes": "Pals que afectan 2 categorias duplican efecto. Granjas cerca en el mapa."
    },
    {
        "name": "Thermal Cores", "category": "materials",
        "method": "Craftear o sacrificar Jetragon regulares (NO alpha)",
        "yield": "Thermal Cores para tecnologias avanzadas",
        "requirements": ["Jetragon (regular)", "Sunbreak Isles Lv70+"],
        "phase": 6,
        "notes": "Tambien se pueden criar con breeding farm."
    },
    {
        "name": "Ancient Civilization Cores", "category": "materials",
        "method": "Expedition Station (1 por base)",
        "yield": "Cores + soralita + coralum pasivos",
        "requirements": ["Pal Expedition Station"],
        "phase": 3,
        "notes": "Empezar temprano para acumular para Lv66+."
    }
]

with open(os.path.join(DATA_DIR, 'farms.json'), 'w', encoding='utf-8') as f:
    json.dump({'version': '1.0', 'farms': farms}, f, indent=2, ensure_ascii=False)
print(f'farms.json: {len(farms)} farming methods')

print('\nAll databases built successfully!')