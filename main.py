# main.py
from modules.prefetch_parser import parse_prefetch
from modules.registry_parser import parse_registry
from modules.evtx_parser import parse_evtx
from modules.timeline_builder import build_timeline

import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Incident Timeline Generator")
    parser.add_argument('--prefetch', help='Path to Prefetch folder')
    parser.add_argument('--registry', help='Path to Registry hives (SOFTWARE, NTUSER.DAT, etc.)')
    parser.add_argument('--evtx', help='Path to EVTX logs')
    parser.add_argument('--output', default='reports/timeline.csv', help='Output timeline file')
    args = parser.parse_args()

    timeline = []

    if args.prefetch:
        timeline.extend(parse_prefetch(args.prefetch))

    if args.registry:
        timeline.extend(parse_registry(args.registry))

    if args.evtx:
        timeline.extend(parse_evtx(args.evtx))

    build_timeline(timeline, args.output)
    print(f"[+] Timeline generated at {args.output}")


if __name__ == '__main__':
    main()
