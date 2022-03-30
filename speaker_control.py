import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

#playlist of songs
plist = ['howLong.mp3', 'godIsAWoman.mp3', 'tillTheWorldEnds.mp3']
songIndex = 0
playlistLength = len(plist)

#play the first song
player = vlc.MediaPlayer(plist[0])
player.audio_set_volume(40)
player.play()


#infinite loop
while (True):
    
    #get integer for gesture detected
    from cameraTest import gesture
    
    
    #pause/play song
    #time.sleep(5)
    if (gesture == 1):
        player.pause()
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        time.sleep(2)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        
    #raise volume
    elif (gesture == 2):
        time.sleep(5)
        
        #if already at max volume, do nothing
        if (player.audio_get_volume() < 100):
            player.audio_set_volume(player.audio_get_volume() + 20)
            GPIO.output(4,GPIO.HIGH)
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
            time.sleep(2)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
            
    #lower volume
    elif (gesture == 3):
        #time.sleep(5)
        #if already at min volume, do nothing
        if (player.audio_get_volume() > 0):
            player.audio_set_volume(player.audio_get_volume() - 20)
            GPIO.output(5,GPIO.HIGH)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
            time.sleep(2)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
            
    #go to next song in playlist
    elif (gesture == 4):
        time.sleep(5)
        #if at last song in playlist, go to beginning
        if (songIndex == playlistLength - 1):
            currentVol = player.audio_get_volume()
            player.pause()
            player = vlc.MediaPlayer(plist[0])
            player.audio_set_volume(currentVol)
            player.play()
            songIndex = 0
            GPIO.output(5,GPIO.HIGH)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(6,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
        else:
            currentVol = player.audio_get_volume()
            player.pause()
            player = vlc.MediaPlayer(plist[songIndex + 1])
            player.audio_set_volume(currentVol)
            player.play()
            songIndex = songIndex + 1
            GPIO.output(5,GPIO.HIGH)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(6,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(4,GPIO.LOW)
            GPIO.output(5,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)
    
    else:
        pass
    
    
