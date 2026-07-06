# Voltage Test Logger

Automated tolerance checker for voltage measurements with CSV logging and statistical reporting.

## Overview

Loads voltage measurements, checks against specification limits (LSL/USL), logs results with timestamps, and generates statistical summary.

This is a foundational project for hardware test automation. It demonstrates the core ATE (Automated Test Equipment) workflow: **measure → validate → log → report**.

## Features

✓ Configurable pass/fail limits (LSL, USL)  
✓ Real-time tolerance checking  
✓ Timestamped CSV logging  
✓ Statistical summary: mean, std dev, min, max, pass rate  
✓ Professional console output  
✓ Error handling  

## Installation

```bash
# Clone repository
git clone https://github.com/soooryanath/voltage-test-logger.git
cd voltage-test-logger

# Install requirements
pip install numpy

# Run script
python project1_voltage_test_logger.py
```

## Usage

### Default behavior (simulated data)

```bash
python project1_voltage_test_logger.py
```

Outputs:
- Console: Pass/fail results, statistics
- CSV: `voltage_test_results.csv` (timestamped data)

### Configure specification limits

Edit script, change:
```python
VOLTAGE_LSL = 4.75  # Lower limit
VOLTAGE_USL = 5.25  # Upper limit
```

## Example Output

**Console:**
```
======================================================================
VOLTAGE TEST LOGGER - AUTOMATED TOLERANCE CHECKER
======================================================================

Configuration:
  Specification limits: 4.75V - 5.25V
  Output file: voltage_test_results.csv

Step 1: Reading voltage measurements...
  Loaded 7 measurements

Step 2: Checking tolerance...
  # | Voltage (V) | Result
-------------------------------------
  1 |      5.0100 | PASS
  2 |      4.9800 | PASS
  3 |      5.2600 | FAIL
  4 |      4.9900 | PASS
  5 |      4.7200 | FAIL
  6 |      5.0000 | PASS
  7 |      5.9900 | FAIL

Step 3: Calculating statistics...
  Total tests:     7
  Passed:          4 (57.1%)
  Failed:          3 (42.9%)
  Mean:            5.1286 V
  Std Dev:         0.4866 V
  Min:             4.7200 V
  Max:             5.9900 V

Step 4: Saving results to CSV...
  ✓ Saved to voltage_test_results.csv

======================================================================
✓ TEST COMPLETE
======================================================================
```

**CSV Output (voltage_test_results.csv):**
```
Test #,Timestamp,Voltage (V),Result
1,2026-07-01 10:15:23,5.0100,PASS
2,2026-07-01 10:15:23,4.9800,PASS
3,2026-07-01 10:15:24,5.2600,FAIL
4,2026-07-01 10:15:24,4.9900,PASS
5,2026-07-01 10:15:25,4.7200,FAIL
6,2026-07-01 10:15:25,5.0000,PASS
7,2026-07-01 10:15:26,5.9900,FAIL
```

## Key Concepts Demonstrated

- **Tolerance checking:** Compare measured values to spec limits
- **Pass/fail logic:** Real-time decision making
- **CSV logging:** Structured data persistence with timestamps
- **Statistical analysis:** Mean, std dev, min, max, pass rate
- **Professional output:** Console summary + data export

## Technologies

- Python 3
- numpy (statistical calculations)
- csv (data export)
- datetime (timestamping)

## Author

Soorya Nath Manikantan  
MSc Smart Electronic Systems, RTU Riga (2026)  
GitHub: https://github.com/soooryanath

## Portfolio Context

**Part 1 of 3-project hardware test automation portfolio:**
1. Voltage Test Logger (tolerance checking) ← You are here
2. Multi-Sensor DAQ (networked instruments)
3. Measurement Analysis Tool (statistical reporting + Cpk)
