#!/usr/bin/env python3
"""
Script to add transition sentences at the end of cameo and special encounters.
Version 2 - handles all encounter ending patterns.
"""

import re
import hashlib

def determine_character_and_path(section_text, line_num):
    """Determine which character's path this encounter belongs to."""

    # Split into lines and check from bottom to top (most recent context first)
    lines = section_text.split('\n')

    # First check the most recent 30 lines for encounter headers
    for i in range(len(lines) - 1, max(0, len(lines) - 30), -1):
        line = lines[i]
        line_upper = line.upper()

        # Check for explicit encounter headers
        if 'CAMEO' in line_upper or 'ENCOUNTER' in line_upper:
            if 'NICK' in line_upper or "NICK'S" in line_upper:
                return ('Nick', 'crimson', 'warrior')
            elif 'CHRISTOPHER' in line_upper or "CHRISTOPHER'S" in line_upper:
                return ('Christopher', 'golden', 'treasure hunter')
            elif 'LENA' in line_upper or "LENA'S" in line_upper:
                return ('Lena', 'silver', 'diplomat')

    # Then check for path descriptions
    text_lower = section_text.lower()

    # Count mentions of each character (weighted towards end)
    recent_text = ' '.join(lines[-20:]).lower()

    if 'golden path leads christopher' in text_lower or 'christopher' in recent_text:
        return ('Christopher', 'golden', 'treasure hunter')
    elif 'crimson path leads nick' in text_lower or 'silver path leads lena' in text_lower:
        if 'crimson' in recent_text or 'nick' in recent_text:
            return ('Nick', 'crimson', 'warrior')
        else:
            return ('Lena', 'silver', 'diplomat')

    # Check for path-specific keywords in recent context
    if 'crimson path' in recent_text or 'battlefield' in recent_text:
        return ('Nick', 'crimson', 'warrior')
    elif 'golden path' in recent_text or 'treasure hunter' in recent_text:
        return ('Christopher', 'golden', 'treasure hunter')
    elif 'silver path' in recent_text or 'diplomat' in recent_text:
        return ('Lena', 'silver', 'diplomat')

    # Default fallback
    return ('the hero', 'golden', 'adventurer')

def get_artifact_from_context(context_text):
    """Extract artifact/reward name from context."""
    # Look for common artifact patterns with word boundaries
    patterns = [
        r'\b([\w\s]{1,30}Crystal)\b',
        r'\b([\w\s]{1,30}Stone)\b',
        r'\b([\w\s]{1,30}Gauntlets?)\b',
        r'\b([\w\s]{1,30}Cloak)\b',
        r'\b([\w\s]{1,30}Compass)\b',
        r'\b([\w\s]{1,30}Banner)\b',
        r'\b([\w\s]{1,30}Greaves)\b',
        r'\b([\w\s]{1,30}Amulet)\b',
        r'\b([\w\s]{1,30}Pack)\b',
        r'ARTIFACT ACQUIRED[:\s]*\n+([^\n]+)',
        r'\*\*([A-Z][A-Z\s]+)\*\*\s*materialize',
    ]

    for pattern in patterns:
        match = re.search(pattern, context_text, re.IGNORECASE)
        if match:
            artifact_name = match.group(1).strip()
            # Clean up - remove leading articles and excessive words
            artifact_name = re.sub(r'^(the|a|an)\s+', '', artifact_name, flags=re.IGNORECASE)
            # Limit length
            if len(artifact_name) < 50:
                return artifact_name

    return None

