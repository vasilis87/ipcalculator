from unittest import TestCase,main


class Ipcalculator_test(TestCase):
    def test_24(self):
        self.assertEqual(ipcalculator('192.168.1.5/24'),('192.168.1.0','255.255.255.0','0.0.0.255','192.168.1.255','192.168.1.1','192.168.1.254'))
    def test_16(self):
        self.assertEqual(ipcalculator('172.16.5.4/16'),('172.16.0.0','255.255.0.0','0.0.255.255','172.16.255.255','172.16.0.1','172.16.255.254'))

    def test_8(self):
        self.assertEqual(ipcalculator('10.2.56.5/8'),('10.0.0.0','255.0.0.0','0.255.255.255','10.255.255.255','10.0.0.1','10.255.255.254'))

    def test_31(self):
        self.assertEqual(ipcalculator('54.58.2.6/31'),('54.58.2.6','255.255.255.254','0.0.0.1','54.58.2.7','54.58.2.7','54.58.2.6'))

    def test_30(self):
        self.assertEqual(ipcalculator('172.16.58.13/30'),('172.16.58.12', '255.255.255.252', '0.0.0.3', '172.16.58.15', '172.16.58.13', '172.16.58.14'))

    def test_29(self):
        self.assertEqual(ipcalculator('10.15.68.4/29'),('10.15.68.0', '255.255.255.248', '0.0.0.7', '10.15.68.7', '10.15.68.1', '10.15.68.6'))

    def test_28(self):
        self.assertEqual(ipcalculator('16.5.2.6/28'),('16.5.2.0', '255.255.255.240', '0.0.0.15', '16.5.2.15', '16.5.2.1', '16.5.2.14'))

    def test_no_32(self):
        with self.assertRaises(ValueError) as e:
            ipcalculator('10.0.0.0/33')
        self.assertEqual('Preffic lenght cant be more than 32',e.exception.args[0])




if __name__ == '__main__':
    main
