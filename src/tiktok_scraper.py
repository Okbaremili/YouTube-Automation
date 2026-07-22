import os
import random
import time
import json
import hashlib
import yt_dlp

class TikTokScraper:
    def __init__(self):
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.niche_hashtags = [
            'historyfacts', 'unknownfacts', 'weirdhistory',
            'ancientmysteries', 'forgottenstories', 'unexplained',
            'strangeevents', 'oddlysatisfying', 'mindblowingfacts',
            'historicalsecrets', 'amazingdiscoveries', 'lostatsea',
            'hiddenhistory', 'mysteriousplaces', 'forbiddenknowledge'
        ]
        
        self.used_file = 'used_videos.json'
        self.used_videos = self._load_used_videos()

    def _load_used_videos(self):
        if os.path.exists(self.used_file):
            try:
                with open(self.used_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _save_used_videos(self):
        with open(self.used_file, 'w') as f:
            json.dump(self.used_videos, f)

    def _get_video_hash(self, video_url):
        return hashlib.md5(video_url.encode()).hexdigest()

    def _is_video_used(self, video_url):
        video_hash = self._get_video_hash(video_url)
        return video_hash in self.used_videos

    def _mark_video_as_used(self, video_url):
        video_hash = self._get_video_hash(video_url)
        self.used_videos.append(video_hash)
        self._save_used_videos()

    def search_tiktok_video(self, hashtag):
        try:
            print(f"🔍 البحث عن فيديو في: #{hashtag}")
            ydl_opts = {
                'quiet': True,
                'extract_flat': True,
                'format': 'best',
                'headers': {'User-Agent': 'Mozilla/5.0'}
            }
            search_url = f"https://www.tiktok.com/tag/{hashtag}"
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(search_url, download=False)
                videos = info.get('entries', [])
                if not videos:
                    return None
                for video in videos:
                    view_count = video.get('view_count', 0)
                    if view_count < 50000 and view_count > 1000:
                        return video.get('url')
                video = random.choice(videos)
                return video.get('url')
        except Exception as e:
            print(f"⚠️ فشل البحث: {e}")
        return None

    def get_random_video_url(self, max_attempts=15):
        for attempt in range(max_attempts):
            print(f"🔄 محاولة {attempt+1}/{max_attempts}...")
            hashtag = random.choice(self.niche_hashtags)
            video_url = self.search_tiktok_video(hashtag)
            if video_url and not self._is_video_used(video_url):
                self._mark_video_as_used(video_url)
                print(f"✅ تم العثور على فيديو جديد")
                return video_url
            time.sleep(random.uniform(2, 5))
        print("❌ لم نتمكن من العثور على فيديو جديد")
        return None

    def download_video(self, video_url):
        try:
            print(f"📥 تحميل فيديو...")
            output_path = f"{self.output_dir}/downloaded_video.mp4"
            ydl_opts = {
                'outtmpl': output_path,
                'quiet': True,
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'headers': {'User-Agent': 'Mozilla/5.0'}
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                print(f"✅ تم التحميل")
                return output_path
        except Exception as e:
            print(f"❌ فشل التحميل: {e}")
        return None