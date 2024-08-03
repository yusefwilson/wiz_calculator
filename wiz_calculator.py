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

tk.Label(stats_frame, text="Player Resist:", font=('Arial', 18)).grid(row=1, column=0, padx=10, pady=5, sticky='e')
player_resist = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_resist.grid(row=1, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Player Pierce:", font=('Arial', 18)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
player_pierce = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_pierce.grid(row=2, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Player Crit Multiplier:", font=('Arial', 18)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
player_crit_multiplier = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
player_crit_multiplier.grid(row=3, column=1, padx=10, pady=5)

tk.Label(stats_frame, text="Enemy Damage:", font=('Arial', 18)).grid(row=0, column=2, padx=10, pady=5, sticky='e')
enemy_damage = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
enemy_damage.grid(row=0, column=3, padx=10, pady=5)

tk.Label(stats_frame, text="Enemy Resist:", font=('Arial', 18)).grid(row=1, column=2, padx=10, pady=5, sticky='e')
enemy_resist = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
enemy_resist.grid(row=1, column=3, padx=10, pady=5)

tk.Label(stats_frame, text="Enemy Pierce:", font=('Arial', 18)).grid(row=2, column=2, padx=10, pady=5, sticky='e')
enemy_pierce = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
enemy_pierce.grid(row=2, column=3, padx=10, pady=5)

tk.Label(stats_frame, text="Enemy Crit Multiplier:", font=('Arial', 18)).grid(row=3, column=2, padx=10, pady=5, sticky='e')
enemy_crit_multiplier = tk.Entry(stats_frame, width=10, borderwidth=5, font=('Arial', 18))
enemy_crit_multiplier.grid(row=3, column=3, padx=10, pady=5)

# hanging effects frame
effects_frame = tk.Frame(root)
effects_frame.grid(row=1, column=0, padx=10, pady=10)

# row of weakness buttons
tk.Label(effects_frame, text="Weakness:", font=('Arial', 18)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
weakness_10 = tk.Button(effects_frame, text="10%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_10, 10))
weakness_10.grid(row=5, column=1, padx=10, pady=5)
weakness_15 = tk.Button(effects_frame, text="15%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_15, 15))
weakness_15.grid(row=5, column=2, padx=10, pady=5)
weakness_20 = tk.Button(effects_frame, text="20%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_20, 20))
weakness_20.grid(row=5, column=3, padx=10, pady=5)
weakness_25 = tk.Button(effects_frame, text="25%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_25, 25))
weakness_25.grid(row=5, column=4, padx=10, pady=5)
weakness_30 = tk.Button(effects_frame, text="30%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_30, 30))
weakness_30.grid(row=5, column=5, padx=10, pady=5)
weakness_35 = tk.Button(effects_frame, text="35%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_35, 35))
weakness_35.grid(row=5, column=6, padx=10, pady=5)
weakness_40 = tk.Button(effects_frame, text="40%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_40, 40))
weakness_40.grid(row=5, column=7, padx=10, pady=5)
weakness_45 = tk.Button(effects_frame, text="45%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_45, 45))
weakness_45.grid(row=5, column=8, padx=10, pady=5)
weakness_60 = tk.Button(effects_frame, text="60%", padx=10, pady=5, bg="red", command=lambda: add_weakness(weakness_60, 60))
weakness_60.grid(row=5, column=9, padx=10, pady=5)

# row of blade buttons
tk.Label(effects_frame, text="Blade:", font=('Arial', 18)).grid(row=6, column=0, padx=10, pady=5, sticky='e')
blade_20 = tk.Button(effects_frame, text="20%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_20, 20))
blade_20.grid(row=6, column=1, padx=10, pady=5)
blade_25 = tk.Button(effects_frame, text="25%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_25, 25))
blade_25.grid(row=6, column=2, padx=10, pady=5)
blade_30 = tk.Button(effects_frame, text="30%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_30, 30))
blade_30.grid(row=6, column=3, padx=10, pady=5)
blade_35 = tk.Button(effects_frame, text="35%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_35, 35))
blade_35.grid(row=6, column=4, padx=10, pady=5)
blade_40 = tk.Button(effects_frame, text="40%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_40, 40))
blade_40.grid(row=6, column=5, padx=10, pady=5)
blade_55 = tk.Button(effects_frame, text="55%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_55, 55))
blade_55.grid(row=6, column=6, padx=10, pady=5)
blade_60 = tk.Button(effects_frame, text="60%", padx=10, pady=5, bg="red", command=lambda: add_buff(blade_60, 60))
blade_60.grid(row=6, column=7, padx=10, pady=5)

# row of trap buttons
tk.Label(effects_frame, text="Trap:", font=('Arial', 18)).grid(row=7, column=0, padx=10, pady=5, sticky='e')
trap_20 = tk.Button(effects_frame, text="20%", padx=10, pady=5, bg="red", command=lambda: add_weakness(trap_20, 20))
trap_20.grid(row=7, column=1, padx=10, pady=5)
trap_25 = tk.Button(effects_frame, text="25%", padx=10, pady=5, bg="red", command=lambda: add_weakness(trap_25, 25))
trap_25.grid(row=7, column=2, padx=10, pady=5)
trap_30 = tk.Button(effects_frame, text="30%", padx=10, pady=5, bg="red", command=lambda: add_weakness(trap_30, 30))
trap_30.grid(row=7, column=3, padx=10, pady=5)
trap_35 = tk.Button(effects_frame, text="35%", padx=10, pady=5, bg="red", command=lambda: add_weakness(trap_35, 35))
trap_35.grid(row=7, column=4, padx=10, pady=5)
trap_70 = tk.Button(effects_frame, text="70%", padx=10, pady=5, bg="red", command=lambda: add_weakness(trap_70, 70))
trap_70.grid(row=7, column=5, padx=10, pady=5)

# row of shield buttons
tk.Label(effects_frame, text="Shield:", font=('Arial', 18)).grid(row=8, column=0, padx=10, pady=5, sticky='e')
shield_20 = tk.Button(effects_frame, text="20%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_20, 20))
shield_20.grid(row=8, column=1, padx=10, pady=5)
shield_25 = tk.Button(effects_frame, text="25%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_25, 25))
shield_25.grid(row=8, column=2, padx=10, pady=5)
shield_40 = tk.Button(effects_frame, text="40%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_40, 40))
shield_40.grid(row=8, column=3, padx=10, pady=5)
shield_50 = tk.Button(effects_frame, text="50%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_50, 50)) 
shield_50.grid(row=8, column=4, padx=10, pady=5)
shield_70 = tk.Button(effects_frame, text="70%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_70, 70))
shield_70.grid(row=8, column=5, padx=10, pady=5)
shield_80 = tk.Button(effects_frame, text="80%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_80, 80))
shield_80.grid(row=8, column=6, padx=10, pady=5)
shield_85 = tk.Button(effects_frame, text="85%", padx=10, pady=5, bg="red", command=lambda: add_shield(shield_85, 85))
shield_85.grid(row=8, column=7, padx=10, pady=5)

# frame for base spell damage
spell_frame = tk.Frame(root)
spell_frame.grid(row=2, column=0, padx=10, pady=10)

# Create entries for spell damage
tk.Label(spell_frame, text="Spell Damage:", font=('Arial', 18)).grid(row=0, column=0, padx=10, pady=5, sticky='e')
spell_damage = tk.Entry(spell_frame, width=10, borderwidth=5, font=('Arial', 18))
spell_damage.grid(row=0, column=1, padx=10, pady=5)

# frame for display, calculate and clear buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, padx=10, pady=10)

# creat entry for display, and buttons for calculating and clearing
display = tk.Entry(button_frame, width=40, borderwidth=5, font=('Arial', 18))
display.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

button_calculate = tk.Button(button_frame, text="Calculate", padx=10, pady=5, command=lambda: calculate())
button_calculate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(button_frame, text="Clear", padx=10, pady=5, command=lambda: clear())
button_clear.grid(row=1, column=1, padx=10, pady=5)

button_hitter = tk.Button(button_frame, text="Player", padx=10, pady=5, bg="green", command=lambda: toggle_player_hitting(button_hitter))
button_hitter.grid(row=1, column=2, padx=10, pady=5)

# state variable for who is hitting
player_hitting = True

# state variables for effects
buffs = []
shields = []
weaknesses = []

def toggle_button_color(button):
    if button.cget("bg") == "green":
        button.config(bg="red")
    else:
        button.config(bg="green")

# button functions for shields and traps
def add_buff(button, buff):
    toggle_button_color(button)
    # add the buff to the list of buffs if button is being checked. Otherwise, remove it.
    if buff in buffs:
        buffs.remove(buff)
    else:
        buffs.append(buff)

def add_shield(button, shield):
    toggle_button_color(button)
    # add the shield to the list of shields if button is being checked. Otherwise, remove it.
    if shield in shields:
        shields.remove(shield)
    else:
        shields.append(shield)

def add_weakness(button, weakness):
    toggle_button_color(button)
    # add the weakness to the list of weaknesses if button is being checked. Otherwise, remove it.
    if weakness in weaknesses:
        weaknesses.remove(weakness)
    else:
        weaknesses.append(weakness)

def toggle_player_hitting(hitter_button):
    toggle_button_color(hitter_button)
    global player_hitting
    player_hitting = not player_hitting
    if player_hitting:
        button_hitter.config(text="Player")
    else:
        button_hitter.config(text="Enemy")

# clear all state variables, reset all button colors to red, clear all entries, clear display
def clear():

    global buffs, shields, weaknesses
    buffs = []
    shields = []
    weaknesses = []

    for button in [weakness_10, weakness_15, weakness_20, weakness_25, weakness_30, weakness_35, weakness_40, weakness_45, weakness_60]:
        button.config(bg="red")
    for button in [blade_20, blade_25, blade_30, blade_35, blade_40, blade_55, blade_60]:
        button.config(bg="red")
    for button in [trap_20, trap_25, trap_30, trap_35, trap_70]:
        button.config(bg="red")
    for button in [shield_20, shield_25, shield_40, shield_50, shield_70, shield_80, shield_85]:
        button.config(bg="red")

    player_damage.delete(0, tk.END)
    player_resist.delete(0, tk.END)
    player_pierce.delete(0, tk.END)
    player_crit_multiplier.delete(0, tk.END)
    enemy_damage.delete(0, tk.END)
    enemy_resist.delete(0, tk.END)
    enemy_pierce.delete(0, tk.END)
    enemy_crit_multiplier.delete(0, tk.END)
    spell_damage.delete(0, tk.END)

    display.delete(0, tk.END)

# ALL HANGING EFFECTS ARE PASSED AS THEIR INTEGER VALUES (e.g. 20% is passed as 20).
# RETURNS: A tuple containing the final damage and the final critical damage respectively.
def damage_calculation(spell_damage: int, buffs: list[float], pierce: float, shields: list[float], weaknesses: list[float], crit_multiplier: float, enemy_resist: float) -> tuple[float]:
    # calculate the total damage multiplier
    total_buffs = 1
    for buff in buffs:
        total_buffs *= 1 + buff / 100
    total_shields = sum(shields)

    # calculate the effective resists
    effective_resist = 0
    if pierce > total_shields:
        effective_resist = max(0,enemy_resist - (pierce - total_shields))

    effective_resist /= 100

    # apply weaknesses
    for weakness in weaknesses:
        total_buffs *= (1 - weakness / 100)

    # calculate the final damage
    final_damage = spell_damage * total_buffs * (1 - effective_resist)

    return (final_damage, final_damage * crit_multiplier)

def calculate():
    new_hitter_damage, new_pierce, new_crit_multiplier, new_enemy_resist = 0, 0, 1, 0

    if player_hitting:
        new_hitter_damage = float(player_damage.get()) if player_damage.get() else 0
        new_pierce = float(player_pierce.get()) if player_pierce.get() else 0
        new_crit_multiplier = (1 + float(player_crit_multiplier.get()) / 100) if player_crit_multiplier.get() else 1
        new_enemy_resist = float(enemy_resist.get()) if enemy_resist.get() else 0

    else:
        new_hitter_damage = float(enemy_damage.get()) if enemy_damage.get() else 0
        new_pierce = float(enemy_pierce.get()) if enemy_pierce.get() else 0
        new_crit_multiplier = (1 + float(enemy_crit_multiplier.get()) / 100) if enemy_crit_multiplier.get() else 1
        new_enemy_resist = float(player_resist.get()) if player_resist.get() else 0

    new_spell_damage = float(spell_damage.get()) if spell_damage.get() else 0
    new_buffs = buffs + [100 + new_hitter_damage] if new_hitter_damage > 0 else buffs
    new_shields = shields
    new_weaknesses = weaknesses
    

    print('buffs:', new_buffs, 'shields:', new_shields, 'weaknesses:', new_weaknesses, 'pierce:', new_pierce, 'crit_multiplier:', new_crit_multiplier, 'enemy_resist:', new_enemy_resist, 'spell_damage:', new_spell_damage)

    damage, crit_damage = damage_calculation(new_spell_damage, new_buffs, new_pierce, new_shields, new_weaknesses, new_crit_multiplier, new_enemy_resist)

    display.delete(0, tk.END)
    display.insert(0, f"Damage: {round(damage, 2)}, Critical Damage: {round(crit_damage, 2)}")

# Run the application
root.mainloop()