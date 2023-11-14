from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("recordings/eng/and_it_is.mp3", format="mp3")
play(sound)
sound = AudioSegment.from_file("recordings/eng/oxygen_is.mp3", format="mp3")
play(sound)