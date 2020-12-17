from pathlib import Path


class File:

    def read(self, file):
        with open(file, 'r') as reader:
            return reader.readlines()

    def write(self, file, content):
        with open(file, 'w') as writer:
            writer.write(content)

    def delete(self, file):
        if Path(file).exists():
            Path(file).unlink()
        else:
            raise FileExistsError("File doesn't exists!")
