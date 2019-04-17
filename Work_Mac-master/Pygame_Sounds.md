# Pygame Sounds 

Video games are are meant to put the player into a virtual reality. It is done mainly visiually, 
but it makes a massive differnece if we put it sound effects in the game. 

### Music and Sound

Video games generally incoproate music in two ways: **Music** and **Sound** Which is backgound music for the game 
or a sound as result of the players actions. 

Music = Background songs
Sound = Sound Effects

Music will just play in the background when you call it to, and sounds will play at any time you call them to play.

## MUSIC

### Play a song once:

```
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)

```

### Play a song infinitely: 

```
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)

```
The number in between the paraenthesis is the number of times you want it to repeat. The above code will play the music
file indefinitely (though you can call it to stop). The -1 signals PyGame to just play forever, but, if you put, say, 
a 5 in there, then the music would play once and 5 more times.

### Queuing a song:

```
pygame.mixer.music.queue('next_song.mp3')
```

## SOUND

```
effect = pygame.mixer.Sound('beep.wav')
effect.play()
```
.....more to come on Thursday 




