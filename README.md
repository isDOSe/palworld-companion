# 🟢 palworld-companion

> Tu companion de progresión para **Palworld 1.0** — una skill de [Hermes Agent](https://hermes-agent.nousresearch.com) + una web interactiva de endgame, hechas para que cualquiera llegue del nivel 1 al 80 sin perderse.

![Palworld 1.0](https://img.shields.io/badge/Palworld-1.0%20%28jul%202026%29-00d992) ![Licencia](https://img.shields.io/badge/license-MIT-818cf8) ![Hecho por](https://img.shields.io/badge/autor-DOSe-ffba00)

---

## 📖 ¿De qué va esto?

Palworld es enorme y su versión **1.0** (lanzada el 10 de julio de 2026) cambió muchas
mecánicas respecto al early access. Esta skill es un **companion personal** que ya viene
"estudiado": en lugar de que tú investigues horas en YouTube/Reddit, la skill ya trae la
ruta paso a paso a endgame, las mejores granjas, los Pals clave y cómo funcionan los raids.

Pensado para que **cualquier persona que juegue Palworld** pueda:

- Saber exactamente **qué hacer a su nivel** (p. ej. "estoy en nivel 44, ¿siguiente paso?").
- Seguir una **ruta ultra-completa Lv1 → Lv80** en 7 fases.
- Consultar **mejores Pals, granjas de dinero/materiales y el sistema de critical hits**.
- Abrir una **web interactiva** con su progreso, checklist guardada y mapa de fases.

---

## 🧭 Alcance (qué cubre y qué NO)

**✅ Cubre (verificado a julio de 2026, v1.0):**
- Ruta a endgame Lv1→Lv80 dividida en 7 fases con desbloqueos por nivel y coordenadas reales.
- Granjas: Dog Coins, oro por pesca, leveling de Pals Lv1→80 en ~3 min, Legendary Schematics, Plasteel.
- Mejores Pals por rol (breeding, base, electricidad, chromite, world tree, daño).
- Sistema de **critical hits / DPS** nuevo de 1.0 (test vivo de Blazamut Ryu).
- Tips de base-building (stacking de plantations, abuso de perímetro).
- Web interactiva `Palworld-Endgame-Guide.html` con tracker de nivel y checklist persistente.

**❌ NO es (y no pretende ser):**
- **Oficial** de Pocketpair. Es una guía **comunitaria**.
- "Siempre actualizada". La info fue verificada en **julio de 2026**. Si Palworld cambia
  después, hay que actualizarla (método abajo).
- Una herramienta que juega por ti. Es conocimiento + organización, no un bot.

---

## 📂 Estructura del repo

```
palworld-companion/
├── SKILL.md                      # La skill de Hermes Agent (frontmatter + guía completa)
├── Palworld-Endgame-Guide.html  # Web interactiva autónoma (abrir en el navegador)
├── references/
│   ├── research-method.md        # Cómo se descubren/transcriben los videos fuente
│   └── repo-context.md           # Contexto del repo para colaboradores
├── README.md                     # Este archivo
└── LICENSE                       # MIT
```

---

## 🚀 Instalación

### Opción A — Usuario de Hermes Agent (quieres que la IA te acompañe)
1. Clona el repo:
   ```bash
   git clone https://github.com/TU_USUARIO/palworld-companion.git
   ```
2. Copia la carpeta `palworld-companion` a tu directorio de skills de Hermes:
   - **Windows:** `%LOCALAPPDATA%\hermes\skills\palworld-companion\`
     (en Git Bash: `/c/Users/<tu_usuario>/AppData/Local/hermes/skills/palworld-companion/`)
   - **Linux/macOS:** `~/.hermes/skills/palworld-companion/`
3. Reinicia Hermes Agent.
4. Pregúntale lo que sea de Palworld. La skill se carga sola.

> Requisito: la skill usa internamente `youtube-content` para actualizar fuentes. No es
> necesaria para usar la guía, solo para refrescarla.

### Opción B — Solo quieres la web guía (sin IA)
Abre `Palworld-Endgame-Guide.html` en cualquier navegador (doble clic). Es un archivo
autónomo: no necesita internet salvo las fuentes de letra. Tu checklist se guarda en el
navegador (localStorage).

---

## 🎮 Cómo se usa la skill (ejemplos)

- *"Soy nivel 44, ¿qué hago ahora?"* → te lista las tareas de la Fase 3 final y Fase 4.
- *"¿Me armas la ruta de chromite?"* → paso a paso de la Fase 5.
- *"¿Cuál es el mejor Pal para mi base de electricidad?"* → Grisbolt / Orzerk.
- *"Explícame los critical hits"* → sistema de 1.0 con el test de Blazamut Ryu.

---

## 🔧 Cómo se construyó (metodología)

La información no se inventó: se extrajeron y leyeron **transcripciones reales** de los
mejores videos de 1.0 (KhrazeGaming "Ultimate LVL 1-80 Progression Guide", Moxsy/IGN,
guías en español), cruzadas con Wikipedia y el feed de noticias de Steam. Detalle en
`references/research-method.md`.

---

## ♻️ Cómo actualizar la skill cuando Palworld cambie

1. Usa la skill `youtube-content` (`fetch_transcript.py`) sobre nuevos videos de la versión X.
2. Revisa r/Palworld y la wiki (nota: wiki.gg bloquea Cloudflare; Fandom a veces queda
   vacío tras parches; Bing a veces no da snippets — prueba varias fuentes).
3. Edita `SKILL.md` y `Palworld-Endgame-Guide.html` con los datos nuevos.
4. Actualiza la fecha de "verificado" en este README y en `references/repo-context.md`.
5. `git commit` y `git push`.

---

## 🤝 Contribuciones

¡Bienvenidas! Si encuentras datos obsoletos o quieres añadir secciones (p. ej. lista de
jefes, builds de raid específicos), abre un *issue* o un *pull request*. Al ser una guía
comunitaria, se mantiene viva entre todos.

---

## 📜 Licencia

MIT — úsala, modifícala y compártela libremente. Ver `LICENSE`.

---

## ✍️ Autor

Hecho por **DOSe** para la comunidad de Palworld. Si te sirvió, pásale el repo a otro
Explorer que esté perdido en el endgame. ⚡
