from __future__ import annotations

from .incident_analysis import analyze_incident
from .output_formatter import format_incident_output


BANNER = "=== Incident Analysis Assistant (SPÅR C) ==="

SCOPE_NOTICE = (
    "Scope & guarantees:\n"
    "- This tool supports a human analyst with structured incident analysis.\n"
    "- It does NOT perform detection/monitoring, access live systems, or take response actions.\n"
    "- Output is deterministic based on the provided text input.\n"
)


def run() -> None:
    print(BANNER)
    print()
    print(SCOPE_NOTICE)

    while True:
        description = input("Describe the incident (or type 'q' to quit):\n> ").strip()
        if not description:
            print("\nPlease provide a short incident description.\n")
            continue

        if description.lower() in {"q", "quit", "exit"}:
            print("\nExiting. Stay safe.\n")
            return

        analysis = analyze_incident(description)

        # All output formatting is handled centrally
        format_incident_output(analysis)

        print("\n---\n")


if __name__ == "__main__":
    run()
