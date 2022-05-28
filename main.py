from scipy.fft import rfft
from scipy.io.wavfile import read
import pygame, time

Count = 18  # Count of columns for vis
DURATION = 0.05  # Timespan for number of Samples that are regarded

file_name = ""      # Add path to wav-file
samplerate, data = read(file_name)
print(samplerate, data)

frame_rate, amplitude = read(file_name)
amplitude = amplitude[:, 0] + amplitude[:, 1]

N = int(samplerate * DURATION)  # Count of samples for rfft
frequency_delta = int(N / (32 * Count))

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
time.sleep(1)
pygame.mixer.music.load(file_name)
pygame.mixer.music.play()
now = time.time()

for i in range(0, int(data.shape[0] / samplerate / DURATION)):
    yf = rfft(amplitude[(i * N):(i * N + N)])

    screen.fill([0, 0, 0])

    for i in range(0, Count):
        pygame.draw.rect(screen,
                         (0, 255, 0),
                         [32,
                          (35 + i * 50),
                          int(max(abs(yf[i * frequency_delta:i * frequency_delta + frequency_delta])) / 4096),
                          32],
                         0)

    pygame.display.flip()
    # print(time.time()-now) # Print Time that is needed for displaying, baking and calculate
    now = now + DURATION
    while time.time() < now:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
