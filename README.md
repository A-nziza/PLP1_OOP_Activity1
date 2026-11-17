# PLP1_OOP_Activity1: Airline Ticket Booking System

Group assignment for Introduction to Python Programming (ALU). An interactive command-line booking system built with Python OOP and inheritance.

## Overview

The program lets a user book an airline ticket in the terminal. It asks for a class (Economy, Business or First Class), collects only the details that class needs, then prints a formatted ticket.

## Class Structure

| Class | Extends | Extra attributes | Luggage allowance |
|---|---|---|---|
| `Passenger` | n/a | `name`, `location`, `destination`, `date` | 20 kg (default) |
| `Economy` | `Passenger` | `seat_preference` | 20 kg |
| `Business` | `Passenger` | `lounge_pass_code` | 100 kg (override) |
| `FirstClass` | `Passenger` | `suite_number`, `chauffeur_service` (True/False) | 100 kg (override) |

Child classes call `super().__init__()` and extend `get_passenger_info()`.

## Features

- Menu to select a class: [1] Economy, [2] Business, [3] First Class
- Dynamic prompts: only class-specific questions are asked
- Input validation: invalid menu choices and empty strings are rejected and re-prompted
- Formatted ticket summary at the end

## How to Run

Requires Python 3.8 or newer.

```bash
python PLP1_OOP_Activity1.py
```

## Example

```
=== Airline Ticket Booking System ===
Select class:
[1] Economy
[2] Business
[3] First Class
Enter choice (1-3): 3
Passenger name: Alice Mukamana
Current location: Kigali
Destination: London
Travel date (YYYY-MM-DD): 2026-12-10
Suite number: S12
Chauffeur service? (Y/N): y

=== TICKET SUMMARY ===
Class: First Class
Name: Alice Mukamana
From: Kigali
To: London
Date: 2026-12-10
Luggage Allowance: 100 kg
Suite Number: S12
Chauffeur Service: Yes
```

## Group Members

| Name | Contribution |
|---|---|
| Member 1 | |
| Member 2 | |
| Member 3 | |
