import os
import pathlib

work_dir = "{YOUR_PATH_HERE}"

filtered = filter(os.path.isfile, os.scandir(work_dir))

image_types             = [".jpg", ".gif", ".png", ".jpeg", "jfif"  ]
video_types             = [".mp4"                                   ]
music_types             = [".mp3", ".opus"                          ]
compressed_types        = [".rar", ".zip", ".7z"                    ]
pdf_types               = [".pdf"                                   ]
document_types          = [".docx"                                  ]
executable_types        = [".exe"                                   ]
object_type             = [".stl"                                   ]

image_destination       = "/IMAGES/"
video_destination       = "/VIDEOS/"
music_destination       = "/MUSIC/"
compressed_destination  = "/COMPRESSED/"
pdf_destination         = "/PDF/"
document_destination    = "/DOCS/"
executable_destination  = "/PROGRAMS/"
object_destination      = "/3D/"

class File:
    def __init__(self, destination, extension):
        self.destination = destination
        self.extension = extension

managed_files = [
    File(image_destination,         image_types         ),
    File(video_destination,         video_types         ),
    File(music_destination,         music_types         ),
    File(compressed_destination,    compressed_types    ),
    File(pdf_destination,           pdf_types           ),
    File(document_destination,      document_types      ),
    File(executable_destination,    executable_types    ),
    File(object_destination,        object_type         )
]

directories = (file.destination for file in managed_files)

for directory in directories:
    try:
        images_dir = os.mkdir(work_dir + directory)
    except:
        print("Dir " + directory + "already exists")

def moveFile(file, dir):
    print("Moving file: " + os.path.basename(file))
    os.rename(
        os.path.realpath(file),
        os.path.dirname(file) + dir + os.path.basename(file)
    )

for file in filtered:

    file_extension = pathlib.Path(file.path).suffix

    for file_type in managed_files:
        if(file_extension.lower() in file_type.extension):
            moveFile(file, file_type.destination)
        else:
            print("Can't classify this filetype: " + file_extension)
