import os
import conans
import subprocess


class ConanFileInst(conans.ConanFile):
    name = "windows-build-tools_installer"
    description = "creates windows-build-tools binaries package"
    version = "0.2"
    license = "MIT"
    url = "https://https://github.com/omicronns/conan-windows-build-tools-installer.git"
    settings = {"os": ["Windows"], "arch": ["x86", "x86_64"]}

    options = {
    "no_sh": [True, False],
    "version": [
        "2.8-201611221915",
        "2.7-201610281058",
        "2.6-201507152002",
    ]}
    default_options = "version=2.8-201611221915", "no_sh=False"
    build_policy = "missing"
    exports = "7z.exe", "*.dll"

    def build(self):
        arch_id = {
            "x86": "win32",
            "x86_64": "win64",
        }.get(str(self.settings.arch))
        url = "https://github.com/gnu-mcu-eclipse/windows-build-tools/releases/download/v%s/gnuarmeclipse-build-tools-%s-%s-setup.exe" % (str(self.options.version)[:3], arch_id, str(self.options.version))
        dest_file = "file.exe"
        self.output.info("Downloading: %s" % url)
        conans.tools.download(url, dest_file, verify=False)
        subprocess.check_call("7z.exe x file.exe -oout".split())

    def package(self):
        if self.options.no_sh:
            self.copy("bin/*", dst="", src="out", excludes="*sh.exe")
        else:
            self.copy("bin/*", dst="", src="out")

    def package_info(self):
        if not self.package_folder is None:
            self.env_info.path.append(os.path.join(self.package_folder, "bin"))

