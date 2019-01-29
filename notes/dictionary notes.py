states = {
        "CA": "California",
        "VA": "Virginia",
        "MD": "Maryland",
        "RI": "Rhode Island",
        "NV": "Nevada"
    }


print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000 # 39,540,000

},

    "VA":{
        "NAME": "Virginia",
        "POPULATION": 8517685  # 8,500,000

},
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718  # 6,042,718

},

    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315

},
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,023,392

 }
}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {"CA": {
        "NAME": "California",
        "POPULATION": 39540000, # 39,540,000
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"

    ]

},

    "VA":{
        "NAME": "Virginia",
        "POPULATION": 8517685,  # 8,500,000
        "CITIES": [
            "Richmond",
            "Norfolk",
            ""
        ]

},
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,  # 6,042,718
        "CITIES": [
            "",
            "Newport",
            "Warwick"

        ]

},

    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315

},
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,023,392

 }
}},
