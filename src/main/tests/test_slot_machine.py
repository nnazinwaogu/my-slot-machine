import pytest
from slot_machine import (
    create_game_state,
    create_symbols,
    create_paylines,
    create_multipliers,
    get_symbol_value,
    get_symbol_weight,
    generate_grid,
    check_winning_lines,
    apply_multiplier,
    update_balance,
    validate_bet_amount,
    handle_spin,
    handle_menu,
    handle_change_lines,
    handle_deposit,
    handle_quit,
    main
)

# Test constants
TEST_SYMBOLS = create_symbols()
TEST_PAYLINES = create_paylines()
TEST_MULTIPLIERS = create_multipliers()

class TestGameState:
    def test_create_game_state(self):
        state = create_game_state()
        assert isinstance(state, dict)
        assert state['balance'] == 100
        assert state['starting_balance'] == 100
        assert state['spins'] == 0
        assert state['wagered'] == 0
        assert state['netpos'] == 0
        assert state['lines_bet'] == 1
        assert len(state['grid']) == 3
        assert all(len(row) == 3 for row in state['grid'])

class TestSymbols:
    def test_create_symbols(self):
        symbols = create_symbols()
        assert len(symbols) == 6
        assert 'Cherry' in symbols
        assert 'Diamond' in symbols
        
        cherry = symbols['Cherry']
        assert cherry['value'] == 2
        assert cherry['weight'] == 35
        
        diamond = symbols['Diamond']
        assert diamond['value'] == 100
        assert diamond['weight'] == 2
    
    def test_get_symbol_value(self):
        assert get_symbol_value(TEST_SYMBOLS, 'Cherry') == 2
        assert get_symbol_value(TEST_SYMBOLS, 'Diamond') == 100
        assert get_symbol_value(TEST_SYMBOLS, 'Invalid') == 0
    
    def test_get_symbol_weight(self):
        assert get_symbol_weight(TEST_SYMBOLS, 'Cherry') == 35
        assert get_symbol_weight(TEST_SYMBOLS, 'Diamond') == 2
        assert get_symbol_weight(TEST_SYMBOLS, 'Invalid') == 0

class TestPaylines:
    def test_create_paylines(self):
        paylines = create_paylines()
        assert len(paylines) == 8
        
        # Test middle horizontal line
        middle_line = paylines[1]
        assert middle_line == [(1,0), (1,1), (1,2)]
        
        # Test diagonal line
        diagonal_line = paylines[4]
        assert diagonal_line == [(0,0), (1,1), (2,2)]

class TestMultipliers:
    def test_create_multipliers(self):
        multipliers = create_multipliers()
        assert len(multipliers) == 12
        assert multipliers[0] == 1  # No multiplier
        assert multipliers[1] == 2  # 2x multiplier
        assert multipliers[5] == 6  # 6x multiplier
        assert multipliers[11] == 12  # 12x multiplier
    
    def test_apply_multiplier(self):
        winnings = 100
        total, multiplier = apply_multiplier(winnings, TEST_MULTIPLIERS)
        assert multiplier in TEST_MULTIPLIERS
        assert total == winnings * multiplier  # Total should be equal to winnings x multiplier
        
class TestGridGeneration:
    def test_generate_grid_structure(self):
        grid = generate_grid(TEST_SYMBOLS)
        assert len(grid) == 3
        assert all(len(row) == 3 for row in grid)
        assert all(isinstance(cell, str) for row in grid for cell in row)
    
    def test_generate_grid_valid_symbols(self):
        grid = generate_grid(TEST_SYMBOLS)
        all_symbols = list(TEST_SYMBOLS.keys())
        assert all(cell in all_symbols for row in grid for cell in row)
    
    def test_generate_grid_consistency(self):
        # Test that grid generation is consistent with symbol definitions
        grid = generate_grid(TEST_SYMBOLS)
        symbol_counts = {}
        for row in grid:
            for symbol in row:
                symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
        
        # Check that high-value symbols appear less frequently
        diamond_count = symbol_counts.get('Diamond', 0)
        cherry_count = symbol_counts.get('Cherry', 0)
        assert diamond_count <= cherry_count

class TestWinChecking:
    def test_check_winning_lines_no_wins(self):
        # Create grid with no winning combinations
        grid = [
            ['Cherry', 'Lemon', 'Bell'],
            ['Seven', 'Bar', 'Diamond'],
            ['Cherry', 'Lemon', 'Bell']
        ]
        wins = check_winning_lines(grid, TEST_PAYLINES, 1)
        assert len(wins) == 0
    
    def test_check_winning_lines_single_line_win(self):
        # Create grid with win on middle horizontal line
        grid = [
            ['Cherry', 'Lemon', 'Bell'],
            ['Cherry', 'Cherry', 'Cherry'],  # Winning line
            ['Seven', 'Bar', 'Diamond']
        ]
        wins = check_winning_lines(grid, TEST_PAYLINES, 1)
        assert len(wins) == 1
        win = wins[0]
        assert win['line_id'] == 1
        assert win['symbol'] == 'Cherry'
        assert win['payout'] == 6  # 2 * 3
    
    def test_check_winning_lines_multiple_lines_win(self):
        # Create grid with wins on multiple lines
        grid = [
            ['Cherry', 'Cherry', 'Cherry'],  # Top horizontal win
            ['Cherry', 'Cherry', 'Cherry'],  # Middle horizontal win
            ['Cherry', 'Cherry', 'Cherry']   # Bottom horizontal win
        ]
        wins = check_winning_lines(grid, TEST_PAYLINES, 3)
        assert len(wins) == 3
        
        line_ids = [win['line_id'] for win in wins]
        assert 1 in line_ids  # Middle horizontal
        assert 2 in line_ids  # Top horizontal
        assert 3 in line_ids  # Bottom horizontal
    
    def test_check_winning_lines_diagonal_win(self):
        # Create grid with diagonal win
        grid = [
            ['Cherry', 'Lemon', 'Bell'],
            ['Seven', 'Cherry', 'Diamond'],
            ['Bar', 'Diamond', 'Cherry']
        ]
        wins = check_winning_lines(grid, TEST_PAYLINES, 4)
        assert len(wins) == 1
        win = wins[0]
        assert win['line_id'] == 4  # Diagonal line
        assert win['symbol'] == 'Cherry'

