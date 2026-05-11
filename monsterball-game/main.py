import gui_core as gui
import random

w = gui.Window('시작하려면 엔터 키를 누르세요')

def initialize(timestamp):
    w.data.numbers = [
        w.newRectangle(0, 0, 800, 600, 'white'),

        w.newImage(120, 20, 'assets/boom_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/basketball.png', isVisible=False),
        w.newImage(120, 20, 'assets/tennis_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/basketball.png', isVisible=False),
        w.newImage(120, 20, 'assets/tennis_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/tennis_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/basketball.png', isVisible=False),
        w.newImage(120, 20, 'assets/golf_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/golf_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/soccer_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/soccer_ball.png', isVisible=False),
        w.newImage(120, 20, 'assets/baseball.png', isVisible=False),
        w.newImage(120, 20, 'assets/baseball.png', isVisible=False),
        w.newImage(120, 20, 'assets/baseball.png', isVisible=False),

        w.newImage(250, 20, 'assets/monster_ball.png', isVisible=False)
    ]
    
    w.data.time_start = 0
    w.data.time_end = 0
    w.data.min_duration_wait = 1.0
    w.data.max_duration_wait = 3.0
    w.data.duration_game = 1.0
    w.data.duration_result = 3.0
    w.data.state = 0
    w.data.previous_state = 0

    


def update(timestamp):

    w.newText(10, 10, 790, '''Escape: 종료''', anchor='nw')
    
    if w.keys['Escape']:
                w.stop()
                return
            
    if w.data.state == 0:
        if w.keys['Return']:
            w.setTitle('기다리는 중...')
            
            for i in range(1,16):                
                w.showObject(w.data.numbers[i])
                
            w.data.time_start = timestamp
            w.data.time_end = timestamp + random.random() * (w.data.max_duration_wait - w.data.min_duration_wait) + w.data.min_duration_wait
            w.data.state = 1
            
    elif w.data.state == 1:
        for idx_toMove in range(1, 16):
            isStacked = True
            
            while isStacked:
                isStacked = False
                new_x1 = random.randint(0, 760)
                new_y1 = random.randint(0, 560)
                new_x2 = new_x1 + 40
                new_y2 = new_y1 + 40

                for idx_toCheck in range(1, idx_toMove):
                    old_x1, old_y1 = w.getPosition(w.data.numbers[idx_toCheck])
                    old_x2 = old_x1 + 40
                    old_y2 = old_y1 + 40

                    if new_x1 <= old_x2 and new_x2 >= old_x1 and new_y1 <= old_y2 and new_y2 >= old_y1:
                        isStacked = True
                        break

            w.moveObject(w.data.numbers[idx_toMove], new_x1, new_y1)
        
        if timestamp >= w.data.time_end:
            w.setTitle('몬스터볼을 눌러주세요!')
            w.data.time_start = timestamp
            w.data.time_end = timestamp + w.data.duration_game
            w.data.state = 2

    elif w.data.state == 2:
        if w.mouse_buttons[1] or w.keys['a'] or w.keys['q']:
            number = w.getTopObjectAt(w.mouse_position_x, w.mouse_position_y)
            if number == w.data.numbers[15]:
                w.setTitle('성공!')
                w.recolorObject(w.data.numbers[0], 'cyan')
            elif w.keys['a'] or w.keys['q']:
                w.setTitle('치트 사용. 성공!')
                w.recolorObject(w.data.numbers[0], 'yellow')
                
            else:
                w.setTitle('몬스터볼을 누르지 않았습니다. 실패!')
                w.recolorObject(w.data.numbers[0], 'magenta')

            w.data.time_start = timestamp
            w.data.time_end = timestamp + w.data.duration_result
            w.data.state = 3
            
        elif timestamp >= w.data.time_end:
            w.setTitle('시간 초과입니다. 실패!')
            w.recolorObject(w.data.numbers[0], 'red')
            
            w.data.time_start = timestamp
            w.data.time_end = timestamp + w.data.duration_result
            w.data.state = 3
            
    elif w.data.state == 3:
        if timestamp >= w.data.time_end:
            w.setTitle('다시 시작하려면 엔터 키를, 그만두시려면 Esc 키를 누르세요.')
            w.recolorObject(w.data.numbers[0], 'white')
            for i in range(1,16):
                w.hideObject(w.data.numbers[i])

            w.data.state = 0

    w.data.previous_state = w.data.state


w.initialize = initialize
w.update = update

w.start()


