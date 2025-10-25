from flask import Flask, request, send_file
import requests
import tempfile

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "ضع رابط الفيديو", 400

    # مثال: رابط فيديو تجريبي
    video_url = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"

    response = requests.get(video_url)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tmp_file.write(response.content)
    tmp_file.close()

    return send_file(tmp_file.name, as_attachment=True, download_name="video.mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
