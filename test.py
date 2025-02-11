import time
import math
import random
import os

def test_cpu():
    print("Тестирование процессора...")
    start_time = time.time()

    # Выполняем тяжелые вычисления
    for _ in range(10**7):
        math.sqrt(random.randint(1, 1000))

    end_time = time.time()
    cpu_time = end_time - start_time
    print(f"Время выполнения CPU-теста: {cpu_time:.2f} секунд")
    return cpu_time

def test_ram():
    print("Тестирование оперативной памяти...")
    start_time = time.time()

    # Создаем и обрабатываем большой список
    data = [random.random() for _ in range(10**7)]
    data.sort()

    end_time = time.time()
    ram_time = end_time - start_time
    print(f"Время выполнения RAM-теста: {ram_time:.2f} секунд")
    return ram_time

def test_disk():
    print("Тестирование диска...")
    start_time = time.time()

    # Записываем и читаем файл
    test_file = "speed_test_file.tmp"
    data = os.urandom(1024 * 1024 * 100)  # 100 МБ данных

    with open(test_file, "wb") as f:
        f.write(data)

    with open(test_file, "rb") as f:
        _ = f.read()

    os.remove(test_file)

    end_time = time.time()
    disk_time = end_time - start_time
    print(f"Время выполнения дискового теста: {disk_time:.2f} секунд")
    return disk_time

def main():
    print("Начало тестирования производительности компьютера...")
    cpu_time = test_cpu()
    ram_time = test_ram()
    disk_time = test_disk()

    print("\nРезультаты тестирования:")
    print(f"CPU: {cpu_time:.2f} секунд")
    print(f"RAM: {ram_time:.2f} секунд")
    print(f"Диск: {disk_time:.2f} секунд")

if __name__ == "__main__":
    main()
