# Git-Hinweise zur Fahnenkorrektur (GitHub Desktop)

Stand: 14.10.2026

## Ausgangslage

- Die Korrekturen (alle ●-Punkte aus `Fahnenkorrektur_Springer_LNM1184.md`) liegen auf dem Branch **fahnenkorrektur** in vier Commits:
  - Teil I
  - Teil II (inkl. „Part I“ → „Part-I“ auf S. 174)
  - Teil III
  - Teil IV, Updated Notes, Nachtrag Teil III
- **main** ist unverändert und enthält den Stand vor den Korrekturen.
- Der Branch ist noch nicht auf GitHub (nicht gepusht).

## Eine Datei, zwei Fassungen

Die TeX-Dateien gibt es nur einmal auf der Platte, aber Git kennt beide Fassungen. Welche Fassung in den Dateien steht, hängt vom aktiven Branch ab:

| Aktiver Branch | Inhalt der Dateien in LN-Book-Springer |
|---|---|
| fahnenkorrektur | korrigierte Fassung |
| main | Fassung vor den Korrekturen |

In GitHub Desktop wechselst du den Branch oben über **Current Branch**. Dort wählst du main oder fahnenkorrektur.

Vor jedem Wechsel sollte links unter **Changes** nichts stehen. Sonst fragt GitHub Desktop, ob die Änderungen mitgenommen oder zwischengespeichert (stash) werden sollen.

## Änderungen ansehen

- **History** (links oben): Klick auf einen Commit zeigt alle geänderten Dateien mit den Unterschieden.
- Rechtsklick auf eine Datei → **Show in Finder** oder **Open in External Editor**.

## Weiteres Vorgehen

- **Auf GitHub hochladen, ohne main zu ändern:** Branch fahnenkorrektur aktiv → **Publish branch** (oben rechts).
- **In main übernehmen:**
  1. Auf **main** wechseln.
  2. Menü **Branch → Merge into Current Branch…** → fahnenkorrektur wählen → **Create a merge commit**.
  3. **Push origin**.
  Alternativ nach dem Publish auf GitHub einen Pull Request erstellen (**Branch → Create Pull Request**).
- **Einzelnen Teil zurücknehmen:** in **History** Rechtsklick auf den Commit → **Revert Changes in Commit**.
- **Alles verwerfen:** auf main wechseln, dann **Branch → Delete…** für fahnenkorrektur. Erst machen, wenn du sicher bist.

## Hinweis zu den md-Dateien in LN-Proof

Die Arbeitsliste und diese Hinweise sind nur im Branch fahnenkorrektur committet. Wechselst du auf main, verschwinden sie aus dem Ordner LN-Proof. Beim Zurückwechseln sind sie wieder da. Nach dem Merge in main sind sie in beiden Branches.
