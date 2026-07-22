# palworld-companion · Project Map

## Arquitectura
- `SKILL.md` — Skill principal para opencode. Define cómo responder consultas de Palworld.
- `data/*.json` — Bases de datos estructuradas (fuente de verdad).
- `Palworld-Endgame-Guide.html` — Web interactiva para el jugador.
- `references/` — Documentación de metodología y contexto.
- `scripts/` — Scripts para reconstruir las DBs.

## Bases de datos
| Archivo | Entidades | Props |
|---|---|---|
| `pals.json` | 251 Pals | id, name, elements, stats (hp/attack/defense), work suitabilities (12 tipos), roles |
| `tech-tree.json` | ~530 techs | level, name, cost, type (regular/ancient) |
| `progression.json` | 7 fases | tasks por nivel con prioridad, key pals, key tech |
| `locations.json` | 16 ubicaciones | coords, tipo (base/resource/breeding/farming), fase |
| `farms.json` | 11 métodos | yield, requirements, fase, notas |

## Flujo de consultas
1. Usuario pregunta → Leer JSON relevante → Responder con datos exactos
2. Si no está en DBs → Navegar fuentes vivas (wiki.gg, Reddit, YouTube)
3. NUNCA inventar datos

## Fuentes de verdad
- palworld.wiki.gg (Palpedia, Technology, Work Suitability)
- YouTube transcripts (KhrazeGaming, Moxsy/IGN)
- Steam news API: `api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1623730`
- r/Palworld en Reddit