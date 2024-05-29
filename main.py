import pygame,configparser,os
from tkinter import messagebox

os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

pygame.init()
pygame.joystick.init()
#초기 변수,환경 설정
config = configparser.ConfigParser()
assets_location = f'{os.path.dirname(__file__)}/assets/'
Controller_Keys = ['BT_A','BT_B','BT_C','BT_D','FX_L','FX_R','KEY_START']
Screen_Width : int = 1280
Screen_Height : int = 720

FPS : int = int(320)

def Loading_Images():
    """
    이미지 로드하는 함수
    """
    START_ON = pygame.image.load(f'{assets_location}start_on.jpg')
    START_OFF = pygame.image.load(f'{assets_location}start_off.jpg')
    BT_ON = pygame.image.load(f'{assets_location}bt_on.jpg')
    BT_OFF = pygame.image.load(f'{assets_location}bt_off.jpg')
    FX_ON = pygame.image.load(f'{assets_location}fx_on.jpg')
    FX_OFF = pygame.image.load(f'{assets_location}fx_off.jpg')
    VOL_L_SPIN_LEFT = pygame.image.load(f'{assets_location}vol_l_l.png')
    VOL_L_SPIN_RIGHT = pygame.image.load(f'{assets_location}vol_l_r.png')
    VOL_R_SPIN_LEFT = pygame.image.load(f'{assets_location}vol_r_l.png')
    VOL_R_SPIN_RIGHT = pygame.image.load(f'{assets_location}vol_r_r.png')
    VOL_OFF = pygame.image.load(f'{assets_location}vol_off.png')
    return START_ON, START_OFF, BT_ON, BT_OFF, FX_ON, FX_OFF, VOL_L_SPIN_LEFT, VOL_L_SPIN_RIGHT, VOL_R_SPIN_LEFT, VOL_R_SPIN_RIGHT, VOL_OFF

def Loading_Configuration():
    """
    Config파일 읽어오는 함수
    """
    config.read(f'{assets_location}config.config')
    key_config = [int(config['KEY_SETTINGS'][key]) for key in Controller_Keys]
    return key_config

def Initialize():#최초 한번만 실행

    if pygame.joystick.get_count() < 1:
        messagebox.showerror('Error','ERROR-100 \n컨트롤러가 감지되지 않았습니다.\n컨트롤러의 연결상태를 확인해주세요.')
        raise Exception


    CLOCK = pygame.time.Clock()

    key_config = Loading_Configuration()

    Images = Loading_Images()

    Screen = pygame.display.set_mode((Screen_Width, Screen_Height))

    pygame.display.set_caption('SDVX CONTROLLER KEY VIEWER v2.0')

    JOYSTICK = pygame.joystick.Joystick(0)
    VOL_L_VALUE_CURRENT = JOYSTICK.get_axis(0)
    VOL_R_VALUE_CURRENT = JOYSTICK.get_axis(1)

    Game_Status = {
        'Is_Game_Running' : True,
        'CONFIG_BT_A' : key_config[0],
        'CONFIG_BT_B' : key_config[1],
        'CONFIG_BT_C' : key_config[2],
        'CONFIG_BT_D' : key_config[3],
        'CONFIG_FX_L' : key_config[4],
        'CONFIG_FX_R' : key_config[5],
        'CONFIG_KEY_START' : key_config[6],
        'IMAGE_KEY_START' : Images[1],
        'IMAGE_BT_A' : Images[3],
        'IMAGE_BT_B' : Images[3],
        'IMAGE_BT_C' : Images[3],
        'IMAGE_BT_D' : Images[3],
        'IMAGE_FX_L' : Images[5],
        'IMAGE_FX_R' : Images[5],
        'IMAGE_VOL_L' : Images[10],
        'IMAGE_VOL_R' : Images[10],
        'IMAGE_KEY_START_ON': Images[0],
        'IMAGE_KEY_START_OFF': Images[1],
        'IMAGE_BT_ON' : Images[2],
        'IMAGE_BT_OFF' : Images[3],
        'IMAGE_FX_ON' : Images[4],
        'IMAGE_FX_OFF' : Images[5],
        'IMAGE_VOL_L_SPIN_LEFT' : Images[6],
        'IMAGE_VOL_L_SPIN_RIGHT' : Images[7],
        'IMAGE_VOL_L_SPIN_PAST' : Images[10],
        'IMAGE_VOL_R_SPIN_LEFT' : Images[8],
        'IMAGE_VOL_R_SPIN_RIGHT' : Images[9],
        'IMAGE_VOL_R_SPIN_PAST' : Images[10],
        'IMAGE_VOL_OFF' : Images[10],
        'Screen' : Screen,
        'VOL_L_VALUE_CURRENT' : VOL_L_VALUE_CURRENT,
        'VOL_R_VALUE_CURRENT' : VOL_R_VALUE_CURRENT,
        'VOL_L_VALUE_PAST' : 0,
        'VOL_R_VALUE_PAST' : 0,
        'CLOCK' : CLOCK,
        'JOYSTICK' : JOYSTICK

    }
    return Game_Status

