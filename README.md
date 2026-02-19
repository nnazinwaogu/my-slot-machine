# Slot Machine Game

A text-based slot machine simulator with realistic betting mechanics, balance management, and multiplier payouts.

**Author:** Nnazirim Nwaogu
**Current Version:** 2.0.0
**Latest Stable:** 2.0.0

---

## Description

This is a fully-featured slot machine game written in Python. It simulates a 3×3 slot machine experience where players can place bets, spin for fruit combinations, and manage their balance. The game includes a multiplier system for varied payouts, deposit functionality, comprehensive statistics tracking, and a complete pytest test suite with 28 tests and 70% coverage.

---

## Features

- **3×3 Grid Display**: Enhanced visual representation with proper formatting for 9 symbols
- **Multi-Line Betting**: 8 traditional slot machine paylines (horizontal, vertical, diagonal)
- **Comprehensive Testing**: 28 pytest tests with 70% coverage and detailed reporting
- **Enhanced Symbols**: 6 slot symbols with weighted random generation for realistic odds
- **Multiplier System**: Random 2x-12x multipliers (only even indices apply) multiply your winnings
- **Balance Management**: Deposit, track current balance, and monitor profit/loss
- **Game Statistics**: View total spins, total wagered amount, and net profit/loss
- **Interactive Menu System**: Navigate through playing, depositing, changing lines, and quitting
- **Win Feedback**: Instant notifications on wins, losses, and multipliers applied
- **Modular Architecture**: Clean separation of concerns with well-organized functions

---

## Installation

### Requirements

- Python 3.6 or higher
- pytest package (for testing)
- pytest-cov package (for coverage reporting) *optional*

### Setup

1. Clone or download the repository
2. Navigate to the project directory in your terminal
3. Ensure `slot_machine.py` is in your working directory
4. Install testing dependencies (optional):
   ```bash
   pip install pytest pytest-cov
   ```

---

## Usage

### Running the Game

```bash
# Run the slot machine game
python slot_machine.py

# Run with verbose output
python slot_machine.py -v

# Run tests (requires pytest)
python -m pytest

# Run tests with coverage reporting
python -m pytest --cov=slot_machine --cov-report=html

# View coverage report
start htmlcov/index.html  # Windows
open htmlcov/index.html    # macOS
xdg-open htmlcov/index.html  # Linux
```

### Gameplay Flow

1. **Main Menu**: Choose to Spin (1), Change Lines (2), Deposit (3), or Quit (4)
2. **Betting**: Enter your wager amount (must be ≤ current balance)
3. **Spin**: Game generates 3×3 grid with weighted random symbols
4. **Win Detection**: Checks all active paylines for winning combinations
5. **Multiplier Application**: Applies random multiplier to total winnings
6. **Results Display**: Shows updated balance, statistics, and spin results
7. **Continue or Quit**: Return to main menu or exit game

### Example Session

```
Welcome to the Enhanced Slot Machine!
- 3×3 Grid Display
- Multi-Line Betting (up to 8 lines)
- Traditional Slot Symbols
- Improved Code Organization

=========================
MAIN MENU
=========================
Balance: $100
Spins: 0
Lines Bet: 1

Choose an option:
1. Spin
2. Change Lines Bet
3. Deposit
4. Quit

Enter choice (1-4): 1

Enter bet amount (Balance: $100): $50

=========================
SLOT MACHINE - 3×3 GRID
=========================
|  Cherry  |  Lemon   |   Bell   |
=========================
|  Cherry  |  Lemon   |   Bell   |
=========================
|  Cherry  |  Lemon   |   Bell   |
=========================

No winning lines this spin!

Current Balance: $50
Total Wagered: $50
Net Position: $-50

=========================
MAIN MENU
=========================
Balance: $50
Spins: 1
Lines Bet: 1

Choose an option:
1. Spin
2. Change Lines Bet
3. Deposit
4. Quit
```

---

## Game Rules

### Win Conditions

- **Winning Spin**: All three symbols in an active payline must match (e.g., Cherry, Cherry, Cherry)
- **Losing Spin**: Any mismatch in an active payline results in loss of wager for that line
- **Multi-Line Wins**: Can win on multiple paylines simultaneously

### Payouts

- **Base Winning Amount**: Bet amount × 3 (for each winning line)
  - Example: Bet $50 on three Cherries = $150 base winnings per line
