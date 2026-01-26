# Changelog

All notable changes to the Slot Machine Game project are documented in this file.

## [1.5.2] - 2026-01-25

### Changes
- Documentation restructured into user-friendly README format
- Technical changelog moved to dedicated CHANGELOG.md file
- Enhanced project documentation with standard sections

## [1.5.1] - Initial Major Refactor

### Overview
Complete refactoring of the slot machine logic and function architecture for improved code clarity and maintainability.

### Changed

#### `lines()` Function
- Definition updated to account for new variables
- Changed fruit values to match bet amount (added significance to wagers)
- Restructured slot machine from 3 separate lists to a 2D list for cleaner data structure
- Integrated wagering logic before spinning (temporary solution; may be reverted in future refactor)
- Added multiplier array system for varied payout outcomes
- Rewrote result logic for better mathematical soundness and realism
- Fixed logic for non-winning spins

#### `spin()` Function → Split into Two Functions
- Partitioned original `spin()` into `play()` and `deposit()` for improved separation of concerns
- Renamed variables throughout codebase for better clarity and descriptiveness
- `play()` now handles user menu flow (spinning, depositing, leaving)
- `deposit()` handles variable assignment and balance updates

#### `leave()` Function
- Manages game results display and final statistics output
- Displays comprehensive session summary to player

#### `main()` Function
- Added essential game variables (tracking balance, spins, wagers, P/L)
- Improved print statements for better user experience
- Restructured flow logic for enhanced clarity

### Architecture Improvements
- Better function separation: betting logic decoupled from game mechanics
- Clearer variable naming throughout
- More organized control flow from menu to gameplay to results
- Improved code readability and maintainability

---

## Version Information

**Current Version:** 1.5.2  
**Latest Stable:** 1.5.1  
**Author:** Nnazirim Nwaogu

For usage information, see [README.md](README.md).
