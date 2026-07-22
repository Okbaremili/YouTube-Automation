#!/usr/bin/env python3
"""Main orchestration script for TikTok to YouTube automation"""
import os
import sys
from src.tiktok_scraper import TikTokScraper
from src.video_transformer import VideoTransformer
from src.uploader import YouTubeUploader

os.makedirs("output", exist_ok=True)

def main():
    try:
        print("\n" + "="*50)
        print("🎬 TikTok to YouTube - Video Repurposer v1.0")
        print("="*50 + "\n")
        
        # Step 1: Scrape TikTok
        print("[1/4] Starting TikTok video search...")
        scraper = TikTokScraper()
        video_url = scraper.get_random_video_url()
        if not video_url:
            print("❌ Failed to find a video")
            return False
        print(f"✅ Found video: {video_url}\n")
        
        # Step 2: Download video
        print("[2/4] Downloading video...")
        downloaded_path = scraper.download_video(video_url)
        if not downloaded_path:
            print("❌ Failed to download video")
            return False
        print(f"✅ Video downloaded to: {downloaded_path}\n")
        
        # Step 3: Transform video
        print("[3/4] Transforming video with effects...")
        transformer = VideoTransformer()
        transformed_path = transformer.drastically_transform(downloaded_path)
        if not transformed_path:
            print("❌ Failed to transform video")
            return False
        print(f"✅ Video transformed: {transformed_path}\n")
        
        # Step 4: Upload to YouTube
        print("[4/4] Uploading to YouTube...")
        uploader = YouTubeUploader()
        video_id = uploader.upload_video(
            video_path=transformed_path,
            title="فيديو مذهل | #shorts",
            description="فيديو مذهل\n\n#shorts #facts #interesting #tiktok"
        )
        
        if video_id:
            print(f"\n" + "="*50)
            print(f"✅ SUCCESS! Video uploaded!")
            print(f"🔗 https://youtube.com/watch?v={video_id}")
            print("="*50 + "\n")
            return True
        else:
            print("❌ Upload failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)