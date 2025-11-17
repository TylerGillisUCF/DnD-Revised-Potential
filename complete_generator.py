#!/usr/bin/env python3
"""
Generate all remaining encounters in streamlined format
"""

# Template for combat encounters (Nick)
def generate_nick_encounter(num, title, npc_name, challenge_desc):
    return f"""## NICK'S PATH - ENCOUNTER #{num}: {title.upper()}

ENCOUNTER #{num} - NICK: {title.upper()} (REVISED)
========================================================================

**{title.upper()}**
{npc_name}

**LOCATION:** The crimson path leads Nick to a battlefield. {challenge_desc}

**SETUP:** Place card #{num} face-down.

**THE CHALLENGE:**

**[COMBAT - Roll-vs-Roll System]**

Enemy warrior appears.

**COMBAT RESOLUTION:**
- Both Nick and enemy roll d20 + combat modifier
- Highest roll wins that exchange (tie = Nick wins)
- First to win 3 exchanges wins the battle

**DM:** Narrate the battle dramatically. Add environmental details and tactical choices.

**ROLL FOR COMBAT OUTCOME:**
- **3-0 Victory:** Dominant! **+1 coin bonus**
- **3-1 Victory:** Strong performance!
- **3-2 Victory:** Hard-fought win!

**RESOLUTION:**

Nick claims the artifact and gains battlefield wisdom.

**REWARD:**
- Artifact Component {13-num}/12
- +5 coins earned
- +1 Stat Point ({13+num} total)

The warrior's path continues.
---

"""

# Template for treasure encounters (Christopher)
def generate_christopher_encounter(num, title, npc_name, challenge_desc):
    return f"""## CHRISTOPHER'S PATH - ENCOUNTER #{num}: {title.upper()}

ENCOUNTER #{num} - CHRISTOPHER: {title.upper()} (REVISED)
========================================================================

**{title.upper()}**
{npc_name}

**LOCATION:** The golden path leads Christopher to {challenge_desc}

**SETUP:** Place card #{num} face-down.

**THE CHALLENGE:**

**[PUZZLE/INVESTIGATION: d20 + INT modifier]**

The treasure is hidden behind a puzzle or challenge.

**DM:** Present the puzzle. Let Christopher think through it before rolling.

**ROLL FOR SUCCESS:**
- **20 (Natural 20):** Perfect! Solved immediately! **+1 coin**
- **15-19:** Excellent deduction!
- **10-14:** You figure it out!
- **5-9:** Takes time but you succeed! **Lose 1 coin**
- **1 (Natural 1):** Comedic mishap but you get it! **Lose 2 coins**

**RESOLUTION:**

Christopher secures the treasure with cleverness and insight.

**REWARD:**
- Artifact Component {13-num}/12
- +5 coins earned
- +1 Stat Point ({13+num} total)

The treasure hunter's odyssey continues.
---

"""

# Template for diplomatic encounters (Lena)
def generate_lena_encounter(num, title, npc_name, challenge_desc):
    return f"""## LENA'S PATH - ENCOUNTER #{num}: {title.upper()}

ENCOUNTER #{num} - LENA: {title.upper()} (REVISED)
========================================================================

**{title.upper()}**
{npc_name}

**LOCATION:** The silver path leads Lena to {challenge_desc}

**SETUP:** Place card #{num} face-down.

**THE CHALLENGE:**

**[DIPLOMACY/PERSUASION: d20 + CHA modifier]**

A social conflict requires diplomatic resolution.

**DM:** Present the conflict. Let Lena choose her approach before rolling.

**ROLL FOR DIPLOMACY:**
- **20 (Natural 20):** Perfect mediation! Everyone's happy! **+1 coin**
- **15-19:** Excellent negotiation!
- **10-14:** Conflict resolved!
- **5-9:** Success but awkward! **Lose 1 coin**
- **1 (Natural 1):** Hilarious but effective! **Lose 2 coins**

**RESOLUTION:**

Lena secures agreement and earns the artifact through skilled diplomacy.

**REWARD:**
- Artifact Component {13-num}/12
- +5 coins earned
- +1 Stat Point ({13+num} total)

The diplomat's path continues.
---

"""

# Generate all encounters 10 through 1
output = ""

encounters = [
    (10, "The Arena of Legends", "The Voice of Glory", "a massive coliseum where glory is earned through combat."),
    (9, "The Frozen Fortress", "The Ice Commander", "a fortress of ice where a tactical battle awaits."),
    (8, "The Mountain Duel", "The Blade Master", "a mountain peak where honor demands single combat."),
    (7, "The Canyon Ambush", "The Guerrilla Fighter", "a narrow canyon where strategy matters more than strength."),
    (6, "The Sacred Ground", "The Monk Warrior", "sacred ground where combat becomes meditation."),
    (5, "The Underground Arena", "The Pit Champion", "an underground fighting pit where survival is victory."),
    (4, "The Siege Defense", "The Wall Captain", "defensive fortifications under siege."),
    (3, "The Naval Battle", "The Ship Commander", "a naval vessel where sea combat rules."),
    (2, "The Sky Fortress", "The Air Marshal", "a floating fortress in the clouds."),
    (1, "The Final Battlefield", "The War General", "the ultimate battlefield before the final push."),
]

for num, title, npc, desc in encounters:
    output += generate_nick_encounter(num, title, npc, desc)
    output += generate_christopher_encounter(num, f"{title} (Treasure)", npc, desc)
    output += generate_lena_encounter(num, f"{title} (Diplomatic)", npc, desc)

    # Add spending/random encounter between some
    if num % 2 == 0:
        output += f"""====================================================================================================
SPENDING ENCOUNTER: MERCHANT #{11-num}
====================================================================================================

**The Traveling Merchant appears offering useful items for coins.**

**MERCHANT'S WARES:**
- Healing Potion (2 coins): Auto-succeed next roll
- Lucky Charm (3 coins): Reroll any die
- Smoke Bomb (5 coins): Escape non-combat situation
- Magic Item (10 coins): +2 to all rolls next encounter

**DM:** Let players shop. Keep it brief (2-3 minutes).

====================================================================================================
"""

# Write to file
with open('/home/user/DnD-Revised-Potential/remaining_encounters.txt', 'w') as f:
    f.write(output)

print(f"Generated {len(output)} characters of encounter content")
print("File written to: remaining_encounters.txt")
