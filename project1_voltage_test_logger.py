#!/usr/bin/env python3
"""
Voltage Test Logger - Project 1

Automated tolerance checker for voltage measurements.
Validates measurements against specification limits (LSL, USL).
Logs results to CSV with timestamps and generates statistical summary.

This is a foundational project for hardware test automation.
Demonstrates core ATE workflow: measure → validate → log → report.

Author: Soorya Nath Manikantan
MSc Smart Electronic Systems, RTU Riga (2026)
"""

import csv
import datetime
import statistics
import numpy as np

# ============================================================================
# CONFIGURATION
# ============================================================================

# Specification limits (Volts)
VOLTAGE_LSL = 4.75  # Lower Specification Limit
VOLTAGE_USL = 5.25  # Upper Specification Limit

# Input and output files
OUTPUT_CSV = "voltage_test_results.csv"

# ============================================================================
# FUNCTIONS
# ============================================================================

def get_voltage_readings():
    """
    Get voltage measurements (simulated or from file).
    Returns: List of voltage values in Volts
    """
    readings = [5.01, 4.98, 5.26, 4.99, 4.72, 5.00, 5.99]
    return readings


def check_voltage_tolerance(voltage, lsl, usl):
    """
    Check if voltage is within specification limits.
    
    Args:
        voltage: Measured voltage (V)
        lsl: Lower specification limit (V)
        usl: Upper specification limit (V)
    
    Returns:
        "PASS" if within limits, "FAIL" otherwise
    """
    if lsl <= voltage <= usl:
        return "PASS"
    else:
        return "FAIL"


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main test workflow"""
    
    print("\n" + "="*70)
    print("VOLTAGE TEST LOGGER - AUTOMATED TOLERANCE CHECKER")
    print("="*70 + "\n")
    
    print(f"Configuration:")
    print(f"  Specification limits: {VOLTAGE_LSL}V - {VOLTAGE_USL}V")
    print(f"  Output file: {OUTPUT_CSV}\n")
    
    # Step 1: Get readings
    print("Step 1: Reading voltage measurements...")
    readings = get_voltage_readings()
    print(f"  Loaded {len(readings)} measurements\n")
    
    # Step 2: Check tolerance
    print("Step 2: Checking tolerance...")
    print(f"{'#':>3} | {'Voltage (V)':>12} | {'Result':<6}")
    print("-" * 35)
    
    results = []
    csv_rows = []
    
    for i, voltage in enumerate(readings, 1):
        # Check tolerance
        status = check_voltage_tolerance(voltage, VOLTAGE_LSL, VOLTAGE_USL)
        results.append(status)
        
        # Get timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create CSV row
        row = [i, timestamp, f"{voltage:.4f}", status]
        csv_rows.append(row)
        
        # Print result
        print(f"{i:>3} | {voltage:>12.4f} | {status:<6}")
    
    print()
    
    # Step 3: Calculate statistics
    print("Step 3: Calculating statistics...")
    passed_count = results.count("PASS")
    failed_count = results.count("FAIL")
    pass_rate = (passed_count / len(results)) * 100
    
    mean_voltage = np.mean(readings)
    std_dev = np.std(readings)
    min_voltage = min(readings)
    max_voltage = max(readings)
    
    print(f"  Total tests:     {len(results)}")
    print(f"  Passed:          {passed_count} ({pass_rate:.1f}%)")
    print(f"  Failed:          {failed_count} ({100-pass_rate:.1f}%)")
    print(f"  Mean:            {mean_voltage:.4f} V")
    print(f"  Std Dev:         {std_dev:.4f} V")
    print(f"  Min:             {min_voltage:.4f} V")
    print(f"  Max:             {max_voltage:.4f} V\n")
    
    # Step 4: Save to CSV
    print("Step 4: Saving results to CSV...")
    try:
        with open(OUTPUT_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(["Test #", "Timestamp", "Voltage (V)", "Result"])
            # Write data rows
            writer.writerows(csv_rows)
        print(f"  ✓ Saved to {OUTPUT_CSV}\n")
    except Exception as e:
        print(f"  ✗ Error saving file: {e}\n")
        return False
    
    # Summary
    print("="*70)
    print("✓ TEST COMPLETE")
    print("="*70 + "\n")
    
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
