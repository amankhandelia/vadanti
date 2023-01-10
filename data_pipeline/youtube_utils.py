from typing import List
from yt_dlp import YoutubeDL


OPTIONS = {
    'outtmpl': '%(id)s.%(ext)s',
    'source_address': '0.0.0.0',
    'dumpjson': True,
    'extract_flat': 'in_playlist',
    'useid': True
}


def get_list_of_videos_from_channel(channel_name: str) -> List:

    channel_path = f"https://www.youtube.com/@{channel_name}/videos"

    ydl = YoutubeDL(OPTIONS)

    with ydl:
        result = ydl.extract_info(
            channel_path,
            download=False  # just want to extract the info
        )
    return result


channel_name = 'dummy_name'
result = get_list_of_videos_from_channel(channel_name)
