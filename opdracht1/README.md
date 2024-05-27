# TINLML02

## Opdracht 1

### Opdrachtbeschrijvng

*De volledige opdrachtbeschrijving staat in [/Opdracht_1.pdf](/Opdracht_1.pdf).*

Het doel is om te leren hoe Neurale Netwerken werken.

Om dit te bereiken maken we een NN dat een uit een zwart-wit-beeld met een resolutie van 3x3 pixels detecteert of een veld een kruis `X` of een cirkel `O` bevat. 

### Design

Een Neuraal Netwerk bestaat uit zogenaamde 'nodes' en 'links'. De 'nodes' zijn de knoppen in het netwerk en de 'links' zijn de pijlen die tussen de nodes lopen, in elke laag.

De input nodes zijn de parameters. Die krijgen een bepaalde waarde. De links geven die vervolgens door aan de nodes in de volgende laag. Die nodes hebben weer links naar de output laag. De links geven de waardes door aan die laag. De links geven de waade niet zomaar door. Elke link heeft een gewicht. Dat is een getal waarmee de waarde van de node mee wordt vermenigvuldigd. Door de gewichten te varieren tellen bepaalde nodes (die inputs voorstellen) zwaarder dan anderen. Dit zorgt voor het 'slimme' van het netwerk.

Voor deze opdracht moest een Neuraal Netwerk gebouwd worden in Python waarmee een cirkel van een kruis onscheiden moest kunnen worden. De symbolen werden voorgesteld door een serie van 3x3 bits.

### Versies

Voor verschillende versies zijn verschillende architecturen gebruikt.

#### V2.0

Voor de eerste versie van de opdracht is begonnen met het implementeren van de intuitieve classes 'Node', 'Link' en 'NeuralNetwork'. Versie 1.0 heeft niet geleidt tot een werkend neuraal netwerk. Daarom is de eerste versie 'V2.0'. Deze is te vinden in [branch opdracht1-v2.0](https://github.com/tdregmans/TINLML02-persoonlijk-verslag/tree/opdracht1-v2.0/opdracht1).

#### V3.1 

Na gebruik van 'Node' en 'Link' objecten is overgegaan op gebruik van numpy matrices om de gewichten te bewaren. Dit heeft als voordeel dat het sneller is, en een kleinere codebase vereist. Dit is geimplementeerd in [branch opdracht1-v3.1](https://github.com/tdregmans/TINLML02-persoonlijk-verslag/tree/opdracht1-v3.1/opdracht1).

#### V5.0 

Alle versies tot V5.0 veranderen de gewichten random. Er wordt dan gekeken of de verandering tot een beter resultaat heeft geleid. Als dat niet zo is, dan wordt de verandering teruggedraaid. Mocht dat wel zo zijn, dan is het model verbeterd in die cycli. De verandering blijft dan staan. Vanaf versie V5.0 wordt gebruik gemaakt van een Neuraal Netwerk dat met behulp van een 'cost-function' en backward propagation efficient het model verbeterd. Dit is gebaseerd op een code-snippet van geeksforgeeks.com: [example of backpropagation in machine learning](https://www.geeksforgeeks.org/backpropagation-in-machine-learning/#example-of-backpropagation-in-machine-learning). Dit voorbeeld is aangepast zodat het toepasbaar voor deze opdracht. Het is geimplementeerd in [branch opdracht1-v5.0](https://github.com/tdregmans/TINLML02-persoonlijk-verslag/tree/opdracht1-v5.0/opdracht1).

### Tests

Voor elke versie geldt dat het is getraind en daarna getest met de testSet die gegeven is in [data.py](https://github.com/tdregmans/TINLML02-persoonlijk-verslag/blob/main/opdracht1/data.py)

Bijvoorbeeld, V3.1 kan het volgende resultaat geven:

```
...
Epoch: 270
Epoch: 271
Epoch: 272
Training completed in 272 epochs.

Testcase 0
Identified as 'O' (with a certainty of 0.68 )
Identified correctly!
Testcase 1
Identified as 'O' (with a certainty of 0.62 )
Identified correctly!
Testcase 2
Identified as 'O' (with a certainty of 0.53 )
Identified correctly!
Testcase 3
Identified as 'O' (with a certainty of 0.61 )
Identified correctly!
Testcase 4
Identified as 'X' (with a certainty of 0.76 )
Identified correctly!
Testcase 5
Identified as 'X' (with a certainty of 0.67 )
Identified correctly!
Testcase 6
Identified as 'X' (with a certainty of 0.73 )
Identified correctly!
Testcase 7
Identified as 'X' (with a certainty of 0.73 )
Identified correctly!

SUCCESSFUL OUTCOME: True
SCORE: [True, True, True, True, True, True, True, True]
```

`SUCCESFUL OUTCOME: True` betekent dat alle symbolen goed gedetecteerd zijn.
