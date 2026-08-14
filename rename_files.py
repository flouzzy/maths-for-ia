def clean_filename(name):
    replacements = {
        "MathÃ©matiques": "Mathematiques",
        "ModÃ¨les": "Modeles",
        "ForÃªt": "Foret",
        "NoÃ«l": "Noel",
        "LÃ ": "La",
        "PÃ¢tes": "Pates",
        "CÃ´te": "Cote",
        "SÃ»r": "Sur",
        "FranÃ§ais": "Francais",
        "NaÃ¯f": "Naif",
        "MaÃ®tre": "Maitre",
        "ThÃorÃ¨me": "Theoreme",
        "$-mathbb{R}^n$": "Rn",
        "$-mathcal{L}^p$": "Lp",
        "$-mathbb{R}$": "R",
        "$": "",
        "\\": ""
    }
    for k, v in replacements.items():
        name = name.replace(k, v)
    return name
