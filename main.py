import sys
import pygame
from pygame.sprite import Group
import game_function as gf
from setting import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from sourceboard import Sourceboard

def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')
    circulation = False if len(sys.argv) > 1 else True
    
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    
    ship = Ship(screen, ai_setting)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_setting)
    play_button = Button(ai_setting, screen, 'Play')
    sb = Sourceboard(ai_setting, screen, stats)
    
    gf.create_fleet(ai_setting, screen, aliens, ship)
    
    while True:
        gf.check_events(ai_setting, screen, ship, bullets, aliens, stats, play_button, sb)
        if stats.game_active:
            gf.update_bullets(bullets, ai_setting, screen, aliens, ship, stats, sb)
            gf.update_aliens(ai_setting, stats, screen, aliens, ship, bullets, sb)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets, stats, play_button, sb)
        if not circulation:
            break
# This is a study case
run_game()
run_game()
run_game()