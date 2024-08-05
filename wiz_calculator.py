# Wizard101 damage calculator
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Stats frame
stats_frame = tk.Frame(root)
stats_frame.grid(row=0, column=0, padx=10, pady=10)

# Create entries for player and enemy, including damage, resist, pierce, crit chance, and crit multiplier
tk.Label(stats_frame, text="Player Damage:", font=('Arial', 18)).grid(row=0, column=0, padx=10, pady=5, sticky='e')
player_damage = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_damage.grid(row=0, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Player Pierce:", font=('Arial', 18)).grid(row=1, column=0, padx=10, pady=5, sticky='e')
player_pierce = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_pierce.grid(row=1, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Player Crit Multiplier:", font=('Arial', 18)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
player_crit_multiplier = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_crit_multiplier.grid(row=2, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Enemy Resist:", font=('Arial', 18)).grid(row=1, column=2, padx=10, pady=5, sticky='e')
enemy_resist = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
enemy_resist.grid(row=1, column=3, padx=10, pady=5)

# hanging effects frame
effects_frame = tk.Frame(root)
effects_frame.grid(row=1, column=0, padx=10, pady=10)

def create_hanging_effect_widget(value: int, row: int, column: int, type: str) -> tuple[tk.Label, tk.Button, tk.Button]:
    label = tk.Label(effects_frame, text=f"{value}% (0)", padx=5, pady=5, bg="orange")
    label.grid(row=row, column=column, padx=10, pady=5)
    plus = tk.Button(effects_frame, text="+", padx=0, pady=0, bg="green")
    plus.grid(row=row, column=column + 1, padx=10, pady=5)
    minus = tk.Button(effects_frame, text="-", padx=0, pady=0, bg="red")
    minus.grid(row=row + 1, column=column + 1, padx=10, pady=5)
    
    if type == "buff":
        plus.config(command=lambda: add_buff(label, value))
        minus.config(command=lambda: remove_buff(label, value))
    elif type == "shield":
        plus.config(command=lambda: add_shield(label, value))
        minus.config(command=lambda: remove_shield(label, value))
    elif type == "weakness":
        plus.config(command=lambda: add_weakness(label, value))
        minus.config(command=lambda: remove_weakness(label, value))

    return label, plus, minus

# row of weakness buttons (10,15,20,25,30,35,40,45,55,60,75)
tk.Label(effects_frame, text="Weaknesses:", font=('Arial', 8)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
weakness_10_label, weakness_10_plus, weakness_10_minus = create_hanging_effect_widget(10, 5, 1, "weakness")
weakness_15_label, weakness_15_plus, weakness_15_minus = create_hanging_effect_widget(15, 5, 3, "weakness")
weakness_20_label, weakness_20_plus, weakness_20_minus = create_hanging_effect_widget(20, 5, 5, "weakness")
weakness_25_label, weakness_25_plus, weakness_25_minus = create_hanging_effect_widget(25, 5, 7, "weakness")
weakness_30_label, weakness_30_plus, weakness_30_minus = create_hanging_effect_widget(30, 5, 9, "weakness")
weakness_35_label, weakness_35_plus, weakness_35_minus = create_hanging_effect_widget(35, 5, 11, "weakness")
weakness_40_label, weakness_40_plus, weakness_40_minus = create_hanging_effect_widget(40, 5, 13, "weakness")
weakness_45_label, weakness_45_plus, weakness_45_minus = create_hanging_effect_widget(45, 5, 15, "weakness")
weakness_55_label, weakness_55_plus, weakness_55_minus = create_hanging_effect_widget(55, 5, 17, "weakness")
weakness_60_label, weakness_60_plus, weakness_60_minus = create_hanging_effect_widget(60, 5, 19, "weakness")
weakness_75_label, weakness_75_plus, weakness_75_minus = create_hanging_effect_widget(75, 5, 21, "weakness")

# row of buff buttons
tk.Label(effects_frame, text="Buffs \n(Blades, Traps, Bubbles, Auras):", font=('Arial', 8)).grid(row=7, column=0, padx=10, pady=5, sticky='e')
buff_10_label, buff_10_plus, buff_10_minus = create_hanging_effect_widget(10, 7, 1, "buff")
buff_15_label, buff_15_plus, buff_15_minus = create_hanging_effect_widget(15, 7, 3, "buff")
buff_20_label, buff_20_plus, buff_20_minus = create_hanging_effect_widget(20, 7, 5, "buff")
buff_25_label, buff_25_plus, buff_25_minus = create_hanging_effect_widget(25, 7, 7, "buff")
buff_30_label, buff_30_plus, buff_30_minus = create_hanging_effect_widget(30, 7, 9, "buff")
buff_35_label, buff_35_plus, buff_35_minus = create_hanging_effect_widget(35, 7, 11, "buff")
buff_40_label, buff_40_plus, buff_40_minus = create_hanging_effect_widget(40, 7, 13, "buff")
buff_45_label, buff_45_plus, buff_45_minus = create_hanging_effect_widget(45, 7, 15, "buff")
buff_50_label, buff_50_plus, buff_50_minus = create_hanging_effect_widget(50, 7, 17, "buff")
buff_55_label, buff_55_plus, buff_55_minus = create_hanging_effect_widget(55, 7, 19, "buff")
buff_60_label, buff_60_plus, buff_60_minus = create_hanging_effect_widget(60, 7, 21, "buff")
buff_70_label, buff_70_plus, buff_70_minus = create_hanging_effect_widget(70, 7, 23, "buff")
buff_80_label, buff_80_plus, buff_80_minus = create_hanging_effect_widget(80, 7, 25, "buff")

# row of shield buttons
tk.Label(effects_frame, text="Shields \n (includes defensive auras):", font=('Arial', 8)).grid(row=9, column=0, padx=10, pady=5, sticky='e')
shield_10_label, shield_10_plus, shield_10_minus = create_hanging_effect_widget(10, 9, 1, "shield")
shield_15_label, shield_15_plus, shield_15_minus = create_hanging_effect_widget(15, 9, 3, "shield")
shield_20_label, shield_20_plus, shield_20_minus = create_hanging_effect_widget(20, 9, 5, "shield")
shield_25_label, shield_25_plus, shield_25_minus = create_hanging_effect_widget(25, 9, 7, "shield")
shield_30_label, shield_30_plus, shield_30_minus = create_hanging_effect_widget(30, 9, 9, "shield")
shield_35_label, shield_35_plus, shield_35_minus = create_hanging_effect_widget(35, 9, 11, "shield")
shield_40_label, shield_40_plus, shield_40_minus = create_hanging_effect_widget(40, 9, 13, "shield")
shield_45_label, shield_45_plus, shield_45_minus = create_hanging_effect_widget(45, 9, 15, "shield")
shield_50_label, shield_50_plus, shield_50_minus = create_hanging_effect_widget(50, 9, 17, "shield")
shield_55_label, shield_55_plus, shield_55_minus = create_hanging_effect_widget(55, 9, 19, "shield")
shield_60_label, shield_60_plus, shield_60_minus = create_hanging_effect_widget(60, 9, 21, "shield")
shield_70_label, shield_70_plus, shield_70_minus = create_hanging_effect_widget(70, 9, 23, "shield")
shield_80_label, shield_80_plus, shield_80_minus = create_hanging_effect_widget(80, 9, 25, "shield")
shield_85_label, shield_85_plus, shield_85_minus = create_hanging_effect_widget(85, 9, 27, "shield")

# frame for base spell damage
spell_frame = tk.Frame(root)
spell_frame.grid(row=2, column=0, padx=10, pady=10)

# Create entries for spell damage
tk.Label(spell_frame, text="Spell Damage:", font=('Arial', 18)).grid(row=0, column=0, padx=10, pady=5, sticky='e')
spell_damage = tk.Entry(spell_frame, width=10, borderwidth=5, font=('Arial', 18))
spell_damage.grid(row=0, column=1, padx=10, pady=5)

# create entry for actual damage
tk.Label(spell_frame, text="Actual Damage:", font=('Arial', 18)).grid(row=0, column=2, padx=10, pady=5, sticky='e')
actual_damage = tk.Entry(spell_frame, width=10, borderwidth=5, font=('Arial', 18))
actual_damage.grid(row=0, column=3, padx=10, pady=5)

# frame for display, calculate and clear buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, padx=10, pady=10)

# creat entry for display, and buttons for calculating and clearing
display = tk.Entry(button_frame, width=80, borderwidth=5, font=('Arial', 18))
display.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

button_calculate = tk.Button(button_frame, text="Calculate", padx=10, pady=5, command=lambda: calculate())
button_calculate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(button_frame, text="Clear", padx=10, pady=5, command=lambda: clear())
button_clear.grid(row=1, column=1, padx=10, pady=5)

button_calculation_type = tk.Button(button_frame, text="Damage", padx=10, pady=5, bg="green", command=lambda: toggle_calculation_type(button_calculation_type))
button_calculation_type.grid(row=1, column=2, padx=10, pady=5)

# state variable for who is hitting
calculating_damage = True

# state variables for effects
buffs = {}
shields = {}
weaknesses = {}

def toggle_button_color(button):
    if button.cget("bg") == "green":
        button.config(bg="red")
    else:
        button.config(bg="green")

# button functions for shields and traps
def add_buff(button, buff: int):
    # add the buff to the list of buffs if button is being checked. Otherwise, remove it.
    if buff in buffs:
        buffs[buff] += 1
    else:
        buffs[buff] = 1
    # change button text to reflect the number of buffs
    button.config(text=f"{buff}% ({buffs[buff]})")

def remove_buff(button, buff: int):
    # remove the buff from the list of buffs
    if buff in buffs:
        buffs[buff] = max(buffs[buff] - 1, 0)
    # change button text to reflect the number of buffs
    button.config(text=f"{buff}% ({buffs[buff]})")

def add_shield(button, shield: int):
    # add the shield to the list of shields if button is being checked. Otherwise, remove it.
    if shield in shields:
        shields[shield] += 1
    else:
        shields[shield] = 1
    # change button text to reflect the number of shields
    button.config(text=f"{shield}% ({shields[shield]})")

def remove_shield(button, shield: int):
    # remove the shield from the list of shields
    if shield in shields:
        shields[shield] = max(shields[shield] - 1, 0)
    # change button text to reflect the number of shields
    button.config(text=f"{shield}% ({shields[shield]})")

def add_weakness(button, weakness: int):
    # add the weakness to the list of weaknesses if button is being checked. Otherwise, remove it.
    if weakness in weaknesses:
        weaknesses[weakness] += 1
    else:
        weaknesses[weakness] = 1
    # change button text to reflect the number of weaknesses
    button.config(text=f"{weakness}% ({weaknesses[weakness]})")

def remove_weakness(button, weakness: int):
    # remove the weakness from the list of weaknesses
    if weakness in weaknesses:
        weaknesses[weakness] = max(weaknesses[weakness] - 1, 0)
    # change button text to reflect the number of weaknesses
    button.config(text=f"{weakness}% ({weaknesses[weakness]})")

def toggle_calculation_type(hitter_button):

    toggle_button_color(hitter_button)
    global calculating_damage
    calculating_damage = not calculating_damage
    if calculating_damage:
        button_calculation_type.config(text="Damage")
    else:
        button_calculation_type.config(text="Resist")

# clear all state variables, reset all button colors to red, clear all entries, clear display
def clear():

    global buffs, shields, weaknesses

    buffs = {}
    shields = {}
    weaknesses = {}

    # reset text of all button labels
    for button_label in [weakness_10_label, weakness_15_label, weakness_20_label, weakness_25_label, weakness_30_label, weakness_35_label, weakness_40_label, weakness_45_label, weakness_55_label, weakness_60_label, weakness_75_label]:
        button_label.config(text=button_label.cget("text").split("(")[0] + "(0)")
    for button_label in [buff_10_label, buff_15_label, buff_20_label, buff_25_label, buff_30_label, buff_35_label, buff_40_label, buff_45_label, buff_50_label, buff_55_label, buff_60_label, buff_70_label, buff_80_label]:
        button_label.config(text=button_label.cget("text").split("(")[0] + "(0)")
    for button_label in [shield_10_label, shield_15_label, shield_20_label, shield_25_label, shield_30_label, shield_35_label, shield_40_label, shield_45_label, shield_50_label, shield_55_label, shield_60_label, shield_70_label, shield_80_label, shield_85_label]:
        button_label.config(text=button_label.cget("text").split("(")[0] + "(0)")

    player_damage.delete(0, tk.END)
    player_pierce.delete(0, tk.END)
    player_crit_multiplier.delete(0, tk.END)
    enemy_resist.delete(0, tk.END)
    spell_damage.delete(0, tk.END)

    display.delete(0, tk.END)

# utilities for damage calculations

# ALL SHIELDS ARE PASSED AS THEIR INTEGER VALUES (e.g. 20% is passed as 20).
def shields_to_effective_shields(shields: list[float], pierce: float) -> tuple[list[float],float]:
    current_pierce = pierce
    effective_shields = []
    for shield in shields:
        if shield <= current_pierce:
            current_pierce -= shield
        else: #shield is strictly greater than pierce
            effective_shields.append(shield - current_pierce)
            current_pierce = 0
    return effective_shields, current_pierce

# ALL DEBUFFS ARE PASSED AS THEIR INTEGER VALUES (e.g. 20% is passed as 20).
def damage_after_debuffs(damage: float, debuffs: list[float]) -> float:
    total_debuff = 1
    for debuff in debuffs:
        total_debuff *= (1 - debuff / 100)
    return damage * total_debuff

# ALL BUFFS ARE PASSED AS THEIR INTEGER VALUES (e.g. 20% is passed as 20).
def damage_after_buffs(damage: float, buffs: list[float]) -> float:
    total_buff = 1
    for buff in buffs:
        total_buff *= (1 + buff / 100)
    return damage * total_buff

# final calculations

# ALL HANGING EFFECTS ARE PASSED AS THEIR INTEGER VALUES (e.g. 20% is passed as 20).
# RETURNS: A tuple containing the final damage and the final critical damage respectively.
def damage_calculation(spell_damage: int, buffs: list[float], pierce: float, shields: list[float], weaknesses: list[float], crit_multiplier: float, enemy_resist: float) -> tuple[float]:
    
    buffed_damage = damage_after_buffs(spell_damage, buffs)

    damage_after_weaknesses = damage_after_debuffs(buffed_damage, weaknesses)

    effective_shields, remaining_pierce = shields_to_effective_shields(shields, pierce)

    damage_after_shields = damage_after_debuffs(damage_after_weaknesses, effective_shields)

    effective_resist = max(enemy_resist - remaining_pierce, 0)

    damage = damage_after_shields * (1 - effective_resist / 100)

    crit_damage = damage * crit_multiplier

    return damage, crit_damage

def resist_calculation(spell_damage: int, buffs: list[float], pierce: float, shields: list[float], weaknesses: list[float], crit_multiplier: float, actual_damage: float) -> tuple[float]:
    
    buffed_damage = damage_after_buffs(spell_damage, buffs) * crit_multiplier

    damage_after_weaknesses = damage_after_debuffs(buffed_damage, weaknesses)

    effective_shields, remaining_pierce = shields_to_effective_shields(shields, pierce)

    damage_after_shields = damage_after_debuffs(damage_after_weaknesses, effective_shields)

    effective_resist = -100 * (actual_damage / damage_after_shields - 1)

    maximum_potential_resist = effective_resist + remaining_pierce

    return effective_resist, maximum_potential_resist

def dict_to_list(d: dict) -> list:
    l = []
    for key in d:
        for i in range(d[key]):
            l.append(key)
    return l

def calculate():
    new_hitter_damage, new_pierce, new_crit_multiplier, new_enemy_resist = 0, 0, 1, 0

    new_hitter_damage = float(player_damage.get()) if player_damage.get() else 0
    new_pierce = float(player_pierce.get()) if player_pierce.get() else 0
    new_crit_multiplier = (1 + float(player_crit_multiplier.get()) / 100) if player_crit_multiplier.get() else 1
    new_enemy_resist = float(enemy_resist.get()) if enemy_resist.get() else 0

    new_spell_damage = float(spell_damage.get()) if spell_damage.get() else 0
    new_actual_damage = float(actual_damage.get()) if actual_damage.get() else 0
    
    # add player damage to list of buffs
    new_buffs = buffs
    new_buffs[new_hitter_damage] = 1
    new_buffs = dict_to_list(new_buffs)

    new_shields = dict_to_list(shields)
    new_weaknesses = dict_to_list(weaknesses)
    
    print('buffs:', new_buffs, 'shields:', new_shields, 'weaknesses:', new_weaknesses, 'pierce:', new_pierce, 'crit_multiplier:', new_crit_multiplier, 'enemy_resist:', new_enemy_resist, 'spell_damage:', new_spell_damage)
    
    display.delete(0, tk.END)
    
    if calculating_damage:
        damage, crit_damage = damage_calculation(new_spell_damage, new_buffs, new_pierce, new_shields, new_weaknesses, new_crit_multiplier, new_enemy_resist)
        display.insert(0, f"Damage: {round(damage, 2)}, Critical Damage: {round(crit_damage, 2)}")
    else:
        effective_resist, maximum_potential_resist = resist_calculation(new_spell_damage, new_buffs, new_pierce, new_shields, new_weaknesses, new_crit_multiplier, new_actual_damage)
        display.insert(0, f"Effective Resist: {round(effective_resist, 2)}, Maximum Potential Resist: {round(maximum_potential_resist, 2)}")
    
# Run the application
root.mainloop()