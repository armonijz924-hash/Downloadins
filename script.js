function downloadVideo() {
    const url = document.getElementById('url').value;
    const msg = document.getElementById('msg');
    msg.textContent = '';

    if (!url) {
        msg.textContent = "ضع رابط الفيديو أولاً!";
        return;
    }

    fetch(`/download?url=${encodeURIComponent(url)}`)
    .then(response => {
        if (response.ok) return response.blob();
        throw new Error("فشل تحميل الفيديو");
    })
    .then(blob => {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'video.mp4';
        document.body.appendChild(link);
        link.click();
        link.remove();
    })
    .catch(err => msg.textContent = err.message);
}
