# ezplot
A super-simple command-line based plotter for `matplotlib`. Graphs numbers piped to it, separated by newlines.

Usage: `blah | python3 ezplot.py` where `blah` is a command or program that prints numerical data to `stdout`.

### Arguments

* `-x` or `--xaxis`: Set a title for the x-axis. Defaults to "Sample"
* `-y` or `--yaxis`: Set a title for the y-axis. Defaults to "Value"
* `-t` or `--title`: Set a title for the x-axis. Defaults to "Plot"
* `-p` or `--plot`: One or more of `[line, points]` for a line and/or point plot, respectively. Defaults to line.



### Example

`cat data.txt | python3 ezplot.py --xaxis "Sample" --yaxis "Value" --title "Contents of data.txt" --plot line points`

#### data.txt

```
100
200
400
800
1600
```

#### Output

![](https://github.com/SomeInterestingUserName/ezplot/raw/master/doc/Figure_example.png "An example plot")
