import insta_download 
import urllib.request

myimg = insta_download.get_img_url()

if myimg['img']:
    num = 0
    imgs = list(set(myimg['img']))
    print(f"총 {len(imgs)}개의 이미지")

    for img in imgs:
        urllib.request.urlretrieve(img,'save_insta_image'+str(num)+'.png')
        num += 1
        print(f"{num}/{len(imgs)}")
if myimg['video']:
    num = 0
    videos = list(set(myimg['video']))
    print(f"총 {len(videos)}개의 동영상 수집")

    for video in videos:
        urllib.request.urlretrieve(video,'save_insta_video'+str(num)+'.mp4')
        num += 1
        print(f"{num}/{len(videos)}")
print('저장성공')