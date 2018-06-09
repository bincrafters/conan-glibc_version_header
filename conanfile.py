#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class GlibcVersionHeaderConan(ConanFile):
    name = "glibc_version_header"
    version = "0.1"
    description = "Build portable Linux binaries without using an ancient distro"
    url = "https://github.com/bincrafters/conan-glibc_version_header"
    homepage = "https://github.com/wheybags/glibc_version_header"
    license = "MIT"
    exports = ["LICENSE.md"]
    options = {'glibc_version': [
        '2.10.2',
        '2.11.3',
        '2.12.2',
        '2.13',
        '2.13.1',
        '2.14',
        '2.15',
        '2.16',
        '2.17',
        '2.18',
        '2.19',
        '2.20',
        '2.21',
        '2.22',
        '2.23',
        '2.24',
        '2.25',
        '2.26',
        '2.27',
        '2.5.1',
        '2.5',
        '2.6.1',
        '2.6',
        '2.7',
        '2.8',
        '2.9'
    ]}
    default_options = 'glibc_version=2.12.2'
    source_subfolder = "source_subfolder"
    no_copy_source = True
    exports_sources = 'version_headers/*'

    def source(self):
        source_url = "https://github.com/wheybags/glibc_version_header.git"
        self.run('git clone --depth 1 %s' % source_url)

        os.rename('glibc_version_header', self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.h", dst="version_headers", src=os.path.join(self.source_subfolder, 'version_headers'))

    def package_info(self):
        header_name = 'force_link_glibc_%s.h' % self.options.glibc_version
        header_path = os.path.join(self.package_folder, 'version_headers', header_name)
        self.cpp_info.cflags = ['-include %s' % header_path, '-static-libgcc']
        self.cpp_info.cppflags = ['-include %s' % header_path, '-static-libgcc', '-static-libstdc++']

    def package_id(self):
        self.info.header_only()
