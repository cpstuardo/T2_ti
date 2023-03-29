## Tarea 2 Taller de integración
Url api: https://tarea2cs.herokuapp.com/music_api

### Herramientas: 

Django (python) y heroku.

### Objetivo: 

Construir API REST que acepte requests GET, POST, PUT y DELETE. 
Crear/obtener/eliminar artistas, álbumes y canciones, y una vez creados, reproducir estos álbumes y canciones. 

### Descripción endpoints

Crear:
- POST /artists: crea un artista y retorna el artista creado.
- POST /artists/<artist_id>/albums: crea un álbum del artista <artist_id> y retorna el álbum creado.
- POST /albums/<album_id>/tracks: crea una canción del álbum <album_id> y retorna la canción creada.

Obtener:
- GET /artists: retorna todos los artistas.
- GET /albums: retorna todos los álbums.
- GET /tracks: retorna todas las canciones.
- GET /artists/<artist_id>: retorna el artista <artist_id>.
- GET /artists/<artist_id>/albums: retorna todos los albums del artista <artist_id>.
- GET /artists/<artist_id>/tracks: retorna todas las canciones del artista <artist_id>.
- GET /albums/<album_id>: retorna el álbum <album_id>.
- GET /albums/<album_id>/tracks: retorna todas las canciones del álbum <album_id>.
- GET /tracks/<track_id>: retorna la canción <track_id>.

Reproducir:
- PUT /artists/<artist_id>/albums/play: reproduce todas las canciones de todos los álbums del artista <artist_id>.
- PUT /albums/<album_id>/tracks/play: reproduce todas las canciones del álbum <album_id>.
- PUT /tracks/<track_id>/play: reproduce la canción <track_id>.

Eliminar (CASCADE):
- DELETE /artists/<artist_id>: elimina el artista <artist_id> y todos sus álbums.
- DELETE /albums/<album_id>: elimina el álbum <album_id> y todas sus canciones.
- DELETE /tracks/<track_id>: elimina la canción <track_id>.
