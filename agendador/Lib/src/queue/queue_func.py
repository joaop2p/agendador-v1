import re
from threading import Thread
from time import sleep
import traceback


class Queue:
    """
        Uma fila de tarefas que executarão de forma assíncrona em relação às tarefas principais.
    """
    started: bool
    works: list[callable]

    def __init__(self):
        super().__init__()
        self.works = []
        self.started = False

    def __str__(self):
        return f"Tarefas adicionadas: {[work.__name__ for work in self.works]}. Inicializado: {self.started}"

    def insert_work(self, work: callable) -> None:
        """Insere uma tarefa na fila de execução 'paralela'"""
        self.works.append(work)

    def remove_work(self, work: callable) -> None:
        """Remove uma tarefa da fila de execução 'paralela'"""
        self.works.remove(work)

    def _execute(self) -> None:
        if len(self.works) < 1:
            raise Exception("A fila deve conter ao menos 1 tarefa para ser executada antes de iniciar")
        while len(self.works) > 0:
            sleep(0.5)
            for work in self.works:
                if work():
                    self.remove_work(work)
                
    def execute(self):
        if self.started:
            raise Exception("Atenção: A fila já está em execução!")
        try:
            Thread(target=self._execute, name="Lista de tarefas", daemon=True).start()
            self.started = True
            return 
        except Exception as e:
            print(traceback.TracebackException(e))
            return e

QUEUE_WORK = Queue()