# Low Power Cache Design using Way Prediction

## Overview
This project implements a **trace-driven cache simulator** to study **low-power cache design techniques**, specifically **way prediction**.

The goal is to reduce energy consumption in set-associative caches while maintaining performance.

We compare:
- Baseline cache (all ways accessed)
- Low-power cache (way prediction)

---

## Key Idea

In a traditional set-associative cache:
- All cache ways are accessed in parallel
- This increases dynamic power consumption

In this project:
- We predict which way contains the data
- Access only one way initially
- If correct → lower energy
- If incorrect → penalty (extra access)

---

## How to run
python main.py
