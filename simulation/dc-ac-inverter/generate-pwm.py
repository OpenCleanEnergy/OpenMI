from math import pi, sin
import os

lineFrequency = 500
pwmFrequendy = 100_000
numOfSamples = pwmFrequendy // lineFrequency + 1
timeStepMicroSeconds = 1 / pwmFrequendy * 1_000_000
edgeTimeMicroSeconds = timeStepMicroSeconds / 1000
maxDutyCycle = 0.9
# print information about the signal
print("Information about the generated signal:")
print(f"  Line frequency:          {lineFrequency} Hz")
print(f"  PWM frequency:           {pwmFrequendy // 1000} kHz")
print(f"  Number of samples:       {numOfSamples}")
print(f"  Time step:               {timeStepMicroSeconds} us")
print(f"  Edge time:               {edgeTimeMicroSeconds} us")
print(f"  Push-Pull PWM frequency: {pwmFrequendy // 2 // 1000} kHz")
print(f"  Max duty cycle:          {maxDutyCycle}")

# Get the path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory to the script directory
os.chdir(script_dir)
# print information in which directoy the txt files are created
print("Text files are generated in the directory:")
print(f"  {os.getcwd()}")

samples = list(
    sin(2 * pi * lineFrequency * t / pwmFrequendy) for t in range(0, numOfSamples)
)
dutyCycles = list(abs(sample) for sample in samples)

with open("sine.txt", "w") as file:
    file.write(f"0 {samples[0]}\n")
    for i in range(1, numOfSamples):
        file.write(f"+{timeStepMicroSeconds}u {samples[i]:.6}\n")

with open("steps.txt", "w") as file:
    file.write(f"0 0\n")
    file.write(f"+{timeStepMicroSeconds / 2}u 0\n")
    for i in range(1, numOfSamples):
        file.write(f"+{edgeTimeMicroSeconds}u {dutyCycles[i]:.6}\n")
        file.write(
            f"+{timeStepMicroSeconds - edgeTimeMicroSeconds}u {dutyCycles[i]:.6}\n"
        )

# fast pwm high side switch
with open("pwm-fast-high.txt", "w") as pwm:
    pwm.write(f"0 0\n")
    pwm.write(f"+{timeStepMicroSeconds / 2}u 0\n")
    for i in range(1, numOfSamples // 2 + 1):
        tOn = round(dutyCycles[i] * maxDutyCycle * timeStepMicroSeconds, 3)
        tOff = timeStepMicroSeconds - tOn
        if tOn <= edgeTimeMicroSeconds * 2:
            pwm.write(f"+{timeStepMicroSeconds}u 0\n")
        else:
            pwm.write(f"+{edgeTimeMicroSeconds}u 1\n")
            pwm.write(f"+{tOn - edgeTimeMicroSeconds:.3f}u 1\n")
            pwm.write(f"+{edgeTimeMicroSeconds}u 0\n")
            pwm.write(f"+{tOff - edgeTimeMicroSeconds:.3f}u 0\n")
    pwm.write(f"+{0.5 /lineFrequency * 1_000}m 0\n")

# fast pwm low side switch
with open("pwm-fast-low.txt", "w") as pwm:
    pwm.write(f"0 0\n")
    pwm.write(f"+{timeStepMicroSeconds / 2}u 0\n")
    pwm.write(f"+{0.5 /lineFrequency * 1_000}m 0\n")
    for i in range(numOfSamples // 2, numOfSamples):
        tOn = round(dutyCycles[i] * maxDutyCycle * timeStepMicroSeconds, 3)
        tOff = timeStepMicroSeconds - tOn
        if tOn <= edgeTimeMicroSeconds * 2:
            pwm.write(f"+{timeStepMicroSeconds}u 0\n")
        else:
            pwm.write(f"+{edgeTimeMicroSeconds}u 1\n")
            pwm.write(f"+{tOn - edgeTimeMicroSeconds:.3f}u 1\n")
            pwm.write(f"+{edgeTimeMicroSeconds}u 0\n")
            pwm.write(f"+{tOff - edgeTimeMicroSeconds:.3f}u 0\n")

slowStepMicroSeconds = 0.5 / lineFrequency * 1_000_000
# slow pwm high side switch
with open("pwm-slow-high.txt", "w") as pwm:
    pwm.write(f"0 0\n")
    pwm.write(f"+{slowStepMicroSeconds}u 0\n")
    pwm.write(f"+{edgeTimeMicroSeconds}u 1\n")
    pwm.write(f"+{slowStepMicroSeconds - 2 * edgeTimeMicroSeconds}u 1\n")
    pwm.write(f"+{edgeTimeMicroSeconds}u 0\n")

# slow pwm low side switch
with open("pwm-slow-low.txt", "w") as pwm:
    pwm.write(f"0 0\n")
    pwm.write(f"+{edgeTimeMicroSeconds}u 1\n")
    pwm.write(f"+{slowStepMicroSeconds - 2 * edgeTimeMicroSeconds}u 1\n")
    pwm.write(f"+{edgeTimeMicroSeconds}u 0\n")
    pwm.write(f"+{slowStepMicroSeconds}u 0\n")
