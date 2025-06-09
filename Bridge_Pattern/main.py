from remote_control import RemoteControl
from devices.TV import TV
from devices.Radio import Radio
from devices.Projector import Projector


tv = TV
radio = Radio
projector = Projector

remote_control = RemoteControl(tv)
remote_control.volume_up()

remote_control = RemoteControl(radio)
remote_control.set_channel('channel2')

remote_control = RemoteControl(Projector)
remote_control.turn_off()