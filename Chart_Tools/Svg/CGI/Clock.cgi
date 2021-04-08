#!/usr/local/bin/perl
# cgi-bin/Clock.cgi

print "Content-type: image/svg+xml\n\n";

### Clock.cgi - Clock Demo ###

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
$g->b("svg","viewBox","0 0 800 300","width","400","height","300","onload","SetTime(evt)");

	$g->printTxt("\n<!--Copyright 2000 Adobe Systems. You may copy, modify, and distribute this file, if you include this notice & do not charge for the distribution. This file is provided \"AS-IS\" without warranties of any kind, including any implied warranties.-->");

	$g->b("defs");
		$g->b("script", "language", "Javascript");
			$g->printTxt("\n\t\t\t<![CDATA[ function SetTime(LoadEvent) {");
			$g->printTxt("\n\t\t\tvar Now = new Date();");
			$g->printTxt("\n\t\t\tvar Seconds = Now.getSeconds();");
			$g->printTxt("\n\t\t\tvar Minutes = Now.getMinutes() + Seconds / 60;");
			$g->printTxt("\n\t\t\tvar Hours = Now.getHours() + Minutes / 60;");
			$g->printTxt("\n\t\t\tvar SVGDocument = LoadEvent.getTarget().getOwnerDocument();");
			$g->printTxt("\n\t\t\tSVGDocument.getElementById(\"seconds\").setAttribute('transform', 'rotate(' + (Seconds * 6) + ')');"); 
			$g->printTxt("\n\t\t\tSVGDocument.getElementById(\"minutes\").setAttribute('transform', 'rotate(' + (Minutes * 6) + ')');"); 
			$g->printTxt("\n\t\t\tSVGDocument.getElementById(\"hours\").setAttribute('transform', 'rotate(' + (Hours * 30) + ')');");
			$g->printTxt("\n\t\t\t} ]]>"); 
		$g->e();

	$g->e();

	$g->d("circle", "cx", "400", "cy", "150", "r", "80", "style", "fill:white;stroke:black");

	my @xvals = (430, 454, 465, 455, 430, 396, 362, 337, 327, 334, 358, 392);
	my @yvals = (96, 121, 156, 190, 216, 225, 216, 190, 156, 121, 96, 87);

	for (my $count=1; $count<13; $count++) {
		$g->b("text", "xval", $xvals[$count-1], "yval", $yvals[$count-1], "style", "font-size:15" );
			$g->printTxt("$count");
		$g->e();
	}

	$g->b(g, transform, "translate(400 150)");
		$g->b("g", "id","hours"); 
			$g->b("line", "x1","0", "y1","0", "x2","0", "y2","-35", "style","stroke-width:4;stroke:black");
				$g->d("animateTransform", "attributeName", "transform", "type","rotate","dur","43200s","values","0;360","repeatCount","indefinite");
			$g->e();
		$g->e();
		$g->b("g", "id","minutes");
			$g->b("line", "x1","0", "y1","0","x2","0","y2","-55","style","stroke-width:2;stroke:black");
				$g->d("animateTransform", "attributeName","transform","type","rotate","dur","3600s","values","0;360","repeatCount","indefinite");
			$g->e();
		$g->e();
		$g->b("g", "id","seconds");
			$g->b("line", "x1","0","y1","0","x2","0","y2","-75","style","stroke-width:1;stroke:red");
				$g->d("animateTransform", "attributeName","transform","type","rotate",dur,"60s","values","0;360","repeatCount","indefinite");
			$g->e();
		$g->e();
	$g->e();

	$g->d("circle", "cx","400","cy","150","r","3","style","fill:black;stroke:black");

# end GMA
$g->e();

$svg->close($g);			# END line
