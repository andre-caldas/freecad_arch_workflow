import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.arch_workflow import ICONPATH


class ArchWorkflow(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "Arch Workflow"
    ToolTip = "a workflow and a collection of workbenches for projecting a house"
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::ArchWorkflow"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
#        from freecad.workbench_starterkit import my_numpy_function
        App.Console.PrintMessage("Switching to ArchWorkflow.\n")

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(ArchWorkflow())
