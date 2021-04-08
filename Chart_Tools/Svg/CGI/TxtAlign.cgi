#!/usr/local/bin/perl
# cgi-bin/TxtAlign.cgi

print "Content-type: image/svg+xml\n\n";

### TxtAlign.cgi - Text Alignment ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi",\*OUT);		# OPEN FILE lines
$svg->open("silent", "public", "encoding", "iso-8859-1");

my $g = $svg->beginGraphics();		# BEGIN GRAPHICS line

# dimensions and measurements
my $vbX = 640;
my $vbY = 480;
my $width = 300;
my $height = 200;
my $x = ($vbX-$width)/2;
my $y = ($vbY-$height)/2;

$g->b("svg","id","SVG","viewBox","0 0 $vbX $vbY","width","400","height","300");
	
	# draw a rectangle against which all the text strings will align
	$g->d("rect", "width", $width, "height", $height, "xval", $x, "yval", $y, "style", "fill:yellow");

	# set font environment variables
	$g->setFontSize("18");
	$g->setFontFamily("Helvetica-Bold");
	$g->setFontColor("red");

	# label four corners of rectangle
	$g->d("txtRB", "Top Left", "xval", $x, "yval", $y, "doStyle" );
	$g->d("txtRT", "Bottom Left", "xval", $x, "yval", $y+$height, "doStyle" );
	$g->d("txtLB", "Top Right", "xval", $x+$width, "yval", $y, "doStyle" );
	$g->d("txtLT", "Bottom Right", "xval", $x+$width, "yval", $y+$height, "doStyle" );

	# change font settings	
	$g->setFontSize("12");
	$g->setFontFamily("Helvetica");
	$g->setFontColor("navy");

	# label four edges of rectangle
	$g->d("txtRM","Left", "xval", $x, "yval", $y+$height/2, "doStyle" );
	$g->d("txtLM","Right", "xval", $x+$width, "yval", $y+$height/2, "doStyle" );
	$g->d("txtCB","Top", "xval", $x+$width/2, "yval", $y, "doStyle" );
	$g->d("txtCM","Middle", "xval", $x+$width/2, "yval", $y+$height/2, "doStyle" );
	$g->d("txtCT","Bottom", "xval", $x+$width/2, "yval", $y+$height, "doStyle" );

	# text strings used in blocks
	my @block = ("First line", "Another line", "Final line");
	my @middle = ("Football", "is Life");

	# user-provided leading space of font
	my $ldg = 0;

	# change font preferences again
	$g->setFontSize("8");
	$g->setFontFamily("Times-Bold");
	$g->setFontColor("gray");	

	# put blocks of text at the four corners
	$g->d("tbLT","xval", $x, "yval", $y, "leading", $ldg, "textStrs", @block, "doStyle" );
	$g->d("tbRT","xval", $x+$width, "yval", $y, "leading", $ldg, "textStrs", @block, "doStyle" );
	$g->d("tbLB","xval", $x, "yval", $y+$height, "leading", $ldg, "textStrs", @block, "doStyle" );
	$g->d("tbRB","xval", $x+$width, "yval", $y+$height, "leading", $ldg, "textStrs", @block, "doStyle" );

	# set font variables again
	$g->setFontSize("6");
	$g->setFontColor("green");	

	# print important message against all four edges
	$g->d("tbCT","xval", $x+$width/2, "yval", $y, "leading", $ldg, "textStrs", @middle, "doStyle");
	$g->d("tbCB","xval", $x+$width/2, "yval", $y+$height, "leading", $ldg, "textStrs", @middle, "doStyle");
	$g->d("tbLM","xval", $x, "yval", $y+$height/2, "leading", $ldg, "textStrs", @middle, "doStyle");
	$g->d("tbRM","xval", $x+$width, "yval", $y+$height/2, "leading", $ldg, "textStrs", @middle, "doStyle");

$g->e();

$svg->close($g);			# END line
