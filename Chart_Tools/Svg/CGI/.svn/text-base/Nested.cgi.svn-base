#!/usr/local/bin/perl
# cgi-bin/Nested.cgi

print "Content-type: image/svg+xml\n\n";

### Nested.cgi - Nested GMAs ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");		# OPEN FILE lines
$svg->open("silent");

my $g = $svg->beginGraphics();		# BEGIN GRAPHICS line

# begin outer GMA
$g->b("svg","viewBox","0,0,800,600","width","400","height","300","id","OUTER");

  # draw backdrop
  $g->d("rect","id","BG","style","fill:black","xval","0","yval","20","width","800","height","600");

  # begin group with mouse-over status bar message behaviour
  $g->b("g","id","GROUP","onmousemove","window.status='Group of shapes'");

    for (my $i=3;$i<8;$i++) {

	# draw rectangles
	my $offset=25;
	$g->d("rect","id","SQUAREa".($i-2),"xval",$offset*$i,"yval",$offset*$i,"width",$offset,"height",$offset,"style","fill:green;stroke:red" );
	$g->d("rect","id","SQUAREb".($i-2),"xval",350-($offset*$i),"yval",$offset*$i,"width",$offset,"height",$offset,"style","fill:red;stroke:gray");

    } # end for

    # begin inner GMA with the mouse-click alert event
    $g->b("svg","viewBox","0 0 800 600","width","300","height","200","id","INNER","onclick", "alert('Clicked');");

	my @colours = qw (blue yellow navy);  # local colour array

	# draw group of 'clickable' circles
	for (my $i=-1; $i<2; $i++) {
	  $g->d("circle","id","CIRCLE".($i+1),"r","100","cx",500+($i*25),"cy",300+($i*25),"style","fill:$colours[$i+1]");
	}

    # end inner GMA
    $g->e();

  # end group of shapes
  $g->e();

  # set font information
  $g->setFontFamily("Helvetica-Bold");
  $g->setFontSize("14pt");
  $g->setFontColor(yellow);

  # draw some text
  $g->b(text,id,TEXT,xval,100,yval,225,"doStyle");
    $g->printTxt("SVG Demo using CGI");
  $g->e();

# end outer GMA
$g->e();

$svg->close($g);				# END line
