from PySide6.QtCore import QThread, Signal, QObject

class WordLookupWorker(QObject):
    finished = Signal(str, str)  # definition, synonym
    error = Signal(str)

    def __init__(self, word):
        super().__init__()
        self.word = word

    def run(self):
        try:
            import wordhoard
            # Fetch data (these may take time)
            definition = wordhoard.definitions(self.word)
            synonym = wordhoard.synonyms(self.word)
            self.finished.emit(definition, synonym)
        except Exception as e:
            self.error.emit(str(e))
