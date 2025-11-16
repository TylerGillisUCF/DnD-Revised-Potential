#!/usr/bin/env python3
"""
Script to add transition sentences at the end of cameo and special encounters.
"""

import re

def determine_character_path(section_text, line_num):
    """Determine which character's path this encounter belongs to."""
    # Look for character names in nearby context
    if 'Nick' in section_text or 'warrior' in section_text.lower() or 'battlefield' in section_text.lower():
        return 'crimson'
    elif 'Christopher' in section_text or 'treasure' in section_text.lower():
        return 'golden'
    elif 'Lena' in section_text or 'diplomat' in section_text.lower():
        return 'silver'

    # Default based on line position (approximate)
    if line_num < 3500:
        return 'golden'  # First third
    elif line_num < 7500:
        return 'crimson'  # Middle third
    else:
        return 'silver'  # Last third

def get_transition_for_cameo(path, reward_text):
    """Generate appropriate transition for cameo encounters."""
    transitions = {
        'crimson': [
            "The warrior secures his new prize and continues down the crimson path. The next battlefield awaits.",
            "Nick nods in respect and moves forward, the crimson path stretching toward his next challenge.",
            "With the artifact safely stowed, the warrior presses on toward his next trial.",
            "The battlefield fades behind him as Nick continues his journey along the crimson path.",
        ],
        'golden': [
            "Christopher carefully packs the treasure and sets off down the golden path toward his next destination.",
            "With the artifact secured in his pack, the treasure hunter continues his odyssey.",
            "The golden path beckons as Christopher moves forward, one step closer to his goal.",
            "Christopher tucks the prize away and ventures onward along the golden path.",
        ],
        'silver': [
            "Lena reflects on the encounter as she continues down the silver path toward her next challenge.",
            "The diplomat thanks her host and departs, the silver path winding ahead.",
            "With newfound knowledge secured, Lena continues her diplomatic journey.",
            "The silver path stretches onward as Lena moves toward her next encounter.",
        ]
    }

    # Use a simple hash to pick a consistent but varied transition
    import hashlib
    hash_val = int(hashlib.md5(reward_text.encode()).hexdigest(), 16)
    options = transitions.get(path, transitions['golden'])
    return options[hash_val % len(options)]

def get_transition_for_special(encounter_type, path):
    """Generate appropriate transition for special encounters (vendor, blacksmith, etc.)."""
    if 'BLACKSMITH' in encounter_type:
        transitions = {
            'crimson': "The warrior thanks the blacksmith and steps back onto the crimson path, better equipped for the battles ahead.",
            'golden': "Christopher nods his appreciation to the blacksmith and returns to the golden path, his gear improved.",
            'silver': "Lena thanks the artisan and continues down the silver path, her equipment enhanced.",
        }
    elif 'POTION' in encounter_type:
        transitions = {
            'crimson': "Nick secures the potions in his pack and returns to the crimson path, ready for what lies ahead.",
            'golden': "With potions safely stowed, Christopher continues his treasure hunt along the golden path.",
            'silver': "Lena carefully packs the potions and moves forward on her diplomatic mission.",
        }
    elif 'BEGGAR' in encounter_type or 'GOD' in encounter_type:
        transitions = {
            'crimson': "The encounter leaves Nick thoughtful as he continues down the crimson path.",
            'golden': "Christopher departs with a blessing, the golden path leading him onward.",
            'silver': "Lena reflects on the mysterious encounter as she continues along the silver path.",
        }
    elif 'GAMBLER' in encounter_type:
        transitions = {
            'crimson': "Nick collects his winnings and exits the tavern, returning to the crimson path.",
            'golden': "Christopher pockets his coins and steps back onto the golden path with renewed confidence.",
            'silver': "Lena leaves the gambling hall and continues down the silver path, richer or wiser for the experience.",
        }
    elif 'INNKEEPER' in encounter_type or 'MEAL' in encounter_type:
        transitions = {
            'crimson': "Refreshed and fed, Nick continues his journey along the crimson path.",
            'golden': "Christopher thanks the innkeeper and sets off down the golden path, restored.",
            'silver': "Lena departs the inn and continues her diplomatic journey, renewed.",
        }
    else:
        # Generic transition
        transitions = {
            'crimson': "The warrior continues down the crimson path toward his next challenge.",
            'golden': "Christopher sets off along the golden path, moving toward his next destination.",
            'silver': "Lena continues her journey down the silver path.",
        }

    return transitions.get(path, transitions['golden'])

def add_transitions(input_file, output_file):
    """Read the file and add transitions where needed."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    transitions_added = 0
    i = 0

    while i < len(lines):
        current_line = lines[i]
        new_lines.append(current_line)

        # Check if this is a REWARD section
        if current_line.strip().startswith('**REWARD:**'):
            # Find the end of the reward section (blank line followed by ---)
            j = i + 1
            reward_content = current_line

            while j < len(lines):
                if lines[j].strip() == '' and j + 1 < len(lines) and lines[j + 1].strip().startswith('---'):
                    # Found the pattern! Add transition after blank line
                    new_lines.append(lines[j])  # blank line

                    # Collect context to determine path
                    context_start = max(0, i - 50)
                    context_text = ''.join(lines[context_start:i+10])
                    path = determine_character_path(context_text, i)

                    # Add transition
                    transition = get_transition_for_cameo(path, reward_content)
                    new_lines.append(f"\n{transition}\n")
                    transitions_added += 1

                    # Skip the blank line we just added
                    i = j + 1
                    break
                else:
                    new_lines.append(lines[j])
                    reward_content += lines[j]
                    j += 1

            if j >= len(lines):
                i += 1
            continue

        # Check if this is a special encounter end marker
        if current_line.strip().startswith('**[Players mark'):
            # Look ahead for dividers
            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                if i + 2 < len(lines) and lines[i + 2].strip().startswith('===='):
                    # Found pattern! Add transition before dividers
                    new_lines.append(lines[i + 1])  # blank line

                    # Determine encounter type and path
                    context_start = max(0, i - 100)
                    context_text = ''.join(lines[context_start:i])
                    path = determine_character_path(context_text, i)

                    # Determine encounter type
                    encounter_type = ''
                    for line in lines[context_start:i]:
                        if '###' in line:
                            encounter_type = line
                            break

                    transition = get_transition_for_special(encounter_type, path)
                    new_lines.append(f"\n{transition}\n")
                    transitions_added += 1

                    i += 2
                    continue
                elif i + 2 < len(lines) and lines[i + 2].strip().startswith('---'):
                    # Simpler divider pattern
                    new_lines.append(lines[i + 1])  # blank line

                    context_start = max(0, i - 100)
                    context_text = ''.join(lines[context_start:i])
                    path = determine_character_path(context_text, i)

                    encounter_type = ''
                    for line in lines[context_start:i]:
                        if 'MEAL' in line or 'INNKEEPER' in line:
                            encounter_type = 'MEAL'
                            break

                    transition = get_transition_for_special(encounter_type, path)
                    new_lines.append(f"\n{transition}\n")
                    transitions_added += 1

                    i += 2
                    continue

        i += 1

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    return transitions_added

if __name__ == '__main__':
    input_file = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt'
    output_file = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt.new'

    count = add_transitions(input_file, output_file)
    print(f"Added {count} transitions")
    print(f"Output written to: {output_file}")
