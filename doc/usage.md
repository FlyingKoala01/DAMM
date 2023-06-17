# Usage

The interface consists of a table of bars. There is a pagination, and it
can be sorted both in ASC and DESC.

You can filter by the name of the bar.

## Display

The interface shows the position of the bar inside the ranking, with the
variation from the last month.

This means that, if the bar was ranked 5th last month, and this month is 1st,
a (+5) will appear next to the ranking position. This is useful when searching
bars that played very well lately.

## Grade and sales

The grade goes from 1 to 10. However, with a lot of bars (our sample data had
23000 bars), there are lots of ties.

We suppose that a commercial would not have that amount of bars, so it would be
easier for them to see which bars are better.

There is also a column showing the total number of sales of a bar, as an extra
indicator.
