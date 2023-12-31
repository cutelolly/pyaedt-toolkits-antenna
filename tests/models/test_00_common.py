from conftest import BasisTest

from ansys.aedt.toolkits.antenna.backend.models.common import StandardWaveguide
from ansys.aedt.toolkits.antenna.backend.models.common import TransmissionLine

test_project_name = "Patch_test"


class TestClass(BasisTest, object):
    def setup_class(self):
        BasisTest.my_setup(self)
        self.tl_calc = TransmissionLine()
        self.wg_standard = StandardWaveguide()

    def teardown_class(self):
        BasisTest.my_teardown(self)

    def test_01_microstrip_calculator(self):
        w1 = self.tl_calc.microstrip_calculator(substrate_height=0.15, permittivity=4.4)
        assert w1[0] - 30.8173 < 1e-6
        assert w1[1] - 0.00913 < 1e-6
        w2 = self.tl_calc.microstrip_calculator(substrate_height=0.15, permittivity=2)
        assert w2[0] - 0.490717 < 1e-6
        assert w2[1] - 0.0094996 < 1e-6

    def test_02_stripline_calculator(self):
        w1 = self.tl_calc.stripline_calculator(substrate_height=10, permittivity=2.2)
        assert w1 - 8.298368 < 1e-6
        w2 = self.tl_calc.stripline_calculator(substrate_height=0.15, permittivity=4.4, impedance=100)
        assert w2 - 0.012117786 < 1e-6

    def test_03_find_waveguide(self):
        w_dim = self.wg_standard.get_waveguide_dimensions("WR-2300", "cm")
        assert w_dim[0] - 58.41999999 < 1e-6
        w_name = self.wg_standard.find_waveguide(10, "GHz")
        assert w_name == "WR-102"