def KEY_DOWN(Game_Status,event):
    if event.button == Game_Status['CONFIG_KEY_START']:
        Game_Status['IMAGE_KEY_START'] = Game_Status['IMAGE_KEY_START_ON']
    if event.button == Game_Status['CONFIG_BT_A']:
        Game_Status['IMAGE_BT_A'] = Game_Status['IMAGE_BT_ON']
    if event.button == Game_Status['CONFIG_BT_B']:
        Game_Status['IMAGE_BT_B'] = Game_Status['IMAGE_BT_ON']
    if event.button == Game_Status['CONFIG_BT_C']:
        Game_Status['IMAGE_BT_C'] = Game_Status['IMAGE_BT_ON']
    if event.button == Game_Status['CONFIG_BT_D']:
        Game_Status['IMAGE_BT_D'] = Game_Status['IMAGE_BT_ON']
    if event.button == Game_Status['CONFIG_FX_L']:
        Game_Status['IMAGE_FX_L'] = Game_Status['IMAGE_FX_ON']
    if event.button == Game_Status['CONFIG_FX_R']:
        Game_Status['IMAGE_FX_R'] = Game_Status['IMAGE_FX_ON']
    
    return Game_Status['IMAGE_KEY_START'], Game_Status['IMAGE_BT_A'], Game_Status['IMAGE_BT_B'], Game_Status['IMAGE_BT_C'], Game_Status['IMAGE_BT_D'], Game_Status['IMAGE_FX_L'], Game_Status['IMAGE_FX_R']

def KEY_UP(Game_Status,event):
    if event.button == Game_Status['CONFIG_KEY_START']:
        Game_Status['IMAGE_KEY_START'] = Game_Status['IMAGE_KEY_START_OFF']
    if event.button == Game_Status['CONFIG_BT_A']:
        Game_Status['IMAGE_BT_A'] = Game_Status['IMAGE_BT_OFF']
    if event.button == Game_Status['CONFIG_BT_B']:
        Game_Status['IMAGE_BT_B'] = Game_Status['IMAGE_BT_OFF']
    if event.button == Game_Status['CONFIG_BT_C']:
        Game_Status['IMAGE_BT_C'] = Game_Status['IMAGE_BT_OFF']
    if event.button == Game_Status['CONFIG_BT_D']:
        Game_Status['IMAGE_BT_D'] = Game_Status['IMAGE_BT_OFF']
    if event.button == Game_Status['CONFIG_FX_L']:
        Game_Status['IMAGE_FX_L'] = Game_Status['IMAGE_FX_OFF']
    if event.button == Game_Status['CONFIG_FX_R']:
        Game_Status['IMAGE_FX_R'] = Game_Status['IMAGE_FX_OFF']
    
    return Game_Status['IMAGE_KEY_START'], Game_Status['IMAGE_BT_A'], Game_Status['IMAGE_BT_B'], Game_Status['IMAGE_BT_C'], Game_Status['IMAGE_BT_D'], Game_Status['IMAGE_FX_L'], Game_Status['IMAGE_FX_R']

