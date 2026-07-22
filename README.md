<center><img src="https://i.postimg.cc/vThPPSsV/banner.png">
</center>
# palworld-companion

> Companion experto de progresión para **Palworld 1.0** — skill de [opencode](https://github.com/anomalyco/opencode) + web interactiva, con base de datos de 251 Pals, árbol tecnológico y guía Lv1→Lv80.

![Palworld 1.0](https://img.shields.io/badge/Palworld-1.0%20%28jul%202026%29-00d992) ![Licencia](https://img.shields.io/badge/license-MIT-818cf8) ![Hecho por](https://img.shields.io/badge/autor-DOSe-ffba00)

---

## ¿De qué va esto?

Palworld es enorme y su versión **1.0** (10-jul-2026) cambió muchas mecánicas. Esta skill es un **companion personal** que conoce todo el juego: Pals, tecnologías, recursos, ubicaciones, rutas de progresión y métodos de farm.

En lugar de buscar horas en YouTube/Wikis, le preguntas al companion y te responde con datos exactos de fuentes verificadas.

---

## Estructura del repo

```
palworld-companion/
├── SKILL.md                       # La skill principal para opencode
├── Palworld-Endgame-Guide.html    # Web interactiva (abrir en navegador)
├── data/
│   ├── pals.json                  # 251 Pals con stats, elementos, work suitabilities
│   ├── tech-tree.json             # ~530 tecnologías por nivel
│   ├── progression.json           # 7 fases de progresión Lv1→Lv80
│   ├── locations.json             # 16 ubicaciones clave
│   └── farms.json                 # 11 métodos de farm
├── scripts/
│   ├── build-db.py                # Script para reconstruir las bases de datos
│   └── build-tech-tree.py
├── references/
│   ├── research-method.md         # Cómo investigar contenido nuevo
│   └── repo-context.md            # Contexto para colaboradores
├── README.md
└── LICENSE
```

---

## Instalación (opencode)

1. Guarda la carpeta `palworld-companion` en tu directorio de skills de opencode.
2. opencode la carga automáticamente cuando preguntas sobre Palworld.
3. La skill lee las bases de datos JSON en `data/` para responder con datos exactos.

---

## Cómo usar

- *"Estoy nivel 51, ¿qué hago ahora?"* → te dice las tareas de tu fase actual.
- *"¿Cómo farmeo chromite?"* → te da las 2 rutas con Pals y passives exactos.
- *"¿Mejor Pal para kindling?"* → busca en la DB y te da el top 5 con stats.
- *"¿Qué desbloqueo a nivel 54?"* → te lista las tecnologías de ese nivel.
- *"¿Stats de Blazamut Ryu?"* → te da HP, ataque, defensa y work suitabilities.

---

## Cómo actualizar cuando Palworld cambie

1. Navegar `palworld.wiki.gg/wiki/Palpedia` y `palworld.wiki.gg/wiki/Technology` para datos frescos.
2. Revisar r/Palworld y YouTube para nuevas guías.
3. Actualizar los JSON en `data/` con `scripts/build-db.py`.
4. Editar `SKILL.md` si hay nuevas mecánicas.
5. Commit y push.

---

## Licencia

MIT — ver `LICENSE`.

## Autor

Hecho por **DOSe** para la comunidad de Palworld.