def generate_transition(char_name, path_color, role, artifact=None, encounter_type='cameo'):
    """Generate appropriate transition text."""

    # Create seed for consistent but varied transitions
    seed = f"{char_name}{path_color}{artifact or ''}{encounter_type}"
    hash_val = int(hashlib.md5(seed.encode()).hexdigest(), 16)

    # Use artifact only if it's clean and short
    use_artifact = artifact and len(artifact) < 30 and not any(bad in artifact.lower() for bad in ['you', 'seek', 'the keeper', 'reward'])

    if path_color == 'crimson':
        if use_artifact:
            templates = [
                f"{char_name} secures the {artifact} and continues down the crimson path toward the next battlefield.",
                f"The warrior nods and moves forward with the {artifact}, the crimson path stretching ahead to the next challenge.",
                f"With the {artifact} safely stowed, {char_name} presses onward along the crimson path.",
                f"The battlefield fades behind {char_name} as the crimson path leads to the next trial.",
                f"{char_name} takes a moment to catch his breath, then continues his journey down the crimson path.",
            ]
        else:
            templates = [
                f"{char_name} secures the prize and continues down the crimson path toward the next battlefield.",
                f"The warrior nods and moves forward, the crimson path stretching ahead to the next challenge.",
                f"With his reward safely stowed, {char_name} presses onward along the crimson path.",
                f"The battlefield fades behind {char_name} as the crimson path leads to the next trial.",
                f"{char_name} takes a moment to catch his breath, then continues his journey down the crimson path.",
            ]
    elif path_color == 'golden':
        if use_artifact:
            templates = [
                f"{char_name} carefully packs the {artifact} and sets off down the golden path toward his next destination.",
                f"With the {artifact} secured in his pack, the treasure hunter continues his odyssey.",
                f"The golden path beckons as {char_name} moves forward, one step closer to his goal.",
                f"{char_name} tucks the {artifact} away safely and ventures onward along the golden path.",
                f"The treasure hunter adjusts his pack and follows the golden path toward the next challenge.",
            ]
        else:
            templates = [
                f"{char_name} carefully packs the treasure and sets off down the golden path toward his next destination.",
                f"With the prize secured in his pack, the treasure hunter continues his odyssey.",
                f"The golden path beckons as {char_name} moves forward, one step closer to his goal.",
                f"{char_name} tucks his reward away safely and ventures onward along the golden path.",
                f"The treasure hunter adjusts his pack and follows the golden path toward the next challenge.",
            ]
    else:  # silver
        if use_artifact:
            templates = [
                f"{char_name} reflects on the {artifact} as she continues down the silver path toward her next challenge.",
                f"The diplomat thanks her host and departs with the {artifact}, the silver path winding ahead.",
                f"With the {artifact} secured, {char_name} continues her diplomatic journey.",
                f"The silver path stretches onward as {char_name} moves toward her next encounter.",
                f"{char_name} takes her leave gracefully, following the silver path to its next destination.",
            ]
        else:
            templates = [
                f"{char_name} reflects on the encounter as she continues down the silver path toward her next challenge.",
                f"The diplomat thanks her host and departs, the silver path winding ahead.",
                f"With newfound knowledge secured, {char_name} continues her diplomatic journey.",
                f"The silver path stretches onward as {char_name} moves toward her next encounter.",
                f"{char_name} takes her leave gracefully, following the silver path to its next destination.",
            ]

    return templates[hash_val % len(templates)]

def has_existing_transition(lines, start_idx, end_idx):
    """Check if encounter already has a transition."""
    for i in range(max(0, end_idx - 10), end_idx):
        if i < len(lines):
            line = lines[i].strip().lower()
            if any(phrase in line for phrase in [
                'path continues',
                'journey continues',
                'adventure continues',
                '[end of encounter]',
                'moves forward',
                'continues down',
                'path leads',
                'sets off',
                'departs',
            ]):
                return True
    return False

