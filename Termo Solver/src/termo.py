import base64
import struct
from datetime import datetime
import pytz
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def Eh():
    time_sp = pytz.timezone("America/Sao_Paulo")
    base_date = datetime(2022, 1, 2, tzinfo=time_sp)
    now_sp = datetime.now(time_sp)
    dif = now_sp - base_date
    return dif.days

def ey(x):
    return Eh() if 1 == x else Eh() - 51

Pf = []

f1 = open(DATA_DIR / "base64_1.txt", "r")
f2 = open(DATA_DIR / "base64_2.txt", "r")

raw_hb = base64.b64decode(f1.read())
raw_xb = base64.b64decode(f2.read())

wB = list(struct.unpack('<' + 'H' * (len(raw_hb) // 2), raw_hb))
xB = list(struct.unpack('<' + 'H' * (len(raw_xb) // 2), raw_xb))
with open(DATA_DIR / "Pf.txt", "r", encoding="utf-8") as f:
    Pf = [linha.strip().replace('"', '') for linha in f.read().split(',')]

bc = [1, 2, 4]

dic = { 1 : "Termo", 2 : "Dueto", 4 : "Quarteto"}

for x in bc:
    results = []
    e = ey(x)
    o = {
        1: Pf,
        2: wB,
        4: xB
    }[x]
    r = x * e % len(o)
    i = o[r:r + x]

    for t in range(x):
        results.append(o[r] if 1 == x else Pf[i[t]])
    print(f'{dic[x]}: {results}')