def VOL_SPIN(Game_Status):
    """
    노브의 방향을 판정하고 이미지를 바꾼다
    """

    SIGN_CHANGE_THRESHOLD_VALUE : int = int(0)

    if Game_Status['VOL_L_VALUE_CURRENT'] < Game_Status['VOL_L_VALUE_PAST']:
        Game_Status['IMAGE_VOL_L'] = Game_Status['IMAGE_VOL_L_SPIN_LEFT']
    if Game_Status['VOL_L_VALUE_CURRENT'] > Game_Status['VOL_L_VALUE_PAST']:
        Game_Status['IMAGE_VOL_L'] = Game_Status['IMAGE_VOL_L_SPIN_RIGHT']

    if Game_Status['VOL_R_VALUE_CURRENT'] < Game_Status['VOL_R_VALUE_PAST']:
        Game_Status['IMAGE_VOL_R'] = Game_Status['IMAGE_VOL_R_SPIN_LEFT']
    if Game_Status['VOL_R_VALUE_CURRENT'] > Game_Status['VOL_R_VALUE_PAST']:
        Game_Status['IMAGE_VOL_R'] = Game_Status['IMAGE_VOL_R_SPIN_RIGHT']

    if Game_Status['VOL_L_VALUE_CURRENT'] == Game_Status['VOL_L_VALUE_PAST']:
        Game_Status['IMAGE_VOL_L'] = Game_Status['IMAGE_VOL_OFF']
    if Game_Status['VOL_R_VALUE_CURRENT'] == Game_Status['VOL_R_VALUE_PAST']:
        Game_Status['IMAGE_VOL_R'] = Game_Status['IMAGE_VOL_OFF']

    if Game_Status['VOL_L_VALUE_CURRENT'] * Game_Status['VOL_L_VALUE_PAST'] < SIGN_CHANGE_THRESHOLD_VALUE:
        Game_Status['IMAGE_VOL_L_SPIN_PAST'] = Game_Status['IMAGE_VOL_L']
    if Game_Status['VOL_R_VALUE_CURRENT'] * Game_Status['VOL_R_VALUE_PAST'] < SIGN_CHANGE_THRESHOLD_VALUE:
        Game_Status['IMAGE_VOL_R_SPIN_PAST'] = Game_Status['IMAGE_VOL_R']

    return Game_Status['IMAGE_VOL_L'], Game_Status['IMAGE_VOL_R']

def Screen_Blit(Game_Status):
    """
    화면 업데이트 하는 함수.
    이 함수를 실행함으로서, 화면이 업데이트되고, 이미지와 텍스트가 화면에 업데이트된다.\n
    screen.blit(image,(x,y))
    """
    Game_Status['Screen'].blit(Game_Status['IMAGE_KEY_START'],(604,157))
    Game_Status['Screen'].blit(Game_Status['IMAGE_BT_A'],(365,310))
    Game_Status['Screen'].blit(Game_Status['IMAGE_BT_B'],(515,310))
    Game_Status['Screen'].blit(Game_Status['IMAGE_BT_C'],(665,310))
    Game_Status['Screen'].blit(Game_Status['IMAGE_BT_D'],(815,310))
    Game_Status['Screen'].blit(Game_Status['IMAGE_FX_L'],(440,490))
    Game_Status['Screen'].blit(Game_Status['IMAGE_FX_R'],(740,490))
    Game_Status['Screen'].blit(Game_Status['IMAGE_VOL_L'],(215,140))
    Game_Status['Screen'].blit(Game_Status['IMAGE_VOL_R'],(965,140))
    pygame.display.update()

def main():

    Game_Status = Initialize()

    while Game_Status['Is_Game_Running']:

        Game_Status['VOL_L_VALUE_CURRENT'] =  Game_Status['JOYSTICK'].get_axis(0)
        Game_Status['VOL_R_VALUE_CURRENT'] =  Game_Status['JOYSTICK'].get_axis(1)
        ################이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Status['Is_Game_Running'] = False
            if event.type == pygame.JOYBUTTONDOWN:
                Game_Status['IMAGE_KEY_START'], Game_Status['IMAGE_BT_A'], Game_Status['IMAGE_BT_B'], Game_Status['IMAGE_BT_C'], Game_Status['IMAGE_BT_D'], Game_Status['IMAGE_FX_L'], Game_Status['IMAGE_FX_R'] = KEY_DOWN(Game_Status,event)
            if event.type == pygame.JOYBUTTONUP:
                Game_Status['IMAGE_KEY_START'], Game_Status['IMAGE_BT_A'], Game_Status['IMAGE_BT_B'], Game_Status['IMAGE_BT_C'], Game_Status['IMAGE_BT_D'], Game_Status['IMAGE_FX_L'], Game_Status['IMAGE_FX_R'] = KEY_UP(Game_Status,event)
        Game_Status['IMAGE_VOL_L'], Game_Status['IMAGE_VOL_R'] = VOL_SPIN(Game_Status)
        ################

        Screen_Blit(Game_Status)

        Game_Status['VOL_L_VALUE_PAST'] = Game_Status['VOL_L_VALUE_CURRENT']
        Game_Status['VOL_R_VALUE_PAST'] = Game_Status['VOL_R_VALUE_CURRENT']

        Game_Status['CLOCK'].tick(FPS)

main()

pygame.joystick.quit()
pygame.quit()