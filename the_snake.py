from random import choice, randint

import pygame as pg

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Создал список для метода reset.
POSITIONS_DIRECTION = [UP, DOWN, LEFT, RIGHT]

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pg.display.set_caption('Змейка')

# Настройка времени:
clock = pg.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Родительский класс."""

    def __init__(self, body_color=None) -> None:
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = body_color

    def draw(self):
        """Отрисовка обьектов с заглушкой для изменения потом"""
        raise NotImplementedError('Метод draw надо определить')


class Apple(GameObject):  # Здесь вроде все готово (Временный комент для себя).
    """
    Яблоко наследуемое от родительского класса.
    Оно должно появляться в случайнок координате.
    """

    def __init__(self, busy_positions=None):
        """Инициализатор яблока и вызов случайной позиции."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position(busy_positions)

    def randomize_position(self, busy_positions=None):
        """Рандомно вычисляются координаты в пределах поля."""
        if busy_positions is None:
            busy_positions = []

        while True:
            self.position = (
                randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if self.position not in busy_positions:
                break

    def draw(self):
        """Отрисовка яблока на экране с прекода."""
        rect = pg.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, self.body_color, rect)
        pg.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Змейка наследуемая от родительского класса."""

    def __init__(self):
        """Инициализотор змейки (ее позиция и цвет и тд)."""
        super().__init__(body_color=SNAKE_COLOR)
        self.next_direction = None
        self.reset()

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позиции змейки (добавляя голову и удаляя хвост.)"""
        head_now_x, head_now_y = self.get_head_position()
        direction_x, direction_y = self.direction

        new_head = (
            (head_now_x + (direction_x * GRID_SIZE)) % SCREEN_WIDTH,
            (head_now_y + (direction_y * GRID_SIZE)) % SCREEN_HEIGHT
        )
        # Новая голова тут и pop удаляет последний el.
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self):
        """Отрисовка змейки с прекода."""
        for position in self.positions:  # Тут убрал срез.
            rect = (pg.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pg.draw.rect(screen, self.body_color, rect)

            if self.last:
                last_rect = pg.Rect(self.last, (GRID_SIZE, GRID_SIZE))
                pg.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки, первый el в [positions]."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змеку в начальное состоянме."""
        screen.fill(BOARD_BACKGROUND_COLOR)
        self.length = 1
        self.positions = [self.position]
        self.direction = choice(POSITIONS_DIRECTION)
        self.last = None


def handle_keys(game_object):
    """Функция обработки действий пользователя."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pg.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pg.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pg.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основной цикл игры, Функция main"""
    # Инициализация PyGame:
    pg.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple(busy_positions=snake.positions)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()
        snake.update_direction()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(busy_positions=snake.positions)

        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        apple.draw()
        snake.draw()
        pg.display.update()


if __name__ == '__main__':
    main()
