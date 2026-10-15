<div align="center">

  <img src="assets/brand/app_logo_wordmark.png" alt="Nuvio TV" width="320" />

  <p>
    <strong>Una experiencia multimedia fluida, moderna y optimizada para Android TV y Smart TVs.</strong>
    <br />
    Organiza tus fuentes en una biblioteca visual con carátulas, calificaciones, subtítulos y sincronización continua.
  </p>

  <p>
    <a href="https://github.com/AlessandroA586/NuvioTV/releases/latest">
      <img src="https://img.shields.io/github/v/release/AlessandroA586/NuvioTV?color=7C3AED&label=%C3%9Altima%20Versi%C3%B3n&style=for-the-badge" alt="Release" />
    </a>
    <a href="https://github.com/AlessandroA586/NuvioTV/blob/dev/LICENSE">
      <img src="https://img.shields.io/badge/Licencia-GPL%20v3.0-blue?style=for-the-badge" alt="License" />
    </a>
    <a href="https://github.com/NuvioMedia/NuvioTV">
      <img src="https://img.shields.io/badge/Proyecto%20Original-NuvioMedia-black?style=for-the-badge&logo=github" alt="Upstream" />
    </a>
  </p>

</div>

---

> [!NOTE]
> ### 📌 Declaración del Proyecto y Reconocimiento de Derechos
> Este repositorio es una **adaptación y compilación personal independiente** (*Juansher Custom Edition*) desarrollada con fines de estudio, personalización y optimización para dispositivos Android TV.
> 
> **Todos los derechos de propiedad intelectual, marca, identidad visual y código base pertenecen íntegra y exclusivamente a sus creadores originales del equipo de [NuvioMedia](https://github.com/NuvioMedia) ([nuvio.tv](https://nuvio.tv)).**
> Expresamos nuestro más sincero agradecimiento y admiración a los autores originales por su enorme labor al concebir y compartir esta increíble plataforma de código abierto con la comunidad.

---

## ✨ Mejoras y Ajustes en esta Edición (Juansher Edition)

Esta versión incorpora refinamientos específicos diseñados para enriquecer la experiencia en televisores y TV Boxes:

- **Detección inteligente de reproducción**: Identificación precisa de la fuente que se encuentra en reproducción activa, destacándola con su etiqueta **`Reproduciendo`** y su marco de acento sin alterar la proporción visual del elemento al recibir el foco del control remoto.
- **Acceso instantáneo a fuentes**: Reutilización de los enlaces de la búsqueda inicial al consultar el panel durante la reproducción, eliminando tiempos de espera innecesarios de re-exploración y manteniendo la opción de actualización manual.
- **Foco y desplazamiento automático**: Al desplegar el menú de fuentes, la lista navega automáticamente hasta la opción en uso para facilitar la selección.
- **Optimización de estabilidad en arranque**: Corrección de cierres inesperados al inicio en launchers Android TV / Google TV.
- **Transparencia en el versionado**: Línea superior dedicada exclusivamente a la versión oficial base del autor original y línea inferior para las revisiones internas de esta edición personalizada.

---

## 📥 Descargas e Instalación

Puedes descargar los paquetes APK compilados para las diferentes arquitecturas de Android TV directamente desde la sección de versiones:

👉 **[Ver Últimas Versiones y Descargas APK](https://github.com/AlessandroA586/NuvioTV/releases/latest)**

- **`armeabi-v7a`**: Recomendado para la gran mayoría de Smart TVs y TV Sticks (Kalley, Xiaomi Mi Box, Fire TV, Chromecast con Google TV HD, etc.).
- **`arm64-v8a`**: Diseñado para dispositivos de 64 bits de mayor rendimiento (Nvidia Shield TV Pro, TV Boxes de gama alta).
- **`universal`**: Compatible con cualquier procesador Android.

---

## 🛠️ Compilación desde el código fuente

```bash
git clone https://github.com/AlessandroA586/NuvioTV.git
cd NuvioTV
./gradlew :app:assembleFullRelease
```

*Construido con Kotlin, Jetpack Compose para TV, TV Material 3 y Media3.*

---

## ⚖️ Licencia y Enlaces Oficiales

- **Sitio web oficial de los creadores:** [nuvio.tv](https://nuvio.tv)
- **Repositorio original de Nuvio:** [NuvioMedia/NuvioTV](https://github.com/NuvioMedia/NuvioTV)
- **Licencia:** Distribuido bajo los términos de la [Licencia Pública General GNU v3.0 (GPL-3.0)](./LICENSE).
