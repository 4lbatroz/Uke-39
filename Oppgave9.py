liste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele",
"endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så",
"lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den",
"er", "lang"]

ordbok = {
    "Så": 6,
    "lykkelig": 4,
    "dag": 2
}

# printer hvor mange elementer det er i listen.
print("lengden er ", len(liste))

sa = liste.count("så")
lykkelig = liste.count("lykkelig")
dag = liste.count("dag")

print("så vises ", sa, " ganger.")
print("lykkelig vises", lykkelig, "ganger")
print("dag vises ", dag, "ganger")

print(ordbok)