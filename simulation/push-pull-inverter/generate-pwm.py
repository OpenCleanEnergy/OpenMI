from math import pi, sin
import os

lineFrequency = 50
samplingFrequency = 200_000
numOfSamples = samplingFrequency // lineFrequency + 1
timesStepMicroSeconds = 1 / samplingFrequency * 1_000_000
edgeTimeMicroSeconds = timesStepMicroSeconds / 1000
maxDutyCycle = 0.9
# print information about the signal
print("Information about the generated signal:")
print(f"  Line frequency:          {lineFrequency} Hz")
print(f"  Sampling frequency:      {samplingFrequency // 1000} kHz")
print(f"  Number of samples:       {numOfSamples}")
print(f"  Time step:               {timesStepMicroSeconds} us")
print(f"  Edge time:               {edgeTimeMicroSeconds} us")
print(f"  Push-Pull PWM frequency: {samplingFrequency // 2 // 1000} kHz")
print(f"  Max duty cycle:          {maxDutyCycle}")

# Get the path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory to the script directory
os.chdir(script_dir)
# print information in which directoy the txt files are created
print("Text files are generated in the directoy:")
print(f"  {os.getcwd()}")

samples = list(
    sin(2 * pi * lineFrequency * t / samplingFrequency) for t in range(0, numOfSamples)
)
dutyCycles = list(abs(sample) for sample in samples)

with open("sine.txt", "w") as file:
    file.write(f"0 {samples[0]}\n")
    for i in range(1, numOfSamples):
        file.write(f"+{timesStepMicroSeconds}u {samples[i]:.6}\n")

with open("steps.txt", "w") as file:
    file.write(f"0 0\n")
    file.write(f"+{timesStepMicroSeconds / 2}u 0\n")
    for i in range(1, numOfSamples):
        file.write(f"+{edgeTimeMicroSeconds}u {dutyCycles[i]:.6}\n")
        file.write(
            f"+{timesStepMicroSeconds - edgeTimeMicroSeconds}u {dutyCycles[i]:.6}\n"
        )

with open("pwm.txt", "w") as pwm:
    pwm.write(f"0 0\n")
    pwm.write(f"+{timesStepMicroSeconds / 2}u 0\n")
    q = 1
    for i in range(1, numOfSamples):
        tOn = round(dutyCycles[i] * maxDutyCycle * timesStepMicroSeconds, 3)
        tOff = timesStepMicroSeconds - tOn
        if tOn <= edgeTimeMicroSeconds * 2:
            pwm.write(f"+{timesStepMicroSeconds}u 0\n")
        else:
            pwm.write(f"+{edgeTimeMicroSeconds}u 1\n")
            pwm.write(f"+{tOn - edgeTimeMicroSeconds:.3f}u 1\n")
            pwm.write(f"+{edgeTimeMicroSeconds}u 0\n")
            pwm.write(f"+{tOff - edgeTimeMicroSeconds:.3f}u 0\n")

with open("pwm-1.txt", "w") as file1, open("pwm-2.txt", "w") as file2:
    file1.write(f"0 0\n")
    file1.write(f"+{timesStepMicroSeconds / 2}u 0\n")
    file2.write(f"0 0\n")
    file2.write(f"+{timesStepMicroSeconds / 2}u 0\n")
    levels = [0, 1]
    for i in range(1, numOfSamples):
        tOn = round(dutyCycles[i] * maxDutyCycle * timesStepMicroSeconds, 3)
        tOff = timesStepMicroSeconds - tOn
        if tOn <= edgeTimeMicroSeconds * 2:
            file1.write(f"+{timesStepMicroSeconds}u 0\n")
            file2.write(f"+{timesStepMicroSeconds}u 0\n")
        else:
            # toggle levels
            levels[0] = (levels[0] + 1) % 2
            levels[1] = (levels[1] + 1) % 2
            # pwm 1
            file1.write(f"+{edgeTimeMicroSeconds}u {levels[0]}\n")
            file1.write(f"+{tOn - edgeTimeMicroSeconds:.3f}u {levels[0]}\n")
            file1.write(f"+{edgeTimeMicroSeconds}u 0\n")
            file1.write(f"+{tOff - edgeTimeMicroSeconds:.3f}u 0\n")
            # pwm 2
            file2.write(f"+{edgeTimeMicroSeconds}u {levels[1]}\n")
            file2.write(f"+{tOn - edgeTimeMicroSeconds:.3f}u {levels[1]}\n")
            file2.write(f"+{edgeTimeMicroSeconds}u 0\n")
            file2.write(f"+{tOff - edgeTimeMicroSeconds:.3f}u 0\n")
