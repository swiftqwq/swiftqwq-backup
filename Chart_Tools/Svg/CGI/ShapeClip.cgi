#!/usr/local/bin/perl
# cgi-bin/ShapeClip.cgi

print "Content-type: image/svg+xml\n\n";

### ShapeClip.cgi - Shapes as Clipping Paths ###

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

my $vbX = 800;
my $vbY = 600;

$g->b("svg","viewBox","0","0",$vbX,$vbY,"width","400","height","300");

  # start a clip-path definition
  $g->b("clipPath", "id", "MyClip");

  	# draw a triangle to be used as a clipping path
  	$g->b("cpath","id","SHAPE","style","fill:red;stoke:none");
    		$g->moveto("abs", "150", "75");
    		$g->lineto("rel", "100", "50");
    		$g->lineto("rel", "-25", "125");
    		$g->closepath();
	$g->e();
  
  $g->e();  

  $g->d("rect", "fill", "red", "style", "clip-path:url(#MyClip)", "xval", "100", "width", "250", "height", "250");
  $g->d("rect", "fill", "blue", "style", "clip-path:url(#MyClip)", "xval", "200", "width", "250", "height", "250");
  
$g->e();

$svg->close($g);			# END line
