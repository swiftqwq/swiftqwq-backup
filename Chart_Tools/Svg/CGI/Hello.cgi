#!/usr/local/bin/perl
# cgi-bin/Hello.cgi

print "Content-type: image/svg+xml\n\n";

### Hello.cgi - Hello World! ###

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

# TEXT lines
$g->b("svg","viewBox","0,0,800,600","width","400","height","300");
  $g->b("text","xval","100","yval","150","style","font-size:24pt;font-face:Helvetica");
$g->printTxt("Hello World");
  $g->e();
$g->e();

$svg->close($g);			# END line
