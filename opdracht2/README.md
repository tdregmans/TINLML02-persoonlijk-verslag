# TINLML02

## Opdracht 2

In de tweede opdracht wordt een uitstapje gemaakt naar Genetische Algoritmen. Een Genetische Algoritme is een algoritme dat natuurlijke selectie gebruikt, om tot betere resultaten te komen. Net als in de natuur, wordt door natuurlijke selectie geselecteerd op een bepaalde kwaliteit. Dit resulteert in het meer voorkomen van die kwaliteit.

Er wordt begonnen met een intiële populatie. Op deze populatie wordt een random mutatie toegepast. Vervolgens wordt volgens de fitheid van deze nieuwe generatie bepaalt. In de opdracht is dit een score gegeven door de gebruiker. Er is gekozen voor een rating van 0 t/m 10 die de gebruiker aan de muziek kan geven. In deze opdracht is de intiële populatie muziek van Bach, zoals aangeleverd door de docenten. Op deze muziek worden random mutatie toegepast. Op basis van de rating van de gebruiker, wordt de muziek vervolgens aangepast.

### Design

Er is in deze implementatie gekozen om telkens de beste muziek die daarvoor gegenereerd is, te gebruiken voor de nieuwe generatie. Wat de 'beste' muziek is, is bepaald door de gebruiker.

De architectuur van de software is soortgelijk aan die van opdracht 1: Er is een [main.py](main.py) die het programma aanstuurt. Deze importeert de [Generator](Generator.py) klasse, en maakt hier een object van. Die wordt vervolgens gebruikt om muziek te genereren. Op de achtergrond wordt gebruik gemaakt van de [muser.py](muser.py) die door het docententeam geleverd is.

Er is een simpele implementatie te vinden in [branch opdracht2-v1.0](https://github.com/tdregmans/TINLML02-persoonlijk-verslag/tree/opdracht2-v1.0/opdracht2).
    