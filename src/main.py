from src.database import SongDatabase
from src.recognize import recognize
from src.utils import load_audio

# Index songs
db = SongDatabase()
db.index_directory("songs/")

# Recognize a clip
audio, sr = load_audio("songs/rock_power.wav")
clip = audio[int(3 * sr):int(8 * sr)]  # 5-second clip
name, score, scores = recognize(clip, sr, db)
print(f"Match: {name} (score: {score})")
print(f"Hash table stats: {db.table.stats()}")