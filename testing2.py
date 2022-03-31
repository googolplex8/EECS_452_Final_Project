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
player.audio_set_volume(40)
player.play()

go = True

def volume_up(channel):
    print("up")
    #raise volume
    #time.sleep(5)
    #if already at max volume, do nothing
    if (player.audio_get_volume() < 100):
        player.audio_set_volume(player.audio_get_volume() + 20)

def volume_down(channel):
    print("down")
    #lower volume
    #time.sleep(5)
    #if already at min volume, do nothing
    if (player.audio_get_volume() > 0):
        player.audio_set_volume(player.audio_get_volume() - 20)

def play_pause(channel):
    print("pause")
    global go

    #turn off
    if(go):
        player.pause()
        go = False
    else:
        player.play()
        go = True
    


GPIO.add_event_detect(22, GPIO.FALLING, callback=volume_up)
GPIO.add_event_detect(27, GPIO.FALLING, callback=volume_down)
GPIO.add_event_detect(17, GPIO.FALLING, callback=play_pause)



#infinite loop
while (True):
    
    #p17 = GPIO.input(17)
    #p22 = GPIO.input(22)
    #p27 = GPIO.input(27)
    
    #if (p17 != 1):
    #    play_pause()
        
    #elif (p22 != 1):
    #    volume_up()
        
    #elif (p27 != 1):
    #    volume_down()
    
    print(GPIO.input(17))
    #print(GPIO.input(22))
    #print(GPIO.input(27))
    
    #get integer for gesture detected
    #from cameraTest import gesture
    #gesture = GPIO.input(17)
    #print(gesture)
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