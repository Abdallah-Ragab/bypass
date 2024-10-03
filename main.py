import time
import pyautogui
import boto3
import ocr

name= "abdallah"
files_dir = "files"    

class S3Client:
    
    bucket_name = 'team'
    def __init__(self):
        self.client = boto3.client(
            service_name='s3',
            aws_access_key_id='kPJksm5XCdn7Cx5A',
            aws_secret_access_key='22nSeXNhQ7BfWnJIQOWPa1aTTvR5kEHXLKFWz8aB',
            endpoint_url='https://s3.tebi.io'
        )

    def upload_file(self, file_path, key):
        # self.bucket.upload_file(Filename=file_path, Key=file_path)
        self.client.upload_file(key, self.bucket_name, file_path)


def screenshot():
    """Take a screenshot of the primary display."""
    return pyautogui.screenshot()

def save_screenshot(img, path):
    """Save a screenshot to a file."""
    img.save(path)

s3_client = S3Client()
def callback(bytes_transferred):
    total_bytes = img.size[0] * img.size[1] * 3
    print(f"{bytes_transferred / total_bytes * 100:.2f}% uploaded")

while True:
    print("Taking screenshot...")
    img = screenshot()
    now = str(int(time.time()))
    object_key = now
    image_file_name = f"{now}.png"
    text_file_name = f"{now}.txt"

    image_path = f"{files_dir}/{image_file_name}"
    txt_path = f"{files_dir}/{text_file_name}"
    
    save_screenshot(img, image_path)
    
    print("Getting text from image...")
    text = ocr.read_image(image_path)
    text = f'{name} \n {text}'
    
    ocr.save_to_txt(text, txt_path)
    
    print("Uploading image file ...")
    s3_client.upload_file(image_file_name, image_path)
    
    print("Uploading text file ...")
    s3_client.upload_file(text_file_name, txt_path)
    
    print("Done!")
    time.sleep(30)