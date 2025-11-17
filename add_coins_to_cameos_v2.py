#!/usr/bin/env python3
"""
Script to add "+5 coins earned" notation to all 36 Cameo encounters.
Updates the REWARD section of each Cameo encounter.
Version 2: More comprehensive pattern matching
"""

import re

def add_coins_to_cameos(file_path):
    """Add +5 coins earned to all Cameo encounter REWARD sections."""

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modifications = 0
    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for lines that contain an Artifact reference in a REWARD section
        if '(Artifact ' in line and '/12)' in line and line.strip().startswith('-'):
            # Check if the next few lines already have "+5 coins earned"
            has_coins = False
            for j in range(i, min(i+5, len(lines))):
                if '+5 coins earned' in lines[j]:
                    has_coins = True
                    break

            # If not, add it
            if not has_coins:
                # Insert the coin line after the artifact line
                indent = len(line) - len(line.lstrip())
                coin_line = ' ' * indent + '- +5 coins earned\n'
                lines.insert(i + 1, coin_line)
                modifications += 1
                i += 1  # Skip the line we just inserted

        i += 1

    # Now clean up old "Current coins:" lines
    lines = [line for line in lines if not re.search(r'- Current coins: \d+ \+/- based on roll', line)]
    lines = [line for line in lines if not re.search(r'- Current coins: varies', line)]
    lines = [line for line in lines if not re.search(r'- Current coins: HIGHLY variable', line)]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return modifications

if __name__ == '__main__':
    file_path = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt'

    print("Adding +5 coins earned to all Cameo encounters...")
    num_updated = add_coins_to_cameos(file_path)

    print(f"Added +5 coins earned to {num_updated} Cameo encounters")
    print("Done!")
