import vlc
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #numbering scheme

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#playlist of songs
plist = ['howLong.mp3', 'godIsAWoman.mp3', 'tillTheWorldEnds.mp3']
songIndex = 0
playlistLength = len(plist)

#play the first song
player = vlc.MediaPlayer(plist[0])
player.audio_set_volume(60)
player.play()

play = True

def volume_up():
    #raise volume
    #time.sleep(5)
    #if already at max volume, do nothing
    if (player.audio_get_volume() < 100):
        player.audio_set_volume(player.audio_get_volume() + 20)
            
def volume_down():
    #lower volume
    #time.sleep(5)
    #if already at min volume, do nothing
    if (player.audio_get_volume() > 0):
        player.audio_set_volume(player.audio_get_volume() - 20)

def play_pause():
    #turn off
    if(play):
        player.pause()
        play = False
    else:
        player.play()
        play = True
            

GPIO.add_event_detect(22, GPIO.FALLING, callback=volume_up)
GPIO.add_event_detect(27, GPIO.FALLING, callback=volume_down)
GPIO.add_event_detect(17, GPIO.FALLING, callback=play_pause)



#infinite loop
while (True):
    
    #get integer for gesture detected
    #from cameraTest import gesture

    #gesture = GPIO.input(17)
    #gesture_2 = GPIO.input(22)
    #gesture_3 = GPIO.input(27)
    #gesture_4 = GPIO.input(23)
    
    
    #pause/play song
    #time.sleep(5)
    """if (gesture == False):
        player.pause()
        
    #go to next song in playlist
    elif (gesture_4 == True):
        time.sleep(5)
        #if at last song in playlist, go to beginning
        if (songIndex == playlistLength - 1):
            currentVol = player.audio_get_volume()
            player.pause()
            player = vlc.MediaPlayer(plist[0])
            player.audio_set_volume(currentVol)
            player.play()
            songIndex = 0
        else:
            currentVol = player.audio_get_volume()
            player.pause()
            player = vlc.MediaPlayer(plist[songIndex + 1])
            player.audio_set_volume(currentVol)
            player.play()
            songIndex = songIndex + 1
    
    else:
        pass"""