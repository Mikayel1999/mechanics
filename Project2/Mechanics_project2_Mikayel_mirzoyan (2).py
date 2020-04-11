from random import randrange, random
from .Environment_Controller import Environment
from .Computation_Controller import ComputationEngine
from .ObjectModel import obj_real
from .Variable_Controller import VariableController
from Computation_Controllers.Simulation_Controller import Simulation
from Computation_Controllers.CSV_controller import CSVController


class Vars:

    g = 10

    def __init__(self):
        self.mass_range = (1, 10)
        self.friction_range = (0, 1)
        self.force_range = (-300, 300)

    def random_mass(self):
        mass = randrange(*self.mass_range)
        return mass

    def random_friction(self):
        friction = random()
        return friction

    def random_force(self):
        F = randrange(*self.force_range)
        return F



class Env:
    var_controller = VariableController()
    obj1, obj2, obj3, g, F = None, None, None, None, None

    def __init__(self):
        self.generate_objects()
        self.get_global_variables()
        self.prepare_objects()

    @staticmethod
    def generate_objects():
        Env.obj1 = obj_real()
        Env.obj2 = obj_real()
        Env.obj3 = obj_real()

    @staticmethod
    def get_global_variables():
        Env.g = VariableController.g
        Env.external_force = Env.var_controller.get_random_F()

    @staticmethod
    def prepare_objects():
        Env.obj1.w, Env.obj2.w, Env.obj3.w = Env.var_controller.get_random_mass(), Env.var_controller.get_random_mass(), Env.var_controller.get_random_mass()
        Env.obj1.fric, Env.obj2.fric, Env.obj3.fric = Env.var_controller.get_random_fric(), Env.var_controller.get_random_fric(), Env.var_controller.get_random_fric()




class Sim:
    Env = None
    Calculator = None

    def __init__(self):
        self.force_time = [[100, 0], [100, 5]]
        self.create_env()
        self.create_compute_calculator()

    @staticmethod
    def create_environment():
        Sim.Env = Env()

    @staticmethod
    def create_compute_engine():
        Sim.Calculator = ComputationCalculator(Sim.Env.obj1, Sim.Env.obj2, Sim.Env.obj3, Sim.Env.g,Sim.Env.F)

    @staticmethod
    def acc_computation():
        data = Sim.Engine.compute_acc()
        return data

class obj_real:

    def __init__(self):
        self.w = 0
        self.fric = 0
        self.pos = [0, 0]
        self.vel = 0

    def coordinate_x(self, x):
        self.pos[0] = self.pos[0] + x

    def coordinate_y(self, y):
        self.pos[0] = self.pos[0] + y




class ComputationCalculator:
    obj1 = obj2 = obj3 = None
    acc_2, acc_1 = 0, 0
    g = F = 0, 0

    def __init__(self, obj1, obj2, obj3, g, F):
        ComputationCalculator.obj1 = obj1
        ComputationCalculator.obj2 = obj2
        ComputationCalculator.obj3 = obj3
        ComputationCalculator.g = g
        ComputationCalculator.F = F

    @staticmethod
    def compute():
        obj1 = ComputationCalculator.obj1
        obj2 = ComputationCalculator.obj2
        obj3 = ComputationCalculator.obj3
        ComputationCalculator.acc_2 = ComputationCalculator.compute_acc_2(obj1.w, obj2.w, obj3.w, obj1.fric, obj2.fric, obj3.fric, ComputationCalculator.g, ComputationCalculator.F)
        ComputationCalculator.acc_1 = ComputationCalculator.compute_acc_1(ComputationCalculator.acc_2, obj1.w, obj2.w, obj1.fric, obj2.fric, ComputationCalculator.g)
        return [ComputationCalculator.acc_2, ComputationCalculator.acc_1]

    @staticmethod
    def compute_accelaration():
        obj1 = ComputationCalculator.obj1
        obj2 = ComputationCalculator.obj2
        obj3 = ComputationCalculator.obj3
        ComputationCalculator.acc_2 = ComputationCalculator.compute_acc_2(obj1.w, obj2.w,
                                                                                    obj3.w, obj1.fric,
                                                                                    obj2.fric, obj3.fric,
                                                                                    ComputationCalculator.g,
                                                                                    ComputationCalculator.F)
        ComputationCalculator.acc_1 = ComputationCalculator.compute_acc_1(ComputationCalculator.acc_2,
                                                                                    obj1.w, obj2.w,
                                                                                    obj1.fric, obj2.fric,
                                                                                    ComputationCalculator.g)
        return [obj1.w, obj2.w, obj3.w, obj1.fric, obj2.fric, obj3.fric, ComputationCalculator.g,
                ComputationCalculator.F, ComputationCalculator.acc_2, ComputationCalculator.acc_1]


@staticmethod
    def compute_acc_1(a2, m1, m2, f1, f2, g):
        acc = (-1*m2*a2 + f2*m2*g - f1*m1*g + f1*m2*a2 + f1*f2*m2*g)/(m1+m2)
        return acc
    @staticmethod
    def compute_acc_2(m1, m2, m3, f1, f2, f3, g, F):
        acc = (-1*(m1+m3)*(f2*m2*g - m3*g + 2*f3*F) + m3*(f2*m2*g - f1*m1*g + f1*f2*m2*g))/(m2*(m1+m3) - m3*(-1*m2 + f1*m2 - m1 - m3))
        return acc



class run:
    simulation = None
    csv_controller = None

    def __init__(self):
        run.simulation = Simulation()

    @staticmethod
    def test_acc():
        result = run.simulation.acc_simulate()
        print(result)

if __name__ == "__main__":
    main_controller = run()
    main_controller.test_acc()
    main_controller.acc_data(10000)