def add_transitions_v2(input_file, output_file):
    """Read the file and add transitions where needed."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    transitions_added = 0
    skip_until = 0

    i = 0
    while i < len(lines):
        if i < skip_until:
            new_lines.append(lines[i])
            i += 1
            continue

        current_line = lines[i]

        # Pattern 1: **REWARD:** followed by blank line and ---
        if current_line.strip().startswith('**REWARD:**'):
            new_lines.append(current_line)
            j = i + 1
            reward_content = current_line

            while j < len(lines):
                if lines[j].strip() == '' and j + 1 < len(lines) and lines[j + 1].strip().startswith('---'):
                    # Check if transition already exists
                    if not has_existing_transition(lines, i, j):
                        new_lines.append(lines[j])  # blank line

                        # Get context (look back more, forward less to avoid next encounter)
                        context_start = max(0, i - 150)
                        context_text = ''.join(lines[context_start:i+5])
                        char_name, path_color, role = determine_character_and_path(context_text, i)
                        # Don't use artifact extraction - too unreliable
                        artifact = None

                        # Add transition
                        transition = generate_transition(char_name, path_color, role, artifact, 'cameo')
                        new_lines.append(f"\n{transition}\n")
                        transitions_added += 1

                        skip_until = j + 1
                    else:
                        new_lines.append(lines[j])
                        skip_until = j + 1
                    break
                else:
                    new_lines.append(lines[j])
                    reward_content += lines[j]
                    j += 1

            i = skip_until if skip_until > i else i + 1
            continue

        # Pattern 2: **[Players mark ...] followed by dividers
        if current_line.strip().startswith('**[Players mark'):
            new_lines.append(current_line)

            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                if i + 2 < len(lines) and (lines[i + 2].strip().startswith('====') or lines[i + 2].strip().startswith('---')):
                    # Check if transition already exists
                    if not has_existing_transition(lines, max(0, i - 5), i):
                        new_lines.append(lines[i + 1])  # blank line

                        # Get context
                        context_start = max(0, i - 150)
                        context_text = ''.join(lines[context_start:i])
                        char_name, path_color, role = determine_character_and_path(context_text, i)

                        # Determine encounter type
                        encounter_type = 'special'
                        for line in lines[context_start:i]:
                            upper_line = line.upper()
                            if 'BLACKSMITH' in upper_line:
                                encounter_type = 'blacksmith'
                            elif 'POTION' in upper_line:
                                encounter_type = 'potion'
                            elif 'BEGGAR' in upper_line or 'GOD' in upper_line:
                                encounter_type = 'beggar'
                            elif 'GAMBLER' in upper_line:
                                encounter_type = 'gambler'
                            elif 'SAGE' in upper_line:
                                encounter_type = 'sage'

                        transition = generate_transition(char_name, path_color, role, None, encounter_type)
                        new_lines.append(f"\n{transition}\n")
                        transitions_added += 1

                        skip_until = i + 2
                    else:
                        new_lines.append(lines[i + 1])
                        skip_until = i + 2

                    i = skip_until
                    continue

        # Pattern 3: Long divider ――――――――――――
        if current_line.strip().startswith('――――――――――――'):
            # Check if transition already exists
            if not has_existing_transition(lines, max(0, i - 15), i):
                # Get context
                context_start = max(0, i - 200)
                context_text = ''.join(lines[context_start:i])

                # Skip if this is a section divider (not an encounter ending)
                if 'TRANSITION NARRATION:' in ''.join(lines[max(0, i-5):i+5]):
                    new_lines.append(current_line)
                    i += 1
                    continue

                # Skip if the previous few lines are mostly empty or headers
                prev_content = ''.join(lines[max(0, i-5):i]).strip()
                if len(prev_content) < 50 or prev_content.startswith('#'):
                    new_lines.append(current_line)
                    i += 1
                    continue

                # This looks like an encounter ending
                char_name, path_color, role = determine_character_and_path(context_text, i)
                # Don't use artifact extraction - too unreliable
                artifact = None

                # Add transition before the divider
                transition = generate_transition(char_name, path_color, role, artifact, 'long')
                new_lines.append(f"\n{transition}\n")
                transitions_added += 1

            new_lines.append(current_line)
            i += 1
            continue

        new_lines.append(current_line)
        i += 1

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    return transitions_added

if __name__ == '__main__':
    input_file = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt'
    output_file = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt.updated'

    count = add_transitions_v2(input_file, output_file)
    print(f"Added {count} transitions")
    print(f"Output written to: {output_file}")
