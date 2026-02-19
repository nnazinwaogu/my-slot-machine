"""
Author: Nnazirim Nwaogu
Enhanced Slot Machine Version 2.0
- Refactored for clarity, modularity and maintainability
- Foundation for 3x3 multi-line support
- Improved data structures and organization
"""

import random

# Game State Structure
def create_game_state():
    """Initialize game state with all necessary variables"""
    return {
        'balance': 100,
        'starting_balance': 100,
        'spins': 0,
        'wagered': 0,
        'netpos': 0,
        'lines_bet': 1,  # Start with single line, expandable
        'grid': [[None]*3 for _ in range(3)]
    }

# Symbol Definitions
def create_symbols():
    """Define slot machine symbols with properties"""
    return {
        'Cherry': {'value': 2, 'weight': 35},
        'Lemon': {'value': 5, 'weight': 30},
        'Bell': {'value': 10, 'weight': 20},
        'Seven': {'value': 20, 'weight': 15},
        'Bar': {'value': 50, 'weight': 10},
        'Diamond': {'value': 100, 'weight': 2}
    }

# Payline Definitions
def create_paylines():
    """Define traditional slot machine paylines for 3x3 grid"""
    return {
        1: [(1,0), (1,1), (1,2)],  # Middle horizontal
        2: [(0,0), (0,1), (0,2)],  # Top horizontal
        3: [(2,0), (2,1), (2,2)],  # Bottom horizontal
        4: [(0,0), (1,1), (2,2)],  # Diagonal
        5: [(0,2), (1,1), (2,0)],  # Anti-diagonal
        6: [(0,0), (1,0), (2,0)],  # Left vertical
        7: [(0,1), (1,1), (2,1)],  # Middle vertical
        8: [(0,2), (1,2), (2,2)]   # Right vertical
    }

# Multiplier System
def create_multipliers():
    """Define multiplier values for winning spins"""
    return [1, 2, 1, 4, 1, 6, 1, 8, 1, 10, 1, 12]

# Helper Functions
def get_symbol_value(symbols, symbol_name):
    """Get the base value of a symbol"""
    return symbols.get(symbol_name, {}).get('value', 0)

def get_symbol_weight(symbols, symbol_name):
    """Get the weight of a symbol for random generation"""
    return symbols.get(symbol_name, {}).get('weight', 0)

# Grid Generation
def generate_grid(symbols):
    """Generate a 3x3 grid with weighted random symbols"""
    symbol_names = list(symbols.keys())
    weights = [symbols[name]['weight'] for name in symbol_names]
    
    # Generate 9 symbols for the 3x3 grid
    spin_result = random.choices(symbol_names, weights=weights, k=9)
    
    # Convert to 3x3 grid structure
    grid = [spin_result[i:i+3] for i in range(0, 9, 3)]
    return grid

# Win Checking (Single Line for now)
def check_winning_lines(grid, paylines, lines_bet=1):
    """Check which paylines have winning combinations"""
    wins = []
    
    # Only check the number of lines currently bet on
    for line_id in range(1, lines_bet + 1):
        if line_id not in paylines:
            continue
            
        positions = paylines[line_id]
        symbols_in_line = [grid[row][col] for row, col in positions]
        
        # Check if all symbols in the line match
        if len(set(symbols_in_line)) == 1:
            wins.append({
                'line_id': line_id,
                'symbol': symbols_in_line[0],
                'positions': positions,
                'payout': get_symbol_value(SYMBOLS, symbols_in_line[0]) * 3
            })
    
    return wins

# Multiplier Application
def apply_multiplier(winnings, multipliers):
    """Apply a random multiplier to the winnings"""
    multiplier = random.choice(multipliers)
    return winnings * multiplier, multiplier

# Balance Management
def update_balance(state, winnings, bet_amount):
    """Update game state balance based on winnings"""
    state['balance'] += winnings - bet_amount
    state['wagered'] += bet_amount
    state['netpos'] += winnings - bet_amount
    return state

# Display Functions
def display_grid(grid):
    """Display the 3x3 slot machine grid"""
    print("\n" + "="*25)
    print("SLOT MACHINE - 3x3 GRID")
    print("="*25)
    
    for row in grid:
        print("|", end="")
        for symbol in row:
            print(f" {symbol:^8} |", end="")
        print("\n" + "="*25)

def display_winnings(wins, multiplier, total_winnings):
    """Display winning information"""
    if wins:
        print(f"\nYou've won on {len(wins)} line(s)!")
        for win in wins:
            print(f"  Line {win['line_id']}: {win['symbol']} x 3 = ${win['payout']}")
        print(f"Multiplier: {multiplier}x")
        print(f"Total Winnings: ${total_winnings}")
    else:
        print("\nNo winning lines this spin!")

# Input Validation
def validate_bet_amount(bet_amount, balance):
    """Validate that bet amount is valid"""
    try:
        bet = int(bet_amount)
        if bet <= 0:
            return False, "Bet amount must be positive"
        if bet > balance:
            return False, f"Bet amount exceeds balance (${balance})"
        return True, bet
    except ValueError:
        return False, "Invalid bet amount - must be a number"

