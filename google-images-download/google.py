from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"갤럭시,아이폰","limit":20,"print_urls":True}

paths = response.download(arguments)
print(paths)