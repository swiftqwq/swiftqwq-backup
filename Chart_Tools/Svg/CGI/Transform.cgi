#!/usr/local/bin/perl
# cgi-bin/Text.cgi

print "Content-type: image/svg+xml\n\n";

### Transform.cgi - Transformations ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");		# OPEN FILE lines
$svg->open("public","encoding","iso-8859-1","silent");
	
my $g = $svg->beginGraphics();		# BEGIN GRAPHICS line

$g->b("svg","viewBox","0,0,800,600","width","400","height","300");

  $g->d("rect","xval","50","yval","50","width","300","height","200","style","fill:#EEEEEE");

  # set font environments
  $g->setFontFamily("Helvetica");
  $g->setFontSize("18");
  $g->setFontColor("yellow");

  my $text = "Text and Shape Transformation";

  # put text on drawing
  $g->d("txtCM",$text,"xval","200","yval","150", "doStyle");
  $g->d("txtCM",$text,"xval","0","yval","0","transform","matrix(.707 .707 -.707 .707 200 150)", "doStyle");

  # draw ellipses too
  $g->d("ellipse","cx","200","cy","150","rx","100","ry","50","style","fill:red;opacity:0.5");
  $g->d("ellipse","cx","0","cy","0","rx","100","ry","50","style","fill:blue;opacity:0.5","transform","matrix(.707 .707 -.707 .707 200 150)");

$g->e();

$svg->close($g);			# END line
