import pytube;
import threading;
from tkinter.filedialog import askdirectory;

def downloadVideo(video: pytube.YouTube, path):
    videoPath = video.title + '.mp4'
    for i in range(10):
        try:
            video.streams.first().download(path, videoPath)
            break;
        except:
            if (i == 10):
                print(f"script failed downloaing video {video.title} 10 times, LEAVE ME ALONE!");
                return;
    print(f'{video.title} done')


def downloadVideos(videos: [pytube.YouTube], path):
    threads = [];
    for video in videos: 
        threads.append(threading.Thread(target=downloadVideo,args=(video, path)));
        threads[-1].start();
    for t in threads: 
        t.join();

link = input('Put you url\n');
youtubePlaylist = pytube.Playlist(link);
path = askdirectory(title='Select Folder')
downloadVideos(youtubePlaylist.videos, path)
print('done, hope you have a great day')