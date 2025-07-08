from datetime import datetime

print(datetime.now())

timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
print(timestamp)


# file_name = 'subtitle-' + timestamp + '.srt'
file_name = f'subtitle-{timestamp}.srt'
print(file_name)