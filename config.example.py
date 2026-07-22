"""Configuration template for YouTube Automation"""

# TikTok Scraper Configuration
TIKTOK_CONFIG = {
    'hashtags': [
        'historyfacts',
        'unknownfacts',
        'weirdhistory',
        'ancientmysteries',
        'forgottenstories',
        'unexplained',
        'strangeevents',
        'oddlysatisfying',
        'mindblowingfacts',
        'historicalsecrets',
        'amazingdiscoveries',
        'lostatsea',
        'hiddenhistory',
        'mysteriousplaces',
        'forbiddenknowledge'
    ],
    'min_view_count': 1000,
    'max_view_count': 50000,
    'max_attempts': 15,
    'search_delay_min': 2,
    'search_delay_max': 5,
}

# Video Transformer Configuration
VIDEO_TRANSFORMER_CONFIG = {
    'resolution': '1920:1080',
    'codec': 'libx264',
    'quality': 18,
    'preset': 'slow',
    'video_speed_min': 0.7,
    'video_speed_max': 1.8,
    'audio_speed_min': 0.8,
    'audio_speed_max': 1.5,
    'audio_pitch_min': 0.9,
    'audio_pitch_max': 1.3,
}

# YouTube Upload Configuration
YOUTUBE_CONFIG = {
    'category_id': '22',  # Shorts category
    'privacy_status': 'public',
    'made_for_kids': False,
    'tags': ['shorts', 'facts', 'tiktok', 'viral'],
    'title_max_length': 95,
    'description_max_length': 5000,
}

# Output Configuration
OUTPUT_CONFIG = {
    'output_dir': 'output',
    'cleanup_temp_files': True,
    'used_videos_file': 'used_videos.json',
}