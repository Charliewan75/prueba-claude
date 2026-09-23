from datetime import datetime

ahora = datetime.now()
print(f"Hola! Fecha y hora actuales: {ahora:%d/%m/%Y %H:%M:%S}")
