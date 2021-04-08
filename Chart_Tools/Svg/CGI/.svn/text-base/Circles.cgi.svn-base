#!/usr/local/bin/perl
# cgi-bin/Circles.cgi

print "Content-type: image/svg+xml\n\n";

### Circles.cgi - Circles and Arcs ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");		# OPEN FILE lines
$svg->open("encoding", "iso-8859-1","silent");

my $g = $svg->beginGraphics();	# BEGIN GRAPHICS line

# viewbox size
my $vbX = 1000;
my $vbY = 600;

# begin GMA
$g->b("svg", "viewBox", "0 0 $vbX $vbY", "width", "400", "height", "300");

  # draw the circular arcs
  $g->b("cpath", "fill","red","stroke","black","stroke-width","5","opacity","0.5");
    $g->moveto("abs", "755", "200");
    $g->curveto("rel", "0", "55.23", "-44.77", "100", "-100", "100");
    $g->scurveto("abs", "555", "255.23", "555", "200", "599.77", "100", "655", "100");
    $g->scurveto("rel", "100", "44.77", "100", "100");
    $g->closepath();
  $g->e();

  # draw the circle using built-in shape
  $g->d("circle", "cx", "655", "cy", "200", "r", "100", "fill","blue","stroke","white","stroke-width","5","opacity","0.5");

  # set font info
  $g->setFontSize("24");
  $g->setFontFamily("Times-Bold");
  $g->setFontColor("maroon");
  my @info = ("The circle is in fact the", "result of a red filled path", "object and a blue filled", "circle. The border is also", "made up of a white", "and a black border");

  # print the text block
  $g->d("tbCM", "xval", "380", "yval", "280", "leading", "0", "textStrs", @info, "doStyle");

$g->e();

$svg->close($g);				# END line
