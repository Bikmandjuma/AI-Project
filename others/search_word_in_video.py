import moviepy.editor as mp

# Load the video
video = mp.VideoFileClip(r"C:\Users\Khadidja\Downloads\Wildn'out\chain_gang.mp4")

# Search for the word
word_location = video.find("my_word")

# Get the start and end times of the word
start_time = word_location[0][0]
end_time = word_location[0][1]

# Cut the video
video_cut = video.subclip(start_time, end_time)

# Save the video
video_cut.write_videofile(r"C:\Users\Khadidja\Downloads\Wildn'out\chain_gang.mp4")