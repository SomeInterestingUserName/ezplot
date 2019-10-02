import matplotlib
import matplotlib.pyplot as plt
import argparse
import sys

parser = argparse.ArgumentParser()

if not sys.stdin.isatty():
    indata = sys.stdin
else:
    print('Error: You must pipe data to ezplot')
    sys.exit(1)

# All these arguments are optional. If not provided, I'll give you defaults.

# yaxis: Set a y-axis title. Default is "Value"
parser.add_argument('-y', '--yaxis',
                    help='Set y-axis title, default: "Value"',
                    dest='yaxis_title')

# xaxis: Set an x-axis title. Default is "Samples"
parser.add_argument('-x', '--xaxis',
                    help='Set x-axis title, default: "Samples"',
                    dest='xaxis_title')

# title: Set a title for the plot. Default is "Plot"
parser.add_argument('-t', '--title',
                    help='Set plot title, default: "Plot"',
                    dest='plot_title')

# plot: Set plot type. Default is a line plot, but you can change it to
# either a point plot or a combination of the two.
parser.add_argument('-p', '--plot',
                    nargs='+',
                    help='Plot type, default: line',
                    dest='plot_type',
                    choices=['line', 'points'])

# Parse the arguments and set their associated variables
args = parser.parse_args()

plot_title = 'Plot'
if(args.plot_title is not None):
    plot_title = args.plot_title
                    
yaxis_title = 'Value'
if(args.yaxis_title is not None):
    yaxis_title = args.yaxis_title

xaxis_title = 'Samples'
if(args.xaxis_title is not None):
    xaxis_title = args.xaxis_title

plot_type = 'line'
if(args.plot_type is not None):
    plot_type = args.plot_type

# Translate data to numbers, and catch any non-numerical data
y_axis = []
for line in indata:
    try:
        y_axis.append(float(line))
    except ValueError:
        print('Error: \"{}\" is not a number.'.format(str(line)))
        sys.exit(1)

# Check that we get at least 2 points
if len(y_axis) < 2:
    print('Error: At least 2 points must be provided')
    sys.exit(1)

# Generate x-axis values
x_axis = range(0, len(y_axis))
fig, ax = plt.subplots()

# Translate line and marker types to matplotlib's argument types
type_line = 'solid' if 'line' in plot_type else 'None'
type_marker = 'o' if 'points' in plot_type else 'None'

# Plot the data and set titles
ax.plot(x_axis, y_axis, linestyle=type_line, marker=type_marker)
ax.set(xlabel=xaxis_title, ylabel=yaxis_title, title=plot_title)

# Add a grid
ax.grid()

# Display the plot
plt.show()
