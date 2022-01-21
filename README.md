<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=300px src="data/images/frog-wordcloud.png" alt="Project logo"></a>
</p>

<h1 align="center">Textarbeit mit Python - Erste Schritte</h1>
<p align="center">Workshop zum Kennenlernen der Programmiersprache Python</p>

<p align="center">Heinz-Alexander Fütterer und Selina Reinhard</p>
<p align="center">Universitätsbibliothek | Freie Universität Berlin</p>

## 🧐 About <a name="about"></a>

Python ist eine weit verbreitete Programmiersprache, die vergleichsweise einfach zu lernen ist. Dieser Workshop bietet einen Einstieg für alle, die wissen wollen, was es mit Python auf sich hat und ob die Programmierung mit Python für die eigene Arbeit mit Texten infrage kommt. Nach kurzem theoretischem Input wird die Arbeit mit Python anhand eines Beispiels anwendungsorientiert geübt.

## 📚 Inhalte <a name="contents"></a>

### Agenda

- A. Block: Motivation und Basiswissen
  - Einsatz Programmiersprachen
  - Vorteile Python
  - Grundlegende Konzepte

- B. Block: Python in der Praxis
  - Jupyter Notebooks / JupyterLab
  - Übungen: Textdaten einlesen und aufbereiten; Textdaten analysieren (nltk); Textdaten visualisieren
  - Strategien zur Problemlösung
  - Umgang mit Fehlermeldungen
  - Dokumentation verstehen

### Lernziele
- Verständnis für den Einsatz und das Potenzial von Programmiersprachen allgemein und Python im Speziellen
- Einführung zu den grundlegenden Konzepten (Datentypen, Funktionen, Bibliotheken)
- Kenntnis von Bibliotheken zu NLP am Beispiel `nltk`
- Verständnis für den Umgang mit Problemen
- Keine Angst vor Fehlermeldungen

## 🏁 Getting Started <a name="getting_started"></a>

Alle für die Teilnahme am Workshop bzw. zum Nacharbeiten benötigten Informationen und Noteboooks sind in diesem Git-Repository enthalten.

### Voraussetzungen

Eine aktuelle Python-Version (> Python 3.6) wird benötigt. Zur Installation siehe:
- https://www.python.org/downloads/
- https://wiki.python.org/moin/BeginnersGuide/Download

### Installation
Zunächst dieses Git-Repository als ZIP herunterladen und entpacken bzw. mit `git clone` klonen:
```
git clone https://github.com/FDM-FUBerlin/Textarbeit-mit-Python.git
cd Textarbeit-mit-Python/
```

Die benötigten Bibliotheken lassen sich am einfachsten mit `pipenv` installieren.
```
pip install --upgrade --user pipenv
pipenv install
pipenv run python -m nltk.downloader punkt stopwords
```

Wenn ebenfalls `JupyterLab` installiert werden soll:

```
pipenv install --dev
```

## 🎈 Nutzung <a name="usage"></a>
Die Jupyter-Notebooks in `notebooks/` sind am besten mit `JupyterLab` auszuführen:

```
pipenv run jupyter lab
```

Alle Notebooks können mit folgendem Befehl ausgeführt werden.
```
pipenv run jupyter nbconvert --to notebook --execute --inplace --allow-errors notebooks/*.ipynb
```
Daraufhin werden die benötigten Daten aus Wikisource heruntergeladen und aufbereitet.

## ⛏️ Bibliotheken <a name="built_using"></a>
- [NLTK](https://www.nltk.org/) - Natural Language Processing
- [pandas](https://pandas.pydata.org/) - Datenanalyse
- [requests](https://docs.python-requests.org/en/latest/) - Web
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Verarbeitung von HTML
- [stylecloud](https://github.com/minimaxir/stylecloud) - Visualierungen
- uvm.

## ✍️ Autor:innen <a name="authors"></a>
- Heinz-Alexander Fütterer
- Selina Reinhard

## 📜 Lizenz <a name="license"></a>
Die Inhalte dieses Git-Repositories sind unter einer [Creative Commons Namensnennung 4.0 International Lizenz](https://creativecommons.org/licenses/by/4.0/) lizenziert.

[![License](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)](https://creativecommons.org/licenses/by/4.0/)

## 🎉 Danksagung <a name="acknowledgement"></a>
- README basiert auf [README_TEMPLATES/Standard.md](https://github.com/kylelobo/The-Documentation-Compendium/blob/master/en/README_TEMPLATES/Standard.md)
