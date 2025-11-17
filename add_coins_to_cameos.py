#!/usr/bin/env python3
"""
Script to add "+5 coins earned" notation to all 36 Cameo encounters.
Updates the REWARD section of each Cameo encounter.
"""

import re

def add_coins_to_cameos(file_path):
    """Add +5 coins earned to all Cameo encounter REWARD sections."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find REWARD sections in Cameo encounters
    # We need to add "+5 coins earned" right after the artifact line

    # Pattern 1: Find lines like "- <Item Name> (Artifact X/12)"
    # followed by "- +1 Stat Point"
    # We want to insert "+5 coins earned" between them

    pattern = r'(\*\*REWARD:\*\*\n- .*?\(Artifact \d+/12\)\n)(\- \+1 Stat Point)'

    # Replace with artifact line + coins line + stat point line
    replacement = r'\1- +5 coins earned\n\2'

    content_updated = re.sub(pattern, replacement, content)

    # Also need to remove or update the old "Current coins: 12 +/- based on roll" lines
    # Replace them with just the new coin system
    content_updated = re.sub(
        r'- Current coins: \d+ \+\/- based on rolls?\n?',
        '',
        content_updated
    )

    # Also remove standalone "Current coins:" lines
    content_updated = re.sub(
        r'- Current coins: \d+ \+\/- based on roll\n',
        '',
        content_updated
    )

    # Count how many replacements were made
    artifact_matches = re.findall(pattern, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_updated)

    return len(artifact_matches)

if __name__ == '__main__':
    file_path = '/home/user/DnD-Revised-Potential/ENHANCED_CAMPAIGN_COMPLETE.txt'

    print("Adding +5 coins earned to all Cameo encounters...")
    num_updated = add_coins_to_cameos(file_path)

    print(f"Updated {num_updated} Cameo encounter REWARD sections")
    print("Done!")
