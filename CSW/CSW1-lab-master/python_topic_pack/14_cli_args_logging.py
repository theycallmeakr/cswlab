"""
Topic 14 — CLI args & logging
argparse basics, logging levels.
Run: python 14_cli_args_logging.py --name Boss --times 2
"""

import argparse, logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="world")
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args()

for _ in range(args.times):
    logging.info("Hello, %s!", args.name)
