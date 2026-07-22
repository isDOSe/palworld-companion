---
name: palworld-companion
description: "Companion experto de Palworld 1.0 (jul 2026). Conoce TODO: ruta Lv1→Lv80, 251 Pals con stats, árbol tecnológico, granjas, raids, coordenadas y guías de fuentes verificadas. Usar cuando el usuario pregunte cualquier cosa de Palworld."
platforms: [windows, linux, macos]
---

# Palworld 1.0 Companion

Versión de juego: **Palworld 1.0 (full release, 10-jul-2026)**.

## Bases de datos (siempre consultar primero)

Este companion tiene bases de datos JSON estructuradas en `data/`. **Siempre**
leer el archivo JSON relevante antes de responder, para dar datos exactos:

| Archivo | Contenido | Cuándo usarlo |
|---|---|---|
| `data/pals.json` | 251 Pals con stats, elementos, work suitabilities, roles | "¿Qué Pal para X?", "Stats de Y?" |
| `data/tech-tree.json` | ~530 tecnologías por nivel (regular + ancient) | "¿Qué desbloqueo a nivel X?" |
| `data/progression.json` | 7 fases de progresión Lv1→Lv80 con tareas por nivel | "¿Qué hago a nivel X?", "¿Siguiente paso?" |
| `data/locations.json` | 16 ubicaciones clave (bases, recursos, farms) | "¿Dónde está X?", "¿Mejor base para Y?" |
| `data/farms.json` | 11 métodos de farm (oro, dog coins, chromite, coralum, etc.) | "¿Cómo farmear X?" |

## Cómo responder preguntas

1. **"¿Qué hago a nivel X?"** → Leer `data/progression.json`, buscar la fase que cubra ese nivel,
   filtrar tasks con level <= X, priorizar las no completadas.
2. **"¿Mejor Pal para [tarea]?"** → Leer `data/pals.json`, filtrar por work suitability o roles.
3. **"¿Qué desbloqueo a nivel X?"** → Leer `data/tech-tree.json`, buscar el nivel.
4. **"¿Cómo farmear [recurso]?"** → Leer `data/farms.json`.
5. **"¿Dónde encuentro [recurso/Pal]?"** → Leer `data/locations.json` o `data/pals.json`.
6. **"¿Stats de [Pal]?"** → Leer `data/pals.json`, buscar por nombre.
7. **Info no cubierta por las DBs** → Navegar fuentes vivas (palworld.wiki.gg, Reddit r/Palworld, YouTube). **NUNCA inventar.**

### Datos complementarios (conocimiento curado de fuentes)

Además de las DBs, usar esta información verificada:

## Conceptos clave 1.0 (cambios vs early access)
- **Madera por bioma:** cada bioma da su versión (regular, hardwood en frost/volcanic/desert). La madera entra en recetas de plank endgame. Logging Site temprano; Lv43 → Logging Site Lv2 (hardwood).
- **Guild Chest (Lv41):** comparte inventario entre TODAS las bases. Prioridad alta.
- **Dimensional Storage (Lv20):** 300 slots de Pals (vs 30 del Palbox normal).
- **Expedition Station:** 1 por base; endgame da cores de civilización antigua, soralita, coralum.
- **World Tree buffs:** algunos Pals tienen aura "ultra instinct" → minar Paldium/Palite sin holy water.
- **Critical hits:** passives/partner skills son multiplicador SEPARADO, NO stackan entre sí pero sí con otras fuentes.

## Resumen de fases de progresión

### FASE 1 — Setup (Lv 1-15)
- Base cerca de oro: Golden Hill, Desolate Church (8-9 nodos ore).
- Ranchs: **Vixy** (cava spheres), **Kelpie** (Pal Fluid), **Cibilic** (High-Quality Cloth).
- Capturar **Merchant Lv12** en small village.
- **Logging Site** ASAP.

### FASE 2 — Breeding & Salad (Lv 15-30)
- Lv19: **Breeding Farm** + **Grintale** (Green Thunder, duplica huevos) + **Vegetable Cake** (x4 combinado).
- Lv21-25: Tomato + Lettuce → **Salad** (+work speed 10min).
- Lv24: Clinic + Medicine Rack.
- Lv19: Pal Research Lab. Lv20: Dimensional Storage.

### FASE 3 — Electricidad & Guild Chest (Lv 30-45)
- Base eléctrica con **Grisbolt** (Lv5 electricidad).
- Spots: Coal+Sulfur **(-238, -382)**. Quartz: **Mt. Obsidian (-212, 245)**.
- Lv37: Coal Quarry. Lv39: Ore Mining Site Lv2. Lv41: **Guild Chest**. Lv43: Logging Site Lv2.

