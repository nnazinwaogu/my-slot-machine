# Slot Machine Game

A text-based slot machine simulator with realistic betting mechanics, balance management, and multiplier payouts.

**Author:** Nnazirim Nwaogu

---

## Description

This is a fully-featured slot machine game written in Python. It simulates a 3×3 slot machine experience where players can place bets, spin for fruit combinations, and manage their balance. The game includes a multiplier system for varied payouts, deposit functionality, and comprehensive statistics tracking.

---

## Features

- **3×3 Slot Machine**: Three independent reels with fruit symbols (Apple, Orange, Banana)
- **Dynamic Betting System**: Wager any amount up to your current balance
- **Multiplier Payouts**: Random 2x-12x multipliers (on even indices) multiply your winnings
- **Balance Management**: Deposit, track current balance, and monitor profit/loss
- **Game Statistics**: View total spins, total wagered amount, and net profit/loss
- **Interactive Menu System**: Navigate through playing, depositing, and quitting
- **Win Feedback**: Instant notifications on wins, losses, and multipliers applied

---

## Installation

### Requirements

- Python 3.6 or higher

### Setup

1. Clone or download the repository
2. Navigate to the project directory in your terminal
3. Ensure `slot_machine_1.5.py` is in your working directory

---

## Usage

### Running the Game

```bash
python slot_machine_1.5.py
```

### Gameplay Flow

1. **Main Menu**: Choose to Play (1) or Leave (2)
2. **Play Menu**: Select Spin (1) or Leave (2)
3. **Deposit Prompt**: When balance is low or if you choose to deposit
4. **Betting**: Enter your wager amount (must be ≤ current balance)
5. **Spin**: Game automatically generates three fruit results and applies multipliers
6. **Results Summary**: View updated balance, profit/loss, and statistics when exiting

### Example Session

```
Oh!
 Hi there!
 Didn't see you there, trying to throw away your mone- *BANG*

 Ahem.. heh, don't mind that. My Name is Mr.Riggedd, and yes, I know it sounds funny.

 Anyhoo, were you looking to Play(1) or Leave Now(2) (while you still can!): 
1

Do you wish to: Spin(1) or Leave now(2)?: 
1
Balance: $0
Must Deposit

Balance: $0 --- How much are you depositing?: 
100

New Balance: $100
Do you want to deposit more(1) or not(2)?: 
2
Game Loading...,

Current Balance: $100 | P/L: $0
Enter 1 to Spin, 2 to Quit: 
1

Current Balance: $100 -- Enter your wager amount: 
25
You've spun a: Apple, Apple, and Apple!
Winnings: $75

Spinning multipliers...
You've spun a: 4x multiplier!

Overall Total: $300

New wallet balance is: $400

Current Balance: $400 | P/L: $300
Enter 1 to Spin, 2 to Quit: 
2
Leaving now...

---RESULTS---

Starting Balance: 100

Spun 1 times

Wagered through $25

Current Balance: 400

Profit/Loss: $300

Hope you had fun! Spread the luck next time!
```

---

## Game Rules

### Win Conditions

- **Winning Spin**: All three fruits must match (e.g., Apple, Apple, Apple)
- **Losing Spin**: Any mismatch (e.g., Apple, Orange, Banana) results in loss of wager

### Payouts

- **Base Winning Amount**: Bet amount × 3 (all three matching fruits × bet value)
  - Example: Bet $25 on three Apples = $75 base winnings
- **Multiplier Application**: Base winnings × random multiplier (2x, 4x, 6x, 8x, 10x, or 12x)
  - Example: $75 × 4x multiplier = $300 total payout
- **Loss**: Player loses their wager amount (deducted from balance)

### Balance Mechanics

- **Starting Balance**: Set upon first deposit
- **Current Balance**: Updates after each spin (win or loss)
- **Profit/Loss**: Running total of net gains or losses from starting balance
- **Deposits**: Can deposit additional funds at any time before spinning

---

## Controls

| Input | Action |
|-------|--------|
| 1 | Spin / Play |
| 2 | Quit / Leave |

At each prompt, enter the corresponding number and press Enter.

---

## Future Improvements

Potential features for future versions:

- **GUI Version**: Graphical user interface with animated reels
- **Difficulty Levels**: Adjustable house edge or multiplier ranges
- **Leaderboard**: Track high scores and best winning streaks
- **More Symbols**: Expand from 3 to 5+ unique fruit symbols
- **Themed Variations**: Different slot machine themes (Vegas, Retro, Fantasy, etc.)
- **Sound Effects**: Audio feedback for spins and wins
- **Save/Load**: Persistent player accounts and game progress
- **Multiple Lines**: Traditional multi-line slot machine mechanics


## Version History

**Current Version:** 1.5.2  
**Latest Stable:** 1.5.2 

For detailed technical changes and patch notes, see [CHANGELOG.md](CHANGELOG.md).

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

