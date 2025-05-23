import pygame
from cfg import *

# Sound effect constants
SOUND_ZOMBIE = 'zombie_ambient'
SOUND_MENU = 'menu_music'
SOUND_VICTORY = 'victory'
SOUND_WALKING = 'walking'
SOUND_SUSPENSE = 'suspense'
SOUND_DEATH = 'death'

# Global sound objects
sounds = {}
current_music = None

def load_sounds():
    """Load all game sounds"""
    global sounds
    
    # Load sound effects
    sounds[SOUND_ZOMBIE] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'zombie_ambient.wav'))
    sounds[SOUND_MENU] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'menu_music.wav'))
    sounds[SOUND_VICTORY] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'victory.wav'))
    sounds[SOUND_WALKING] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'walking.wav'))
    sounds[SOUND_SUSPENSE] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'suspense.wav'))
    sounds[SOUND_DEATH] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'death.wav'))
    
    # Set volumes
    sounds[SOUND_ZOMBIE].set_volume(0.3)
    sounds[SOUND_MENU].set_volume(0.4)
    sounds[SOUND_VICTORY].set_volume(0.5)
    sounds[SOUND_WALKING].set_volume(0.2)
    sounds[SOUND_SUSPENSE].set_volume(0.4)
    sounds[SOUND_DEATH].set_volume(0.5)

def play_sound(sound_name, loops=0):
    """Play a sound effect"""
    if sound_name in sounds:
        sounds[sound_name].play(loops)

def stop_sound(sound_name):
    """Stop a specific sound effect"""
    if sound_name in sounds:
        sounds[sound_name].stop()

def stop_all_sounds():
    """Stop all currently playing sounds"""
    for sound in sounds.values():
        sound.stop()

def play_music(music_name):
    """Play background music"""
    global current_music
    if current_music:
        pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(SONS_DIR, f'{music_name}.wav'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    current_music = music_name

def stop_music():
    """Stop background music"""
    pygame.mixer.music.stop()
    global current_music
    current_music = None 