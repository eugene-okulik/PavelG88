import os
import argparse
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)


def colorize(word):
    """Возвращает слово с цветом в зависимости от типа"""
    upper = word.upper()
    if "ERROR" in upper:
        return f"{Fore.RED}{word}{Style.RESET_ALL}"
    elif "WARN" in upper:
        return f"{Fore.YELLOW}{word}{Style.RESET_ALL}"
    elif "INFO" in upper:
        return f"{Fore.CYAN}{word}{Style.RESET_ALL}"
    return word


def read_file(file_path, search_text):
    """Сканирует файл построчно и ищет указанный текст"""
    results = []
    with open(file_path, encoding="utf-8", errors="ignore") as f:
        for num, line in enumerate(f, start=1):
            if search_text in line:
                words = line.split()
                for i, word in enumerate(words):
                    if search_text in word:
                        start = max(0, i - 5)
                        end = min(len(words), i + 6)
                        snippet_words = [colorize(w) for w in words[start:end]]
                        results.append((num, " ".join(snippet_words)))
                        break
    return results


def main():
    parser = argparse.ArgumentParser(description="Поиск текста в логах")
    parser.add_argument("path", help="Путь к файлу или папке с логами")
    parser.add_argument("--text", required=True, help="Текст для поиска")
    args = parser.parse_args()

    search_text = args.text
    path = args.path

    if not os.path.exists(path):
        print(f"Ошибка: путь '{path}' не найден.")
        return

    # Если указан конкретный файл
    if os.path.isfile(path):
        print(f"Проверяем файл: {os.path.basename(path)}")
        results = read_file(path, search_text)
        if results:
            for num, snippet in results:
                print(f"{path}:{num} → {snippet}")
        else:
            print("Ничего не найдено.")

    # Если указана папка
    elif os.path.isdir(path):
        print(f"Ищем во всех файлах в папке: {path}")
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                results = read_file(file_path, search_text)
                if results:
                    print(f"\nНайдено в файле: {file}")
                    for num, snippet in results:
                        print(f"  Строка {num}: {snippet}")
        print("\nПоиск завершён.")
    else:
        print("Ошибка: указанный путь не является файлом или папкой.")


if __name__ == "__main__":
    main()
