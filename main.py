from decouple import Config
from game_logic import play_game


def load_config():
    config = Config('config/settings.ini')
    min_number = config('min_number', default=1, cast=int)
    max_number = config('max_number', default=100, cast=int)
    attempts = config('attempts', default=5, cast=int)
    initial_capital = config('initial_capital', default=100, cast=int)

    return min_number, max_number, attempts, initial_capital


if __name__ == "__main__":
    min_number, max_number, attempts, initial_capital = load_config()
    final_capital = play_game(min_number, max_number, attempts, initial_capital)
    print(f"Игра окончена. Ваш конечный капитал: {final_capital}")