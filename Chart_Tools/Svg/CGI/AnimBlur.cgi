#!/usr/local/bin/perl
# cgi-bin/AnimBlur.cgi

print "Content-type: image/svg+xml\n\n";

### AnimBlur.cgi - Blur Effect Demo ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");		# OPEN FILE lines
$svg->open(public,encoding,"iso-8859-1","silent");	

my $g = $svg->beginGraphics();		# BEGIN GRAPHICS line

# begin GMA
$g->b("svg","viewBox","0 0 800 300","width","400","height","300");

	$g->printTxt("\n<!--Copyright 2000 Adobe Systems. You may copy, modify, and distribute this file, if you include this notice & do not charge for the distribution. This file is provided \"AS-IS\" without warranties of any kind, including any implied warranties.-->");

	# define blur effect
	$g->b("defs");
		$g->b("filter","id","BLUR","filterUnits","objectBoundingBox","xval","0%","yval","0%","width","150%","height","150%");			
			$g->b("feGaussianBlur","result","BlurredSource","stdDeviation","0","in","SourceGraphic");
				$g->d("animate","id","ANIM","begin","indefinite","attributeName","stdDeviation","values","8;0","dur","1s","repeatCount","1");
			$g->e();
		$g->e();
	$g->e();

	# blur text
	$g->b("text","font-size","40","filter","url(#BLUR)","xval","200","yval","200");
		$g->printTxt("Click Here");
	$g->e();

	# clear text
	$g->b("text","font-size","40","fill","none","stroke","black","fill-rule","evenodd","stroke-width","0.5","xval","200","yval","200");
		$g->printTxt("Click Here");
	$g->e();

	# link it to blur effect on mouse click
	$g->b("a","xlink:href","#ANIM");
		$g->d("rect","id","click","xval","200","yval","165","width","200","height","40","style","opacity:0;");
	$g->e();

# end GMA
$g->e();

$svg->close($g);			# END line
