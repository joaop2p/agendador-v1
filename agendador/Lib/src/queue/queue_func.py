import asyncio
from datetime import datetime
import re
import traceback


class Queue:
    """
        # Queue
        ### O que faz?
        Uma fila de tarefas que executarão de forma assíncrona em relação às tarefas principais.
    """
    works: list[callable]

    def __init__(self):
        super().__init__()
        self.works = []

    def __str__(self):
        return f"Tarefas adicionadas: {self.works}."

    def insert_work(self, work: callable) -> None:
        """Insere uma tarefa na fila de execução 'paralela'"""
        self.works.append(work)

    async def remove_work(self, work: callable) -> None:
        """Remove uma tarefa da fila de execução 'paralela'"""
        self.works.remove(work)

    async def _execute(self) -> None:
        if len(self.works) < 1:
            raise Exception("A fila deve conter ao menos 1 tarefa para ser executada antes de iniciar")
        while len(self.works) > 0:
            await asyncio.sleep(1)
            for work in self.works:
                if work():
                    await self.remove_work(work)
                
    def execute(self):
        try:
            return asyncio.run(self._execute())
        except Exception as e:
            return e