#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_header_only
import os

if __name__ == "__main__":

    arch = os.environ["ARCH"]
    builder = build_template_header_only.get_builder()
    for version in ["2.10.2", "2.11.3", "2.12.2", "2.13", "2.14", "2.14.1", "2.15",
                    "2.16", "2.17", "2.18", "2.19", "2.20", "2.21", "2.22", "2.23", "2.24",
                    "2.25", "2.26", "2.27", "2.5.1", "2.5", "2.6.1", "2.6", "2.7", "2.8", "2.9"]:
        builder.add(options={"glibc_version_header:glibc_version": version},
                    settings={"os_build" : build_shared.get_os(), "arch_build" : arch})
    builder.run()
