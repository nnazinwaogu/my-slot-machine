# Running Tests for Slot Machine Game

## Quick Start

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run with coverage reporting
python -m pytest --cov=slot_machine --cov-report=html
```

## Test Structure

The test suite is organized into several categories:

- **Unit Tests**: Individual function testing
- **Integration Tests**: End-to-end game flow testing  
- **Performance Tests**: Speed and efficiency testing
- **Edge Case Tests**: Boundary condition testing

## Running Specific Tests

```bash
# Run specific test file
python -m pytest tests/test_slot_machine.py

# Run tests for a specific class
python -m pytest tests/test_slot_machine.py::TestSymbols

# Run a specific test method
python -m pytest tests/test_slot_machine.py::TestSymbols::test_create_symbols

# Run tests with specific markers
python -m pytest -m "unit"  # Run unit tests only
python -m pytest -m "integration"  # Run integration tests only
```

## Coverage Reporting

```bash
# Generate coverage report
python -m pytest --cov=slot_machine --cov-report=html

# View coverage report
start htmlcov/index.html  # Windows
open htmlcov/index.html    # macOS
xdg-open htmlcov/index.html  # Linux

# Check coverage percentage
python -m pytest --cov=slot_machine --cov-report=term
```

## Test Categories

### Unit Tests
- `TestGameState`: Game state initialization
- `TestSymbols`: Symbol definitions and validation  
- `TestPaylines`: Payline configurations
- `TestMultipliers`: Multiplier system testing
- `TestGridGeneration`: Grid creation and validation
- `TestWinChecking`: Win detection logic
- `TestBalanceManagement`: Balance calculation
- `TestBetValidation`: Bet amount validation

### Integration Tests
- `test_full_game_flow_win`: Complete win scenario
- `test_full_game_flow_loss`: Complete loss scenario

### Performance Tests
- `test_grid_generation_performance`: Grid generation speed
- `test_win_checking_performance`: Win checking efficiency

### Edge Case Tests
- `test_zero_balance`: Zero balance handling
- `test_maximum_bet`: Maximum bet validation
- `test_minimum_bet`: Minimum bet validation

## Test Dependencies

- Python 3.6+
- pytest package
- pytest-cov package (for coverage)

## Common Issues

### Permission Errors
If you get permission errors, try running as administrator or check file permissions.

### Module Not Found
Make sure the `src/main` directory is in your Python path:
```bash
export PYTHONPATH=$PYTHONPATH:src/main  # Linux/macOS

# Or add to conftest.py as shown in the test setup
```

### Coverage Not Working
Ensure pytest-cov is installed:
```bash
pip install pytest pytest-cov
```

## Development Workflow

1. **Write tests first** - Use test-driven development
2. **Run tests frequently** - Catch issues early
3. **Check coverage** - Aim for 90%+ coverage
4. **Fix failing tests** - Address integration test issues
5. **Run performance tests** - Ensure efficiency

## Example Test Output

```
============================= test session starts ==============================
platform win32 -- Python 3.14.0, pytest-7.4.3, pluggy-1.2.0
rootdir: C:\Users\nnazm\OneDrive\Documents\Coding\my-slot-machine\src\main
testpaths: tests
collected 28 items

 tests/test_slot_machine.py ..........        [ 42%]
 tests/test_slot_machine.py ..........        [ 85%]
 tests/test_slot_machine.py ..                    [100%]

============================== 28 passed in 2.34s ==============================
```

## Coverage Example

```
----------- coverage: platform win32, python 3.14.0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
slot_machine.py           187     15    92%
```