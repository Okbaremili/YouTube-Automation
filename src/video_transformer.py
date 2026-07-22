import os
import random
import subprocess
import sys

class VideoTransformer:
    def __init__(self):
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)

    def drastically_transform(self, input_path):
        try:
            print("🎨 تغيير الفيديو تغييراً جذرياً...")
            temp1 = self._apply_visual_effects(input_path)
            if not temp1:
                return None
            temp2 = self._apply_audio_effects(temp1)
            if not temp2:
                return None
            final_path = self._add_text_overlay(temp2)
            if final_path:
                print("✅ تم تغيير الفيديو بنجاح")
            return final_path
        except Exception as e:
            print(f"❌ فشل التحويل: {e}")
            return None

    def _apply_visual_effects(self, input_path):
        output_path = f"{self.output_dir}/visual_effects.mp4"
        try:
            speed = random.uniform(0.7, 1.8)
            color_filters = [
                f'colorbalance=rs={random.uniform(0.1, 0.3)}:gs={random.uniform(0.1, 0.2)}:bs={random.uniform(0.1, 0.2)}',
                f'colorchannelmixer=rr={random.uniform(0.7, 0.9)}:rg={random.uniform(0.1, 0.2)}:rb={random.uniform(0.05, 0.15)}',
                f'hue=h={random.randint(10, 50)}:s={random.uniform(1.1, 1.4)}',
                'curves=preset=filmstock'
            ]
            selected_filter = random.choice(color_filters)
            zoom = f'zoompan=z=1.0+0.01*sin(2*PI*time/{random.randint(3, 8)}):x=iw/2:y=ih/2:d=5'
            noise = f'noise=alls={random.randint(2, 6)}'
            scale = 'scale=1920:1080:flags=lanczos'
            video_filter = f"{scale},{zoom},{selected_filter},{noise}"
            cmd = ['ffmpeg', '-i', input_path, '-vf', video_filter, '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-y', output_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and os.path.exists(output_path):
                return output_path
        except Exception as e:
            print(f"Visual effects error: {e}")
        return None

    def _apply_audio_effects(self, input_path):
        output_path = f"{self.output_dir}/audio_effects.mp4"
        try:
            speed = random.uniform(0.8, 1.5)
            pitch = random.uniform(0.9, 1.3)
            audio_effects = [f'atempo={speed}', f'asetrate=44100*{pitch}']
            if random.random() > 0.5:
                audio_effects.append('aecho=0.8:0.9:1000:0.3')
            audio_filter = ','.join(audio_effects)
            cmd = ['ffmpeg', '-i', input_path, '-af', audio_filter, '-c:v', 'copy', '-y', output_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and os.path.exists(output_path):
                return output_path
        except Exception as e:
            print(f"Audio effects error: {e}")
        return None

    def _add_text_overlay(self, input_path):
        output_path = f"{self.output_dir}/final_transformed.mp4"
        try:
            texts = ["حقيقة مذهلة ✨", "هل تعلم؟ 🤔", "قصة مثيرة 📖", "معلومات جديدة 💡", "شاهد المزيد 👀"]
            selected_text = random.choice(texts)
            cmd = ['ffmpeg', '-i', input_path, '-vf', f"drawtext=text='{selected_text}':fontsize=50:fontcolor=white:x=W/2:y=H-100:shadowcolor=black:shadowx=3:shadowy=3", '-c:a', 'copy', '-y', output_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and os.path.exists(output_path):
                return output_path
        except Exception as e:
            print(f"Text overlay error: {e}")
        return None