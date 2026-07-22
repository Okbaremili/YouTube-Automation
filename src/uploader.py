import os
import googleapiclient.discovery
import googleapiclient.http
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

class YouTubeUploader:
    def __init__(self):
        self.client_id = os.environ.get("YOUTUBE_CLIENT_ID")
        self.client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
        self.refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")

    def get_authenticated_service(self):
        creds = Credentials(
            None,
            refresh_token=self.refresh_token,
            client_id=self.client_id,
            client_secret=self.client_secret,
            token_uri="https://oauth2.googleapis.com/token",
        )
        return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    def upload_video(self, video_path, title, description):
        try:
            print("📤 رفع الفيديو إلى YouTube...")
            youtube = self.get_authenticated_service()
            body = {
                "snippet": {
                    "title": title[:95],
                    "description": description[:5000],
                    "tags": ["shorts", "facts", "tiktok"],
                    "categoryId": "22",
                },
                "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False},
            }
            media = googleapiclient.http.MediaFileUpload(video_path, chunksize=10*1024*1024, resumable=True, mimetype="video/mp4")
            request = youtube.videos().insert(part=",".join(body.keys()), body=body, media_body=media)
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    print(f"📤 الرفع: {int(status.progress() * 100)}%")
            print(f"✅ تم الرفع بنجاح! Video ID: {response['id']}")
            return response["id"]
        except Exception as e:
            print(f"❌ خطأ في الرفع: {e}")
            return None