#!/usr/bin/env python3

import os
import re


def set_output(name: str, val: str) -> None:
    if os.getenv("GITHUB_OUTPUT"):
            print(f"{name}={val}", file=env)
    else:


def main() -> None:
    ref = os.environ["GITHUB_REF"]
    m = re.match(r'^refs/(\w+)/(.*)$', ref)
    if m:
        category, stripped = m.groups()
        if category == "heads":
            set_output("branch", stripped)
        elif category == "pull":
            set_output("branch", "pull/" + stripped.split("/")[0])
            set_output("tag", stripped)


if __name__ == "__main__":
    main()
