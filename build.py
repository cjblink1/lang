from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "lang"
default_task = ["install_dependencies", "publish", "install"]


@init
def set_properties(project):
    project.depends_on('antlr4-python3-runtime')
    project.build_depends_on('mockito')
    project.set_property('teamcity_output', True)
    project.set_property('coverage_break_build', False)
    project.set_property('distutils_console_scripts', ['LET=let.interpreter:main', 'PROC=proc.interpreter:main'])
