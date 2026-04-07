import argparse
import csv
import sys

from tabulate import tabulate

from reports.coffee import MedianCoffee


REPORT_REGISTRY = {
    'median-coffee': MedianCoffee(),
}


def read_csv_files(file_paths):
    combined_data = []
    for path in file_paths:
        try:
            with open(path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    combined_data.append(row)
        except FileNotFoundError:
            print(f'Файл не найден - {path}', file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f'Ошибка при чтении {path}: {e}', file=sys.stderr)
            sys.exit(1)
    return combined_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    report_engine = REPORT_REGISTRY.get(args.report)

    if not report_engine:
        print(f'Репорт "{args.report}" не найден.', file=sys.stderr)
        sys.exit(1)

    try:
        all_data = read_csv_files(args.files)

        if not all_data:
            print('Файл пуст или нет данных.', file=sys.stderr)
            sys.exit(1)

        table_data = report_engine.calculate(all_data)
        print(tabulate(
            table_data,
            headers=['student', 'coffee_spent'],
            tablefmt='grid'
        ))

    except Exception as e:
        print(f'Произошла ошибка: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