class TestBalanceManagement:
    def test_update_balance_win(self):
        state = create_game_state()
        initial_balance = state['balance']
        
        # Simulate a win
        state = update_balance(state, 300, 100)  # Win $300, bet $100
        
        assert state['balance'] == initial_balance + 200  # 300 - 100
        assert state['wagered'] == 100
        assert state['netpos'] == 200
    
    def test_update_balance_loss(self):
        state = create_game_state()
        initial_balance = state['balance']
        
        # Simulate a loss
        state = update_balance(state, 0, 50)  # Lose $50
        
        assert state['balance'] == initial_balance - 50
        assert state['wagered'] == 50
        assert state['netpos'] == -50

class TestBetValidation:
    def test_validate_bet_amount_valid(self):
        balance = 100
        valid, result = validate_bet_amount(50, balance)
        assert valid is True
        assert result == 50
    
    def test_validate_bet_amount_zero(self):
        balance = 100
        valid, result = validate_bet_amount(0, balance)
        assert valid is False
        assert "must be positive" in str(result)
    
    def test_validate_bet_amount_negative(self):
        balance = 100
        valid, result = validate_bet_amount(-10, balance)
        assert valid is False
        assert "must be positive" in str(result)
    
    def test_validate_bet_amount_exceeds_balance(self):
        balance = 100
        valid, result = validate_bet_amount(150, balance)
        assert valid is False
        assert "exceeds balance" in str(result)
    
    def test_validate_bet_amount_non_integer(self):
        balance = 100
        valid, result = validate_bet_amount("abc", balance)
        assert valid is False
        assert "must be a number" in str(result)

# Integration Tests
class TestGameIntegration:
    def test_full_game_flow_win(self, monkeypatch):
        # Mock user inputs for a winning game flow
        inputs = iter(['2', '8', '1', '50', '4'])  # Go to change lines, set to 8 lines, play, bet $50, quit
        
        def mock_input(prompt):
            return next(inputs)
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        # Mock random for predictable win
        random_choices = iter([['Cherry', 'Cherry', 'Cherry'] * 3])
        random_multipliers = iter([4])  # 4x multiplier
        
        def mock_random_choices(population, weights, k):
            return next(random_choices)
        
        def mock_random_choice(population):
            return next(random_multipliers)
        
        monkeypatch.setattr('random.choices', mock_random_choices)
        monkeypatch.setattr('random.choice', mock_random_choice)
        
        # Run main with mocked inputs
        main()
        # If we get here without errors, the flow worked
        assert True
    
    def test_full_game_flow_loss(self, monkeypatch):
        # Mock user inputs for a losing game flow
        inputs = iter(['2', '8', '1', '50', '4'])  # Go to change lines, set to 8 lines, play, bet $50, quit
        
        def mock_input(prompt):
            return next(inputs)
        
        monkeypatch.setattr('builtins.input', mock_input)
        
        # Mock random for predictable loss
        random_choices = iter([['Cherry', 'Lemon', 'Bell'] * 3])  # No win
        random_multipliers = iter([1])  # 1x multiplier (no effect)
        
        def mock_random_choices(population, weights, k):
            return next(random_choices)
        
        def mock_random_choice(population):
            return next(random_multipliers)
        
        monkeypatch.setattr('random.choices', mock_random_choices)
        monkeypatch.setattr('random.choice', mock_random_choice)
        
        # Run main with mocked inputs
        main()
        # If we get here without errors, the flow worked
        assert True

# Performance Tests
class TestPerformance:
    def test_grid_generation_performance(self):
        import time
        
        start_time = time.time()
        for _ in range(1000):
            grid = generate_grid(TEST_SYMBOLS)
        end_time = time.time()
        
        duration = end_time - start_time
        assert duration < 1.0  # Should generate 1000 grids in under 1 second
    
    def test_win_checking_performance(self):
        import time
        
        # Create a grid with a win on every line
        grid = [
            ['Cherry', 'Cherry', 'Cherry'],
            ['Cherry', 'Cherry', 'Cherry'],
            ['Cherry', 'Cherry', 'Cherry']
        ]
        
        start_time = time.time()
        for _ in range(1000):
            wins = check_winning_lines(grid, TEST_PAYLINES, 8)
        end_time = time.time()
        
        duration = end_time - start_time
        assert duration < 0.5  # Should check 1000 wins in under 0.5 seconds

# Edge Case Tests
class TestEdgeCases:
    #zero balance edge case is already manually tested in the main function of slot_machine.py
    
    def test_maximum_bet(self):
        state = create_game_state()
        balance = state['balance']
        
        valid, result = validate_bet_amount(balance, balance)
        assert valid is True
        assert result == balance
    
    def test_minimum_bet(self):
        state = create_game_state()
        
        valid, result = validate_bet_amount(1, state['balance'])
        assert valid is True
        assert result == 1

# Utility Functions
def create_test_grid(symbols, pattern):
    """Create a test grid with a specific pattern"""
    grid = []
    for row_pattern in pattern:
        row = [symbols[symbol] for symbol in row_pattern]
        grid.append(row)
    return grid

if __name__ == "__main__":
    pytest.main([__file__])