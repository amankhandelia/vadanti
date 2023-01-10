from typing import List, Tuple
from yt_dlp import YoutubeDL


OPTIONS = {
    'outtmpl': '%(id)s.%(ext)s',
    'source_address': '0.0.0.0',
    'dumpjson': True,
    'extract_flat': 'in_playlist',
    'useid': True
}


def get_list_of_videos_from_channel(channel_name: str) -> Tuple[List[Tuple[str, str, str]], int]:

    channel_path = f"https://www.youtube.com/@{channel_name}/videos"

    ydl = YoutubeDL(OPTIONS)

    with ydl:
        result = ydl.extract_info(
            channel_path,
            download=False  # just want to extract the info
        )
    audio_ls = []
    total_duration = 0
    for entry in result['entries']:
        total_duration += entry['duration']//60
        audio_ls.append((entry['id'], entry['title'], entry['duration']//60, channel_name))
    
    return audio_ls, total_duration