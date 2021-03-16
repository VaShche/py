import unittest
import sys
import subprocess


py_pass = sys.executable
calc_script = "calc.py"
one_line = True


def script_executer(in_params) -> []:
    """
    :param in_params: [] lines for cin
    :return: (output lines from cout, exit code)
    """
    in_lines = []
    with open('in.txt', 'w') as f:
        if one_line:
            in_lines = ''.join(map(str, in_params))
        else:
            for line in in_params:
                in_lines.append(str(line) + '\n')
        f.writelines(in_lines)
    with open('out.txt', 'w') as f_out:
        with open('in.txt', 'r') as f_in:
            code = subprocess.call([py_pass, calc_script], stdin=f_in, stdout=f_out, stderr=f_out)
    with open('out.txt', 'r') as f_out:
        result_lines = f_out.readlines()
    return result_lines, code


class CalcTestCasePlus(unittest.TestCase):
    in_params = [11, '+', 20.5]
    exp_res = '31.5'

    exp_len = 1
    res = None
    exit_code = None
    message = None

    @classmethod
    def setUpClass(cls):
        cls.res, cls.exit_code = script_executer(cls.in_params)
        cls.message = cls.getmessage(cls.in_params, cls.exp_res)

    @staticmethod
    def getmessage(in_params, expected):
        return '\nTrying "{0} = {1}", but:\n'.format(' '.join(map(str, in_params)), expected)

    def test_exit_code_0(self):
        self.assertEqual(self.exit_code, 0, self.message + 'Script crash, exit code != 0')

    @unittest.skip
    def test_coutlines(self):
        self.assertEqual(self.exp_len, len(self.res),
                         self.message + 'Script result is more then {0} lines:\n{1}'.format(self.exp_len, self.res))

    def test_working(self):
        self.assertIn(self.exp_res, ''.join(self.res), self.message + 'No correct answer')


class CalcTestCaseMinus(CalcTestCasePlus):
    in_params = [11, '-', 22]
    exp_res = '-11'


class CalcTestCaseMulti(CalcTestCasePlus):
    in_params = [3, '*', -4]
    exp_res = '-12'


class CalcTestCasePow(CalcTestCasePlus):
    in_params = [-5, '^', 2]
    exp_res = '25'


class CalcTestCaseDiv(CalcTestCasePlus):
    in_params = [9, '/', 2]
    exp_res = '4.5'

    def test_div_0(self):
        p = [1, '/', 0]
        r, c = script_executer(p)
        m = self.getmessage(p, 'INF')
        self.assertEqual(c, 0, m + 'Script crash, exit code != 0')
        #self.assertEqual(len(r), self.exp_len,
        #                 m + 'Script result is more then {0} lines:\n{1}'.format(self.exp_len, r))


class CalcTestCaseParams(unittest.TestCase):
    def test_input_in_one_line(self):
        self.assertTrue(one_line, "Input in one line is not tested")

class CalcTestMoreThanOneOperations(CalcTestCasePlus):
    in_params = [-5.1, '+', 2.6, '-', -5]
    exp_res = '2.5'

class CalcTestPriorityOperations(CalcTestCasePlus):
    in_params = [2, '+', 2, '*', 2, '+', 3, '/', 2]
    exp_res = '7.5'

class CalcTestPriorityOperations2(CalcTestCasePlus):
    in_params = [2, '*', 2, '+', 2, '+', 3, '/', 2]
    exp_res = '7.5'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        calc_script = sys.argv[1]
        sys.argv = [sys.argv[0]]
    unittest.main()
