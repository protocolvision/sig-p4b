# Kickoff film score

The score for the kickoff film (`kickoffslides08102026/film.html`), rendered offline in the browser and mastered with ffmpeg.

- `score.html`: the composition and the synthesis. 100 bpm in D major, so every scene change in the film lands on a beat (the end card at 81.6 s is the downbeat of the final chord). It checks its own harmony: chord tones on strong beats, notes in the key on weak ones.
- `grab.mjs`: renders `score.html` in headless Chrome and saves a WAV. Serve this folder first (`python3 -m http.server 8745` here), then `SPDIR=/tmp node grab.mjs http://127.0.0.1:8745/score.html raw.wav`.
- `measure.py raw.wav`: loudness, true peak, energy per frequency band and the loudness of each section.

Master and encode (two-pass loudness normalization to −16 LUFS, true peak under −1.5 dB):

    ffmpeg -i raw.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -    # note the measured values
    ffmpeg -i raw.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=…:measured_TP=…:measured_LRA=…:measured_thresh=…:offset=…:linear=true -c:a pcm_s24le master.wav
    ffmpeg -i master.wav -c:a aac -b:a 160k -movflags +faststart ../../kickoffslides08102026/kickoff-score.m4a
    ffmpeg -i master.wav -c:a libmp3lame -q:a 2 ../../kickoffslides08102026/kickoff-score.mp3

If the film's timeline changes, update the scene times (`S`) at the top of `score.html` to match the `SC` list in `film.html`.
