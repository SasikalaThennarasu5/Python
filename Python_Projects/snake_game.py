import curses
import random

class Snake:
    def __init__(self, y, x):
        self.body = [[y, x]]
        self.direction = curses.KEY_RIGHT

    def move(self, grow=False):
        head = self.body[0][:]
        if self.direction == curses.KEY_RIGHT:
            head[1] += 1
        elif self.direction == curses.KEY_LEFT:
            head[1] -= 1
        elif self.direction == curses.KEY_UP:
            head[0] -= 1
        elif self.direction == curses.KEY_DOWN:
            head[0] += 1
        self.body.insert(0, head)
        if not grow:
            self.body.pop()

    def collides(self, max_y, max_x):
        head = self.body[0]
        return (head in self.body[1:] or
                head[0] in [0, max_y] or
                head[1] in [0, max_x])

def generate_food(snake, max_y, max_x):
    while True:
        food = [random.randint(1, max_y-2), random.randint(1, max_x-2)]
        if food not in snake.body:
            yield food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    snake = Snake(sh//2, sw//4)
    food_gen = generate_food(snake, sh, sw)
    food = next(food_gen)

    while True:
        stdscr.clear()
        stdscr.border()

        stdscr.addch(food[0], food[1], '*')
        for y, x in snake.body:
            stdscr.addch(y, x, '#')

        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            opposite = {curses.KEY_RIGHT: curses.KEY_LEFT,
                        curses.KEY_LEFT: curses.KEY_RIGHT,
                        curses.KEY_UP: curses.KEY_DOWN,
                        curses.KEY_DOWN: curses.KEY_UP}
            if key != opposite.get(snake.direction, None):
                snake.direction = key

        snake.move(grow=(snake.body[0] == food))

        if snake.body[0] == food:
            food = next(food_gen)

        if snake.collides(sh, sw):
            msg = "Game Over!"
            stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
            stdscr.refresh()
            curses.napms(2000)
            break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
