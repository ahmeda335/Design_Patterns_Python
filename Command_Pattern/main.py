from devices import *
from commands import *
from controller import RemoteControl


light = Light()
music_player = Music()
garage = Garage()

light_on = LightONCommand(light)
light_off = LightOFFCommand(light)

play_music = MusicONCommand(music_player)
stop_music = MusicOFFCommand(music_player)

open_garage = GarageOpenCommand(garage)
close_garage = GarageCloseCommand(garage)


remote = RemoteControl()
remote.set_command("button1", light_on)
remote.set_command("button2", light_off)
remote.set_command("button3", play_music)
remote.set_command("button4", stop_music)
remote.set_command("button5", open_garage)
remote.set_command("button6", close_garage)


remote.press("button1")  # Turns on the light
remote.press("button3")  # Plays music
remote.press("button5")  # Opens garage

remote.display_last_command()
