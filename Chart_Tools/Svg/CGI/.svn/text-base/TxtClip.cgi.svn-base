#!/usr/local/bin/perl
# cgi-bin/TxtClip.cgi

print "Content-type: image/svg+xml\n\n";

### TxtClip.cgi - Text as Clippath ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;
use Svg::Graphics;

my $svg = Svg::File->new("cgi");
$svg->open("public", "encoding", "iso-8859-1", "silent");
my $g = $svg->beginGraphics();

my $vbX = 400;
my $vbY = 300;

$g->b("svg","viewBox","0","0",$vbX,$vbY,"width","400","height","300");

  # set text environments
  $g->setFontSize("24");
  $g->setFontFamily("Helvetica-Bold");

  # start a clip-path definition
  $g->b("clipPath","id","MyClip");

	# draw a text string
  	$g->d("txtCM","I am a clipping path","id","TEXT","xval",$vbX/2,"yval",$vbY/2, "doStyle");

  $g->e();

  # draw the red and blue rectangles that 
  # use the text string as the clipping path
  $g->d("rect","id","RECT","xval",$vbX/6,"yval",$vbY/3,"width",$vbX*2/3,"height",$vbY*2/11,"style","fill:red;clip-path:url(#MyClip)");
  $g->d("rect","id","RECT","xval",$vbX/6,"yval",$vbY/3+$vbY*2/11,"width",$vbX*2/3,"height",$vbY/5,"style","fill:blue;clip-path:url(#MyClip)");

$g->e();

$svg->close($g);			# END line
