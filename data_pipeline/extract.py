import os
from typing import Optional
from youtube_utils import get_list_of_videos_from_channel
import pandas as pd


CHANNEL_URL_FIELD = 'Channel Link'
TAGS_FIELD = 'Description'
CHANNEL_NAME_FIELD = 'Channel Name'


def dump_channels_data(audio_book_csv_url: str, output_csv_dir: Optional[str] = None) -> None:
    channel_data = pd.read_csv(audio_book_csv_url)

    channel_names = channel_data[CHANNEL_NAME_FIELD].map(str.strip).tolist()
    channel_stat_ls = []
    for channel in channel_names:
        
        # path to store information
        if output_csv_dir:
            output_csv_path = os.path.join(output_csv_dir, f'{channel}.csv')
        else:
            output_csv_path = f'{channel}.csv'

        # skip channel if already in the data dump
        if not os.path.exists(output_csv_path):
            
            # extract information
            audio_ls, total_duration = get_list_of_videos_from_channel(channel)
            
            # save information
            audio_df = pd.DataFrame(audio_ls, columns=['id', 'title', 'duration[minutes]', 'channel_name'])
            audio_df.to_csv(output_csv_path, index=False)

            print(f"Channel: {channel},\
                    \n\tTotal Duration: {total_duration//60} hours,\
                    \n\tAudio Count: {len(audio_ls)},\
                    \n\tAvg Duration: {audio_df['duration[minutes]'].mean()}\
                    \n\tMedian Duration: {audio_df['duration[minutes]'].median()}")
            
            channel_stat_ls.append((channel, total_duration//60, len(audio_ls), audio_df['duration[minutes]'].mean(), audio_df['duration[minutes]'].median()))
        
        channel_stat_df = pd.DataFrame(channel_stat_ls, columns=['Channel', 'Total Duration', 'Audio Count', 'Avg Duration', 'Median Duration'])

        if output_csv_dir:
            channel_csv_path = os.path.join(output_csv_dir, 'stats.csv')
        else:
            channel_csv_path = 'stats.csv'
        
        channel_stat_df.to_csv(channel_csv_path)