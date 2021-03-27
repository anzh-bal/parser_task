import pytest
from lib import schedule_parser
import numpy as np
class TestUnitParser:
    @pytest.fixture
    def set_up(self):
        """
        Prepares info for reference input file(s)
        @return: None
        """
       # self.keywords = ("DATES", "COMPDAT", "COMPDATL")
       # self.parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
       #           "Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
       #           "Skin factor", "D-factor", "Dir_well_penetrates_grid_block", "Press_eq_radius")


        self.input_file_reference = "test_schedule_input_reference.inc"
        self.output_csv_reference = "schedule_output_reference.csv"

        self.clean_file = "handled_schedule.inc"
        self.output_csv = "output.csv"

        with open(self.clean_file, "r", encoding="utf-8") as file:
            self.clean_file_text = file.read()

        self.parse_list_output_reference = [
        [np.nan], ['',np.nan], ['W1', np.nan, '10', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0'],
        ['W2', np.nan, '32', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '2.0',''],
        ['',np.nan], ['W3', np.nan, '5', '36', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '3.0'],
        ['W4', np.nan, '40', '30', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '4.0',''],
        ['',np.nan], ['W5', np.nan, '21', '21', '4', '4', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '5.0',''],
        ['01 JUN 2018 '],
        ['01 JUL 2018 '], ['',np.nan], ['W3', np.nan, '32', '10', '1', '1', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0718'],
        ['W5', np.nan, '21', '21', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '5.0',''],
        ['01 AUG 2018 /01 SEP 2018 '], ['', np.nan],
        ['W1', np.nan, '10', '10', '2', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0918'],
        ['W2', np.nan, '32', '10', '1', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '2.0',''],
        [''],['W3', 'LGR1', '10', '10', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0918',''],
        ['01 OCT 2018 '],
        ['01 NOV 2018 '],
        ['01 DEC 2018 ']]

    def test_parse_schedule(self, set_up):
        assert schedule_parser.parse_schedule(self.clean_file_text) == self.parse_list_output_reference

def test_parse_keyword_compdatl_line ():
    imput = "'W3' 'LGR1' 10 10 2 2 OPEN 1* 1 2 1 3* 1.0918 /"
    output = ['W3', 'LGR1', '10', '10', '2', '2', 'OPEN', '1*', '1', '2', '1', '3*', '1.0918']
    assert schedule_parser.parse_keyword_COMPDATL_line(imput) == output

