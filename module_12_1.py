from unittest import TestCase
from runner import Runner

class RunnerTest(TestCase):
    def test_walk(self):
        r1 = Runner('Алина')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance,50)
    def test_run(self):
        r2 = Runner('Игорь')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)
    def test_challenge(self):
        r1 = Runner('Алина')
        r2 = Runner('Игорь')
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)
