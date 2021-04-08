#!/usr/local/bin/perl
# cgi-bin/Anim.cgi

print "Content-type: image/svg+xml\n\n";

### Anim.cgi - Animation Sample ###

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

# begin GMA
$g->b("svg","viewBox","0 0 800 300","width","400","height","300");

	# draw a rectangle
	$g->b("rect","id","RECT","width","300","height","100","fill","rgb(255,255,0)","stroke-width",5);	
	
		# move it on the screen
		$g->b("animation","attributeType","XML","fill","freeze");
			$g->move("0s","10s","500","200","0","0","10s","10s","0","0","800","0","20s","10s","800","0","0","200","30s","10s","0","200","500","200");
			$g->change("0s","20s","width","300","0","20s","20s","width","0","300","0s","20s","height","100","0","20s","20s","height","0","100");
		$g->e();

		# change its properties whilst it slides about
		$g->b("animation","attributeType","CSS","fill","freeze");
			$g->change("0s","20s","stroke-width","5","0","20s","20s","stroke-width","0","5");
			$g->change("0s","10s","fill","rgb(255,255,255)","rgb(255,0,255)","10s","10s","fill","rgb(255,0,255)","rgb(100,0,100)","20s","5s","fill","rgb(100,0,100)","rgb(100,150,100)","25s","15s","fill","rgb(100,150,100)","rgb(255,255,255)","0s","10s","stroke","rgb(255,255,255)","rgb(0,100,150)","10s","10s","stroke","rgb(0,100,150)","rgb(0,200,200)","20s","5s","stroke","rgb(0,200,200)","rgb(200,0,100)","25s","15s","stroke","rgb(200,0,100)","rgb(255,255,255)");
		$g->e();

	# end rectangle
	$g->e();

	# open a group with a set opacity value
	$g->b("g","id","TEXT","opacity","1");
		
		# set font environment variables
		$g->setFontSize("24");
		$g->setFontFamily("Helvetica-Bold");
		$g->setFontColor("navy");

		# draw a text string that fades in and out and glows at the end
		$g->b("txtCM","Animation Demo","xval","400","yval","150","doStyle");

			# mimic glowing effect
			$g->b("animation","attributeType","CSS");
				$g->change("40s","1s","fill","navy","yellow","41s","0.5s","fill","yellow","white","41.5s","0.5s","fill","white","yellow","42s","0.5s","fill","yellow","red","42.5s","0.5s","fill","red","navy");
			$g->e();

		# end text string
		$g->e();

		# fades the text string
		$g->b("animation","attributeType","CSS");
			$g->change("0s","15s","opacity","1","0","15s","10s","opacity","0","0","25s","15s","opacity","0","1");
		$g->e();

	# end group
	$g->e();

# end GMA
$g->e();

$svg->close($g);			# END line
