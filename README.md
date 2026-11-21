# SECOM Sensor Selection with NSGA-II

Multi-objective sensor selection (maximize balanced accuracy, minimize number of
sensors) on the SECOM semiconductor dataset, using an NSGA-II implementation
written from scratch.

**Status:** work in progress

## Setup
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python src/download_data.py