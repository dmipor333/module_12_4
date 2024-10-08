import unittest
import logging
import rt_with_exceptions


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            item_walk = rt_with_exceptions.Runner('Ran1', -50)
            for i in range(10):
                item_walk.walk()
            self.assertEqual(item_walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {item_walk}')
        except:
            logging.warning(f'"Неверная скорость для Runner".', exc_info=True)

    def test_run(self):
        try:
            item_run = rt_with_exceptions.Runner('25')
            for i in range(10):
                item_run.run()
                self.assertEqual(item_run.distance, 100)
                logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'"Неверный тип данных для объекта Runner".',exc_info=True)

    def test_challenge(self):
        item1 = rt_with_exceptions.Runner('Ran3')
        item2 = rt_with_exceptions.Runner('Ran4')
        for i in range(10):
            item1.walk()
            item2.run()
        self.assertNotEqual(item1.distance, item2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                        format="%(asctime)s - %(levelname)s - %(message)s")
