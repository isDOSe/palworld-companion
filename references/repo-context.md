# Repo Context — palworld-companion

Esta skill vive en un repositorio git público cuyo objetivo es que CUALQUIER persona
que juegue Palworld 1.0 pueda clonarla y usarla como companion de progresión.

- **Autor / mantenedor:** DOSe
- **Estado de la información:** guía comunitaria **verificada a julio de 2026** (versión
  1.0 de Palworld, full release 10-jul-2026). NO es oficial ni se promete "siempre actualizada".
- **Alcance:** ruta a endgame Lv1→Lv80, granjas, mejores Pals, raids/critical hits, dinero.
- **Cómo se construyó:** las fuentes se extrajeron en vivo (jul 2026) con `youtube-content`
  (transcripciones de KhrazeGaming, Moxsy/IGN, guías ES) + Wikipedia + Steam news API.
- **Cómo actualizar cuando Palworld cambie:**
  1. Usar skill `youtube-content` (fetch_transcript.py) sobre nuevos videos de 1.x.
  2. Navegar r/Palworld y palworld.wiki.gg (wiki.gg bloquea Cloudflare; Fandom a veces
     vacío tras 1.0; Bing a veces no da snippets — probar varias fuentes).
  3. Editar SKILL.md y Palworld-Endgame-Guide.html con los datos nuevos.
  4. Commitear y pushear. Actualizar la fecha de "verificado" en el README.
- **Lenguaje:** la skill responde en español por defecto (autor hispanohablante).

## Estructura del repo
- `SKILL.md` — la skill de Hermes Agent (frontmatter + guía).
- `Palworld-Endgame-Guide.html` — web interactiva autónoma para el jugador (abrir en navegador).
- `references/research-method.md` — cómo se descubren/transcriben videos.
- `references/repo-context.md` — este archivo.
- `README.md` — explicación para la comunidad.

## Instalación para usuario de Hermes Agent
Copiar esta carpeta a:
`%LOCALAPPDATA%\hermes\skills\palworld-companion\`
(en MSYS: `/c/Users/<user>/AppData/Local/hermes/skills/palworld-companion/`)
Reiniciar Hermes. La skill se carga sola cuando el usuario pregunta por Palworld.
