#!/usr/bin/env python3
"""
Process the campaign script to:
1. Update combat to roll-vs-roll system
2. Shorten Cameo encounters to target length
3. Keep Spending/Random encounters as-is
"""

def shorten_lena_cameo_12():
    """Return a shortened version of Lena's Cameo 12 encounter"""
    return """## LENA - CAMEO 12: THE HALL OF AWKWARD NEGOTIATIONS

CAMEO 12 - LENA: THE HALL OF AWKWARD NEGOTIATIONS (REVISED)
========================================================================

**THE HALL OF AWKWARD NEGOTIATIONS**
A Nervous Noble - The Lord of First Impressions

**LOCATION:** The silver path leads Lena to a magnificent palace that seems almost right, but slightly off. A noble in a tilted fedora stumbles down the grand staircase, trying desperately to appear confident. "Oh! Princess! You're here! I'm the Lord of First Impressions! I need your help hosting a summit of awkward kingdoms!"

**SETUP:** Place card #12 face-down.

**THE CHALLENGE - DIPLOMATIC COACHING:**

**[PART 1 - THE GREETING TEST: d20 + CHA modifier]**

The Lord must greet five different representatives, each requiring a different approach:
- The Stoic Knight (formal and brief)
- The Friendly Merchant (warm and enthusiastic)
- The Shy Scholar (gentle and patient)
- The Proud Noble (confident respect)
- The Jovial Bard (playful and authentic)

**DM:** Let Lena coach the Lord on how to greet each one appropriately.

**Roll to see how well the Lord follows Lena's coaching:**
- **20:** Perfect! All five feel welcome! **+1 coin**
- **15-19:** Excellent! Everyone is comfortable!
- **10-14:** Good enough! A few awkward moments but it works!
- **5-9:** Rocky start but they recover! **Lose 1 coin**
- **1:** Maximum awkwardness but endearing! **Lose 2 coins**

**[PART 2 - DIPLOMATIC WISDOM]**

The Lord asks: "What's more important—successful diplomacy or authentic diplomacy?"

**DM:** Let Lena answer (all answers are valid—this is about the player's philosophy)

The Lord responds thoughtfully, realizing: "Diplomacy isn't about being smooth. It's about being real while also being kind."

**NARRATIVE CONNECTION:**
He mentions: "You're not the first diplomat I've seen today. Well, maybe you are? Time is weird. But there are others on different paths!"

**RESOLUTION:**

The **Charm Crystal** appears—a silver stone glowing with warm light.

"You taught me that diplomacy balances authenticity with appropriateness. Thank you, princess!"

**REWARD:**
- Charm Crystal (Artifact 1/12)
- +5 coins earned
- +1 Stat Point (13 total)

The diplomat's path continues, carrying the reminder that genuine effort matters more than perfection.
---

"""


def shorten_nick_encounter(encounter_text, encounter_num, title, character_name):
    """Shorten a Nick encounter to target length"""
    # For now, return the encounter text as-is if it's already short
    # We'll manually process the longer ones
    return encounter_text


def update_combat_mechanics(text):
    """Update any combat sections to use roll-vs-roll system"""
    # Replace health/armor references with roll-vs-roll
    replacements = {
        "health points": "combat exchanges",
        "HP": "wins",
        "armor class": "combat roll",
        "AC": "defense roll",
        "damage": "exchange win",
        "takes damage": "loses the exchange",
        "deal damage": "win the exchange",
        "reduce HP": "score a win",
        "hit points": "combat wins",
    }

    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)

    return result


def main():
    """Main processing function"""
    # Read the original file
    with open('/home/user/DnD-Revised-Potential/CAMPAIGN_SCRIPT.txt', 'r') as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from original file")

    # For now, let's identify all the Cameo encounters
    cameo_starts = []
    for i, line in enumerate(lines):
        if 'CAMEO 12' in line or 'CAMEO 11' in line or 'CAMEO 10' in line:
            cameo_starts.append((i, line.strip()))

    for start in cameo_starts[:10]:  # Show first 10
        print(f"Line {start[0]}: {start[1]}")


if __name__ == "__main__":
    main()