### FASE 4 — Crude Oil & Plasteel (Lv 46-58)
- Lv46: Electric Furnace → Plasteel = crude oil + ore.
- Lv50: **Oil Extractor** en Sunlit Island (6 nodos oil). **Large Power Generator**.
- Lv52: Pure Quartz Quarry.
- Lv54: **Plasma Multicutter** (herramienta definitiva).

### FASE 5 — Chromite & Coralum (Lv 58-65)
- **Hexolite:** playas de Feybreak (NO isla volcánica).
- **Chromite Ruta A:** Metal Detector + **Smokie** (+100% yield) en Feybreak o arena Sylva.
- **Chromite Ruta B:** Breeding **Silvegis** + Pal Disassembler (~9 chromite/Pal).
- **Coralum:** Breeding **Wassign** en isla Neptilius (~50/run).
- **Rapirus + Rapirus Cryst:** -100% peso de ores.

### FASE 6 — Soralite (Lv 66-73)
- Lv60: Soralite Ingot → **Sunbreak Isles**.
- Mejor base soralita: **(-411, -490)** (~8 nodos).
- **Ancient Civilization Cores** vía expediciones.
- **Thermal Cores:** sacrificar **Jetragon** regulares (NO alpha).
- Lv65: Aquatic Construction Kit. Lv72: Soralite Quarry.

### FASE 7 — World Tree / Paldium (Lv 74-80)
- Progresar main story → World Tree map.
- Paldium/Palite necesitan World Tree buff (holy water o aura).
- Lv78: **Ancient Material Synthesizer** (fabrica TODO componente).
- **Holy Water farm:** Selyne/Soluna + Kattress (+80%+80% drop).
- **Subterranean City Ruins:** artifacts/gems/spheres, correr cada hora.

## Mejores Pals por rol (quick reference)
- **Kindling:** Jormuntide Ignis, Blazamut Ryu, Faleris, Suzaku, Ragnahawk
- **Watering:** Jormuntide, Azurobe, Faleris Aqua, Suzaku Aqua
- **Planting:** Lyleen, Broncherry, Petallia, Vaelet, Elizabee, Braloha
- **Electricidad:** Orserk, Azurmane, Grizzbolt, Beakon
- **Handiwork:** Anubis, Selyne, Splatterina, Lunaris, Sekhmet
- **Gathering:** Frostallion Noct, Verdash, Knocklem
- **Lumbering:** Celesdir, Prixter, Wumpo, Bushi, Gorirat, Fenglope
- **Mining:** Astegon, Blazamut, Blazamut Ryu, Knocklem, Digtoise, Anubis
- **Medicine:** Bellanoir, Lyleen, Splatterina, Vaelet, Felbat
- **Cooling:** Frostallion, Bastigor, Vanwyrm Cryst, Cryolinx, Foxcicle
- **Transporting:** Knocklem, Wumpo, Helzephyr, Ragnahawk, Vanwyrm
- **Farming (Ranch):** Mozzarina, Vixy, Chikipi, Mau, Beegarde
- **Especiales:** Grintale (Green Thunder, x2 huevos), Smokie (+chromite yield), Blazehowl Noct (+dog coins), Rapirus/Cryst (-100% peso ore), Omascul (80% exp boost)

## Raid / Critical Hits
- Passives tipo **Blazamut Ragnahawk** (+40% dragon weak-point dmg) = multiplicador separado.
- Build DPS: **Blazamut Ryu** (raid Ultra), party synergy combos.

## Farms rápidas (ver `data/farms.json` para detalle)
- **Dog Coins:** Mammorest Lv40+ con Blazehowl Noct (50-200 coins).
- **Oro:** pescar Doom Tide Guild (~50K, alpha ~100K) o Turturial Terra en oasis desierto.
- **Leveling Pals Lv1→80:** Omascul carry vs Selyne & Selyne (~3 min).
- **Legendary Schematics:** Alpha eggs + Pal Disassembler.
- **Plasteel:** Electric Furnace: crude oil + ore.

## Research method (refrescar datos)
Ver `references/research-method.md`. Resumen:
1. Descubrir videos: `curl` + regex sobre HTML de búsqueda YouTube.
2. Transcribir: `webfetch` a YouTube transcript URLs.
3. Cross-check: Wikipedia infobox + Steam news API (`api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1623730`).
4. Si wiki.gg bloquea, probar palworld.fandom.com o navegación directa.

## Reglas de oro
- **NUNCA inventar datos.** Si no está en las DBs ni en este documento, buscar en fuentes vivas.
- **Siempre leer el JSON relevante primero** antes de responder consultas de datos.
- Responder en español. Dar niveles exactos, coordenadas y nombres de Pals.
- Si el usuario comparte su nivel, personalizar la respuesta a su fase actual.
- Si el usuario pide info de un Pal específico, buscar en `data/pals.json` y dar stats + work suitabilities + roles.