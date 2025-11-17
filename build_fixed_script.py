#!/usr/bin/env python3
"""
Build the fixed campaign script with:
1. Roll-vs-roll combat system
2. Shortened Cameo encounters
3. Unchanged Spending/Random encounters
"""

import re

# Read the original file
with open('/home/user/DnD-Revised-Potential/CAMPAIGN_SCRIPT.txt', 'r') as f:
    original_content = f.read()

# Read what we've already built
with open('/home/user/DnD-Revised-Potential/Sunday Night Fix.txt', 'r') as f:
    new_content = f.read()

# Start building from what we have
output = new_content

# Now I need to add all remaining encounters systematically
# The file structure is:
# - Cameo 12 (done)
# - Spending 1 (done)
# - Cameo 11 (need to add - shorten if long)
# - Continue through all encounters

# Find the original Cameo 11 sections
nick_11_match = re.search(r'(##NICK\'SPATH-ENCOUNTER#11.*?)((?=##)|(?=====*SPEND)|(?=$))', original_content, re.DOTALL)
christopher_11_match = re.search(r'(##CHRISTOPHER\'SPATH-ENCOUNTER#11.*?)((?=##)|(?=$))', original_content, re.DOTALL)
lena_11_match = re.search(r'(##LENA\'SPATH-ENCOUNTER#11.*?)((?=##)|(?=====*)|(?=$))', original_content, re.DOTALL)

print("Building complete campaign script...")
print(f"Current output length: {len(output)} chars")
print("Processing remaining encounters...")

# Since the encounters are very long and complex, let me use a simpler approach:
# Extract sections and modify them programmatically

def shorten_encounter(text, target_length_lines=70):
    """
    Shorten an encounter to approximately target length while preserving structure
    """
    lines = text.split('\n')

    # If already short enough, return as-is
    if len(lines) <= target_length_lines:
        return text

    # Keep the header, location, setup sections (usually first 20% of lines)
    keep_start = int(len(lines) * 0.2)

    # Keep the resolution, rewards sections (usually last 15% of lines)
    keep_end = int(len(lines) * 0.15)

    # From the middle,take key sections
    result_lines = []
    result_lines.extend(lines[:keep_start])

    # Add simplified middle section
    result_lines.append("")
    result_lines.append("**[ENCOUNTER CHALLENGE]**")
    result_lines.append("")
    result_lines.append("**DM:** Present the challenge to the player. Let them make a choice about their approach.")
    result_lines.append("")
    result_lines.append("**Roll d20 + relevant modifier:**")
    result_lines.append("- **20 (Natural 20):** Exceptional success! **+1 coin**")
    result_lines.append("- **15-19:** Great success!")
    result_lines.append("- **10-14:** Standard success!")
    result_lines.append("- **5-9:** Success with setback! **Lose 1 coin**")
    result_lines.append("- **1 (Natural 1):** Hilarious success! **Lose 2 coins**")
    result_lines.append("")

    # Add the ending
    result_lines.extend(lines[-keep_end:])

    return '\n'.join(result_lines)

def update_combat_to_roll_vs_roll(text):
    """
    Replace health/armor combat with roll-vs-roll system
    """
    # Find combat sections with AC and HP
    combat_pattern = r'(AC\s+\d+,\s+\d+\s+HP.*?(?:\n|$))'

    text = re.sub(r'AC\s+\d+,\s+\d+\s+HP[^\n]*',
                  'COMBAT: Both roll d20 + modifiers. First to 3 wins prevails.', text)

    text = text.replace('hit points', 'combat wins')
    text = text.replace('damage', 'exchange wins')
    text = text.replace('HP', 'wins')
    text = text.replace('armor class', 'combat roll')
    text = text.replace('takes damage', 'loses an exchange')
    text = text.replace('deal damage', 'win an exchange')

    return text

print("\nScript setup complete. Manual processing required for full conversion.")
print("Due to complexity, continuing with bash append method...")

