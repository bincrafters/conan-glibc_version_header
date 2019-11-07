import os
from conans import ConanFile, tools


class GlibcVersionHeaderConan(ConanFile):
    name = "glibc_version_header"
    version = "0.1"
    description = "Build portable Linux binaries without using an ancient distro"
    url = "https://github.com/bincrafters/conan-glibc_version_header"
    homepage = "https://github.com/SSE4/glibc_version_header"
    license = "MIT"
    exports = ["LICENSE.md"]
    settings = {"os_build": ["Linux"], "arch_build": ["x86", "x86_64"]}
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
    _commit_id = "aef5c1637b4810056c45ac40a55b72e0c31a2ed1"

    @property
    def _header_name(self):
        return "force_link_glibc_%s.h" % self.options.glibc_version

    def source(self):
        tools.get("{}/archive/{}.zip".format(self.homepage, self._commit_id))
        os.rename("{}-{}".format(self.name, self._commit_id), self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.TXT", dst="licenses", src=self._source_subfolder)
        arch = "x86" if self.settings.arch_build == "x86" else "x64"
        self.copy(pattern=self._header_name, dst=os.path.join("version_headers", arch), src=os.path.join(self._source_subfolder, "version_headers", arch))

    def package_info(self):
        arch = "x86" if self.settings.arch_build == "x86" else "x64"
        header_path = os.path.join(self.package_folder, "version_headers", arch, self._header_name)
        self.cpp_info.cflags = ["-include %s" % header_path, "-static-libgcc"]
        self.cpp_info.cxxflags = ["-include %s" % header_path, "-static-libgcc", "-static-libstdc++"]
