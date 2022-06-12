import turtle
import math
import time

numIterations = 10  # num fractals to make


sc = turtle.Screen()
t = turtle.Turtle()
sc.colormode(255)
defaultSpeed = 5
curIterations = 0
segments = [(sc.window_width(), 0, (0, 0, 0))]

t.speed(defaultSpeed)
t.penup()
t.setposition(-sc.window_width() / 2, 0)
t.pendown()
t.setposition(sc.window_width() / 2, 0)
t.penup()
t.speed(2)
t.setposition(-sc.window_width() / 2, 0)
t.pendown()
t.clear()


def draw(data):
    global curIterations, numIterations, defaultSpeed, segments
    segments.clear()

    # perform pre-calculations
    for segment in data:  # split each segment into 4 (middle becomes two)
        segments.append((segment[0] / 3, segment[1], (0, 0, 0)))

        angleLength = ((segment[0] / 3) / 2) / math.sin(math.radians(30))
        segments.append((angleLength, segment[1] + 60, (255, 0, 0)))
        segments.append((angleLength, segment[1] - 60, (255, 0, 0)))

        segments.append((segment[0] / 3, segment[1], (0, 0, 0)))

    # draw calculated segments
    for segment in segments:
        t.pencolor(segment[2])
        t.setheading(segment[1])
        t.forward(segment[0])

    curIterations += 1

    if curIterations < numIterations:
        t.speed(2)
        t.penup()
        t.setposition(-sc.window_width() / 2, 0)
        t.pendown()
        t.speed(defaultSpeed + curIterations)
        t.clear()
        draw(segments[:])
    return


if __name__ == '__main__':
    draw(segments[:])
    time.sleep(5)
