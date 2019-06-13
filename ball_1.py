# -*- coding: utf-8 -*-
import simpleguitk as simplegui
import random

WIDTH = 500
HEIGHT = 500
BALL_RADIUS = 8
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 8
HALF_PADDLE_WIDTH = PADDLE_WIDTH / 2
HALF_PADDLE_HEIGHT = PADDLE_HEIGHT / 2
ball_pos= [250, 250]
ball_vel= [1, 2]
paddle_pos=220
paddle_vel=0
live=3
score=0
# 发球
def spawn_ball():
    global ball_pos, ball_vel
    ball_pos= [250, 250]
    ball_vel= [1, 2]
def new_game():
    global score, live
    global paddle_pos, paddle_vel
    score = 0
    live = 3
    paddle_pos = HEIGHT / 2
    paddle_vel = 0
    spawn_ball()
def draw(canvas):
    global score, live, paddle_pos, ball_pos, ball_vel, paddle_vel
    canvas.draw_line([0, 250], [500, 250], 5, 'white')
    canvas.draw_line([250, 250], [250, 500], 5, 'white')
    canvas.draw_circle([ball_pos[0], ball_pos[1]], 10, 5, 'white', 'white')
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
    canvas.draw_line([paddle_pos, 495], [paddle_pos+60, 495], 10, 'white')
    canvas.draw_text(' 生命： '+str(live), (10, 30), 10, 'yellow')
    canvas.draw_text(' 分数： '+str(score), (80, 30), 10, 'yellow')
    if ball_pos[1] <= 0:
        ball_vel[1] = -ball_vel[1]
    if live >= 1:
        if ball_pos[1] >= 620:
            live -= 1
            ball_pos = [250, 250]
            ball_vel = [1, 2]
    if live == 0:
        canvas.draw_text(' 游戏结束 ', (200, 200), 20, 'yellow')
    if live > 0:
        if score >= 50:
            canvas.draw_text(' 成功！ ', (50, 250), 50, 'yellow')
    if ball_pos[0] >= 495 or ball_pos[0] <= 5:
        ball_vel[0] = -ball_vel[0]
    paddle_pos += paddle_vel
    if paddle_pos < 0:
        paddle_pos = 0
    elif paddle_pos+60 > 496:
        paddle_pos = 440
    if paddle_pos <= ball_pos[0] <= paddle_pos+60:
        if ball_pos[1] == 492:
            ball_vel[1] = -ball_vel[1]
            score += 1
            if ball_vel[0] < 0:
                ball_vel[0] -= 0.1
            elif ball_vel[0] > 0:
                ball_vel[0] += 0.1
            if ball_vel[1] < 0:
                ball_vel[1] -= 0.1
            elif ball_vel[1] > 0:
                ball_vel[1] += 0.1
def keydown(key):
    global paddle_vel
    if key == simplegui.KEY_MAP['left']:
        paddle_vel = -5
    elif key == simplegui.KEY_MAP['right']:
        paddle_vel = 5
def keyup(key):
    global paddle_vel
    if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right']:
        paddle_vel = 0
frame = simplegui.create_frame(" 单人壁球 ", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background("brown")
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button(" 重新开始 ", new_game, 100)

new_game()
frame.start()