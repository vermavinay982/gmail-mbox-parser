import email
from email.policy import default

class MboxReader:
    def __init__(self, filename):
        self.handle = open(filename, 'rb')
        assert self.handle.readline().startswith(b'From ')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle.close()

    def __iter__(self):
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()
            if line == b'' or line.startswith(b'From '):
                yield email.message_from_bytes(b''.join(lines), policy=default)
                if line == b'':
                    break
                lines = []
                continue
            lines.append(line)

path = "YOUR_MBOX.mbox"
mbox = MboxReader(path)
from tqdm import tqdm

with open('Output2.txt','w',encoding="utf-8") as file:
    for idx,message in tqdm(enumerate(mbox)):
        # print(message.keys())
        print(idx,message['From'])
        mail_from = f"{str(message['From'])}\n".replace('"','')
        file.write(mail_from)
