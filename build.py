#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
from builder import Builder, CMakeAndroidBuilder, CMakeWindowsVsMsvcBuilder


def get_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build and install the project")
    parser.add_argument("--platform", help="Build the project",
                        default="Android", choices=["Windows", "Android", "Linux"])
    parser.add_argument("--clean", action="store_true",
                        help="Clean the build directory")
    args = parser.parse_args()
    return args


def get_builder(args) -> Builder:
    if args.platform == "Android":
        return CMakeAndroidBuilder("build", "output")
    else:
        return CMakeWindowsVsMsvcBuilder("build", "output")


if __name__ == "__main__":
    args = get_args()
    builder = get_builder(args)
    if args.clean:
        builder.clean()
        exit(0)
    builder.build()
    # builder.install()