# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DnD-Revised-Potential** is a custom Dungeons & Dragons campaign featuring a revised character progression system and an immersive three-path adventure structure.

### Campaign Structure

The campaign follows a unique narrative where three player characters (Christopher, Lena, and Nick) must each complete separate quests to rescue their captured leader from the Void Tyrant at Shadowspire Fortress.

**Three Character Paths:**
- **Golden Path** (Christopher) - Treasure Hunter's Odyssey: Collecting treasures from land, sea, and sky to forge the Key of Fortune
- **Silver Path** (Lena) - Diplomat's Gambit: Uncovering secrets in towns and taverns to weave the Key of Knowledge
- **Crimson Path** (Nick) - Battlefront Crusade: Winning victories on ten battlefields to earn the Key of Power

Each path contains 12 numbered encounters (Cameo 12 down to Cameo 1), plus special encounters (Sage, Gambler, Talent Show, Vendor, Cursed Warrior).

### Character Progression System

**Revised Stats System:**
- Players start with 12 stat points to distribute across 6 abilities (STR, DEX, CON, INT, WIS, CHA)
- Players earn 1 additional stat point per encounter (17 total encounters = 29 total points at campaign end)
- Stat modifiers: 8+ points = +3, 4-7 points = +2, 2-3 points = +1, 0-1 points = -1

**Coin System:**
- Players start with 12 coins (marked with circles ○)
- Coins are used for various in-game purchases and challenges

## Repository Structure

Currently, the repository contains:
- `Final Script.docx` - Complete campaign script including DM narration, encounter details, and character sheets

## Working with This Repository

### Extracting Content from the DOCX File

Since the main content is in a Word document, use this command to extract readable text:

```bash
unzip -q -c "Final Script.docx" word/document.xml 2>/dev/null | sed 's/<[^>]*>//g' | sed 's/^[[:space:]]*//' | sed '/^$/d'
```

### Potential Development Tasks

When working on this repository, you may be asked to:

1. **Convert to Markdown**: Extract content from the .docx and create structured markdown files (e.g., `campaign-script.md`, `character-sheet.md`, `encounters/`)

2. **Create Digital Tools**: Build character sheet generators, stat calculators, or encounter tracking systems

3. **Organize Content**: Split the monolithic script into:
   - `docs/dm-script.md` - DM narration and instructions
   - `docs/character-sheets/` - Character creation templates
   - `docs/encounters/nick/` - Nick's 12 encounters
   - `docs/encounters/christopher/` - Christopher's 12 encounters
   - `docs/encounters/lena/` - Lena's 12 encounters
   - `docs/special-encounters/` - Sage, Gambler, Talent Show, etc.

4. **Build Interactive Tools**: Create web apps or CLI tools for:
   - Character sheet management
   - Stat point allocation and validation
   - Encounter progression tracking
   - Dice rolling utilities

### Campaign Narrative Flow

**Act I: The Tavern & The Taking**
- Players meet at the Howling Moon Tavern (run by Max the Husky and Luna the Aussiedor)
- The Void Tyrant captures the party leader
- Players must choose their individual paths
- The three heroes separate

**Act II: The Three Paths** (12 encounters each)
- Each character faces unique challenges suited to their skills
- Character stats grow from 12 to 29 points
- Special encounters provide items, information, and resources

**Act III: The Reunion & Final Battle**
- Heroes reunite at Shadowspire Fortress
- Three keys combine to unlock the leader's prison
- Final confrontation with the Void Tyrant

### Key NPCs

- **Max** - Silver-and-white Husky innkeeper with blue eyes and boundless energy
- **Luna** - Brown-and-white Aussiedor innkeeper with remarkable intelligence
- **The Void Tyrant** - Primary antagonist who imprisoned the party leader
- **Various Cameo Characters** - Encountered throughout the 12-stop journey on each path

### Important Mechanics

**The Knock Code**: 3 knocks, pause, 2 knocks, pause, 1 knock (represents: three heroes, two companions, one leader)

**Stat Modifier Table**:
- 8+ points: +3 (Master)
- 4-7 points: +2 (Proficient)
- 2-3 points: +1 (Average)
- 0-1 points: -1 (Weak)

**Point Progression**: 12 (start) + 1 (Cameo 12) + 1 (Cameo 11) + ... + 1 (Cursed Warrior) + 1 (Cameo 2) + 1 (Cameo 1) = 29 total points

## File Formats

When creating new files for this project:
- Use Markdown (.md) for documentation and narrative content
- Use JSON for character data, encounter definitions, and game state
- Use YAML for configuration files
- Consider web technologies (HTML/CSS/JS) for interactive character sheets
- Consider Python for CLI tools and game mechanics

## Campaign Tone

The campaign balances:
- **Epic fantasy adventure** with high stakes and dramatic moments
- **Humor and lightheartedness** through parody characters and witty dialogue
- **Emotional depth** through bonds of friendship and sacrifice
- **Player agency** with meaningful choices and consequences
