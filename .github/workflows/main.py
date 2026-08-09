import time
from datetime import datetime

dt = datetime.fromtimestamp(time.time() + 129600)
dt_str = dt.strftime("%a %d %b %H:%M:%S %Y +0200")
print('->', dt_str)

with open("date", "w") as f:
    f.write(f"{dt_str}")
