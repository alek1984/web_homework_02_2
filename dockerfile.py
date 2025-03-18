# Вибираємо офіційний образ Python
FROM python:3.10-slim

# Встановлюємо необхідні інструменти
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Встановлюємо Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Встановлюємо змінну середовища для Poetry
ENV PATH="/root/.local/bin:$PATH"

# Створюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файли проєкту
COPY . .

# Вказуємо версію Python у Poetry
RUN poetry env use python3.10

# Встановлюємо залежності через Poetry
RUN poetry install --no-root --no-dev

# Вказуємо, що контейнер запускає CLI-застосунок
ENTRYPOINT ["poetry", "run", "python", "assistant.py"]
