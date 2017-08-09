import subprocess
import conans

class ConanFileInst(conans.ConanFile):
    name = "windows-build-tools_installer_test"
    requires = "windows-build-tools_installer/0.1@demo/test_package"

    def build(self):
        pass

    def test(self):
        try:
            subprocess.check_output("make --version".split())
        except FileNotFoundError as e:
            self.output.error("%s package test failed" % self.name)
        else:
            self.output.success("%s package test passed" % self.name)
