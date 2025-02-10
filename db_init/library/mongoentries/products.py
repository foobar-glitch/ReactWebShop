from datetime import datetime
from bson.objectid import ObjectId

ALL_WASHING_MASCHINES = [
       {
          "_id": ObjectId(),
          "productId": 1,
          "product": "Siemens WM14N123",
          "rating": "4.5",
          "numRatings": 10,
          "numOrder": 281,
          "category": "household",
          "subcategory": "washingmachine",
          "price": "439.00", 
          "features": {
              "capacity": "8 kg",
              "energy_rating": "A+++",
              "color": "White"
          },
          "description": """
          Mit der Siemens WM14N123 Waschmaschine bewältigst du deine Wäscheberge schnell und energieeffizient. 
          Hast du es häufig eilig? Dann wird die varioSpeed Funktion von großem Nutzen für dich sein. 
          Dank der Funktion wäschst du dein Lieblingsoutfit bis zu 60 Prozent schneller und erzielst das gleiche saubere Ergebnis. 
          Ab sofort verbrauchst du weniger Wasser und Energie. Die Siemens Waschmaschine verfügt über die iSensoric Technologie, 
          die mit Sensoren den Verschmutzungsgrad deiner Wäsche misst und den Wasser- und Energieverbrauch dementsprechend anpasst. 
          Arbeitest du häufig im Homeoffice und möchtest nicht gestört werden? Durch den bürstenlosen iQdrive Motor werden Lärm und Vibrationen reduziert. 
          Mit der Energieeffizienzklasse B arbeitet deine Siemens Waschmaschine zusätzlich sparsam.
          """
    },
      
    {
        "_id": ObjectId(),
        "productId": 2,
        "product": "LG FH4U2VFN4",
        "rating": "4.3",
        "numRatings": 25,
        "numOrder": 345,
        "category": "household",
        "subcategory": "washingmachine",
        "price": "399.00",
        "features": {
        "capacity": "7 kg",
        "energy_rating": "A++",
        "color": "White"
        },
        "description": """
        Inverter Direct Drive® Energieeffizienter, langlebiger und leiser Motor Der Inverter Direct Drive® Motor verfügt über eine einzigartige Magnettechnik. Dank direkter Kraftübertragung (bürstenlos und ohne Keilriemen) sorgt er für eine bessere Energieeffizienz und mehr Laufruhe. Durch weniger verschleißanfällige Teile erhöht sich die Lebensdauer der Geräte spürbar – für einen langlebigen und robusten Betrieb.
        Dieses Modell ist sogar um ganze 10\% effizienter als der Grenzwert für eine "A-Klasse". Sparen Sie so nachhaltig kostbare Energie und Stromkosten.
        AI DD®: intelligente Erkennung der Fasern für 18 % mehr Gewebeschutz Der AI Direktantrieb von LG Waschmaschinen und Waschtrocknern macht intelligente Wäschepflege zur Realität. Im Gegensatz zu herkömmlichen Maschinen, die Waschmuster vbasierend auf der Füllmenge oder dem Waschprogramm wählen, nutzt LG über 20.000 Datensätze, um neben dem Beladungsgewicht auch den Weichheitsgrad des Gewebes zu erkennen und das am besten geeignete Waschmuster (6 Motion) anzuwenden. Dies führt zu 18 % weniger Stoffschäden und schont Ihre Kleidung.
        6 unterschiedliche Trommelbewegungen LG Waschmaschinen und Waschtrockner sind mit einer besonderen Technik ausgestattet, die die Wäsche schonend wäscht. Denn je nach Weichheitsgrad der Wäsche sind andere Waschmuster – also Bewegungsarten und Laufrichtungen der Trommel – besonders gut geeignet, um sie gründlich und gleichzeitig schonend zu reinigen. LG Waschmaschinen und Waschtrockner sind durch die Magnettechnik des Direktantriebs mit 6 Motion ausgestattet und können somit verschiedenste Waschmuster abbilden. Für eine schonende und individuelle Wäschepflege. 
        """
    },
    {
        "_id": ObjectId(),
        "productId": 3,
        "product": "Samsung WW80J5555MW",
        "rating": "4.6",
        "numRatings": 87,
        "numOrder": 412,
        "category": "household",
        "subcategory": "washingmachine",
        "price": "479.00",
        "features": {
            "capacity": "8 kg",
            "energy_rating": "A+++",
            "color": "Graphite"
        },
        "description": """
        Mit der Samsung WW90T4048EE/EG Frontlader Waschmaschine mit Steam Wash Programm wird deine Wäsche besonders sauber. 
        Das Programm nutzt Dampf, um Allergene und Bakterien zu entfernen. Das ist besonders praktisch, wenn du zum Beispiel an Heuschnupfen leidest. 
        Die Maschine verfügt außerdem über die EcoBubble Technologie, welche das Waschmittel in Schaumblasen verwandelt. 
        So dringt es tief in die Fasern deiner Kleidung ein und reinigt sie auch bei niedrigenTemperaturen gründlich. 
        Dabei machst du dir keine Sorgen um deine Lieblingsstücke, denn die Schontrommel schützt den Stoff vor Verschleiß, wodurch du länger Freude an deiner Kleidung hast. 
        Und mit dem Trommelreinigungsprogramm und der selbstreinigenden Schublade bleibt deine Samsung Waschmaschine sauber, ohne dass du sie manuell reinigst.
        """
    },

    {
        "_id": ObjectId(),
        "productId": 4,
        "product": "Miele WCD120 WCS",
        "rating": "1.8",
        "numRatings": 19,
        "numOrder": 217,
        "category": "household",
        "subcategory": "washingmachine",
        "price": "799.00",
        "features": {
            "capacity": "8 kg",
            "energy_rating": "A+++",
            "color": "White"
        },
        "description": """
        W1 Waschmaschine Frontlader: A-10%* I 8 kg I 1400 U/min I SteamCare I Automatische Dosierung I Miele@home
        """
    },

    {
      "_id": ObjectId(),
      "productId": 5,
      "product": "Electrolux EW6F421B",
      "rating": "3.8",
      "numRatings": 56,
      "numOrder": 171,
      "category": "household",
      "subcategory": "washingmachine",
      "price": "379.99",
      "features": {
          "capacity": "6 kg",
          "energy_rating": "A++",
          "color": "White"
      },
      "description": """
      Der refurbed AEG 9000 AbsoluteCare® Plus Wärmepumpentrockner mit 3D-Scan-Technologie ermitteln die Restfeuchte tief im Gewebe, 
      wodurch selbst mehrlagige Textilien höchst präzise, vollständig und gleichmäßig getrocknet werden, 
      damit Kleidungsstücke und Daunenjacken schön flauschig und warm bleiben.
      """
    },

    {
      "_id": ObjectId(),
      "productId": 6,
      "product": "Hoover H3W4102DBBE",
      "rating": "4.3",
      "numRatings": 62,
      "numOrder": 674,
      "category": "household",
      "subcategory": "washingmachine",
      "price": "399.99",
      "features": {
          "capacity": "10 kg",
          "energy_rating": "A++",
          "color": "Black"
      },
      "description": """
      W1 Waschmaschine Frontlader: A-10%* I 8 kg I 1400 U/min I SteamCare I Automatische Dosierung I Miele@home
      """
    },
    {
      "_id": ObjectId(),
      "productId": 7,
      "product": "Indesit BWE101684XW",
      "rating": "4.2",
      "numRatings": 18,
      "numOrder": 181,
      "category": "household",
      "subcategory": "washingmachine",
      "price": "459.00",
      "features": {
          "capacity": "10 kg",
          "energy_rating": "A+++",
          "color": "White"
      },
      "description": """
      W1 Waschmaschine Frontlader: A-10%* I 8 kg I 1400 U/min I SteamCare I Automatische Dosierung I Miele@home
      """
    },
    {
      "_id": ObjectId(),
      "productId": 8,
      "product": "Beko WTG841B2",
      "rating": "4.4",
      "numRatings": 21,
      "numOrder": 138,
      "category": "household",
      "subcategory": "washingmachine",
      "price": "349.00",
      "features": {
          "capacity": "8 kg",
          "energy_rating": "A++",
          "color": "Black"
      },
      "description": """
      W1 Waschmaschine Frontlader: A-10%* I 8 kg I 1400 U/min I SteamCare I Automatische Dosierung I Miele@home
      """
    }
    ]


