# practice-dimafyodorov

Репозиторий с практиками.

## Запуск
Скачать проект.
```
git clone https://github.com/11OP-group/practice-dimafyodorov.git
cd practice-dimafyodorov
```

Сейчас есть только тестовый проект `temp-test`.

### Через чистый Python
Рекомендуемая версия 3.13.*. Желательно установить зависимости (нужно для 2 способа).
```bash
# Создать виртуальное окружение
python -m venv .venv

# Активировать виртуальное окружение
# На Windows в командной строке
.venv\Scripts\activate.bat
# На Windows в PowerShell
.\.venv\Scripts\Activate.ps1
# На Windows в Git Bash
source .venv/Scripts/activate
# На MacOS и Linux
source .venv/bin/activate

# Установить зависимости
pip install -e .

# Доп. Везде чтобы выйти из виртуального окружения
deactivate
```

Есть 2 способа:
- Запуск конкретного файла
```bash
python src/temp_test/__main__.py
```
- Запуск как модуля
```bash
python -m temp_test
# или просто
temp_test
```

### Используя UV
Нужно установить пакетный менеджер uv с [официального сайта](https://docs.astral.sh/uv/#highlights). Потом нужно установить зависимости.
```bash
uv sync
```

Для запуска есть 2 способа:
- Запуск конкретного файла
```bash
uv run src/temp_test/__main__.py
```
- Запуск модуля (рекомендуется)
```bash
uv run temp-test
```

### Используя nix flake
Лично я использую этот вариант, но не работает напрямую на Windows (только если через WSL), и ещё большее усложнение для этой задачи.

Нужно установить nix (у меня сразу NixOS) с [официального сайта](https://nixos.org). Потом нужно включить экспериментальные опции "nix-command" и "flakes".
Нужно активировать окружение, оно само поставит зависимости, а дальше также как с uv.
```bash
nix develop
```

Также в этом случае можно использовать [direnv](https://github.com/direnv/direnv), что бы автоматически активировать окружение при переходе в папку.
```bash
direnv allow
```
