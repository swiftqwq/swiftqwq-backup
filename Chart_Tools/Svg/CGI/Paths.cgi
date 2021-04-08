#!/usr/local/bin/perl
# cgi-bin/Paths.cgi

print "Content-type: image/svg+xml\n\n";

### Paths.cgi - Lines and Curves ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;					# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");			# OPEN FILE lines
$svg->open("encoding", "iso-8859-1","silent");

my $g = $svg->beginGraphics();			# BEGIN GRAPHICS line

# viewbox size
my $vbX = 800;
my $vbY = 600;

# begin GMA
$g->b("svg", "viewBox", "0 0 $vbX $vbY", "width", $vbX/2, "height", $vbY/2);

	# coordinate variables
	my $xoff=130, $yoff=130;

	# print 5 lines with incrementing widths
	for (my $count=0; $count<5; $count++) {
		my $wid=1;
		if (eval($count)!=0) {$wid=$count*3}
		$g->b("cpath", "style", "fill:none;stroke:black;stroke-width:$wid");
			$g->moveto("abs", $xoff, $yoff);
			$g->lineto("rel", $xoff*3, "0");
		$g->e();
		$g->d("txtLM","Line width \"".$wid."\"", "xval", $xoff*4+10, "yval", $yoff, "doStyle");
		$yoff+=20;
	}

	# spacing between line patterns
	$yoff+=20;
	
	# print 4 curves with various line cap styles
	my @linecaps = qw(square butt round inherit);	
	for ($xoff, $yoff, $count=0; $count<@linecaps; $count++) {
		$g->b("cpath", "style", "fill:none;stroke:black;stroke-width:5;stroke-linecap:$linecaps[$count]");
			$g->moveto("abs", $xoff, $yoff);
			$g->curveto("rel", "0", "0", $xoff*1.5, "15", $xoff*3, "0");
		$g->e();
		$g->d("txtLM","Line Cap \"$linecaps[$count]\"", "xval", $xoff*4+10, "yval", $yoff, "doStyle");
		$yoff+=10;
	}

	# spacing between line patterns
	$yoff+=20;

	# print 3 dashed lines width various spacing
	my $dash1 = "10 5";
	my $dash2 = "15 9 5 3 3 5 9 15";
	my $dash3 = "3 7 9";
	my @dasharray = ($dash1, $dash2, $dash3);	
	for ($xoff, $yoff, $count=0; $count<@dasharray; $count++) {
		$g->b("cpath", "style", "fill:none;stroke:black;stroke-width:5;stroke-dasharray:$dasharray[$count]");
			$g->moveto("abs", $xoff, $yoff);
			$g->lineto("rel", $xoff*3, "0");
		$g->e();
		$g->d("txtLM","Line Dash Array \"$dasharray[$count]\"", "xval", $xoff*4+10, "yval", $yoff, "doStyle");
		$yoff+=10;
	}

	# spacing between line patterns
	$yoff+=20;

	# print 4 lines illustrating different line-joining patterns
	my @linejoins = qw(miter round bevel inherit);
	for ($xoff, $yoff, $count=0; $count<@linejoins; $count++) {
		$g->b("cpath", "style", "fill:none;stroke:black;stroke-width:5;stroke-linejoin:$linejoins[$count]");
			$g->moveto("abs", $xoff, $yoff);
			$g->lineto("rel", $xoff*3, "10");
			$g->lineto("rel", -$xoff*3, "10");
		$g->e();
		$g->d("txtLM","Line Join \"$linejoins[$count]\"", "xval", $xoff*4+10, "yval", $yoff+10, "doStyle");
		$yoff+=30;
	}

# end the drawing
$g->e();

$svg->close($g);				# END line
