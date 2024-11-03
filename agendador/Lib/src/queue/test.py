import unittest
import asyncio
from queue_func import Queue  # Supondo que sua classe Queue esteja no arquivo queue_module.py

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_insert_work(self):
        def sample_work():
            return True
        self.queue.insert_work(sample_work)
        self.assertIn(sample_work, self.queue.works)

    def test_remove_work(self):
        async def sample_work():
            return True
        self.queue.insert_work(sample_work)
        asyncio.run(self.queue.remove_work(sample_work))
        self.assertNotIn(sample_work, self.queue.works)

    def test_execute(self):
        def sample_work():
            return True
        self.queue.insert_work(sample_work)
        self.queue.execute()
        self.assertEqual(len(self.queue.works), 0)

if __name__ == '__main__':
    unittest.main()
