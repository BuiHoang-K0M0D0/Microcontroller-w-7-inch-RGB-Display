# High-Performance Embedded Processing & 7-Inch RGB Display Board

A 4-layer custom PCB integrating an **STM32F407VET6** MCU (ARM Cortex-M4) and an **Allwinner F1C100s** MPU (ARM926EJ-S with integrated 32MB DDR) to deliver a dual-core heterogeneous computing and rich multimedia display solution.

---

## 📌 System Architecture & Overview

The board separates high-level graphical interface tasks from real-time physical control:
- **Application & Multimedia Core (Allwinner F1C100s):** Runs U-Boot / Embedded Linux, directly drives a 7-inch 800x480 RGB LCD panel, and handles high-speed storage (SDIO/TF Card) and USB connectivity.
- **Real-Time Control Core (STM32F407VET6):** Handles real-time I/O, precise timing tasks, sensor acquisition, and peripheral communication.
- **Inter-Core Communication:** UART link allowing deterministic bidirectional data flow between the MCU and MPU.

---

## 🛠 Key Hardware Specifications

| Parameter | Specification | Details |
| :--- | :--- | :--- |
| **Main Processing Unit** | Allwinner F1C100s | ARM926EJ-S @ 408 MHz, 32MB SIP DDR1 |
| **Real-Time Microcontroller** | STM32F407VET6 | ARM Cortex-M4 @ 168 MHz, 512KB Flash, 192KB SRAM |
| **Display Interface** | 24-bit Parallel RGB | Direct FPC interface for 7-inch TFT LCD (800×480) with backlight driver |
| **PCB Form Factor** | 4-Layer Stackup | Signal - GND - Power - Signal with 50Ω single-ended & differential impedance control |
| **Power Distribution** | Multi-rail Power Tree | 8 distinct voltage rails derived from a single 5V/12V input using discrete Buck regulators and low-noise LDOs |
| **Peripheral Interfaces** | High-Speed & Industrial | MicroSD (SDIO), USB 2.0 OTG, SWD/JTAG debug headers, UART/CAN expansion pins |

---

## ⚡ Power Tree & PCB Layout Highlights

- **Power Integrity (PI):** Designed a robust power network supplying critical rails (+5V, +3.3V, +2.5V, +1.8V, +1.2V, VCC-DRAM, VDD-Core, and LCD Backlight boost voltage). Decoupling capacitors are placed immediately adjacent to BGA/QFP power pins to minimize parasitic inductance.
- **Signal Integrity (SI):** Controlled trace impedance and strictly adhered to PCB Design Rule Checks (DRC) for length matching on RGB parallel data buses, SDIO clock/data, and USB differential pairs (90Ω).
- **Thermal & EMI Management:** Dedicated continuous internal ground plane to provide uninterrupted return paths, shield high-frequency noise, and assist thermal dissipation from the F1C100s SoC.

---

## 📁 Repository Structure

```text
├── Hardware/
│   ├── Schematics/         # PDF and Altium Designer schematic sheets
│   ├── Layout/             # PCB layout files (4-layer stackup)
│   ├── Manufacturing/      # Production Gerber files, NC Drill, and BOM
│   └── 3D_Model/           # STEP export for mechanical enclosure modeling
├── Docs/                   # Architectural diagrams, power tree maps, and test data
└── README.md
