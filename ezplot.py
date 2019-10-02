import matplotlib
import matplotlib.pyplot as plt
import argparse
import sys

parser = argparse.ArgumentParser()

if not sys.stdin.isatty():
    indata = sys.stdin
else:
    print("Error: You must pipe data to ezplot")
    sys.exit(1)

parser.add_argument('-y', '--yaxis',
                    help="Set y-axis title",
                    dest='yaxis_title')

parser.add_argument('-t', '--title',
                    help="Set plot title",
                    dest='plot_title')

args = parser.parse_args()

plottitle = "Plot"
if(args.plot_title is not None):
    plottitle = args.plot_title
                    

ytitle = "Plot"
if(args.yaxis_title is not None):
    ytitle = args.yaxis_title
    


yaxis = []
for line in indata:
    try:
        yaxis.append(int(line))
    except ValueError:
        print("Error: \"{}\" is not a number.".format(str(line)))
        sys.exit(1)

if len(yaxis) < 2:
    print("Error: At least 2 points must be provided")
    sys.exit(1)
    
xaxis = range(0, len(yaxis))
fig, ax = plt.subplots()
ax.plot(xaxis, yaxis)
ax.set(xlabel="Samples", ylabel=ytitle, title=plottitle)

ax.grid()

plt.show()
