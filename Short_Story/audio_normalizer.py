from pydub import AudioSegment
from pydub.playback import play

def normalize_audio(file_path, target_dBFS=-10.0):
    # Load the audio file
    audio = AudioSegment.from_file(file_path, format="mp3")
    
    # Calculate the current dBFS value
    change_in_dBFS = target_dBFS - audio.dBFS
    
    # Normalize the volume
    normalized_audio = audio.apply_gain(change_in_dBFS)
    
    # Save the result (change the filename as you wish)
    normalized_audio.export(file_path, format="mp3")

# Example of function usage
for i in range(1,15):
    filename = f'{i}_OzTheWiz_British.mp3'
    normalize_audio(filename)
