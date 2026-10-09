import subprocess, re, sys
f=sys.argv[1]
out=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',f,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
print(' '.join(re.findall(r'(I:\s+-?[\d.]+ LUFS|LRA:\s+[\d.]+ LU|Peak:\s+-?[\d.]+ dBFS)', out.split('Summary')[-1])))
for n,a,b in [('sub 20-60',20,60),('bass 60-200',60,200),('low-mid 200-500',200,500),('mid 500-2k',500,2000),('presence 2-5k',2000,5000),('air 5-12k',5000,12000)]:
    o=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',f,'-af',f'highpass=f={a},lowpass=f={b},astats=measure_overall=RMS_level:measure_perchannel=0','-f','null','-'],capture_output=True,text=True).stderr
    v=re.findall(r'RMS level dB: (-?[\d.inf]+)',o); print(f'  {n:16s} {float(v[-1]):7.1f} dB')
subprocess.run(['ffmpeg','-hide_banner','-nostats','-y','-i',f,'-af','ebur128=metadata=1,ametadata=print:key=lavfi.r128.M:file=/tmp/claude-501/mom.txt','-f','null','-'],capture_output=True)
t=[float(x) for x in re.findall(r'pts_time:([\d.]+)', open('/tmp/claude-501/mom.txt').read())]; m=[float(x) for x in re.findall(r'lavfi.r128.M=(-?[\d.inf]+)', open('/tmp/claude-501/mom.txt').read())]
print('  arc:', '  '.join(f'{n} {sum(v)/len(v):.1f}' for n,a,b in [('intro',0,13.2),('break',13.2,18),('leak',18,31.2),('hard',31.2,44.4),('warm',44.4,63.6),('join',63.6,81.6),('end',81.6,88)] for v in [[x for tt,x in zip(t,m) if a<=tt<b and x>-70]]))