# Main Game Functions
def handle_spin(state, symbols, paylines, multipliers, bet_amount):
    """Process a single spin of the slot machine"""
    # Generate new grid
    grid = generate_grid(symbols)
    state['grid'] = grid
    
    # Check for winning lines (currently only checking lines_bet)
    wins = check_winning_lines(grid, paylines, state['lines_bet'])
    
    # Calculate total winnings from all winning lines
    total_payout = sum(win['payout'] for win in wins)
    
    # Apply multiplier
    total_winnings, multiplier = apply_multiplier(total_payout, multipliers)
    
    # Update balance and game state
    state = update_balance(state, total_winnings, bet_amount)
    state['spins'] += 1
    
    # Display results
    display_grid(grid)
    display_winnings(wins, multiplier, total_winnings)
    
    print(f"\nCurrent Balance: ${state['balance']}")
    print(f"Total Wagered: ${state['wagered']}")
    print(f"Net Position: ${state['netpos']}")
    
    return state

def handle_menu(state):
    """Display main menu and handle user choices"""
    while True:
        print(f"\n" + "="*25)
        print("MAIN MENU")
        print("="*25)
        print(f"Balance: ${state['balance']}")
        print(f"Spins: {state['spins']}")
        print(f"Lines Bet: {state['lines_bet']}")
        print("\nChoose an option:")
        print("1. Spin")
        print("2. Change Lines Bet")
        print("3. Deposit")
        print("4. Quit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            return 'spin'
        elif choice == "2":
            return 'change_lines'
        elif choice == "3":
            return 'deposit'
        elif choice == "4":
            return 'quit'
        else:
            print("Invalid choice! Please enter 1-4.")

def handle_change_lines(state, paylines):
    """Allow user to change the number of lines bet on"""
    max_lines = len(paylines)
    
    while True:
        print(f"\n" + "="*25)
        print("CHANGE LINES BET")
        print("="*25)
        print(f"Current Lines Bet: {state['lines_bet']}")
        print(f"Available Lines: 1 to {max_lines}")
        print("\nChoose number of lines to bet on:")
        
        try:
            lines_choice = int(input(f"Enter lines (1-{max_lines}): ").strip())
            if 1 <= lines_choice <= max_lines:
                state['lines_bet'] = lines_choice
                print(f"Lines bet changed to {lines_choice}")
                return state
            else:
                print(f"Please enter a number between 1 and {max_lines}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def handle_deposit(state):
    """Handle deposit functionality"""
    while True:
        print(f"\n" + "="*25)
        print("DEPOSIT")
        print("="*25)
        print(f"Current Balance: ${state['balance']}")
        
        try:
            deposit_amount = int(input("Enter deposit amount: $").strip())
            if deposit_amount <= 0:
                print("Deposit amount must be positive!")
                continue
                
            state['balance'] += deposit_amount
            if state['starting_balance'] == 0:
                state['starting_balance'] = state['balance']
                
            print(f"New Balance: ${state['balance']}")
            return state
            
        except ValueError:
            print("Invalid deposit amount! Please enter a number.")

def handle_quit(state):
    """Handle quitting the game and show results"""
    print(f"\n" + "="*25)
    print("GAME RESULTS")
    print("="*25)
    print(f"Starting Balance: ${state['starting_balance']}")
    print(f"Total Spins: {state['spins']}")
    print(f"Total Wagered: ${state['wagered']}")
    print(f"Final Balance: ${state['balance']}")
    print(f"Net Position: ${state['netpos']}")
    
    if state['netpos'] < state['starting_balance']:
        print("\nBetter luck next time!")
    else:
        print("\nCongratulations on your winnings!")
    
    print("Thanks for playing!")
    return None

#Global Constants intialization before main function
global SYMBOLS, PAYLINES, MULTIPLIERS
SYMBOLS = create_symbols()
PAYLINES = create_paylines()
MULTIPLIERS = create_multipliers()

def main():
    """Main game loop"""
    print("""Welcome to the Enhanced Slot Machine!
- 3x3 Grid Display
- Multi-Line Betting (up to 8 lines)
- Traditional Slot Symbols
- Improved Code Organization
""")
    
    # Initialize game state and constants
    state = create_game_state()

    
    # Main game loop
    while state:
        try:
            action = handle_menu(state)
            
            if action == 'spin':
                if state['balance'] <= 0:
                    print("\nYou need to deposit funds to continue!")
                    state = handle_deposit(state)
                    continue
                
                # Get bet amount
                while True:
                    try:
                        bet_amount = int(input(f"\nEnter bet amount (Balance: ${state['balance']}): $").strip())
                        valid, result = validate_bet_amount(bet_amount, state['balance'])
                        if valid:
                            state = handle_spin(state, SYMBOLS, PAYLINES, MULTIPLIERS, result)
                            break
                        else:
                            print(f"Error: {result}")
                    except ValueError:
                        print("Invalid bet amount! Please enter a number.")
                        
            elif action == 'change_lines':
                state = handle_change_lines(state, PAYLINES)
            elif action == 'deposit':
                state = handle_deposit(state)
            elif action == 'quit':
                state = handle_quit(state)
                
        except (EOFError, KeyboardInterrupt):
            print("\n\nThanks for playing!")
            state = handle_quit(state)
            break

if __name__ == "__main__":
    main()