import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from GoodwingTimetabler.csp import *
from GoodwingTimetabler.util import ExcelScheduleManager
from GoodwingTimetabler.myTests import test_csp_solver_performance

def run_app():
    generateScheduleUsingCSP()

    # To let console stay open upon app end of execution (important if we run the .exe !)
    input("\nPress Enter to exit...")


def run_test():
    test_csp_solver_performance()


def generateScheduleUsingCSP():
    print("app running...\n\n\n")
    print("=========== Goodwing Timetabler v0.2.2 ===========\n\n")

    # Get the absolute path of the project root (parent directory of GoodwingTimetabler)
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    # Construct the correct path to the Inputs folder
    input_path = os.path.join(base_dir, "Inputs/")

    # Create the university
    my_univ = generateUniv2(input_path)
    print("Univ generated successfully : ", my_univ)
    print("Generating the CSP...")
    # Instantiate and solve the CSP
    scheduler = CSP(my_univ)

    # Output the generated schedules
    outputSchedulesFromCSP(scheduler)


def outputSchedulesFromCSP(csp_solver: CSP):
    # Excel output
    excel_manager = ExcelScheduleManager(csp_solver.university, csp_solver.generated_courses)
    excel_manager.generate_excel_schedule('./Outputs/excel/schedule.xlsx')