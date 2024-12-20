import cv2
from tqdm import tqdm
from PIL import Image


def Video2Hex(
    videoname: str, filename: str, height: int = 64, width: int = 128
) -> None:
    cap = cv2.VideoCapture(videoname)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    ret, frame = cap.read()
    if not ret:
        print("End of video or error occurred.")
        exit()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    try:
        with open(filename, "ab") as f:
            for _ in tqdm(range(total_frames)):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                resized = cv2.resize(
                    gray, (width, height), interpolation=cv2.INTER_AREA
                )

                image = Image.fromarray(resized)
                hres = b""
                for k in range(height // 8):
                    for x in range(width):
                        res = ""
                        for y in range(8):
                            pixel = image.getpixel((x, 8 * k + y))
                            # 将像素值转换为1或0
                            res = "1" + res if pixel > 128 else "0" + res
                        temp = "{:02x}".format(int(res, 2))
                        hres += bytes.fromhex(temp)
                    f.write(hres)
                    f.write(b"\n")
    except Exception as e:
        print(f"Error: {e}")
        exit()
    finally:
        cap.release()
        f.close()


if __name__ == "__main__":
    video_name = "badapple.mp4"
    output_filename = "output.hex"
    Video2Hex(video_name, output_filename)
