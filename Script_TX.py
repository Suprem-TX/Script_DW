import os as _0, sys as _1, subprocess as _2
def _3(_4, _5='./'):
    import yt_dlp as _6
    _7 = {'format': 'mp4', 'outtmpl': f'{_5}%(title)s.%(ext)s'}
    with _6.YoutubeDL(_7) as _8:
        _8.download([_4])
if __name__ == "__main__":
    import base64 as _9
    _a = _9.b64decode("YnlTdXByZW0tVFg==").decode("utf-8")
    print(_a)
    
    _b = input("Introduce la URL: ")
    _3(_b)
