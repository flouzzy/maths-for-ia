def clean_filename(filename):
    replacements = {
        "Ã©": "e",
        "Ã¨": "e",
        "Ãª": "e",
        "Ã«": "e",
        "Ã ": "a",
        "Ã¢": "a",
        "Ã´": "o",
        "Ã»": "u",
        "Ã§": "c",
        "Ã¯": "i",
        "Ã®": "i",
        "Ã": "e",
        "$-mathbb{R}^n$": "Rn",
        "$-mathcal{L}^p$": "Lp",
        "$-mathbb{R}$": "R",
        "$": "",
        "\\": ""
    }
    for old, new in replacements.items():
        filename = filename.replace(old, new)
    return filename
