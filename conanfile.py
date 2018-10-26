#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class GlibcVersionHeaderConan(ConanFile):
    name = "glibc_version_header"
    version = "0.1"
    description = "Build portable Linux binaries without using an ancient distro"
    url = "https://github.com/bincrafters/conan-glibc_version_header"
    homepage = "https://github.com/wheybags/glibc_version_header"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    settings = {"os_build": ["Linux"]}
    options = {"glibc_version": [
        "2.10.2",
        "2.11.3",
        "2.12.2",
        "2.13",
        "2.14",
        "2.14.1",
        "2.15",
        "2.16",
        "2.17",
        "2.18",
        "2.19",
        "2.20",
        "2.21",
        "2.22",
        "2.23",
        "2.24",
        "2.25",
        "2.26",
        "2.27",
        "2.5.1",
        "2.5",
        "2.6.1",
        "2.6",
        "2.7",
        "2.8",
        "2.9"
    ]}
    default_options = {"glibc_version": "2.12.2"}
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    _commit_id = "dd030738014620a1a0a0a49b58808914e79408ae"

    @property
    def _header_name(self):
        return "force_link_glibc_%s.h" % self.options.glibc_version

    def source(self):
        tools.get("{}/archive/{}.zip".format(self.homepage, self._commit_id))
        os.rename("{}-{}".format(self.name, self._commit_id), self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.TXT", dst="licenses", src=self._source_subfolder)
        self.copy(pattern=self._header_name, dst="version_headers", src=os.path.join(self._source_subfolder, "version_headers"))

    def package_info(self):
        header_path = os.path.join(self.package_folder, "version_headers", self._header_name)
        self.cpp_info.cflags = ["-include %s" % header_path, "-static-libgcc"]
        self.cpp_info.cppflags = ["-include %s" % header_path, "-static-libgcc", "-static-libstdc++"]
