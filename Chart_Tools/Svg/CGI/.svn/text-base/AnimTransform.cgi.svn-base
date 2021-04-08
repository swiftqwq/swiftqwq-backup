#!/usr/local/bin/perl
# cgi-bin/AnimTransform.cgi

print "Content-type: image/svg+xml\n\n";

### AnimTransform.cgi - Animated Transformation ###

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

	$g->printTxt("\n<!--Copyright 2000 Adobe Systems. You may copy, modify, and distribute this file, if you include this notice & do not charge for the distribution. This file is provided \"AS-IS\" without warranties of any kind, including any implied warranties.-->");

	$g->b("g","transform","translate(400 150)");

		# animate and transform green circle
		$g->b("circle","id","circle0","fill","green","stroke","#3AF","stroke-width","3","opacity","0.5","cx","0","cy","0","r","30");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;360","additive","sum","dur","10s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;30;-40;190;90;170;320;290;210;170;0","additive","sum","dur","9s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","scale","values","4 1;0.5 1;4 1","additive","sum","dur","5s","repeatDur","indefinite");
		$g->e();

		# animate and transform red circle
		$g->b("circle","id","circle1","fill","red","stroke","black","stroke-width","3","opacity","0.7","cx","0","cy","0","r","30");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;360","additive","sum","dur","3s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","scale","values","4 1;0.5 1;4 1","additive","sum","dur","4s","repeatDur","indefinite");
		$g->e();

		# animate and transform blue circle
		$g->b("circle","id","circle2","fill","blue","stroke","#0A8","stroke-width","3","opacity","0.5","cx","0","cy","0","r","30");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;-360","additive","sum","dur","12s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;30;-40;190;90;170;320;290;210;170;0","additive","sum","dur","7s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","scale","values","1 5;3 0.5;1 5","additive","sum","dur","3s","repeatDur","indefinite");
		$g->e();

		# animate and transform yellow circle
		$g->b("circle","id","circle3","fill","yellow","stroke","#0C0","stroke-width","3","opacity","0.7","cx","0","cy","0","r","30");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;-360","additive","sum","dur","12s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","rotate","values","0;30;-40;190;90;170;320;290;210;170;0","additive","sum","dur","8s","repeatDur","indefinite");
			$g->d("animateTransform","attributeName","transform","type","scale","values","4 1;0.5 1;4 1","additive","sum","dur","3s","repeatDur","indefinite");
		$g->e();

	$g->e();

# end GMA
$g->e();

$svg->close($g);			# END line
