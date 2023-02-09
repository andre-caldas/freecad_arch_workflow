from setuptools import setup
import os
# from freecad.workbench_starterkit.version import __version__
# name: this is the name of the distribution.
# Packages using the same name here cannot be installed together

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "ArchWorkflow", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.ArchWorkflow',
      version=str(__version__),
      packages=['freecad',
                'freecad.ArchWorkflow'],
      maintainer="André Caldas",
      maintainer_email="andre.em.caldas@gmail.com",
      url="https://github.com/andre-caldas/freecad_arch_workflow",
      description="a flow of workbenches to project a house",
      install_requires=['numpy'], # should be satisfied by FreeCAD's system dependencies already
      include_package_data=True)
