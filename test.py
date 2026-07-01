with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()
if "🔥 **Enrichi** *(10 Exos + 5 TP)*" in readme:
    print("Dashboard marked enriched.")
