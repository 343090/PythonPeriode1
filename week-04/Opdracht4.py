# Opdracht - Weapon Selector
# Het programma laat een speler een wapen kiezen en toont de bijbehorende damage.

# Stap 1: Kies een speler en een wapen. Verander deze waarden om iets anders te testen.
player_name = "Steve"
selected_weapon = "Sword"
weapon_damage = 0

match selected_weapon:
    case "Sword":
        weapon_damage = 20
        print("Je gebruikt een zwaard!")
    case "Bow":
        weapon_damage = 15
        print("Je gebruikt een boog!")
    case "Staff":
        weapon_damage = 25
        print("Je gebruikt een magische staf!")
    case "Axe":
        weapon_damage = 30
        print("Je gebruikt een bijl!")
    
    case _:
        weapon_damage = 0
        print("Onbekend wapen!")


print(f"Speler: {player_name}")
print(f"Wapen: {selected_weapon}")
print(f"Damage: {weapon_damage}")

# Stap 2: match-case kiest de code die bij het gekozen wapen hoort.


# Stap 4: De comments hierboven leggen uit wat de code doet,
# waarom match-case wordt gebruikt en wat er gebeurt bij een onbekend wapen.

# Stap 5: De variabelen gebruiken snake_case en duidelijke Engelse namen.
# Bijvoorbeeld: selected_weapon (goed), niet selectedWeapon (camelCase).

# BONUS 1 (optioneel): Voeg zelf minimaal twee wapens toe aan de match-case.
# Geef ieder wapen een eigen damage en beschrijving.

# BONUS 2 (optioneel): Laat de speler met een for-loop drie keer aanvallen.
# Gebruik enemy_health = 100 en zorg dat de health niet onder 0 komt.

# BONUS 3 (optioneel): Gebruik een while-loop om aan te vallen totdat de
# vijand geen health meer heeft. Print daarna "Vijand verslagen!"
