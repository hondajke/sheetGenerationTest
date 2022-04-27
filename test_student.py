import unittest
from institute import Institute
from main import Student

class TestAddStudent(unittest.TestCase):
    
    def test_1(self): # correct add(One object)
        st = Student(172544, 'Филиппов Петр')
        inst = Institute()
        inst.add_student(st)
        self.assertEqual(len(inst.students), 1)
        
    def test_2(self): # correct add(Two objects)
        st1 = Student(172544, 'Филиппов Петр Петрович')
        st2 = Student(199999, "Егоров Айтал Никитич")
        inst = Institute()
        inst.add_student(st1)
        inst.add_student(st2)
        self.assertEqual(len(inst.students), 2)
        
    def test_3(self): # incorrect add(Existing object)
        st = Student(172544, 'Филиппов Петр')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(st)
            inst.add_student(st)
        self.assertEqual("Student already exist", str(context.exception))
        self.assertEqual(len(inst.students), 1)
    
    def test_4(self): # incorrect add(None object) 
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(None)
        self.assertEqual("Student is null", str(context.exception))
        self.assertEqual(len(inst.students), 0)
        
    def test_5(self): # incorrect add(Existing student code)
        st1 = Student(172544, 'Филиппов Петр Петрович')
        st2 = Student(172544, "Егоров Айтал Никитич")
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(st1)
            inst.add_student(st2)
        self.assertEqual("Student code already exist", str(context.exception))
        self.assertEqual(len(inst.students), 1)
        
    def test_6(self): # incorrect add(Wrong type)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(1)
        self.assertEqual("Wrong type", str(context.exception))
        self.assertEqual(len(inst.students), 0)
    
    def test_7(self): # incorrect type(Wrong student code)
        st = Student(1000, 'Филиппов Петр')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(st)
        self.assertEqual("Wrong student code", str(context.exception))
        self.assertEqual(len(inst.students), 0)
        
    def test_8(self): # incorrect type(Fio is null)
        st = Student(172544, '')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_student(st)
        self.assertEqual("Student fio is null", str(context.exception))
        self.assertEqual(len(inst.students), 0)
        
        
class TestGetStudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls._stud = Student(172544, 'Иванов Иван Иванович')
        cls._inst = Institute()
        cls._inst.add_student(cls._stud)
    
    def test_1(self): # correct get
        get_stud = self._inst.get_student(172544)
        self.assertEqual(get_stud, self._stud)
    
    #def test_2(self): # incorrect get(Wrong type)
    #    with self.assertRaises(Exception) as context:
    #        get_spec = self._inst.get_spec("172544")
    #    self.assertEqual("Wrong type", str(context.exception))