- **Total Payout**: Sum of all winning line payouts × random multiplier
  - Example: 2 winning lines × $150 × 4x multiplier = $1200 total payout
- **Loss**: Player loses their wager amount (deducted from balance)
- **Multiplier System**: Random multipliers (2x, 4x, 6x, 8x, 10x, 12x) only apply to even indices

### Balance Mechanics

- **Starting Balance**: Set upon first deposit (default $100)
- **Current Balance**: Updates after each spin (win or loss)
- **Profit/Loss**: Running total of net gains or losses from starting balance
- **Deposits**: Can deposit additional funds at any time before spinning
- **Lines Bet**: Number of active paylines (1-8, default 1)

### Paylines (8 Total)

1. **Middle Horizontal**: Row 1 (positions 1,2,3)
2. **Top Horizontal**: Row 0 (positions 0,1,2)
3. **Bottom Horizontal**: Row 2 (positions 6,7,8)
4. **Diagonal**: Top-left to bottom-right (positions 0,4,8)
5. **Anti-diagonal**: Top-right to bottom-left (positions 2,4,6)
6. **Left Vertical**: Column 0 (positions 0,3,6)
7. **Middle Vertical**: Column 1 (positions 1,4,7)
8. **Right Vertical**: Column 2 (positions 2,5,8)

---

## Controls

| Input | Action |
|-------|--------|
| 1 | Spin / Play |
| 2 | Change Lines Bet |
| 3 | Deposit |
| 4 | Quit / Leave |

At each prompt, enter the corresponding number and press Enter.

---

## Testing

### Running Tests

The game includes a comprehensive pytest test suite with 28 tests covering all functionality:

```bash
# Run all tests
python -m pytest

# Run with detailed output
python -m pytest -v

# Run specific test categories
python -m pytest -m "unit"      # Unit tests only
python -m pytest -m "integration"  # Integration tests only
python -m pytest -m "performance"  # Performance tests only
```

For detailed testing notes, see [TESTS.md](TESTS.md).

---

## Architecture

### Modular Design

The game follows a modular architecture with clear separation of concerns:

- **Game State**: Centralized state management with all game variables
- **Symbols Module**: Symbol definitions and properties
- **Paylines Module**: Traditional slot machine payline configurations
- **Grid Generation**: Weighted random symbol generation for 3×3 grid
- **Win Checking**: Multi-line win detection logic
- **Multiplier System**: Random multiplier application
- **Balance Management**: Comprehensive balance tracking
- **User Interface**: Interactive menu and display functions

### Data Structures

- **Symbols**: Dictionary with value and weight properties
- **Paylines**: Dictionary mapping line IDs to position coordinates
- **Game State**: Dictionary containing all game variables
- **Grid**: 3×3 list structure for slot machine display

---

## Future Improvements

Potential features for future versions:

- **GUI Version**: Graphical user interface with animated reels
- **Difficulty Levels**: Adjustable house edge or multiplier ranges
- **Leaderboard**: Track high scores and best winning streaks
- **More Symbols**: Expand from 6 to 8+ unique slot symbols
- **Themed Variations**: Different slot machine themes (Vegas, Retro, Fantasy, etc.)
- **Sound Effects**: Audio feedback for spins and wins
- **Save/Load**: Persistent player accounts and game progress
- **Enhanced Testing**: Fix integration test failures and reach 90%+ coverage
- **Advanced Features**: Progressive jackpots, bonus rounds, etc.

---

## Version History

**Current Version:** 2.0.0  
**Latest Stable:** 2.0.0  
**Author:** Nnazirim Nwaogu

### Version 2.0.0 (2026-02-18)
- Complete architectural overhaul from version 1.5
- 3×3 grid display system
- Multi-line betting (8 paylines)
- Comprehensive pytest test suite (28 tests)
- Enhanced symbol system with weighted random generation
- Multiplier system (2x-12x)
- Improved user interface and menu system
- Modular function structure

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project for both personal and commercial purposes. See the LICENSE file for more details.

### MIT License Summary
- ✓ Commercial use
- ✓ Modification
- ✓ Distribution
- ✓ Private use
- ✗ Liability
- ✗ Warranty

---

For detailed technical changes and patch notes, see [CHANGELOG.md](CHANGELOG.md).