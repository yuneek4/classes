class MusicLibrary():
    def __init__(self):
        self.genre=''
        self.artist=''
        self.sex=''
        self.total_albums=''
        self.band=''
ipod=MusicLibrary()
ipod.genre='r&B'
ipod.artist='LL Cool J, Melissa Morgan'
ipod.sex='Male,Female'
ipod.total_albums='10'
ipod.band='rock band'

print("My favoride genre on my ipod is", ipod.genre)
print("My favorite artist on my ipod is", ipod.artist)

computer=ipod
computer.genre='old school'
computer.artist='Jeff Red'
computer.sex='Male'
computer.total_albums='5'
computer.band='Meriachi'

print("My favoride genre on my computer is", computer.genre)
print("My favorite artist on my computer is", computer.artist)

mp3player=computer
mp3player.genre='pop'
mp3player.artist='Justin Beiber'
mp3player.sex='Female'
mp3player.total_albums='15'
mp3player.band='rock and role'

print("My favoride genre on my mp3 player is", mp3player.genre)
print("My favorite artist on my mp3 player is", mp3player.artist)

