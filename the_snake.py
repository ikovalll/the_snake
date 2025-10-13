from random import choice, randint

import pygame

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
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Родительский класс"""

    def __init__(self) -> None:
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = None

    def draw(self):
        """Отрисовка обьектов с заглушкой для изменения потом"""
        pass


class Apple(GameObject):  # Здесь вроде все готово (Временный комент для себя).
    """
    Яблоко наследуемое от родительского класса.
    Оно должно появляться в случайнок координате.
    """

    def __init__(self):
        """Инициализатор яблока и вызов случайной позиции."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Рандомно вычисляются координаты в пределах поля."""
        x_position = randint(0, 31) * GRID_SIZE  # Уменьшил диапазон на 1.
        y_position = randint(0, 23) * GRID_SIZE  # Уменьшил диапазон на 1.
        self.position = (x_position, y_position)

    def draw(self):
        """Отрисовка яблока на экране с прекода."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Змейка наследуемая от родительского класса."""

    def __init__(self):
        """Инициализотор змейки (ее позиция и цвет и тд)."""
        super().__init__()
        self.body_color = SNAKE_COLOR
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позиции змейки (добавляя голову и удаляя хвост.)"""
        head_now_x, head_now_y = self.get_head_position()
        if self.direction == RIGHT:
            head_now_x += GRID_SIZE
        elif self.direction == LEFT:
            head_now_x -= GRID_SIZE
        elif self.direction == DOWN:
            head_now_y += GRID_SIZE
        elif self.direction == UP:
            head_now_y -= GRID_SIZE

        head_now_x %= SCREEN_WIDTH
        head_now_y %= SCREEN_HEIGHT

        new_head = (head_now_x, head_now_y)

        if new_head in self.positions[1:]:
            self.reset()
            return

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self):
        """Отрисовка змейки с прекода."""
        for position in self.positions:  # Тут убрал срез.
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        """Отрисовка головы змейки."""
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        """Затирание последнего сегмента."""
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки, первый el в [positions]."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змеку в начальное состоянме."""
        self.__init__()
        self.direction = choice(POSITIONS_DIRECTION)


def handle_keys(game_object):
    """Функция обработки действий пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основной цикл игры, Функция main"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)
        # Тут опишите основную логику игры.
        handle_keys(snake)

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        snake.update_direction()
        snake.move()
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
